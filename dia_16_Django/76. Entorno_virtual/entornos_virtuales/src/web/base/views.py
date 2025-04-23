from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
#Importar desde django para la creación de una nueva tarea
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Tarea

# Create your views here.
class ListaPendientes(ListView):
    model = Tarea
    context_object_name = 'tareas'

class DetalleTarea(DetailView):
    model = Tarea
    context_object_name = "tarea"
    template_name = "base/tarea.html"

#Se crea la clase que permita realizar la creación de la nueva tarea
class CrearTarea(CreateView):
    model = Tarea
    fields = '__all__'
    success_url = reverse_lazy('tareas')

