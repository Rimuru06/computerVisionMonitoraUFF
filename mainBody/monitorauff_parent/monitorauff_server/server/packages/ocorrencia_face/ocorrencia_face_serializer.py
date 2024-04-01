from rest_framework import serializers

from .ocorrencia_face_model import OcorrenciaFace
from server.packages.individuo import IndividuoSerializer


class OcorrenciaFaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OcorrenciaFace
        fields = '__all__'
