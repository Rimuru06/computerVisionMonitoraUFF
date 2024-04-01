from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from server.packages.permissao_individuo_grupo.permissao_individuo_grupo_model import PermissaoIndividuoGrupo

from .permissao_individuo_model import PermissaoIndividuo
from .permissao_individuo_serializer import PermissaoIndividuoSerializer
from . import permissao_individuo_queries as queries


class PermissaoIndividuoViewSet(viewsets.ModelViewSet):
    queryset = PermissaoIndividuo.objects.all()
    serializer_class = PermissaoIndividuoSerializer

    @action(detail=False, methods=['get'], url_path='by-individuo', url_name='by-individuo')
    def get_permissao_by_individuo(self, request):
        '''
        Retorna as permissões de um indivíduo.
        '''
        individuo_id = request.query_params.get('individuo_id')
        permissoes = PermissaoIndividuo.objects.raw(
            queries.query_get_permissao_by_individuo, [individuo_id])

        return Response(self.get_serializer(permissoes, many=True).data)

    @action(detail=False, methods=['get'], url_path='by-grupo', url_name='by-grupo')
    def get_permissao_by_grupo(self, request):
        '''
        Retorna as permissões de um grupo (área).
        '''
        grupo_id = request.query_params.get('grupo_id')
        permissoes = PermissaoIndividuo.objects.raw(
            queries.query_get_permissao_by_grupo, [grupo_id])

        return Response(self.get_serializer(permissoes, many=True).data)

    @action(detail=True, methods=['post'], url_path='permissao-grupo', url_name='permissao-grupo')
    def add_permissao_grupo(self, request, pk=None):
        '''
        Adiciona uma permissão de acesso a um grupo (área).
        '''
        permissao_individuo = self.get_object()
        grupos: list[int] = request.data['grupos']
        for grupo in grupos:
            if self.grupo_ja_cadastrado(permissao_individuo, grupo):
                continue

            permissao_individuo_grupo = PermissaoIndividuoGrupo.objects.create(
                permissao=permissao_individuo,
                grupo_id=grupo
            )
            permissao_individuo_grupo.save()

        return Response(self.get_serializer(permissao_individuo).data)

    @add_permissao_grupo.mapping.delete
    def remove_permissao_grupo(self, request, pk=None):
        '''
        Remove uma permissão de acesso a um grupo (área).
        '''
        permissao_individuo = self.get_object()
        grupos: list[int] = request.data['grupos']
        for grupo in grupos:
            if not self.grupo_ja_cadastrado(permissao_individuo, grupo):
                continue

            permissao_individuo_grupo = PermissaoIndividuoGrupo.objects.get(
                permissao=permissao_individuo,
                grupo_id=grupo
            )
            permissao_individuo_grupo.delete()

        return Response(self.get_serializer(permissao_individuo).data)

    def grupo_ja_cadastrado(self, permissao_individuo: PermissaoIndividuo, grupo: int) -> bool:
        '''
        Verifica se o grupo já foi cadastrado.
        '''
        return PermissaoIndividuoGrupo.objects.filter(
            permissao=permissao_individuo,
            grupo_id=grupo
        ).exists()
