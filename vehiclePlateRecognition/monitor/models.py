from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    STATUS = (
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo')
    )
    TIPO = (
        ('Gerente', 'Gerente'), 
        ('Analista', 'Analista'), 
        ('Segurança', 'Segurança')
    )

    name = models.CharField(max_length=200, blank=True, verbose_name='Nome completo')
    tipoUser = models.CharField(blank=True, max_length=150, choices=TIPO, verbose_name='Função')
    matricula = models.CharField(blank=True, max_length=150, verbose_name='Matricula', unique=True)
    status = models.CharField(max_length=8, choices=STATUS, blank=True, default=STATUS[1][1])

    def status_verbose(self):
        return dict(User.STATUS)[self.status]
    
    def tipo_verbose(self):
        return dict(User.TIPO)[self.tipoUser]

class Layer(models.Model):
    STATUS = (
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo')
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=8, choices=STATUS, default=STATUS[0][0])
    
    def __str__(self):
        return self.name


class ControlPoint(models.Model):
    STATUS = (
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo')
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.CharField(max_length=8, choices=STATUS, default=STATUS[0][0])
    layer = models.ForeignKey(Layer, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name


class Camera(models.Model):
    DIRECTIONS = (
        ('in', 'Entrada do campus'),
        ('out', 'Sa\u00EDda do campus'),
        ('even', 'Lado par da via'),
        ('odd', 'Lado \u00EDmpar da via'),
        ('free', 'Movimento livre (domo)'),
        ('sidewalk', 'C\u00E2mera de cal\u00E7ada')
    )

    STATUS = (
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo')
    )
    
    id = models.AutoField(primary_key=True)
    tag_slug = models.SlugField(max_length=50, unique=True)
    direction = models.CharField(max_length=8, choices=DIRECTIONS)
    model = models.CharField(max_length=200)
    rtsp_url = models.URLField(max_length=200)
    agent_user = models.CharField(max_length=100)
    agent_server = models.GenericIPAddressField(max_length=200)
    status = models.CharField(max_length=8, choices=STATUS, default=STATUS[0][0])
    controlpoint = models.ForeignKey(ControlPoint, on_delete=models.PROTECT)
        
    def direction_verbose(self):
        return dict(Camera.DIRECTIONS)[self.direction]
        
    def __str__(self):
        return self.tag_slug

class Veiculo(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=200, blank=True)
    modelo = models.CharField(max_length=200, blank=True)
    ano = models.CharField(max_length=100, blank=True)
    cor = models.CharField(max_length=200, blank=True)
    roubo = models.CharField(max_length=200, blank=True)

class DetectedLicensePlate(models.Model):
    id = models.AutoField(primary_key=True)
    detection_date = models.DateTimeField()
    license_plate = models.CharField(max_length=7)
    data_filename = models.CharField(max_length=256)
    img_filename = models.CharField(max_length=256, blank=True)
    data_password = models.CharField(max_length=8)
    data_md5 = models.CharField(max_length=32)
    camera = models.ForeignKey(Camera, on_delete=models.PROTECT)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT, blank=True, null=True)

class AlertVeiculo(models.Model):
    id = models.AutoField(primary_key=True)
    license_plate = models.CharField(max_length=7, verbose_name='Placa')
    motivo = models.TextField(max_length=400, blank=True)

class HistoricoAlert(models.Model):
    id = models.AutoField(primary_key=True)
    evento = models.CharField(max_length=200)
    obs = models.TextField(max_length=400, blank=True)
    update_date = models.DateTimeField()
    alertVeiculo = models.ForeignKey(AlertVeiculo, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)


