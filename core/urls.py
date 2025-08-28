from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_view, name='hello'),
    path('nombre/', views.nombre_view, name='nombre'),
]
