from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Add_ewaste
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class EgarbagePageView(TemplateView):
    template_name = 'ewaste.html'

class AddewastePageView(TemplateView):
    template_name = 'addewaste.html'

    
def Login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('email'), password=request.POST.get('password'))
        if user is not None:
            return render(request, 'MainPageAfterLogin.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

class RegisterPageView(TemplateView):
    template_name = 'register.html'

class MainPageView(TemplateView):
    template_name = 'mainpage.html'

def Register_view(request):
    if request.method == 'POST':
        user = User.objects.create_user(request.POST.get('name'), request.POST.get('email'), request.POST.get('password'))
        user.save()
        return render(request, 'MainPageAfterLogin.html')
    else:
        return render(request, 'register.html')

def add_ewaste(request):
    if request.method == 'POST':
        form = Add_ewaste()
        form.Name = request.POST.get('name')
        form.Surname = request.POST.get('surname')
        form.Ward = request.POST.get('ward no')
        form.Mob_number = request.POST.get('number')
        form.Email = request.POST.get('email')
        form.Address = request.POST.get('address')
        print(form.Address)
        form.Image = request.FILES['image']
        form.save()
        return render(request, 'MainPageAfterLogin.html')
    else:
        print('abcd')
        return render(request, 'addewaste.html')
