# -*- coding: UTF-8 -*-
from django import forms
from .models import *

class LoginForm(forms.Form):
	User = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'User', 'class' : 'form-control'}))
	Password = forms.URLField(widget=forms.TextInput(attrs={'placeholder': 'Password', 'class' : 'form-control', 'type' : 'password'}))

class RegForm(forms.ModelForm):
	class Meta:
		model = Usuario
		widgets = {
			'User' : forms.TextInput(attrs={'placeholder': 'NickName', 'name': 'User', 'class' : 'form-control'}),
			'Nombre' : forms.TextInput(attrs={'placeholder': 'Nombre', 'class' : 'form-control'}),
			'Apellidos' : forms.TextInput(attrs={'placeholder': 'Apellidos', 'class' : 'form-control'}),
			'Email' : forms.TextInput(attrs={'placeholder': 'Email', 'class' : 'form-control'}),
			'Dni': forms.TextInput(attrs={'placeholder': 'DNI', 'class':'form-control'}),
			'FechaNacimiento' : forms.SelectDateWidget(years=range(1950, 2016), attrs={'class' : 'form-control'}),
			'Password': forms.PasswordInput(attrs={'placeholder': 'Password', 'class' : 'form-control'}),
			'ConfirmaPass': forms.PasswordInput(attrs={'placeholder': 'ConfirmaPass', 'class' : 'form-control'}),
			'Visa' : forms.TextInput(attrs={'placeholder': 'VISA', 'class' : 'form-control'}),
			
			}
		fields = ('User', 'Nombre', 'Apellidos', 'Email', 'Dni', 'FechaNacimiento', 'Password', 'ConfirmaPass', 'Visa')

class Armadura(forms.ModelForm):
	class Meta:
		model=Armadura
		widgets={
			'nombre' : forms.TextInput(attrs={'placeholder': 'nombre', 'class' : 'form-control'}),
			'titulo' : forms.TextInput(attrs={'placeholder': 'titulo', 'class' : 'form-control'}),
			'descripcion' : forms.Textarea(attrs={'placeholder': 'descripcion','class' : 'form-control'}),
			'precio' : forms.TextInput(attrs={'placeholder': 'precio','class' : 'form-control'}),
		}
		fields=('imagen','nombre','titulo','descripcion', 'precio')
