from django.urls import include, path
from rest_framework import routers

from server import views

router = routers.DefaultRouter()
router.register(r'alerta-individuo', views.AlertaIndividuoViewSet)
router.register(r'etiqueta-individuo', views.EtiquetaIndividuoViewSet)
router.register(r'individuo', views.IndividuoViewSet)
router.register(r'ocorrencia-face', views.OcorrenciaFaceViewSet)
router.register(r'permissao-individuo', views.PermissaoIndividuoViewSet)
router.register(r'servico_deteccao_face', views.ServicoDeteccaoFaceViewSet)
router.register(r'tipo-servico', views.TipoServicoViewSet)
router.register(r'usuario', views.UserViewSet)
router.register(r'monitor', views.MonitorDTOViewSet, basename='monitor')
router.register(r'grupo', views.GroupDTOViewSet, basename='grupo')

app_name = "server"
urlpatterns = [
    path('', include(router.urls)),
]
