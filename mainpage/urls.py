from django.urls import path
from .views import Login_view, RegisterPageView,MainPageView,Register_view

urlpatterns = [
    path('', MainPageView.as_view(),name='mainpage'),
    path('register/', Register_view),
    path('login/', Login_view),
    path('register/', RegisterPageView.as_view(), name='register'),
]