from django.views.generic import TemplateView, CreateView
from .models import Contacto

class index(TemplateView):
	template_name = 'index.html'

class servicios(TemplateView):
	template_name = 'servicios.html'

class contacto(CreateView):
	template_name = 'mailContacto/contacto.html'
	model = Contacto
	success_url = 'contacto.html'
