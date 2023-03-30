from django.shortcuts import render,redirect,HttpResponse
from apna_bazaar.forms import ApnaBazaarForm, CreateNewUserForm, AddAddressForm
from apna_bazaar.models import ApnaBazaar, Wishlist, Address, Order, OrderItem
from mysite.core.cart_helper import add_item_to_cart, remove_item_from_cart
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.serializers import ModelSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

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
            return redirect('homepage')
    return render(request,'login_ecom.html',{})

def logout_user_ecom(request):
    # import pdb;pdb.set_trace()
    del request.session['cart']
    logout(request)
    return redirect("homepage")

def home(request):
    return render(request, 'home.html')

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


@api_view(http_method_names=('post',))
def login_user_view(request):
    # import pdb;pdb.set_trace()
    username = request.data['username']
    password = request.data['password']
    user = authenticate(username=username,password=password)
    login(request, user)
    u = User.objects.get(username = username)
    token = Token.objects.create(user = u)
    # print(token)
    serializer = UserSerializer(user)
    return Response({"data":serializer.data, "Token":token.key,})

@api_view(http_method_names=('post',))
@permission_classes([IsAuthenticated])
def logout_api(request):
    # import pdb;pdb.set_trace()
    request.user.auth_token.delete()
    logout(request)
    return Response({"data":"Logout Successful"})

class ProductSerializer(ModelSerializer):
    class Meta:
        model = ApnaBazaar
        fields = '__all__'

@api_view()
def show_products(request):
    product_list = ApnaBazaar.objects.all()
    return Response({"Product_list": ProductSerializer(product_list, many = True).data})

@api_view(http_method_names=('post',))
def add_product_view(request):
    # import pdb; pdb.set_trace()
    serializer = ProductSerializer(data = request.data)
    serializer.is_valid()
    serializer.save()
    return Response({"data":serializer.data})


@api_view(http_method_names=('put',))
def update_product_view(request, pk):
    # import pdb; pdb.set_trace()
    product = ApnaBazaar.objects.get(id=pk)
    serializer = ProductSerializer(product,data = request.data,)
    serializer.is_valid()
    serializer.save()
    return Response({"message":serializer.data})

@api_view(http_method_names = ('patch',))
def partial_update(request, pk):
    prodcut = ApnaBazaar.objects.get(id = pk)
    serializer = ProductSerializer(prodcut, data = request.data, partial = True)
    serializer.is_valid()
    serializer.save()
    return Response({"updated_data":serializer.data})

@api_view(http_method_names=('delete',))
def delete_product(request,pk):
    prod = ApnaBazaar.objects.get(id=pk)
    prod.delete()
    return Response({"message":"product_deleted"})

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

@api_view()
@permission_classes([IsAuthenticated])
def show_address(request):
    addr = Address.objects.all()
    address = AddressSerializer(addr, many = True)
    return Response({'data':address.data})

@api_view(http_method_names=('post',))
@permission_classes([IsAuthenticated])
def add_new_address(request):
    # import pdb;pdb.set_trace()
    request.data['user'] = request.user.id
    serializer = AddressSerializer(data = request.data)
    serializer.is_valid()
    serializer.save()
    return Response({'data':serializer.data})

# @api_view(http_method_names=('post',))
# def update_address_put(request, user_id, address_id):
#     addr = AddressSerializer.objects.get()
#     pass

@api_view(http_method_names=('put',))
@permission_classes([IsAuthenticated])
def update_address_view(request, pk):
    try:
        request.data['user'] = request.user.id
        address = Address.objects.get(id=pk, user=request.user.id)
        serializer = AddressSerializer(address, data = request.data)
        if serializer.is_valid():
            serializer.save()
    except:
        return  Response({'Message':' Address Not Found!'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'Address':serializer.data}, status=status.HTTP_200_OK)

