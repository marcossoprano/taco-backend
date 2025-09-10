from django.urls import path
from .views import ConsultaAlimentoAPIView, SugestoesAlimentoAPIView

urlpatterns = [
    path('', ConsultaAlimentoAPIView.as_view(), name='consulta-alimento'),
    path('consulta/', ConsultaAlimentoAPIView.as_view(), name='consulta-alimento-consulta'),
    path('sugestoes/', SugestoesAlimentoAPIView.as_view(), name='sugestoes-alimento'),
]
