from distutils.log import error
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from Account.models import Customer
from Product.models import Category

# Create your views here.
class registration(View):
    def post(self, request):
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']

        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'User name is used')
                return redirect('registration')

            elif User.objects.filter(email = email).exists():
                messages.info(request, 'This Email is used')
                return redirect('registration')

            else:
                user = User.objects.create_user(username = username, password = password1, email = email, first_name = name)
                user.save();
                Customers = Customer(name = name, email = email, address = address, city = city, phone = phone, password = password1)
                Customers.password = make_password(Customers.password)
                Customers.save();
                return redirect('login')

        else:
            messages.info(request, 'Password not matched')
            return redirect('registration')

    def get(self, request):
        Categories = Category.objects.all() 
        return render(request, 'registration.html', {'name' : 'Registration', 'Category' : Categories})


class login(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        data = request.POST.get('data')

        user = auth.authenticate(username = username, password = password)
        Customers = Customer.objects.filter(email = username).first()
        if user is not None:
            if Customers:
                flag = check_password(password, Customers.password)
                if flag:
                    request.session['customer_email'] = Customers.email
                    if data:
                        return redirect('cart/checkout')
                    else:
                        return redirect('/')
                else:
                    error_message = 'Invalid Password'
                    return redirect('login', {'error_message': error_message})
            else:
                auth.login(request, user)
                return redirect('/')
        else:
            if Customers:
                flag = check_password(password, Customers.password)
                if flag:
                    request.session['customer_email'] = Customers.email
                    return redirect('/')
                else:
                    error_message = 'Invalid Password'
                    return redirect('login', {'error_message': error_message})

            else:
                error_message = 'Invalid Password/Email'
                return redirect('login', {'error_message': error_message})


    def get(self, request):
        Categories = Category.objects.all() 
        return render(request, 'login.html', {'name' : 'Login', 'Category' : Categories})



def logout(request):
    auth.logout(request);
    for key in list(request.session.keys()):
        del request.session[key]
    return redirect('index')