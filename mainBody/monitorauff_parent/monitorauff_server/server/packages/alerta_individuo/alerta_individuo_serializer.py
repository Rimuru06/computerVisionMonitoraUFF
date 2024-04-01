from rest_framework import serializers

from .alerta_individuo_model import AlertaIndividuo


class AlertaIndividuoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertaIndividuo
        fields = ['id', 'face', 'permissao', 'criado_em', 'atualizado_em']
