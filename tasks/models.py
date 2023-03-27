from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    titulo = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    creacion = models.DateTimeField(auto_now_add=True)
    frcha_completado = models.DateTimeField(null=True, blank=True)
    imprtante = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo + ' - creado por : ' + self.user.username
    
