from rest_framework import serializers

from .user_model import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'tipoUser', 'matricula',
                  'status', 'criado_em', 'atualizado_em']
