from django.urls import path, include

from . import views
app_name = "myProfile"

urlpatterns =[
    path('', views.homepage, name = 'homepage') 
]