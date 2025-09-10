
from django.db import models

class Alimento(models.Model):
	nome = models.CharField(max_length=100, unique=True)
	calorias = models.FloatField(help_text='Calorias por 100g')
	proteinas = models.FloatField(help_text='Proteínas por 100g')
	carboidratos = models.FloatField(help_text='Carboidratos por 100g')
	gorduras = models.FloatField(help_text='Gorduras por 100g')

	def __str__(self):
		return self.nome
