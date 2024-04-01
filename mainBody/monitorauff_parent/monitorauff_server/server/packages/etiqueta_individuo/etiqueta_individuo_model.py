from django.db import models
from server.packages.base.base_model import BaseModel
from server.packages.permissao_individuo.permissao_individuo_model import \
    PermissaoIndividuo


class EtiquetaIndividuo(BaseModel):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    permissoes = models.ManyToManyField(
        PermissaoIndividuo, through='EtiquetaPermissaoIndividuo')

    class Meta:
        db_table = 'TB_ETIQUETA_INDIVIDUO'
