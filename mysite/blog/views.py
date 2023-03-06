from django.shortcuts import render
from django.http import HttpResponse,Http404
from blog.forms import BlogForm

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
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            # blog = form.save()
            # blog.is_published = True
            form.save()

    return render(request, 'name.html',{'form':form})