@api_view(http_method_names=('patch',))
@permission_classes([IsAuthenticated])
def partial_update_address_view(request, pk):
    try:
        request.data['user'] = request.user.id
        address = Address.objects.get(id=pk, user_id = request.user.id)
        print(address)
        serializer = AddressSerializer(address, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
    except:
        return  Response({'Message':' Address Not Found!'})
    return Response({'Address':serializer.data}, status=status.HTTP_200_OK)

# @permission_required('blog.add_blog',raise_exception=True)
def add_product(request):
    form = ApnaBazaarForm()
    if request.method == 'POST':
        form = ApnaBazaarForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            print("ss")
            form.save()
            return redirect('success')
        else:
            ApnaBazaarForm()
    return render(request, 'add_product.html', {'forms':form})

def success(request):
    return render(request, 'success.html')

# def show_products(request):
#     products = ApnaBazaar.objects.all()
#     return render(request, 'products.html', {'Products':products})

def show_product_detail(request, **kwargs):
    # context={}
    if pk := kwargs.get('pk'):
        # name = request.session.get('name')
        product = ApnaBazaar.objects.get(pk = pk)
    # context = {'Product':product, 'name':name}

    return render(request, 'product_detail.html', {'Product':product})


def add_to_cart(request, **kwargs):
    """
    Step 1:- create add to cart form 
    step 2:- save product in session
    Step 3:- Redirect to cart page
    """
    if request.user.is_authenticated:
        adc = add_item_to_cart(request, **kwargs)
    else:
        redirect('login_ecom')
    return redirect('cart')
    # return render(request,'cart.html', {'name':adc})
    
def remove_from_cart(request, **kwargs):
    remove_item_from_cart(request, **kwargs)
    # return redirect('cart')        
    return render(request, 'cart.html', )

# def add_to_wishlist(request, **kwargs):
#     if pk := kwargs.get('pk'):
#         product = ApnaBazaar.objects.get(pk = pk)
#         wishlist = request.session.get('wishlist',[])
#         item = {'name_of_product':product.name, 'Price':product.price, 'Id':product.pk, 'product_image':product.product_image}
#         wishlist.append(item)
#         request.session['wishlist'] = wishlist
#     return render(request, 'wishlist.html')

def show_cart(request):
    return render(request,'cart.html')

def show_products_listing(request):
    product_list = ApnaBazaar.objects.all()
    paginator = Paginator(product_list, 3) 
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    return render(request, 'products.html', {'Products':products})

def add_to_wishlist(request, **kwargs):
    # import pdb;pdb.set_trace()
    if pk := kwargs.get('pk'):
        product = ApnaBazaar.objects.get(pk = pk)
        Wishlist.objects.create(product = product, user = request.user)
    
    return redirect('show_products')
    
def show_wishlist(request):
    wish_list = Wishlist.objects.filter(user = request.user)
    return render(request, 'wishlist.html', {'wish_list':wish_list})
 
def remove_from_wishlist(request, **kwargs):
    # import pdb;pdb.set_trace()
    if pk := kwargs.get('pk'):
        product = Wishlist.objects.get(pk = pk)
        product.delete()
    return redirect('wishlist')

def shipping_details(request):
    form = AddAddressForm()
    if request.method == 'POST':
        form = AddAddressForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print("ss")
            form.save()
            return redirect('success')
        else:
            AddAddressForm()
    # return render(request, 'add_product.html', {'forms':form})
    return render(request, 'shipping_details_address.html', {'forms':form})

def checkout(request):
    # import pdb;pdb.set_trace()
    total = 0
    for i in request.session['cart']:
        total += int(i['Price'])*int(i['quantity'])
    address = Address.objects.filter(user = request.user)
    return render(request, 'checkout.html', {'address':address, 'total':total})

def userprofile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return redirect('login_ecom')
    
def ordered(request, **kwargs):
    # import pdb;pdb.set_trace()
    shipping_address = Address.objects.filter(user = request.user)
    total_price = 0
    for i in request.session['cart']:
        total_price += int(i['Price'])*int(i['quantity'])
    Order.objects.create(user = request.user, address = shipping_address, total =  total_price)
    order = Order.objects.filter(user = request.user)
    for i in request.session['cart']:
        OrderItem.objects.create(order = order, product_id = i['Id'], price = i['Price'])
    return redirect('success')


# def update_password(request):
#     u = User.objects.get(username=request.user)
#     u.set_password('new password')
#     u.save()