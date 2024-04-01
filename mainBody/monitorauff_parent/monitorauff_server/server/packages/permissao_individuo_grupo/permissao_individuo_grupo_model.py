from django.db import models
from server.packages.base.base_model import BaseModel
from server.packages.permissao_individuo.permissao_individuo_model import PermissaoIndividuo


class PermissaoIndividuoGrupo(BaseModel):
    permissao = models.ForeignKey(
        PermissaoIndividuo, related_name='grupos', on_delete=models.CASCADE)
    grupo_id = models.IntegerField()

    class Meta:
        db_table = 'RL_PERMISSAO_INDIVIDUO_GRUPO'
        unique_together = ['permissao', 'grupo_id']
