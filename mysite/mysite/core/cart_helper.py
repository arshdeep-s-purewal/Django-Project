from apna_bazaar.models import ApnaBazaar

def add_item_to_cart(request, **kwargs):
    if pk := kwargs.get('pk'):
        product = ApnaBazaar.objects.get(pk = pk)
        cart = request.session.get('cart',[])
        # import pdb;pdb.set_trace()
        item = {'name_of_product':product.name, 'Price':product.price, 'Id':product.pk, 'product_image':product.product_image.url}
        cart.append(item)
        request.session['cart'] = cart
    return request.session['cart']

# def add_item_to_cart(request, **kwargs):
#     import pdb;pdb.set_trace()
#     if pk := kwargs.get('pk'):
#         product = ApnaBazaar.objects.get(pk=pk)
#         cart= request.session.get('cart', {})
#         # print(request.session['cart'])
#         for i in cart:
#             if pk in i:
#                 cart[pk]['quantity'] += 1
#             else:
#                 cart = {'name_of_product':product.name, 'Price':product.price, 'Id':product.pk, 'product_image':product.product_image.url, 'quantity':1}
                
#             request.session['cart'] = cart
#         return request.session['cart']

def remove_item_from_cart(request, **kwargs):
    # import pdb;pdb.set_trace()
    if pk := kwargs.get('pk'):
        product = ApnaBazaar.objects.get(pk = pk)
        for i in request.session['cart']:
            if i['Id'] == product.pk:
                request.session['cart'].remove(i)
    
    return request.session['cart']          