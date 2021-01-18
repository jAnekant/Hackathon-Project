from django.urls import path
from .views import LoginPageView, RegisterPageView,MainPageView,Login_view

urlpatterns = [
    path('', MainPageView.as_view(),name='mainpage'),
    path('register/', Login_view),
    path('login/', LoginPageView.as_view(), name='login'),
    path('register/', RegisterPageView.as_view(), name='register'),
]