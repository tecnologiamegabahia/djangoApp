from django import forms
from apps.usuario.models import usuario
from django.contrib.auth.forms import UserCreationForm


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = [
            'documento',
            'nombre',
            'apellido',
            'email',
            'phone',
            'ciudad',
            'username',
            'password',
            'rol'
        ]
        labels = {
            'documento': 'Documento',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'e-mail',
            'phone': 'Telefono',
            'ciudad': 'Ciudad',
            'username': 'UserName',
            'password': 'Password',
            'rol': 'rol'
        }
        widgets = {
            'documento': forms.TextInput(attrs={'class': 'form-control', "autocomplete": "off"}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', "autocomplete": "off"}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', "autocomplete": "off"}),
            'email': forms.TextInput(attrs={'class': 'form-control', "autocomplete": "off"}),
            'phone': forms.TextInput(attrs={'class': 'form-control', "autocomplete": "off"}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control', "autocomplete": "off"}),
            'username': forms.TextInput(attrs={'class': 'form-control', "autocomplete": "off", }),
            'password': forms.PasswordInput(attrs={'class': 'form-control', "autocomplete": "off"}),
            'rol': forms.Select(attrs={'class': 'form-control'}),
        }

    class RegistroForm(UserCreationForm):
        class Meta:
            model = usuario
            fields = [
                'nombre',
                'apellido',
                'documento',
                'email',
                'phone',
                'ciudad',
                'rol'

            ]
            labels = {
                'nombre': 'Nombre',
                'apellido': 'Apellido',
                'documento': 'Documento',
                'email': 'email',
                'phone': 'Telefono',
                'ciudad': 'Ciudad',
                'rol': 'rol'
            }
            widgets = {
                'nombre': forms.TextInput(attrs={'class': 'form-control'}),
                'apellido': forms.TextInput(attrs={'class': 'form-control'}),
                'documento': forms.TextInput(attrs={'class': 'form-control'}),
                'email': forms.TextInput(attrs={'class': 'form-control'}),
                'phone': forms.TextInput(attrs={'class': 'form-control'}),
                'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
                'rol': forms.Select(attrs={'class': 'form-control required '}),

            }


class UsuarioUpdateForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = [
            'documento',
            'username',
            'password',

        ]
        labels = {
            'documento': 'Documento',
            'username': 'UserName',
            'password': 'Nuevo Password',
        }
        widgets = {
            'documento': forms.TextInput(
                attrs={'class': 'form-control', "autocomplete": "off", 'readonly': 'readonly'}),
            'username': forms.TextInput(attrs={'class': 'form-control', "autocomplete": "off", 'readonly': 'readonly'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', "autocomplete": "off"}),
        }
