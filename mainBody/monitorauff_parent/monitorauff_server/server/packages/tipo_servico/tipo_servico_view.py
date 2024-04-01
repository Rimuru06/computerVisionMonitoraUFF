from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from server.packages.tipo_servico_monitor.tipo_servico_monitor_model import TipoServicoMonitor

from .tipo_servico_model import TipoServico
from .tipo_servico_serializer import TipoServicoSerializer


class TipoServicoViewSet(viewsets.ModelViewSet):
    queryset = TipoServico.objects.all()
    serializer_class = TipoServicoSerializer

    @action(detail=False, methods=['get'], url_path='by-monitor', url_name='by-monitor')
    def get_by_monitor(self, request):
        monitor_id = request.query_params.get('monitor_id')
        tipos = self.queryset.filter(servico__monitor_id=monitor_id)

        return Response(self.get_serializer(tipos, many=True).data)

    @action(detail=True, methods=['post'], url_path='vinculo-monitor', url_name='vinculo-monitor')
    def vincular_monitor(self, request, pk=None):
        '''
        Vincula um monitor a um tipo de serviço.
        '''
        tipo_servico = self.get_object()
        monitores: list[int] = request.data['monitores']
        for monitor in monitores:

            # TODO: Consultar o Zoneminder e verificar se o monitor existe e está ativo.

            tipo_servico_monitor = TipoServicoMonitor.objects.create(
                servico=tipo_servico,
                monitor_id=monitor
            )
            tipo_servico_monitor.save()

        return Response(status=200)

    @vincular_monitor.mapping.delete
    def desvincular_monitor(self, request, pk=None):
        '''
        Desvincula um monitor de um tipo de serviço.
        '''
        tipo_servico = self.get_object()
        monitores: list[int] = request.data['monitores']
        for monitor in monitores:
            tipo_servico_monitor = TipoServicoMonitor.objects.get(
                servico=tipo_servico,
                monitor_id=monitor
            )
            tipo_servico_monitor.delete()

        return Response(status=200)
