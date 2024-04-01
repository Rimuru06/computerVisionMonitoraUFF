from rest_framework import serializers

from .individuo_model import Individuo


class IndividuoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Individuo
        fields = ['id', 'nome', 'etiquetas', 'criado_em', 'atualizado_em']
