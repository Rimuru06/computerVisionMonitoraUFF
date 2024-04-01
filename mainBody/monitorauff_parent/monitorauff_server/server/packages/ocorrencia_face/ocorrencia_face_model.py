from django.db import models
from server.packages.individuo import Individuo
from server.packages.base.base_model import BaseModel


class OcorrenciaFace(BaseModel):
    individuo = models.ForeignKey(
        Individuo, on_delete=models.PROTECT, blank=True, null=True)
    camera_id = models.IntegerField(blank=False)
    img_filename = models.CharField(blank=False, max_length=256)
    data_md5 = models.CharField(blank=False, max_length=256)

    class Meta:
        db_table = 'TB_OCORRENCIA_FACE'
