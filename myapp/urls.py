from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('logout/',views.logout,name='logout'),
    # path('lender_index/',views.lender_index,name='lender_index'),
    path('profile/',views.profile,name='profile'),
    path('change_password/',views.change_password,name='change_password'),
    path('forgot_password/',views.forgot_password,name='forgot_password'),
    path('verify_otp/',views.verify_otp,name='verify_otp'),
    path('update_password/',views.update_password,name='update_password'),
    path('add_product/',views.add_product,name='add_product'),
]