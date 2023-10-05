from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('listUser/', views.listUser),
    path('registroUser/', views.registroUser),
    path('userRegistrado/', views.userRegistrado),
    path('eliminarCurso/<codigo>', views.eliminarCurso),
    path('editarCurso/<codigo>', views.editarCurso),
    path('cursoEditado/', views.cursoEditado)
]