from django.db import models

class Contacto(models.Model):
	nombre = models.CharField(max_length=100)
	asunto = models.CharField(max_length=100)
	email = models.EmailField()
	descripcion = models.TextField(max_length=700)

	def __unicode__(self):
		return self.nombre
