from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.rol.models import rol
from django.views.generic import CreateView, ListView
from apps.rol.forms import RolForm
from django.contrib import  messages

# Create your views here.
def index(request):
    return render(request, "rol/rol_list.html")


# metodo Listar
def rol_list(request):
    try:
        rolx = rol.objects.filter(state=1)
        contexto = {'rols': rolx}
        return render(request, 'rol/rol_list.html', contexto)
    except Exception as e:
        print(e)


# metodo crear
def rol_create(request):
    try:
        if request.method == 'POST':
            form = RolForm(request.POST)
            if form.is_valid():
                form.state = '1'
                form.save()
                messages.success(request, 'Creado Correctamente')
            return redirect('rol:index')
        else:
            form = RolForm
        return render(request, 'rol/rol_form.html', {'form': form})
    except Exception as e:
        print(e)


# metodo editar
def rol_edit(request, id):
    rolx = rol.objects.get(id=id)
    try:
        if request.method == 'GET':
            form = RolForm(instance=rolx)
        else:
            form = RolForm(request.POST, instance=rolx)
            if form.is_valid():
                form.save()
                messages.success(request, 'Creado Correctamente')
            return redirect('rol:index')
        return render(request, 'rol/rol_form.html', {'form': form})
    except Exception as e:
        print(e)


# metodo Eliminar-estatus0
def rol_delete(request, id):
    try:
        rolx = rol.objects.get(id=id)
        if request.method == 'POST':
            rolx.state = 0
            rolx.save()
            return redirect('rol:index')
        return render(request, 'rol/rol_eliminar.html', {'rol': rolx})
    except Exception as e:
        print(e)
