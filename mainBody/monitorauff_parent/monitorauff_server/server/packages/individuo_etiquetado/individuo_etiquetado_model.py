from django.db import models
from server.packages.base.base_model import BaseModel
from server.packages.etiqueta_individuo.etiqueta_individuo_model import \
    EtiquetaIndividuo
from server.packages.individuo.individuo_model import Individuo


class IndividuoEtiquetado(BaseModel):
    '''
        Classe de relacionamento entre Individuo e EtiquetaIndividuo
    '''

    individuo = models.ForeignKey(Individuo, on_delete=models.CASCADE)
    etiqueta_individuo = models.ForeignKey(
        EtiquetaIndividuo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'RL_INDIVIDUO_ETIQUETA'
