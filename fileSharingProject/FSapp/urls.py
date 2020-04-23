from django.urls import path
from . import views

urlpatterns = [
	path('', views.fshome, name='fshome'),
]