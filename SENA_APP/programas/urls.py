from django.urls import path
from . import views

urlpatterns = [
    path('programas/', views.programas, name='lista_programas'),
    path('programas/<str:codigo_programa>/', views.detalle_programa, name='detalle_programa'),

]

