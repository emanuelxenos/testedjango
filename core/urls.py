from django.contrib import admin
from django.urls import path, include
from .views import home, salvar, editar, update, apagar, init, register

urlpatterns = [
    path('', init),
    path('salvar/',salvar, name="salvar"),
    path('editar/<int:id>',editar, name="editar"),
    path('update/<int:id>',update, name="update"),
    path('apagar/<int:id>',apagar, name="apagar"),
    path('register/', register),
    path('home/', home),
]
