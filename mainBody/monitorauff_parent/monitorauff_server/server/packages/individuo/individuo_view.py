from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import (FileUploadParser, JSONParser,
                                    MultiPartParser)
from rest_framework.response import Response
from server.packages.helpers.response_helper import (bad_request,
                                                     internal_server_error)
from server.packages.ocorrencia_face.ocorrencia_face_service import \
    OcorrenciaFaceService

from .individuo_model import Individuo
from .individuo_serializer import IndividuoSerializer


class IndividuoViewSet(viewsets.ModelViewSet):
    queryset = Individuo.objects.all().order_by('nome')
    serializer_class = IndividuoSerializer
    filterset_fields = ['etiquetas']
    parser_classes = [JSONParser, MultiPartParser, FileUploadParser]
    ocorrencia_face_service = OcorrenciaFaceService()

    # Adicionar etiquetas a indivíduo.
    @action(detail=True, methods=['post'], url_path='etiqueta')
    def adicionar_etiqueta(self, request, pk=None):
        individuo = self.get_object()
        etiqueta_individuo: list[int] = request.data['etiquetas']
        for etiqueta in etiqueta_individuo:
            individuo.etiquetas.add(etiqueta)
        return Response(self.get_serializer(individuo).data)

    # Remover etiquetas de indivíduo.
    @adicionar_etiqueta.mapping.delete
    def remover_etiqueta(self, request, pk=None):
        individuo = self.get_object()
        etiqueta_individuo: list[int] = request.data['etiquetas']
        for etiqueta in etiqueta_individuo:
            individuo.etiquetas.remove(etiqueta)
        return Response(self.get_serializer(individuo).data)

    @action(detail=False, methods=['post'], url_path='by-image')
    def get_individuo_by_image(self, request):
        '''
        Retorna indivíduos que contém a imagem passada como parâmetro. \n
        Para funcionar corretamento o cliente deve passar o atributo 'filename' no Header da requisição. \n
        Ex.: Content-Disposition: attachment; filename=upload.jpg
        '''
        imagem_recebida = request.data['file'].read()
        faces_encontradas = self.ocorrencia_face_service.find_faces_semelhantes(
            imagem_recebida)
        individuos = self.get_queryset().filter(
            ocorrenciaface__in=faces_encontradas).distinct()

        return Response(self.get_serializer(individuos, many=True).data)

    @action(detail=False, methods=['get'], url_path='by-face-id')
    def get_individuo_by_face_id(self, request):
        '''
        Retorna o individuo que contém a face passada como parâmetro.
        '''
        face_id = request.query_params.get('face_id')
        individuos: list[Individuo] = self.get_queryset().filter(
            ocorrenciaface__pk=face_id).distinct()

        if individuos.__len__() == 0:
            return bad_request("Indivíduo não encontrado.")

        if individuos.__len__() > 1:
            return internal_server_error("Mais de um indivíduo encontrado para a mesma face.")

        return Response(self.get_serializer(individuos[0]).data)
