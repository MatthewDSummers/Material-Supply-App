from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.user_page),
    path('admin', views.admin_page),
    path('management', views.mgmt_page),
]