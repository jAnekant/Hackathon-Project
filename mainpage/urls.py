from django.urls import path
from .views import Login_view, RegisterPageView,MainPageView,Register_view,EgarbagePageView,add_ewaste,detail_ewaste,detail_ewaste2\
    ,detail_ewaste3,detail_ewaste4,detail_ewaste5,detail_ewaste6,detail_ewaste_all,pay_ewaste_bill,sell_ewaste,main_page_after_login

urlpatterns = [
    path('', MainPageView.as_view(),name='mainpage'),
    path('register/', Register_view),
    path('login/', Login_view),
    path('register/', RegisterPageView.as_view(), name='register'),
    path('ewaste/', EgarbagePageView.as_view(), name='ewaste'),
    path('addewaste/', add_ewaste),
    path('detail_ewaste/' ,detail_ewaste),
    path('detail_ewaste2/' ,detail_ewaste2),
    path('detail_ewaste3/' ,detail_ewaste3),
    path('detail_ewaste4/' ,detail_ewaste4),
    path('detail_ewaste5/' ,detail_ewaste5),
    path('detail_ewaste6/' ,detail_ewaste6),
    path('detail_ewaste_all/' ,detail_ewaste_all),
    path('pay_ewaste_bill/',pay_ewaste_bill),
    path('sell_ewaste/',sell_ewaste),
    path('mainpageafterlogin/',main_page_after_login)
]