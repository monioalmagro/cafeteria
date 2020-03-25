from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import user

# Create your models here.
class Category (models.Model):
    title = models.CharField(max_length=200, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    update = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de actualizacióṇ̣')

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ['-created']
    def __str__(self):
        return self.title    
    
        


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    published = models.DateTimeField(default = now, verbose_name='Fecha de publicación')
    content = models.CharField(max_length=200, verbose_name='Contenido')
    image = models.ImageField (verbose_name='Imagen', upload_to='services')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    update = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de actualizacióṇ̣')
    categories =  models.ManyToManyField(Category, verbose_name='Categorias', related_name="get_posts")
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Post"
        ordering = ['-created']

    def __str__(self):
        return self.title    


        
    
        