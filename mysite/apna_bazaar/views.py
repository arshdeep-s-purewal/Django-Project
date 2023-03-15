from django.shortcuts import render
from apna_bazaar.forms import ApnaBazaarForm
from apna_bazaar.models import ApnaBazaar
from mysite.core.cart_helper import add_item_to_cart, remove_item_from_cart
# Create your views here.
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
        