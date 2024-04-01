from rest_framework import viewsets

from server.packages.helpers.response_helper import bad_request

from .alerta_individuo_model import AlertaIndividuo
from .alerta_individuo_serializer import AlertaIndividuoSerializer


class AlertaIndividuoViewSet(viewsets.ModelViewSet):
    queryset = AlertaIndividuo.objects.all()
    serializer_class = AlertaIndividuoSerializer

    def update(self, request, *args, **kwargs):
        return bad_request('Não é possível atualizar alertas')
