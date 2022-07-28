from django.shortcuts import render
from django.views import View

# Create your views here.
class index(View):
    def post(self, request):
        return render(request, 'shopDetails.html', {'name' : 'Shop Details'})

    def get(self, request):
        return render(request, 'index.html', {'item' : 'Hi'})
