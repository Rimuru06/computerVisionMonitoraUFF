from django.db import models
from server.packages.base.base_model import BaseModel
from server.packages.etiqueta_individuo.etiqueta_individuo_model import \
    EtiquetaIndividuo


class Individuo(BaseModel):
    nome = models.CharField(blank=False, max_length=256)
    etiquetas = models.ManyToManyField(
        EtiquetaIndividuo, blank=True, through='IndividuoEtiquetado')

    class Meta:
        db_table = 'TB_INDIVIDUO'
