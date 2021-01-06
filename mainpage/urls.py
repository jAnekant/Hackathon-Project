from django.urls import path
from .views import LoginPageView, RegisterPageView,MainPageView

urlpatterns = [
    path('', MainPageView.as_view(),name='mainpage'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('register/', RegisterPageView.as_view(), name='register'),
]