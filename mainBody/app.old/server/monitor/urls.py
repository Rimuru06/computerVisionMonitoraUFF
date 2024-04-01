from django.urls import path

from . import views

app_name = "monitor"
urlpatterns = [
    path('', views.index, name='index'),
    path('monitoramento', views.monitor, name='monitoramento'),
    path('rtsp-panel/<int:controlpoint_id>/<str:monitor_id>/', views.rtsp_panel, name='rtsp-panel'),
    path('placaList', views.placaListView, name='placaList'),
    path('placaList/avancado', views.buscaAvancada, name='buscaAvancada'),
    path('placa/<int:id>', views.placaView, name='placa'),
    path('administracao', views.admin, name='administracao'),
    path('usuario', views.user_list, name='user_list'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('editar-cadastro/<int:id>', views.editar_cadastro, name='editar_cadastro'),
    path('alert', views.alert, name='alert'),
    path('add-layer', views.add_layer, name='add_layer'),
    path('add-controlpoint', views.add_controlpoint, name='add_controlpoint'),
    path('add-camera', views.add_camera, name='add_camera'),
    path('add-alerta', views.add_alert, name='add_alert'),
    path('update-user/<int:id>', views.update_user, name='update_user'),
    path('update-layer/<int:id>', views.update_layer, name='update_layer'),
    path('update-controlpoint/<int:id>', views.update_controlpoint, name='update_controlpoint'),
    path('update-camera/<int:id>', views.update_camera, name='update_camera'),
    path('update-alerta/<int:id>', views.update_alert, name='update_alert'),
    path('delete-user/<int:id>', views.delete_user, name='delete_user'),
    path('delete-layer/<int:id>', views.delete_layer, name='delete_layer'),
    path('delete-controlpoint/<int:id>', views.delete_controlpoint, name='delete_controlpoint'),
    path('delete-camera/<int:id>', views.delete_camera, name='delete_camera'),
    path('delete-alerta/<int:id>', views.delete_alert, name='delete_alert'),
    path('erro', views.erro, name='erro'),
    path('erro_dadosAssociados', views.erro_dadosAssociados, name='erro_dadosAssociados'),
    path('inativo', views.inativo, name='inativo'),
    path('agent/<str:tag_slug>/start/', views.agent_start, name='agent-start')
]
