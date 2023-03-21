from django.shortcuts import render,redirect
from apna_bazaar.forms import ApnaBazaarForm, CreateNewUserForm
from apna_bazaar.models import ApnaBazaar
from mysite.core.cart_helper import add_item_to_cart, remove_item_from_cart
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def home_ecom(request):
    return render(request,'home_ecom.html')

def register_user(request):
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
    return render(request,'register_ecom.html', {'form':form})

def login_ecom(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        print('======================>')
        print(user)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request,'login_ecom.html',{})

def logout_user(request):
    logout(request)
    return redirect("index")




def add_product(request):
    form = ApnaBazaarForm()
    if request.method == 'POST':
        form = ApnaBazaarForm(request.POST)
        form.save()

    return render(request, 'add_product.html', {'forms':form})

def show_products(request):
    products = ApnaBazaar.objects.all()
    return render(request, 'products.html', {'Products':products})

def show_product_detail(request, **kwargs):
    context={}
    if pk := kwargs.get('pk'):
        name = request.session.get('name')
        product = ApnaBazaar.objects.get(pk = pk)
    context = {'Product':product, 'name':name}
    return render(request, 'product_detail.html', context)



def add_to_cart(request, **kwargs):
    adc = add_item_to_cart(request, **kwargs)
    return render(request,'cart.html', {'name':adc})
    
def remove_from_cart(request, **kwargs):
    remove_item_from_cart(request, **kwargs)        
    return render(request, 'cart.html', )
        

def add_to_wishlist(request, **kwargs):
    if pk := kwargs.get('pk'):
        product = ApnaBazaar.objects.get(pk = pk)
        wishlist = request.session.get('wishlist',[])
        item = {'name_of_product':product.name, 'Price':product.price, 'Id':product.pk}
        wishlist.append(item)
        request.session['wishlist'] = wishlist
    return render(request, 'wishlist.html')
