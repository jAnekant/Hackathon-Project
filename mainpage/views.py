from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Login

class LoginPageView(TemplateView):
    template_name = 'login.html'
    success_url='maiPage.html'

class RegisterPageView(TemplateView):
    template_name = 'register.html'

class MainPageView(TemplateView):
    template_name = 'mainpage.html'

def Login_view(request):
    if request.method == 'POST':
        record = Login()
        record.email = request.POST.get('email')
        record.pwd   = request.POST.get('password')
        record.login   = request.POST.get('login')
        record.state   = request.POST.get('state')
        record.city   = request.POST.get('city')
        record.address   = request.POST.get('address')
        print(record.email)
        print(record.pwd)
        record.save()
        return render(request, 'register.html')
    else:
        return render(request, 'register.html')
