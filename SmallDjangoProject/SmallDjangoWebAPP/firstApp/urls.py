from django.contrib import admin
from django.urls import path
from firstApp import views
urlpatterns = [
    path('', views.index, name='Home' ),
    path('index', views.index, name='Home' ),
    path('about', views.about, name='about'),
    path('pages', views.pages, name='pages'),
    path('documentations', views.documentations, name='documentations'),
    path('services', views.service, name='services'),
    path('blogs', views.blogs, name='blogs'),
    path('directions', views.directions, name='directions'),
    path('products', views.products, name='products'),
    path('locations', views.locations, name='locations'),
    path('links', views.links, name='links'),
    path('contacts', views.contacts, name='contacts'),   
    path('disclaimer', views.disclaimer, name='disclaimer'),   
    path('privacypolicy', views.privacypolicy, name='privacypolicy'),
       
   ## For compatibility with general html code 
    path('index.html', views.index, name='Home' ),
    path('about.html', views.about, name='about'),
    path('pages.html', views.pages, name='pages'),
    path('documentations.html', views.documentations, name='documentations'),
    path('services.html', views.service, name='services'),
    path('blogs.html', views.blogs, name='blogs'),
    path('directions.html', views.directions, name='directions'),
    path('products.html', views.products, name='products'),
    path('locations.html', views.locations, name='locations'),
    path('links.html', views.links, name='links'),
    path('contacts.html', views.contacts, name='contacts'),
    path('disclaimer.html', views.disclaimer, name='disclaimer'),
    path('privacypolicy.html', views.privacypolicy, name='privacypolicy')
]
