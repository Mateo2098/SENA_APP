from django.urls import path
from . import views

urlpatterns = [
    path('instructores/', views.instructores, name='lista_instructores'),
    path('instructor/<int:id_aprendiz>/', views.detalle_instructor, name='detalle_instructor'),
]