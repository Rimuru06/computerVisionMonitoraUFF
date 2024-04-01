from enum import Enum
from django.db import models
from server.packages.base.base_model import BaseModel


class TipoServico(BaseModel):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1000)

    class Meta:
        db_table = 'TB_TIPO_SERVICO'


class TipoServicoEnum(Enum):
    DETECCAO_PLACA = 1
    DETECCAO_FACE = 2
