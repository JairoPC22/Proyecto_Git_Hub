from django.db import models

# Create your models here.
class Pelicula(models.Model):
    nombre = models.CharField(max_length=150,verbose_name='Titulo de la pelicula',unique=True)

    Sinopsis = models.TextField(max_length=1000, verbose_name='Sinopsis')
    duracion= models.DecimalField(default=0.00, max_digits=5, decimal_places=2, verbose_name='Indicar el tiempo en horas')
    tamanio= models.CharField('Definir tamaño de la pelicula', max_length=50)
    poster= models.ImageField(verbose_name='Poster de la pelicula',upload_to='posters/peliculas/',null=True)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name= 'Pelicula'
        verbose_name_plural = 'Peliculas'





