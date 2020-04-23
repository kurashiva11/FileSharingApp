from django.urls import path
from . import views

urlpatterns = [
	path('', views.authhome, name='authhome'),
	path('register', views.register, name='register'),
	path('login', views.login, name='login'),
	path('signout', views.signout, name='signout'),
]