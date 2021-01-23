from django.urls import path
from .views import Login_view, RegisterPageView,MainPageView,Register_view,EgarbagePageView,AddewastePageView,add_ewaste

urlpatterns = [
    path('', MainPageView.as_view(),name='mainpage'),
    path('register/', Register_view),
    path('login/', Login_view),
    path('register/', RegisterPageView.as_view(), name='register'),
    path('ewaste/', EgarbagePageView.as_view(), name='ewaste'),
    #path('addewaste/', AddewastePageView.as_view(), name='addewaste'),
    path('addewaste/', add_ewaste),
]