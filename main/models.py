from django.db import models

# Create your models here.

class Projetos (models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    details = models.CharField(max_length=50)
    date = models.DateField()
    link = models.CharField(max_length=50)
    github = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to ='static/uploads/')
    filter_choices = (
        ('app', 'app'),
        ('web', 'web'),
        ('card', 'card'),
    )
    type = models.CharField(max_length=100, null=True, choices=filter_choices)
    
