from django.core.management.base import BaseCommand
from alimentos.models import Alimento

class Command(BaseCommand):
    help = 'Popula o banco com alimentos principais da TACO'

    def handle(self, *args, **kwargs):
        alimentos = [
            {
                'nome': 'Arroz branco cozido',
                'calorias': 128,
                'proteinas': 2.5,
                'carboidratos': 28.1,
                'gorduras': 0.2
            },
            {
                'nome': 'Feijão carioca cozido',
                'calorias': 76,
                'proteinas': 4.8,
                'carboidratos': 13.6,
                'gorduras': 0.5
            },
            {
                'nome': 'Frango grelhado',
                'calorias': 163,
                'proteinas': 32.0,
                'carboidratos': 0.0,
                'gorduras': 3.6
            },
            {
                'nome': 'Batata cozida',
                'calorias': 52,
                'proteinas': 1.2,
                'carboidratos': 11.9,
                'gorduras': 0.1
            },
            {
                'nome': 'Ovo cozido',
                'calorias': 146,
                'proteinas': 13.3,
                'carboidratos': 0.6,
                'gorduras': 9.5
            },
            {
                'nome': 'Carne bovina grelhada',
                'calorias': 232,
                'proteinas': 32.0,
                'carboidratos': 0.0,
                'gorduras': 10.7
            },
            {
                'nome': 'Maçã',
                'calorias': 56,
                'proteinas': 0.3,
                'carboidratos': 15.2,
                'gorduras': 0.2
            },
            {
                'nome': 'Banana prata',
                'calorias': 89,
                'proteinas': 1.0,
                'carboidratos': 22.8,
                'gorduras': 0.2
            },
            {
                'nome': 'Leite integral',
                'calorias': 61,
                'proteinas': 3.2,
                'carboidratos': 4.7,
                'gorduras': 3.3
            },
            {
                'nome': 'Pão francês',
                'calorias': 300,
                'proteinas': 7.9,
                'carboidratos': 56.4,
                'gorduras': 3.5
            }
        ]
        for alimento in alimentos:
            obj, created = Alimento.objects.get_or_create(nome=alimento['nome'], defaults=alimento)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Adicionado: {obj.nome}"))
            else:
                self.stdout.write(self.style.WARNING(f"Já existe: {obj.nome}"))
