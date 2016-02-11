# -*- coding: UTF-8 -*-
from django.db import models
from django.core.validators import RegexValidator
from django.core.files.storage import FileSystemStorage
from datetime import datetime


class Usuario(models.Model):
	User = models.CharField(max_length=20)
	Nombre = models.CharField(max_length=30)
	Apellidos = models.CharField(max_length=30)
	Email = models.EmailField()
	Dni= models.IntegerField(max_length=8)
	FechaNacimiento = models.DateField()
	Password = models.CharField(max_length=15)
	ConfirmaPass = models.CharField(max_length=15)
	Visa = models.CharField(max_length=19, validators=[RegexValidator(regex='(((\d{4}-){3})|((\d{4} ){3}))\d{4}', message='Formato de Visa inválido', code='nomatch')])

	def __str__(self):
		return self.User

class Armadura(models.Model):
	imagen = models.FileField(blank=True, upload_to='/')
	nombre = models.CharField(max_length=30)
	titulo = models.CharField(max_length=60)
	descripcion = models.TextField(max_length=10000)
	#fecha = models.DateTimeField(default=datetime.now(), blank=True)
	precio = models.CharField(max_length=8)

