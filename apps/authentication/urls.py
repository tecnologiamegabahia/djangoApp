from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import login_view, register_user, PrimerLogin, usuarios_edit_pass
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login/', login_view, name="login"),
    path('', login_required(login_view), name="login"),
    path('register/', login_required(register_user), name="register"),
    path("logout/", login_required(LogoutView.as_view()), name="logout"),
    path("primer_login/<str:id>/", usuarios_edit_pass, name="primer_login"),
    url(r'^editar/(?P<id>\d+)/$', login_required(usuarios_edit_pass), name='usuario_editar'),
]
