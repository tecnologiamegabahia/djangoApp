# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from apps.usuario.models import usuario
from apps.usuario.forms import UsuarioUpdateForm


def login_view(request):
    try:
        form = LoginForm(request.POST or None)
        msg = None

        if request.method == "POST":
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    if (request.user.updated_user_id == '1'):
                        return redirect("primer_login", request.user.id)
                    else:
                        return redirect('usuario:dashboard')
                else:
                    msg = 'Invalid credentials'
            else:
                msg = 'Error validating the form'
        return render(request, "accounts/login.html", {"form": form, "msg": msg})
    except Exception as e:
        print(e)


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


def UserLogin(request, userLogin):
    try:
        model = usuario
        queryset = model.objects.filter(username=userLogin)
        return queryset
    except Exception as e:
        print(e)


def PrimerLogin(request):
    return render(request, "accounts/primer_login.html")


def usuarios_edit_pass(request, id):
    try:
        usuariox = usuario.objects.get(id=id)
        if request.method == 'GET':
            form = UsuarioUpdateForm(instance=usuariox)
        else:
            form = UsuarioUpdateForm(request.POST, instance=usuariox)
            preSave = form.save(commit=False)
            password = form.cleaned_data['password']
            preSave.updated_user_id = '2'
            preSave.set_password(password)
            preSave.save()
            return redirect('usuario:dashboard')
        return render(request, 'accounts/primer_login.html', {'form': form})
    except Exception as e:
        print(e)
