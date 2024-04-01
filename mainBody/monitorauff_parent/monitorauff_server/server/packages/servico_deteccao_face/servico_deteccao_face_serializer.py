from rest_framework import serializers

from .servico_deteccao_face_model import ServicoDeteccaoFace


class ServicoDeteccaoFaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicoDeteccaoFace
        fields = '__all__'
        read_only_fields = ['monitor']
