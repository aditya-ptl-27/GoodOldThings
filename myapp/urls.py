from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout'),
    path('logout',views.logout,name='logout'),
    # path('lender_index',views.lender_index,name='lender_index'),
]