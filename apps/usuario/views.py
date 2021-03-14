from django.shortcuts import render, redirect
from django.http import HttpResponse
# importacion MTC
from apps.usuario.forms import UsuarioForm
from apps.usuario.models import usuario
from django.views.generic import CreateView, ListView
from django.db import connection
import json


# Create your views here.
def indexLogin(request):
    return render(request, "dashboard/dashboard.html")


def index(request):
    return render(request, "usuario/usuario_list.html")


# Vista Index
def usuarios_view(request):
    try:
        if request.method == 'POST':
            form = UsuarioForm(request.POST)
            if form.is_valid():
                preSave = form.save(commit=False)
                password = form.cleaned_data['password']
                preSave.set_password(password)
                preSave.save()
            return redirect('usuario:index')
        else:
            form = UsuarioForm
        return render(request, 'usuario/usuario_form.html', {'form': form})
    except Exception as e:
        print(e)


# vista Listar
def usuarios_list(request):
    try:
        usuariox = usuario.objects.filter(status=1)
        contexto = {'usuarios': usuariox}
        return render(request, 'usuario/usuario_list.html', contexto)
    except Exception as e:
        print(e)


# Vista editar
def usuarios_edit(request, id):
    try:
        usuariox = usuario.objects.get(id=id)
        if request.method == 'GET':
            form = UsuarioForm(instance=usuariox)
        else:
            form = UsuarioForm(request.POST, instance=usuariox)
            if form.is_valid():
                preSave = form.save(commit=False)
                password = form.cleaned_data['password']
                preSave.set_password(password)
                preSave.save()
            return redirect('usuario:index')
        return render(request, 'usuario/usuario_form.html', {'form': form})
    except Exception as e:
        print(e)


# vista Eliminar-estatus0
def usuario_delete(request, id):
    try:
        usuariox = usuario.objects.get(id=id)
        if request.method == 'POST':
            usuariox.status = 0
            usuariox.save()
            return redirect('usuario:index')
        return render(request, 'usuario/usuario_eliminar.html', {'usuario': usuariox})
    except Exception as e:
        print(e)


class UsuariosList(ListView):
    try:
        model = usuario
        queryset = model.objects.filter(status=1)
        template_name = 'usuario/usuario_list.html'
    except Exception as e:
        print(e)
