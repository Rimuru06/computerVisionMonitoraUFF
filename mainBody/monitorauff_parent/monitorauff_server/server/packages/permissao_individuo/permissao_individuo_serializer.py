from rest_framework import serializers

from server.packages.permissao_individuo_grupo.permissao_individuo_grupo_model import PermissaoIndividuoGrupo

from .permissao_individuo_model import PermissaoIndividuo


class PermissaoIndividuoSerializer(serializers.ModelSerializer):
    grupos = serializers.SlugRelatedField(
        queryset=PermissaoIndividuoGrupo.objects.all(),
        many=True,
        slug_field='grupo_id'
    )

    class Meta:
        model = PermissaoIndividuo
        fields = ['id', 'nome', 'descricao',
                  'grupos', 'criado_em', 'atualizado_em']
