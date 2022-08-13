from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

from Product.models import Product, Category
from Account.models import Customer
from Cart.models import Order

# Create your views here.
class cartDetail(View):
    def post(self, request):
        Products = request.POST.get('Products')
        remove = request.POST.get('remove')
        remove_item = request.POST.get('remove_item')

        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(Products)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(Products)
                    else:
                        cart[Products] = quantity - 1
                elif remove_item:
                    cart.pop(Products)
                else:
                    cart[Products] = quantity + 1
            else:
                cart[Products] = 1
        else:
            cart = {}
            cart[Products] = 1
        
        request.session['cart'] = cart

        return redirect('cartDetail')

    def get(self, request):
        ids = list(request.session.get('cart').keys())
        Products = Product.objects.filter(id__in = ids)

        Categories = Category.objects.all()
        category_id = request.GET.get('Categories')
        if category_id:
            request.session['category_id'] = category_id
            return redirect('by_category')
        return render(request, 'cartDetail.html', {'Category' : Categories, 'Product' : Products})


class checkout(View):
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        cart = request.session.get('cart')
        Products = Product.objects.filter(id__in = list(cart.keys()))

        customer_email = request.session.get('customer_email')

        if customer_email:
            if Customer.objects.filter(email = customer_email).exists():
                Customers = Customer.objects.get(email = customer_email)
                for item in Products:
                    Orders = Order(Product = item,  Customer = Customers, price = item.price, quantity = cart.get(str(item.id)))
                    Orders.save();

                request.session['cart'] = {}

                Orders = Order.objects.filter(Customer = Customers)
                Categories = Category.objects.all() 
                return render(request, 'orderHistory.html', {'name' : 'Order History', 'Category' : Categories, 'Order': Orders, 'Customers' : Customers})

            else:
                pass

        elif request.user.is_authenticated:
            if Customer.objects.filter(email = email).exists():
                Customers = Customer.objects.get(email = email).first()
                for item in Products:
                    Orders = Order(Product = item,  Customer = Customers, price = item.price, quantity = cart.get(str(item.id)))
                    Orders.save();
                        
                request.session['cart'] = {}
                return redirect('orderHistory')

            else:
                Customers = Customer(name = name, email = email, address = address, city = city, phone = phone, password = password1)
                Customers.password = make_password(Customers.password)
                Customers.save();
                for item in Products:
                    Orders = Order(Product = item,  Customer = Customers, price = item.price, quantity = cart.get(str(item.id)))
                    Orders.save();
                                
                request.session['cart'] = {}
                return redirect('orderHistory')

        elif Customer.objects.filter(email = email).exists():
            
            #return redirect('login', {'data' : "n"})
            pass

        else:
            if password1 == password2:
                Customers = Customer(name = name, email = email, address = address, city = city, phone = phone, password = password1)
                Customers.password = make_password(Customers.password)
                Customers.save();
                for item in Products:
                    Orders = Order(Product = item,  Customer = Customers, price = item.price, quantity = cart.get(str(item.id)))
                    Orders.save();

                request.session['customer_email'] = email               
                request.session['cart'] = {}
                return redirect('orderHistory')

            else:
                data = {}
                data['name'] = name
                data['email'] = email
                data['phone'] = phone
                data['address'] = address
                data['city'] = city

                return redirect('checkout', {'data' : data})
                    
                

    def get(self, request):
        ids = list(request.session.get('cart').keys())
        Products = Product.objects.filter(id__in = ids)
        
        customer_email = request.session.get('customer_email')
        if customer_email:
            Customers = Customer.objects.get(email = customer_email)
        elif request.user.is_authenticated:
            Customers = request.user
        else:
            Customers = None
        Categories = Category.objects.all() 
        category_id = request.GET.get('Categories')
        if category_id:
            request.session['category_id'] = category_id
            return redirect('by_category')
        return render(request, 'checkout.html',  {'Customers' : Customers, 'Category' : Categories, 'Product' : Products})


class orderHistory(View):
    def post(self, request):
        return render(request, 'orderHistory.html', {'name' : 'Order History2'})

    def get(self, request):
        customer_email = request.session.get('customer_email')
        if customer_email:
            if Customer.objects.filter(email = customer_email).exists():
                Customers = Customer.objects.filter(email = customer_email).first()
                Orders = Order.objects.filter(Customer = Customers).order_by('-date')

        elif request.user.is_authenticated:
            Customers = Customer.objects.filter(email = request.user.email).first()
            Orders = Order.objects.filter(Customer = Customers).order_by('-date')

        Categories = Category.objects.all() 
        category_id = request.GET.get('Categories')
        if category_id:
            request.session['category_id'] = category_id
            return redirect('by_category')
        return render(request, 'orderHistory.html', {'name' : 'Order History', 'Category' : Categories, 'Order': Orders, 'Customers' : Customers})