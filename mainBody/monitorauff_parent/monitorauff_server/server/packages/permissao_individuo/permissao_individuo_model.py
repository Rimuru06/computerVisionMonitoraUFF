from django.db import models
from server.packages.base.base_model import BaseModel


class PermissaoIndividuo(BaseModel):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    class Meta:
        db_table = 'TB_PERMISSAO_INDIVIDUO'
