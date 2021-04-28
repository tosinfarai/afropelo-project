from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    #path('', views.home, name='home'),
    path('', views.shop, name='home'),
    path('shop/', views.shop, name='shop'),
    path('shop/<int:product_id>/', views.detail, name='detail'),
    path('about/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact'),
]
