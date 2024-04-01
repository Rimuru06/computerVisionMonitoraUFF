from rest_framework import serializers

from .etiqueta_individuo_model import EtiquetaIndividuo


class EtiquetaIndividuoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EtiquetaIndividuo
        fields = ['id', 'nome', 'descricao',
                  'permissoes', 'criado_em', 'atualizado_em']
