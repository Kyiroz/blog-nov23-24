from django.db import models

# Create your models here.
class Post(models.Model):   #Post es una tabla en la base de datos
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    #Cuando se crea un post, se crea un autor
    updated_at = models.DateTimeField(auto_now=True)    #Aqui se actualiza el post
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)   #Aqui se relaciona el post con el autor, el auto es una llave foranea que hace referencia a la tabla User de Django
 
    def __str__(self):
        return self.title