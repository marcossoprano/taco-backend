
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Alimento
from .serializers import AlimentoSerializer


class ConsultaAlimentoAPIView(APIView):
	def get(self, request):
		nome = request.query_params.get('nome')
		quantidade = request.query_params.get('quantidade')
		if not nome or not quantidade:
			return Response({'erro': 'Informe nome e quantidade (gramas).'}, status=status.HTTP_400_BAD_REQUEST)
		try:
			quantidade = float(quantidade)
		except ValueError:
			return Response({'erro': 'Quantidade deve ser um número.'}, status=status.HTTP_400_BAD_REQUEST)
		try:
			alimento = Alimento.objects.get(nome__iexact=nome)
		except Alimento.DoesNotExist:
			return Response({'erro': 'Alimento não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
		fator = quantidade / 100.0
		resultado = {
			'nome': alimento.nome,
			'quantidade': quantidade,
			'calorias': round(alimento.calorias * fator, 2),
			'proteinas': round(alimento.proteinas * fator, 2),
			'carboidratos': round(alimento.carboidratos * fator, 2),
			'gorduras': round(alimento.gorduras * fator, 2),
		}
		return Response(resultado)


# Endpoint para sugestões de alimentos
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Alimento

class SugestoesAlimentoAPIView(APIView):
	def get(self, request):
		termo = request.query_params.get('q', '')
		if termo:
			alimentos = Alimento.objects.filter(nome__icontains=termo).values_list('nome', flat=True)
		else:
			alimentos = Alimento.objects.all().values_list('nome', flat=True)
		return Response({'sugestoes': list(alimentos)})
