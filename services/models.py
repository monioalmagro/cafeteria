from django.db import models

# Create your models here.


class Services(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    subtitle = models.CharField(max_length=200, verbose_name='Subtitulo')
    content = models.CharField(max_length=200, verbose_name='Contenido')
    image = models.ImageField (verbose_name='Imagen', upload_to='services')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    update = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de actualizacióṇ̣')

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ['-created']

    def __str__(self):
        return self.title    
