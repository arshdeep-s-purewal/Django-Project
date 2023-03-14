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

def show_product_detail(request, **kwargs):
    # import pdb;pdb.set_trace()
    context={}
    if pk := kwargs.get('pk'):
        # import pdb;pdb.set_trace()
        # request.session['name'] = 'Arsh'
        name = request.session.get('name')
        product = ApnaBazaar.objects.get(pk = pk)
    context = {'Product':product, 'name':name}
    return render(request, 'product_detail.html', context)



# def add_to_cart(request, **kwargs):
#     context={}
#     import pdb;pdb.set_trace()
#     # if request.session['cart'] ==  []:
#     if pk := kwargs.get('pk'):
#         product = ApnaBazaar.objects.get(pk = pk)
#         # request.session['cart'] = []
#         item = {'name_of_product':product.Name, 'Price':product.Price}
#         request.session['cart'].append(item)
#         name = request.session['cart'] 
#     context = {'name':name}
#     return render(request, 'cart.html', context)

def add_to_cart(request, **kwargs):
    # context={}
    # import pdb;pdb.set_trace()
    if pk := kwargs.get('pk'):
        product = ApnaBazaar.objects.get(pk = pk)
        cart = request.session.get('cart',[])
        item = {'name_of_product':product.Name, 'Price':product.Price}
        cart.append(item)
        request.session['cart'] = cart
        name = request.session['cart']
        return render(request,'cart.html', {'name':name})