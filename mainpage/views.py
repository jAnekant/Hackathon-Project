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
    template_name = 'index.html'

def main_page_after_login(request):
    return render(request, 'MainPageAfterLogin.html')

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
        form.Price = request.POST.get('price')
        form.description = request.POST.get('description')
        form.Image = request.FILES['image']
        form.save()
        return render(request, 'sell_ewaste.html')
    else:
        return render(request, 'addewaste.html')

def pay_ewaste_bill(request):
    return render(request, 'pay_ewaste_bill.html')

def sell_ewaste(request):
    return render(request,'sell_ewaste.html')

def detail_ewaste_all(request):
    obj = Add_ewaste.objects.all()
    context = {
        "object_list":obj,
    }
    return render(request,'details/detail_ewaste_all.html',context)

def detail_ewaste(request):
    obj = Add_ewaste.objects.all()
    context = {
        "object_list":obj,
    }
    return render(request,'details/detail_ewaste.html',context)

def detail_ewaste2(request):
    obj = Add_ewaste.objects.all()
    context = {
        "object_list":obj,
    }
    return render(request,'details/detail_ewaste2.html',context)

def detail_ewaste3(request):
    obj = Add_ewaste.objects.all()
    context = {
        "object_list":obj,
    }
    return render(request,'details/detail_ewaste3.html',context)

def detail_ewaste4(request):
    obj = Add_ewaste.objects.all()
    context = {
        "object_list":obj,
    }
    return render(request,'details/detail_ewaste4.html',context)

def detail_ewaste5(request):
    obj = Add_ewaste.objects.all()
    context = {
        "object_list":obj,
    }
    return render(request,'details/detail_ewaste5.html',context)

def detail_ewaste6(request):
    obj = Add_ewaste.objects.all()
    context = {
        "object_list":obj,
    }
    return render(request,'details/detail_ewaste6.html',context)
