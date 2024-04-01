from django.conf import settings
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import (FileUploadParser, JSONParser, FormParser,
                                    MultiPartParser)
from rest_framework.response import Response
from server.packages.helpers.response_helper import bad_request

from server.packages.individuo.individuo_model import Individuo

from .ocorrencia_face_model import OcorrenciaFace
from .ocorrencia_face_serializer import OcorrenciaFaceSerializer
from .ocorrencia_face_service import OcorrenciaFaceService


class OcorrenciaFaceViewSet(viewsets.ModelViewSet):
    queryset = OcorrenciaFace.objects.all().order_by('id')
    serializer_class = OcorrenciaFaceSerializer
    filterset_fields = ['individuo']
    parser_classes = [JSONParser, FormParser,
                      MultiPartParser, FileUploadParser]
    ocorrencia_face_service = OcorrenciaFaceService()

    def create(self, request, *args, **kwargs):
        request = self.ocorrencia_face_service.trata_request_imagem(request)

        try:
            response = super().create(request, *args, **kwargs)

            self.ocorrencia_face_service.apos_salvar()
            return response
        except Exception as e:
            self.ocorrencia_face_service.deletar_imagem_face(
                request.data['img_filename'])
            raise e

    def update(self, request, *args, **kwargs):
        if (settings.DEBUG):
            request = self.ocorrencia_face_service.trata_request_imagem(
                request)
            return super().update(request, *args, **kwargs)
        else:
            return bad_request('Não é possível atualizar ocorrências de faces')

    def destroy(self, request, *args, **kwargs):
        self.ocorrencia_face_service.deletar_imagem_face(
            self.get_object().img_filename)
        return super().destroy(request, *args, **kwargs)

    @action(detail=False, methods=['post'], url_path='filter-by-image')
    def get_ocorrencia_faces_by_image(self, request):
        '''
        Retorna as ocorrências de faces que contém a imagem passada como parâmetro. \n
        Para funcionar corretamento o cliente deve passar o atributo 'filename' no Header da requisição. \n
        Ex.: Content-Disposition: attachment; filename=upload.jpg
        '''
        imagem_recebida = request.data['file'].read()
        faces_encontradas = self.ocorrencia_face_service.find_faces_semelhantes(
            imagem_recebida)
        ocorrencia_faces = self.get_queryset().filter(
            id__in=faces_encontradas)

        return Response(self.get_serializer(ocorrencia_faces, many=True).data)

    # Associa um indivíduo a uma face
    @action(detail=True, methods=['post'], url_path='associar-individuo', url_name='Associar Indivíduo')
    def associar_individuo(self, request, pk=None):
        ocorrencia_face = self.get_object()
        individuo_id = request.data['individuo']
        try:
            individuo = Individuo.objects.get(id=individuo_id)
            ocorrencia_face.individuo = individuo
            ocorrencia_face.save()
            return Response(self.get_serializer(ocorrencia_face).data)
        except Individuo.DoesNotExist:
            return bad_request(f'Indivíduo de id {individuo_id} não existe ou não foi encontrado.')

    # Desassocia um indivíduo de uma face
    @action(detail=True, methods=['post'], url_path='desassociar-individuo', url_name='Desassociar Indivíduo')
    def desassociar_individuo(self, request, pk=None):
        ocorrencia_face = self.get_object()
        ocorrencia_face.individuo = None
        ocorrencia_face.save()
        return Response(self.get_serializer(ocorrencia_face).data)

    # Atualiza em lote
    # Usado somente em desenvolvimento
    @action(detail=False, methods=['post'], url_path='atualizar-em-lote', url_name='Atualizar em Lote')
    def atualizar_em_lote(self, request):
        if (settings.DEBUG):
            self.ocorrencia_face_service.atualizar_imagem_em_lote(
                OcorrenciaFace)
            return Response(status=200)
        else:
            return bad_request('Não é possível atualizar em lote')
