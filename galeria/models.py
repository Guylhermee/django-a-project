from datetime import datetime
from django.db import models

# Create your models here.
class Fotografia (models.Model):

    OPC_CATEGORIA = [   #tem que ser uma tupla
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta")
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=150, choices=OPC_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now, blank=False, null=False)

    def __str__(self):
        return self.nome