from django.views.generic import TemplateView

class LoginPageView(TemplateView):
    template_name = 'login.html'
    success_url='maiPage.html'

class RegisterPageView(TemplateView):
    template_name = 'register.html'

class MainPageView(TemplateView):
    template_name = 'mainpage.html'
