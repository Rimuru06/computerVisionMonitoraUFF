from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from . import models

admin.site.register(models.AlertaIndividuo)
admin.site.register(models.EtiquetaIndividuo)
admin.site.register(models.EtiquetaPermissaoIndividuo)
admin.site.register(models.Individuo)
admin.site.register(models.IndividuoEtiquetado)
admin.site.register(models.OcorrenciaFace)
admin.site.register(models.PermissaoIndividuo)
admin.site.register(models.PermissaoIndividuoGrupo)
admin.site.register(models.ServicoDeteccaoFace)
admin.site.register(models.TipoServico)


@admin.register(models.User)
class UserAdmin(auth_admin.UserAdmin):
    model = models.User
