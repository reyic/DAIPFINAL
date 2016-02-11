# -*- coding: UTF-8 -*-

import os 

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *

from django import forms

from pymongo import MongoClient
from DAI import forms

import time

from django.http import JsonResponse

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.test_database

usuarios=db['usuarios']
armaduras=db['armaduras']

#contador_arm = {}

def index(request):
	#reclama_datos()
	return render(request,'index.html')

def login(request):
	if request.method=='POST':
		form_log = LoginForm(request.POST)
		x = db.usuarios.find_one({"Usuario":request.POST['username']})
		if x!=None:
			if x[u'Password']==request.POST['password']:
				request.session['username']=request.POST['username']
				return render(request,'index.html', {'form_log':form_log, 'Usuario' : request.session['username']})
			else:
				return render(request, 'index.html', {'form_log':form_log})
		else:
			return render(request, 'index.html', {'form_log':form_log})
	if 'username' in request.session:
		return render(request,'index.html',{'form_log':form_log})
	return render(request,'index.html',{'form_log':LoginForm()})

def logout(request):

	del request.session['username']
	return HttpResponseRedirect('/')
	#return render(request,'index.html',{'form_log':LoginForm()})

def inscripcion(request):
	if request.method=='POST':
		form_reg=RegForm(request.POST)
		if form_reg.is_valid():
			x=db.usuarios.find_one({"Usuario": request.POST['User']})
			if x==None:
				request.session["username"]=request.POST['User']
				db.usuarios.insert({
					"Usuario": request.POST['User'],
					"Nombre": request.POST['Nombre'],
					"Apellidos": request.POST['Apellidos'],
					"Email": request.POST['Email'],
					"Dni": request.POST['Dni'],
					"FechaNacimiento_dia": request.POST['FechaNacimiento_day'],
					"FechaNacimiento_mes": request.POST['FechaNacimiento_month'],
					"FechaNacimiento_anio": request.POST['FechaNacimiento_year'],
					"Password": request.POST['Password'],
					"ConfirmaPass": request.POST['ConfirmaPass'],
					"Visa": request.POST['Visa'],

					})
				return render(request, 'index.html',{'form_log' : LoginForm(), 'usuario' : request.session['username'], 'alert': 'El usuario se ha registrado'})
			else:
				return render(request, 'inscripcion.html',{'form_log' : LoginForm(), 'form_reg' : form_reg})
		else:
			return render(request, 'inscripcion.html', {'form_reg' : form_reg})
	return render(request,'inscripcion.html', {'form_reg':RegForm()})

'''def perfil(request):
		if 'username' in request.session:
			infom=infoUsers(request.session['username'])
			#if request.method=='POST':
			print 'Hola'
			return render(request,'perfil.html',{'infom':infom})
			#else:
				#return render(request,'perfil.html',{'form_log' : LoginForm(),'usuario' : request.session['username']})
		else:
			return render(request,'index.html',{'form_log' : LoginForm()})'''


def editar(request):
	if 'username' in request.session:
		info=infoUsers(request.session['username'])
		if request.method=='POST':
			db.usuarios.update(
				{"Usuario":info[0]},{
				"Usuario":info[0],
				"Nombre":request.POST['Nombre'],
				"Apellidos":request.POST['Apellidos'],
				"Email":request.POST['Email'],
				"Dni":request.POST['Dni'],
				"FechaNacimiento_dia":info[5],
				"FechaNacimiento_mes":info[6],
				"FechaNacimiento_anio":info[7],
				"Password":request.POST['Password'],
				"ConfirmaPass":request.POST['ConfirmaPass'],
				"Visa":request.POST['Visa'],
			})
			return render(request, 'index.html', {'form_log' : LoginForm(), 'usuario' : request.session['username']})
		else:
			return render(request, 'editar.html', {'form_log' : LoginForm(), 'usuario' : request.session['username'], 'info' : info})
	return render(request, 'index.html', {'form_log' : LoginForm() })


