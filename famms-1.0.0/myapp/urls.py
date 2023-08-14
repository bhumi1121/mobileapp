from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('blog_list',views.blog_list,name='blog_list'),
    path('contact',views.contact,name='contact'),
    path('product',views.product,name='product'),
    path('testimonial',views.testimonial,name='testimonial'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('fpswd',views.fpswd,name='fpswd'),
    path('verify_otp',views.verify_otp,name='verify_otp'),
    path('set_pswd',views.set_pswd,name='set_pswd'),
    path('seller_index',views.seller_index,name='seller_index'),
    path('add_mobile',views.add_mobile,name='add_mobile'),
    path('mobiles',views.mobiles,name='mobiles'),
    path('update_mobile/<int:pk>',views.update_mobile,name='update_mobile'),
    path('delete_mobile/<int:pk>',views.delete_mobile,name="delete_mobile"),
    path('search',views.search,name='search'),
]
