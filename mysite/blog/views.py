from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
from blog.forms import BlogForm, CreateNewUserForm
from blog.models import Blog
from django.contrib.auth.models import User
from django.contrib import messages
# from .forms import NewUserForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required, permission_required 
from django.views import View


def index_page(request):
     return render(request, 'index.html')

@permission_required('blog.add_blog',raise_exception=True)
def create_blog(request):
    form = BlogForm()
    if request.method == 'POST':
        # import pdb;pdb.set_trace()
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()
            blog.is_published = True
            form.save()
            return redirect('/blogs/list')
    return render(request, 'create.html',{'form':form})

class BlogView(View):
    form = BlogForm()
    def get(self,request):
        form = BlogForm(request.POST)
        return render(request, 'create.html', {'form':form})
    
    def post(self, request):
        if request.user.is_authenticated and request.user.has_perm('blog.add_blog'):
            form = BlogForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('list_blogs')
            return render(request, 'create.html', {'form':form})


def list_blogs(request):
    blog = Blog.objects.all()
    return render(request, 'list.html',{'blogs':blog})
    
class BlogList(View):
    def get(self, request):
        blog = Blog.objects.all()
        return render(request, 'list.html', {'blogs':blog})

def delete_blog(request, **kwargs):
    error_message = ""
    if pk := kwargs.get('pk'):
        try:
            blog = Blog.objects.get(pk=pk)  #(database pk, request pk) and blog here is primary key
            blog.delete()
        except Exception as e:
            error_message = "Blog does not exist."
    blogs = Blog.objects.all()
    return render(request, 'list.html',{'blogs':blogs})

def update_blog(request, **kwargs):
    error_message = ""
    if pk := kwargs.get('pk'):
        try:
            blog = Blog.objects.get(pk=pk)
            form = BlogForm(request.POST or None, instance=blog)
            form.save()
            return redirect('/blogs/list')
        except Exception as e:
            error_message = "Blog does not exist."
    
    return render(request, 'create.html',{'form':form})


def create_new_user(request):
    # import pdb;pdb.set_trace()
    form = CreateNewUserForm()
    if request.method == 'POST':
        form = CreateNewUserForm(request.POST)
        # print(request.user)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email')
        user = User.objects.create_user(username, password=password, email=email)
        user.save()
    
    return render(request,'register.html', {'form':form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        print('======================>')
        print(user)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request,'login.html',{})

def logout_user(request):
    logout(request)
    return redirect("index")





from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    full_name = serializers.SerializerMethodField()

    def get_full_name(self, name):
        fl_name = name.first_name + " " +name.last_name
        return fl_name

class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class CreateBlogView(CreateAPIView):
    serializer_class = BlogSerializer
    def create(self, request, *args, **kwargs):
        response =  super().create(request, *args, **kwargs)
        response.data = {"message":"Blog Created Successfully"}
        return response  
    
class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.filter(is_published=True)
    serializer_class = BlogSerializer

class BlogRetrieveAPIView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    

