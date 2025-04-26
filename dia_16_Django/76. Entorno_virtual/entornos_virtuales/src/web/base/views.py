from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
#Importar desde django para la creación de una nueva tarea
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
#Se importa LoginRequiredMixin para autorixar unicamente a los que se logueron correctamente
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Tarea

class Logueo(LoginView):
    template_name = "base/login.html"
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tareas')

# Create your views here.
class ListaPendientes(LoginRequiredMixin, ListView):#Se hereda la primero loginrequiredmixin para obligar a validar si está logueado el usuario y luego se configura los settings del proyecto con la palabra clave LOGIN_URL = 'login' donde redirigirá hacia la página de inicio de sesión
    model = Tarea
    context_object_name = 'tareas'
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tareas'] = context['tareas'].filter(usuario=self.request.user)
        context['count'] = context['tareas'].filter(completo=False).count()
        return context
    

class DetalleTarea(DetailView):
    model = Tarea
    context_object_name = "tarea"
    template_name = "base/tarea.html"

#Se crea la clase que permita realizar la creación de la nueva tarea
class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    fields = ['titulo', 'descripción', 'completo']
    success_url = reverse_lazy('tareas')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(CrearTarea, self).form_valid(form)


#Se crea clase para editar una tarea
class EditarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    fields = ['titulo', 'descripción', 'completo']
    success_url = reverse_lazy('tareas')

#Se crea la clase para eliminar una tarea
class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    context_object_name = 'tarea'
    success_url = reverse_lazy('tareas')