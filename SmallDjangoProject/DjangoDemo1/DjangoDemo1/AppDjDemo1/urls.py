from django.urls import path
from . import views


urlpatterns = [
      path('', views.home, name='home'),
      path("numbers/<int:Numbers>", views.numbers, name='numbers'),
      path("names/<str:Names>", views.Member_Names, name='Member_Names'),
      path('index', views.index, name='index'),
      path('Viewindex/', views.Viewindex, name='Viewindex'),
      path('wfb/', views.wfb, name='wfb'),
      path('AppDjDemo1/baseTemplateDemo/', 
           views.baseTemplateDemo, name='baseTemplateDemo'),
      path('AppDjDemo1/HomeTemplateDemo/', 
           views.HomeTemplateDemo, name='HomeTemplateDemo'),
      path('login/', views.login, name='login'),
      path('logout/', views.logout_view, name='logout'),
      
      
]
