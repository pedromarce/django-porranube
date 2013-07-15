from django.db import models

# Create your models here.
class Usuario(models.Model):
	usuario = models.CharField(max_length=30)
	def __unicode__(self):
		return self.usuario
	def puntuacion(self):
		puntos = 0
		for apuesta in Apuesta.objects.get(usuario=self)
			if apuesta.resultado = apuesta.partido.resultado
				puntos =+ 1

class Temporada(models.Model):
	temporada = models.IntegerField(default=0)
	def __unicode__(self):
		return str(self.temporada)

class Partido(models.Model):
	temporada = models.ForeignKey(Temporada)
	partido = models.CharField(max_length=30)
	resultado = models.CharField(max_length=30)
	cierre = models.DateTimeField('Fecha Cierre')
	def __unicode__(self):
		return self.partido + ' ' + str(self.cierre)
	def cerrado(self):
		return self.cierre < timezone.now()

class Apuesta(models.Model):
	partido = models.ForeignKey(Partido)
	usuario = models.ForeignKey(Usuario)
	resultado = models.CharField(max_length=30) 
	def __unicode__(self):
		return self.usuario.usuario + ' ' + self.partido.partido + ':' + self.resultado