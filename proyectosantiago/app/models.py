from django.db import models

class EntradaBlog(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField()

class Pagina(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
