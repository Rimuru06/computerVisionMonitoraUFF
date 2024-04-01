from django.contrib.auth.models import AbstractUser
from django.db import models
from server.packages.base.base_model import BaseModel


class User(AbstractUser, BaseModel):
    nome = models.CharField(blank=True, max_length=200,
                            verbose_name='Nome completo')

    class Meta:
        db_table = 'TB_USUARIO'
