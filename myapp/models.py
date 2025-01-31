from django.db import models

# Create your models here.
class Proyectos(models.Model):
    Nombre = models.CharField(max_length=200)
    Descripcion = models.CharField(max_length=200)
    Imagen = models.CharField(max_length=200)
    Video_url = models.CharField(max_length=200)
    
    def __str__(self):
        return self.Nombre  + ' - ' + self.Descripcion + ' - ' + self.Imagen + ' - ' + self.Video_url


class Habilidades(models.Model):
    Nombre = models.CharField(max_length=200)
    Decripcion = models.CharField(max_length=200)
    Imagen = models.CharField(max_length=200)

    def __str__(self):
        return self.Nombre  + ' - ' + self.Decripcion + ' - ' + self.Imagen

class Servicios(models.Model):
    Nombre = models.CharField(max_length=200)
    Decripcion = models.CharField(max_length=200)
    Imagen = models.CharField(max_length=200)
    
    def __str__(self):
        return self.Nombre + ' - ' + self.Decripcion + ' - ' + self.Imagen
