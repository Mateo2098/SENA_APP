from django.db import models

class Programas(models.Model):
    NIVEL_FORMACION_CHOICES = [
        ('AUX', 'Auxiliar'),
        ('OPE', 'Operario'),
        ('TECNICO', 'Técnico'),
        ('TECNOLOGO', 'Tecnólogo'),
        ('ESP', 'Especialización Tecnológica'),
        ('COM', 'Complementario'),
    ]
    
    MODALIDAD_CHOICES = [
        ('PRE', 'Presencial'),
        ('VIR', 'Virtual'),
        ('MIX', 'Mixto'),
    ]
    
    ESTADO_CHOICES = [
        ('ACT', 'Activo'),
        ('INA', 'Inactivo'),
        ('SUS', 'Suspendido'),
        ('CAN', 'Cancelado'),
    ]
    codigo_programa = models.CharField(max_length=20, unique=True, verbose_name="Código del Programa")
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Programa")
    modalidad = models.CharField(max_length=50, choices=MODALIDAD_CHOICES, default='PRE')
    duracion_meses = models.PositiveIntegerField(verbose_name="Duración en Meses")
    duracion_horas = models.PositiveIntegerField(verbose_name="Duración en Horas")
    descripcion = models.TextField(verbose_name="Descripción del Programa")
    competencias = models.TextField(verbose_name="Competencias a desarrollar")
    perfil_egreso = models.TextField(verbose_name="Perfil de Egreso")
    requisitos_ingreso = models.TextField(verbose_name="Requisitos de Ingreso")
    centro_formacion = models.CharField(max_length=200, verbose_name="Centro de Formación")
    regional = models.CharField(max_length=100, verbose_name="Regional")
    estado = models.CharField(max_length=3, choices=ESTADO_CHOICES, default='ACT', verbose_name="Estado")
    fecha_creacion = models.DateField(verbose_name="Fecha de Creación del programa")
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")

    class Meta: 
        verbose_name = "Programa de formacion"
        verbose_name_plural = "Programas de formacion"
        ordering = ['nombre']
        
    def __str__(self):
        return self.nombre
