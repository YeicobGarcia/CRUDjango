from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Curso, Usuarios

# Create your views here.

def home(request):
    #cursoEnlistado = Curso.objects.all()
    return render(request, 'index.html')

# Redirecciones

def registroUser(request):
    return render(request, 'CRUD/Create.html')

def listUser(request):
    users = Usuarios.objects.all()
    data = {"usuarios" : users}

    return render(request, 'CRUD/Read.html', data)

def editUser(request):
    return render(request, 'CRUD/Update.html')

def deleteUser(request):
    return render(request, 'CRUD/Delete.html')

# Operaciones en templates

def userRegistrado(request):
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    correo = request.POST['txtEmail']
    telefono = request.POST['txtTelefono']
    cumple = request.POST['txtNacimiento']
    
    registro = Usuarios.objects.create(nombre = nombre, apellido = apellido, correo = correo, telefono = telefono, f_nacimiento = cumple)

    return redirect('CRUD/Create.html')

def eliminarCurso(request, codigo):
    cursoEliminar = Curso.objects.get(codigo=codigo)
    cursoEliminar.delete()

    return redirect('/')


def editarCurso(request, codigo):
    editarCurso = Curso.objects.get(codigo=codigo)  
    return render(request, 'edit.html', {"Cursos":editarCurso})

def cursoEditado(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.get(codigo=codigo)

    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    return redirect('/')