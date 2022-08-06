from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from Product.models import Product, Category

# Create your views here.
class by_category(View):
    def post(self, request):
        Products = request.POST.get('Products')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(Products)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(Products)
                    else:
                        cart[Products] = quantity - 1
                else:
                    cart[Products] = quantity + 1
            else:
                cart[Products] = 1
        else:
            cart = {}
            cart[Products] = 1
        
        request.session['cart'] = cart
        
        return redirect('by_category')

    def get(self, request):
        product_id = request.GET.get('Products')
        if product_id:
            request.session['product_id'] = product_id
            return redirect('by_id')

        category_id = request.session.get('category_id')
        if category_id:
            Products = Product.objects.filter(category = category_id)
        
        category_id = request.GET.get('Categories')
        if category_id:
            Products = Product.objects.filter(category = category_id)

        Categories = Category.objects.all()
        trendy_products = Product.objects.filter(trendy = True)
        return render(request, 'product_by_categories.html', {'Category' : Categories, 'Product' : Products, 'trendy_product' : trendy_products})
            
        

class by_id(View):
    def post(self, request):
        Products = request.POST.get('Products')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(Products)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(Products)
                    else:
                        cart[Products] = quantity - 1
                else:
                    cart[Products] = quantity + 1
            else:
                cart[Products] = 1
        else:
            cart = {}
            cart[Products] = 1
        
        request.session['cart'] = cart
        
        request.session['product_id'] = Products
        return redirect('by_id')

    def get(self, request):
        products = request.GET.get('Products')
        product_id = request.session.get('product_id')
        if products:
            Products = Product.objects.filter(id = products)

        elif product_id:
            Products = Product.objects.filter(id = product_id)

        category_id = request.GET.get('Categories')
        if category_id:
            request.session['category_id'] = category_id
            return redirect('by_category')
            

        Categories = Category.objects.all()
        trendy_products = Product.objects.filter(trendy = True)
        return render(request, 'product_by_id.html', {'Category' : Categories, 'Product' : Products, 'trendy_product' : trendy_products})
        
