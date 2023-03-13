from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
from blog.forms import BlogForm
from blog.models import Blog

# Create your views here.
# def addition(num1,num2):
#     res = int(num1)+int(num2)
#     return res

# def subtract(num1,num2):
#     res = int(num1)-int(num2)
#     return res

# def multiply(num1,num2):
#     res = int(num1)*int(num2)
#     return res

# def divide(num1,num2):
#     res = int(num1)/int(num2)
#     return res



def index(request):
    return HttpResponse("Index page of project file.")
    # num1 = request.GET.get('num1','')
    # num2 = request.GET.get('num2','')
    # result = " "
    
    # if  request.method  == "GET":
        
    #     print(request.GET)
    #     if 'add' in request.GET:
    #         result = addition(num1,num2)
    #     if 'sub' in request.GET:
    #         result = subtract(num1,num2)
    #     if 'mul' in request.GET:
    #         result = multiply(num1,num2)
    #     if 'div' in request.GET:
    #         result = divide(num1,num2)
       
    # return render(request, 'name.html', {'result':result})

    # form = RegistrationForm
   
   
def create_blog(request):
    form = BlogForm()
    # import pdb;pdb.set_trace()
    # breakpoint()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()
            blog.is_published = True
            form.save()
            return redirect('/blogs/list')
    return render(request, 'create.html',{'form':form})


def list_blogs(request):
    blog = Blog.objects.all()
    return render(request, 'list.html',{'blogs':blog})
    

def delete_blog(request, **kwargs):
    error_message = ""
    import pdb; pdb.set_trace()
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