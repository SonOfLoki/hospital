from django.urls import path
from .views import HomePage, AboutPage, DoctorPage,NewsPage, DetailPage, ContactPage

urlpatterns = [
    path('contact/', ContactPage, name='contact' ),
    path('news/<slug:slug>/', DetailPage, name='blog-detail'),
    path('news/',NewsPage, name='blog' ),
    path('doctors/', DoctorPage, name='doctorpage'),
    path('about/', AboutPage, name='about'),
    path('', HomePage, name='home')
]