def infoUsers(usuario):
	u = db.usuarios.find_one({"Usuario":usuario})
	info=[]
	info.append(u[u'Usuario'])
	info.append(u[u'Nombre'])
	info.append(u[u'Apellidos'])
	info.append(u[u'Email'])
	info.append(u[u'Dni'])
	info.append(u[u'FechaNacimiento_dia'])
	info.append(u[u'FechaNacimiento_mes'])
	info.append(u[u'FechaNacimiento_anio'])
	info.append(u[u'Password'])
	info.append(u[u'ConfirmaPass'])
	info.append(u[u'Visa'])
	return info

def armaduras(request):
	datos = listaArmaduras()
	return render(request,'armaduras.html',{'datos' : datos})

def armaduragen(request):

	if request.method=='POST':
		form=Armadura(request.POST,request.FILES)
		#if form.is_valid():
		x=db.armaduras.find_one({"Nombre": request.POST['nombre']})
		print x
		if x==None:
			#contador_arm[request.POST['nombre']] = 0
			url='static/img/'+request.FILES['imagen'].name
			imagenes(request)
			db.armaduras.insert({
				"Nombre": request.POST['nombre'],
				"Titulo": request.POST['titulo'],
				"Descripcion": request.POST['descripcion'],
				"Imagen": url,
				"Fecha":  time.strftime("%x"),
				"Precio":request.POST['precio'],
				"Visitas": 0
				})
			return render(request, 'armaduras.html',{'datos' : listaArmaduras()})
		#else:
			#return render(request, 'armadurasgen.html',{'form' : Armadura()})
	
	if 'username' in request.session and request.session['username'] == 'admin':		
		return render(request,'armaduragen.html', {'form': Armadura()})
	else:
		return HttpResponseRedirect('/')



def imagenes( request ):
	directorio = 'DAI/static/img/'
	fichero = request.FILES['imagen']
	if not os.path.isdir(directorio):
		os.mkdir(directorio)
	with  open (  directorio + fichero.name ,'wb+') as destination :
		for  chunk  in  fichero.chunks ():
			destination.write(chunk)


def listaArmaduras():
	x=db.armaduras.find({},{"_id": 0, "Nombre":1,"Titulo":1,"Descripcion":1,"Imagen":1,"Fecha":1,"Precio":1})
	infoArms=[]
	for doc in x:
		infoArms.append(doc)
		#print doc["Precio"]
	return infoArms

def infoArms(armadura):
	u = db.armaduras.find_one({"Nombre":armadura})
	info=[]
	info.append(u['Imagen'])
	info.append(u['Precio'])
	info.append(u['Nombre'])
	info.append(u['Descripcion'])
	info.append(u['Titulo'])
	info.append(u['Visitas'])
	return info

def sube_visita(armadura):
	info=infoArms(armadura)
	db.armaduras.update(
		{"Nombre":info[2]},{
			"Imagen":info[0],
			"Precio":info[1],
			"Nombre":info[2],
			"Descripcion":info[3],
			"Titulo":info[4],
			"Visitas": int(info[5])+1,
		})

def mostrararmaduras(request):
	armadura=request.GET.get('a',None)
	if armadura != None:
		x=db.armaduras.find_one({"Nombre":armadura})
		if x!=None:
			#contador_arm[armadura] += 1
			sube_visita(armadura)
			datos=infoArms(armadura)
			if 'username' in request.session:
				return render(request,"visionarms.html", {'info':datos, 'listaArms':listaArmaduras()})
			else:
				return render(request,"index.html",{'form_log' : LoginForm()})
	return render(request,'editar.html')
				

def reclama_datos(request):
	datos={}
	a=db.armaduras.find({},{'_id': 0, 'Nombre' : 1, 'Visitas' : 1})
	datos[0]=list() #armaduras_nombre
	datos[1]=list() #visitas_armadura

	for an in a:
		datos[0].append(an['Nombre'])
		datos[1].append(an['Visitas'])
		
	return JsonResponse(datos, safe=False)


def grafica(request):
	return render(request,"graficas.html") 
