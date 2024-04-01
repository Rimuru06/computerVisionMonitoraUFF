from django.db import models
from server.packages.base.base_model import BaseModel
from server.packages.etiqueta_individuo.etiqueta_individuo_model import \
    EtiquetaIndividuo
from server.packages.permissao_individuo.permissao_individuo_model import \
    PermissaoIndividuo


class EtiquetaPermissaoIndividuo(BaseModel):
    '''
    Classe que representa a permissão de acesso a etiqueta de indivíduo.
    '''
    etiqueta_individuo = models.ForeignKey(
        EtiquetaIndividuo, on_delete=models.CASCADE)
    permissao_individuo = models.ForeignKey(
        PermissaoIndividuo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'RL_ETIQUETA_PERMISSAO_INDIVIDUO'
