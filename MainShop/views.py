from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from Product.models import Product, Category
from Account.models import Customer
from Cart.models import Order
from MainShop.models import Intro


# Create your views here.
class index(View):
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

        Products = Product.objects.get(id = Products)
        Products = Product.objects.filter(category = Products.category)
        trendy_products = Product.objects.filter(trendy = True)
        return render(request, 'product_by_categories.html', {'Product' : Products, 'trendy_product' : trendy_products})

    def get(self, request):
        customer_email = request.session.get('customer_email')
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
            
        Categories = Category.objects.all()

        category_id = request.GET.get('Categories')
        if category_id:
            request.session['category_id'] = category_id
            return redirect('by_category')

        product_id = request.GET.get('Products')
        if product_id:
            request.session['product_id'] = product_id
            return redirect('by_id')

        trendy_products = Product.objects.filter(trendy = True)
        Intros = Intro.objects.all()
        return render(request, 'index.html', {'Category' : Categories, 'trendy_product' : trendy_products, 'customer_email' : customer_email, 'Intro' : Intros})


class shop(View):
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
        return redirect('shop')

    def get(self, request):
        Products = Product.objects.all()
        trendy_products = Product.objects.filter(trendy = True)

        product_id = request.GET.get('Products')
        if product_id:
            request.session['product_id'] = product_id
            return redirect('by_id')

        Categories = Category.objects.all()

        category_id = request.GET.get('Categories')
        if category_id:
            request.session['category_id'] = category_id
            return redirect('by_category')

        return render(request, 'shop.html', {'Category' : Categories, 'Product' : Products, 'trendy_product' : trendy_products})


class shopDetail(View):
    def post(self, request):
        pass

    def get(self, request):
        Categories = Category.objects.all() 
        category_id = request.GET.get('Categories')
        if category_id:
            request.session['category_id'] = category_id
            return redirect('by_category')

        trendy_products = Product.objects.filter(trendy = True)
        return render(request, 'shopDetail.html', {'Category' : Categories, 'trendy_product' : trendy_products})


class contact(View):
    def post(self, request):
        pass

    def get(self, request):
        Categories = Category.objects.all() 
        category_id = request.GET.get('Categories')
        if category_id:
            request.session['category_id'] = category_id
            return redirect('by_category')
        trendy_products = Product.objects.filter(trendy = True)
        return render(request, 'contact.html', {'Category' : Categories, 'trendy_product' : trendy_products})


class profile(View):
    def post(self, request):
        pass

    def get(self, request):
        customer_email = request.session.get('customer_email')
        if customer_email:
            Customers = Customer.objects.filter(email = customer_email).first()
            Orders = Order.objects.filter(Customer = Customers).order_by('-date')

            return render(request, 'profile.html', {'name' : 'Your Orders', 'Order': Orders, 'Customers' : Customers})


        if request.user.is_authenticated:
            Customers = Customer.objects.filter(email = request.user.email).first()
            Orders = Order.objects.filter(Customer = Customers).order_by('-date')

            return render(request, 'profile.html', {'name' : 'Your Orders', 'Order': Orders})

        Categories = Category.objects.all()
        category_id = request.GET.get('Categories')
        if category_id:
            request.session['category_id'] = category_id
            return redirect('by_category') 

        trendy_products = Product.objects.filter(trendy = True)
        return render(request, 'profile.html', {'Category' : Categories, 'name' : 'Your Not', 'trendy_product' : trendy_products})


        
