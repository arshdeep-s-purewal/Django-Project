from django.shortcuts import render
from apna_bazaar.forms import ApnaBazaarForm
from apna_bazaar.models import ApnaBazaar
# Create your views here.
def add_product(request):
    form = ApnaBazaarForm()
    if request.method == 'POST':
        form = ApnaBazaarForm(request.POST)
        # if form.is_valid():
        form.save()

    return render(request, 'add_product.html', {'forms':form})

def show_products(request):
    products = ApnaBazaar.objects.all()
    return render(request, 'products.html', {'Products':products})

def show_product_detail(request):
    products = ApnaBazaar.objects.all()
    return render(request, 'product_detail.html', {'Products':products})

def add_to_cart():
    pass
