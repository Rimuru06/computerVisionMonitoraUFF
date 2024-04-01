from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .etiqueta_individuo_model import EtiquetaIndividuo
from .etiqueta_individuo_serializer import EtiquetaIndividuoSerializer


class EtiquetaIndividuoViewSet(viewsets.ModelViewSet):
    queryset = EtiquetaIndividuo.objects.all().order_by('nome')
    serializer_class = EtiquetaIndividuoSerializer
    filterset_fields = ['permissoes']

    # Adicionar permissões de acesso a etiqueta de indivíduo.
    @action(detail=True, methods=['post'], url_path='permissao', url_name="Permissões de Etiqueta de Indivíduo")
    def add_permission(self, request, pk=None):
        etiqueta_individuo = self.get_object()
        permissao_individuo: list[int] = request.data['permissoes']
        for permissao in permissao_individuo:
            etiqueta_individuo.permissoes.add(permissao)
        return Response(self.get_serializer(etiqueta_individuo).data)

    # Remover permissões de acesso a etiqueta de indivíduo.
    @add_permission.mapping.delete
    def remove_permission(self, request, pk=None):
        etiqueta_individuo = self.get_object()
        permissao_individuo: list[int] = request.data['permissoes']
        for permissao in permissao_individuo:
            etiqueta_individuo.permissoes.remove(permissao)
        return Response(self.get_serializer(etiqueta_individuo).data)
