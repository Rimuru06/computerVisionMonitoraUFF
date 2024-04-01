from django.db import models
from server.packages.base.base_model import BaseModel
from server.packages.tipo_servico.tipo_servico_model import TipoServico


class TipoServicoMonitor(BaseModel):
    '''
        Classe de relacionamento entre TipoServico e Monitor
    '''

    servico = models.ForeignKey(
        TipoServico, related_name='servico', on_delete=models.CASCADE)
    monitor_id = models.IntegerField()

    class Meta:
        db_table = 'RL_TIPO_SERVICO_MONITOR'
        unique_together = ['servico', 'monitor_id']
