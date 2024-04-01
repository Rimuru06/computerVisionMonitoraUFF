from django.db import models
from server.packages.base.base_model import BaseModel
from server.packages.ocorrencia_face import OcorrenciaFace
from server.packages.permissao_individuo_grupo.permissao_individuo_grupo_model import PermissaoIndividuoGrupo


class AlertaIndividuo(BaseModel):
    face = models.ForeignKey(OcorrenciaFace, on_delete=models.PROTECT)
    permissao = models.ForeignKey(
        PermissaoIndividuoGrupo, on_delete=models.PROTECT)

    class Meta:
        db_table = 'TB_ALERTA_INDIVIDUO'
