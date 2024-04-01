from django.db import models
from server.packages.base.base_model import BaseModel


class ServicoDeteccaoFace(BaseModel):

    monitor = models.IntegerField(unique=True)

    class Meta:
        db_table = 'TB_SERVICO_DETECCAO_FACE'
