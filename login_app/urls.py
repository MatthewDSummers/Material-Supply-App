from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register_user),
    path('register-page', views.reg_page),
    path('login', views.login),
    path('signin', views.signin_page),
    path('logout', views.logout),
    # path('login/<int:ticket_sender_id>', views.user_profile),
]
