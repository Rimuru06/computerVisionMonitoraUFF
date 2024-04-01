from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from server.packages.helpers.response_helper import bad_request, internal_server_error
from server.packages.servico_deteccao_face.servico_deteccao_face_service import ServicoDeteccaoFaceService
from server.packages.tipo_servico_monitor.tipo_servico_monitor_model import TipoServicoMonitor

from .servico_deteccao_face_model import ServicoDeteccaoFace
from .servico_deteccao_face_serializer import ServicoDeteccaoFaceSerializer


class ServicoDeteccaoFaceViewSet(viewsets.ModelViewSet):
    queryset = ServicoDeteccaoFace.objects.all()
    serializer_class = ServicoDeteccaoFaceSerializer
    service = ServicoDeteccaoFaceService()
    filterset_fields = ['monitor']

    @action(detail=False, methods=['post'], url_path='ativar', url_name='Ativar Servico')
    def ativar_servico(self, request):
        monitor: int = request.data['monitor']

        if not self.servico_permitido(monitor):
            return bad_request(f'O serviço não pode ser ativado para o monitor de id {monitor}.')

        try:
            self.service.ativar_servico(monitor)
            ServicoDeteccaoFace.objects.create(monitor=monitor)
        except Exception as e:
            internal_server_error("Erro ao ativar serviço.")

        return Response(data={'message': 'Serviço ativado com sucesso.'}, status=200)

    @action(detail=False, methods=['post'], url_path='desativar', url_name='Desativar Servico')
    def desativar_servico(self, request):
        monitor: int = request.data['monitor']

        try:
            self.service.desativar_servico(monitor)
            ServicoDeteccaoFace.objects.filter(monitor=monitor).delete()
        except Exception as e:
            internal_server_error("Erro ao desativar serviço.")

        return Response(data={'message': 'Serviço desativado com sucesso.'}, status=200)

    def servico_permitido(self, monitor_id: int) -> bool:
        return TipoServicoMonitor.objects.filter(
            servico=self.service.get_tipo(),
            monitor_id=monitor_id
        ).exists()
