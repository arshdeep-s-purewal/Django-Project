from apna_bazaar.models import ApnaBazaar

def add_item_to_cart(request, **kwargs):
    # import pdb;pdb.set_trace()
    if pk := kwargs.get('pk'):
        product = ApnaBazaar.objects.get(pk = pk)
        cart = request.session.get('cart',[])
        item = {'name_of_product':product.name, 'Price':product.price, 'Id':product.pk}
        cart.append(item)
        request.session['cart'] = cart
    return request.session['cart']

# def add_item_to_cart(request, **kwargs):
#     product = ApnaBazaar.objects.get(pk = pk)
#     cart = request.session.get('cart',{})
#     if str(kwargs) in cart:
#         cart

def remove_item_from_cart(request, **kwargs):
    # import pdb;pdb.set_trace()
    if pk := kwargs.get('pk'):
        product = ApnaBazaar.objects.get(pk = pk)
        for i in request.session['cart']:
            if i['Id'] == product.pk:
                request.session['cart'].remove(i)
    
    return request.session['cart']          