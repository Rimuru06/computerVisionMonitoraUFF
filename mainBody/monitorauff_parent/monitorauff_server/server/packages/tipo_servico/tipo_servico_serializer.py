from rest_framework import serializers

from .tipo_servico_model import TipoServico


class TipoServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoServico
        fields = '__all__'
        read_only_fields = ['nome', 'descricao']
