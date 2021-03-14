from django import forms
from apps.rol.models import rol


class RolForm(forms.ModelForm):
    class Meta:
        model = rol
        fields = [
            'code',
            'name',
            'description',
            'permisoAdmin',
            'permisoCalidad',
            'permisoContactos',
            'permisoEstadisticas',
            'permisoGestion',
            'permisoMonitoreo',
            'permisoProcesos',
            'permisoReportes',
        ]
        labels = {
            'code': 'Codigo',
            'name': 'Nombre',
            'description': 'Descripcion',
            'permisoAdmin': 'permiso Administracion',
            'permisoCalidad': 'permiso Calidad',
            'permisoContactos': 'permiso Contactos',
            'permisoEstadisticas': 'permiso Estadisticas',
            'permisoGestion': 'permiso Gestion',
            'permisoMonitoreo': 'permiso Monitoreo',
            'permisoProcesos': 'permiso Procesos',
            'permisoReportes': 'permiso Reportes',

        }
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control', "autocomplete": "off"}),
            'name': forms.TextInput(attrs={'class': 'form-control', "autocomplete": "off"}),
            'description': forms.TextInput(attrs={'class': 'form-control', "autocomplete": "off"}),
            'permisoAdmin': forms.Select(choices=(('0', 'NO'), ('1', 'SI')), attrs={'class': 'form-control'}),
            'permisoCalidad': forms.Select(choices=(('0', 'NO'), ('1', 'SI')), attrs={'class': 'form-control'}),
            'permisoContactos': forms.Select(choices=(('0', 'NO'), ('1', 'SI')), attrs={'class': 'form-control'}),
            'permisoEstadisticas': forms.Select(choices=(('0', 'NO'), ('1', 'SI')), attrs={'class': 'form-control'}),
            'permisoGestion': forms.Select(choices=(('0', 'NO'), ('1', 'SI')), attrs={'class': 'form-control'}),
            'permisoMonitoreo': forms.Select(choices=(('0', 'NO'), ('1', 'SI')), attrs={'class': 'form-control'}),
            'permisoProcesos': forms.Select(choices=(('0', 'NO'), ('1', 'SI')), attrs={'class': 'form-control'}),
            'permisoReportes': forms.Select(choices=(('0', 'NO'), ('1', 'SI')), attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
        }
