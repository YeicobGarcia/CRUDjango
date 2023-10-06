from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('listUser/', views.listUser, name='ListaUsuarios'),
    path('registroUser/', views.registroUser, name='AgregarUsuario'),
    path('userRegistrado/', views.userRegistrado),
    path('eliminarCurso/', views.eliminarCurso, name='EliminarUsuario'),
    path('editUser', views.editUser, name='EdicionUsuario'),
    path('userEditado/', views.userEditado)
]