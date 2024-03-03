import logging, os
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.conf import settings
from django.db.models import F
from .models import Layer, ControlPoint, Camera, DetectedLicensePlate, Veiculo, AlertVeiculo, User
from .forms import LayerForm, ControlpointForm, CameraForm, AlertForm, UserUpdateForm, UserCreationForm, EditCadForm


log_format = '%(asctime)s---%(levelname)s---%(filename)s---%(message)s'
logging.basicConfig(filename='tcc.log',
                    # w -> sobrescreve o arquivo a cada log
                    # a -> não sobrescreve o arquivo
                    filemode='w',
                    level=logging.DEBUG,
                    format=log_format)
logger = logging.getLogger('root')


# Função para permitir acesso somente a usuários ativos
def ativo(user):
    return user.status.endswith('Ativo')

# Função para permitir acesso a determinada view apenas ao gerente
def tipo_gerente(user):
    return user.tipoUser.endswith('Gerente')

# Função para permitir acesso a determinada view apenas ao gerente
def tipo_analista_gerente(user):
    if user.tipoUser == 'Gerente' or user.tipoUser == 'Analista':
        return True

def index(request):    
    return render(request, "monitor/index.html")

def erro(request):    
    return render(request, "monitor/erro.html")

def erro_dadosAssociados(request):    
    return render(request, "monitor/erro_dadosAssociados.html")

def inativo(request):    
    return render(request, "monitor/inativo.html")

# Página do monitor (mapa)
@login_required
@user_passes_test(ativo, login_url='/inativo')
@user_passes_test(tipo_analista_gerente, login_url='/erro')
def monitor(request):
    context = {
        'layer_list': Layer.objects.filter(status='Ativo'),
        'controlpoint_list': ControlPoint.objects.filter(status='Ativo'),
        'camera_list': Camera.objects.filter(status='Ativo').order_by('controlpoint', 'direction', 'tag_slug'),
    }
    return render(request, "monitor/monitor.html", context)

# Painel de visualização da câmera
@login_required
@user_passes_test(ativo, login_url='/inativo')
@user_passes_test(tipo_analista_gerente, login_url='/erro')
def rtsp_panel(request, controlpoint_id, monitor_id):
    context = {
        'monitor_id': monitor_id,
        'controlpoint': ControlPoint.objects.get(pk=controlpoint_id),
        'camera_list': Camera.objects.filter(controlpoint=controlpoint_id).order_by('direction', 'tag_slug'),
    }
    return render(request, "monitor/rtsp-panel.html", context)


# Visualizar os dados salvos de uma placa
@login_required
@user_passes_test(ativo, login_url='/inativo')
def placaListView(request):
    # Verifica se existe alguma placa que não está com os dados do veiculo. 
    # Caso positivo verifica se dados já foram salvos antes
    # Se não busca na API e salva
    listPlacaAPI = DetectedLicensePlate.objects.filter(veiculo=None)
    if listPlacaAPI:
        for placa in listPlacaAPI:
            placas_veiculos = DetectedLicensePlate.objects.filter(license_plate=placa.license_plate).exclude(veiculo=None)
            if placas_veiculos: 
                for i in placas_veiculos:
                    veiculo = i.veiculo_id
                DetectedLicensePlate.objects.filter(id=placa.id).update(veiculo_id=veiculo)
            else:
                # Conexão com API DENATRAN
                #veiculo_update = Veiculo.objects.create(marca='GM', modelo='Celta', ano='2008',cor='Preta')
                #placa.veiculo = veiculo_update
                #placa.save()
                pass    

    # Ordenar dados           
    ordem = request.GET.get('order_by', 'detection_date')
    lista = DetectedLicensePlate.objects.all().values(identificador=F('id'), data=F('detection_date'), imagem=F('img_filename'), placa=F('license_plate'), marca=F('veiculo__marca'), modelo=F('veiculo__modelo'), 
                                                      ano=F('veiculo__ano'), cor=F('veiculo__cor'), direcao=F('camera__direction'), endereco=F('camera__controlpoint__address'), 
                                                      controlpoint=F('camera__controlpoint__name'), campi=F('camera__controlpoint__layer__name')).order_by(ordem)
    
    # Busca por placa
    search = request.GET.get('search')
    if search:
        lista = DetectedLicensePlate.objects.filter(license_plate__icontains=search).values(identificador=F('id'), data=F('detection_date'), imagem=F('img_filename'), placa=F('license_plate'), marca=F('veiculo__marca'), modelo=F('veiculo__modelo'), 
                                                      ano=F('veiculo__ano'), cor=F('veiculo__cor'), direcao=F('camera__direction'), endereco=F('camera__controlpoint__address'), 
                                                      controlpoint=F('camera__controlpoint__name'), campi=F('camera__controlpoint__layer__name')).order_by(ordem)
    
    # Busca avançada
    if request.method == "GET":
        campus = request.GET.get('campus')
        controlpoint = request.GET.get('controlpoint')
        endereco = request.GET.get('endereco')
        direcao = request.GET.get('direcao')
        marca = request.GET.get('marca')
        modelo = request.GET.get('modelo')
        cor = request.GET.get('cor')
        ano = request.GET.get('ano')
        placa = request.GET.get('placa')
        dataIncial = request.GET.get('dataInicial')
        dataFinal = request.GET.get('dataFinal')
        

    
    #paginação
    paginator = Paginator(lista, 5)
    page = request.GET.get('page')
    placas = paginator.get_page(page)

    context = {'placa_list': placas}
    return render(request, "monitor/placaList.html", context)


@login_required
@user_passes_test(ativo, login_url='/inativo')
def buscaAvancada(request):
    # Ordenar dados
    ordem = request.GET.get('order_by', 'detection_date')
    # Fazer busca avançada
    query = {}
    
    campus = request.GET.get('campus')
    if campus:
        query['camera__controlpoint__layer__name__icontains'] = campus
    controlpoint = request.GET.get('controlpoint')
    if controlpoint:
        query['camera__controlpoint__name__icontains'] = controlpoint
    endereco = request.GET.get('endereco')
    if endereco:
        query['camera__controlpoint__address__icontains'] = endereco
    direcao = request.GET.get('direcao')
    if direcao:
        query['camera__direction__icontains'] = direcao
    marca = request.GET.get('marca')
    if marca:
        query['veiculo__marca__icontains'] = marca
    modelo = request.GET.get('modelo')
    if modelo:
        query['veiculo__modelo__icontains'] = modelo
    cor = request.GET.get('cor')
    if cor:
        query['veiculo__cor__icontains'] = cor
    ano = request.GET.get('ano')
    if ano:
        query['veiculo__ano__icontains'] = ano
    placa = request.GET.get('placa')
    if placa:
        query['license_plate__icontains'] = placa
    dataIncial = request.GET.get('dataInicial')
    if dataIncial:
        query['detection_date__gte'] = dataIncial
    dataFinal = request.GET.get('dataFinal')
    if dataFinal:
        query['detection_date__lte'] = dataFinal    

    
    lista = DetectedLicensePlate.objects.filter(**query).values(identificador=F('id'), data=F('detection_date'), imagem=F('img_filename'), placa=F('license_plate'), marca=F('veiculo__marca'), modelo=F('veiculo__modelo'), 
                                                ano=F('veiculo__ano'), cor=F('veiculo__cor'), direcao=F('camera__direction'), endereco=F('camera__controlpoint__address'), 
                                                controlpoint=F('camera__controlpoint__name'), campi=F('camera__controlpoint__layer__name')).order_by(ordem)
    
    
    #paginação
    paginator = Paginator(lista, 5)
    page = request.GET.get('page')
    placas = paginator.get_page(page)

    context = {'placa_list': placas}
    return render(request, "monitor/placaList.html", context)

@login_required
@user_passes_test(ativo, login_url='/inativo')
def placaView(request, id):
    placa = get_object_or_404(DetectedLicensePlate, pk=id)
    listPlacaAPI = DetectedLicensePlate.objects.filter(veiculo=None)
    veiculo = placa.veiculo
    placa_list = DetectedLicensePlate.objects.raw('SELECT layer.name as layer, controlpoint.address, camera.direction, placa.detection_date, placa.ID ' 
                                    'FROM monitor_layer as layer, monitor_controlpoint as controlpoint, monitor_camera as camera, monitor_detectedlicenseplate as placa ' 
                                    'WHERE layer.id = controlpoint.layer_id and controlpoint.id = camera.controlpoint_id and camera.id = placa.camera_id and placa.license_plate = %s', [placa.license_plate])
    context = { 
        'placa': placa,
        'placa_list': placa_list,
        'veiculo': veiculo,
        'test': listPlacaAPI
    }
    return render(request, "monitor/placa.html", context)


# Página de edição dos layer, pontos de decontroles e câmeras
@login_required
@user_passes_test(ativo, login_url='/inativo')
@user_passes_test(tipo_gerente, login_url='/erro')
def admin(request):
    context = {
        'layer_list': Layer.objects.all().order_by('status'),
        'controlpoint_list': ControlPoint.objects.all().order_by('status'),
        'camera_list': Camera.objects.all().order_by('status','controlpoint', 'direction', 'tag_slug'),
    }
    return render(request, "monitor/admin.html", context)

# CRUD usuário
@login_required
@user_passes_test(ativo, login_url='/inativo')
@user_passes_test(tipo_gerente, login_url='/erro')
def user_list(request):
    context = { 'user_list': User.objects.all()}
    return render(request, "monitor/usuarios.html", context)


def cadastro(request):
    if request.method == 'POST':        
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('/accounts/login/')
        else:
            render(request, 'monitor/registration/cadastro.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'monitor/registration/cadastro.html', {'form': form})

@login_required
def editar_cadastro(request, id):
    user = get_object_or_404(User, pk=id)
    form = EditCadForm(instance=user)
    if request.method == "POST":
        form = EditCadForm(request.POST, instance=user)
        if form.is_valid():
            user.save()
            return redirect('/') 
        else:
            return redirect('/')
    else:    
        return render(request, "monitor/registration/editar_cadastro.html", {'form': form, 'user': user})

@login_required
@user_passes_test(ativo, login_url='/inativo')
@user_passes_test(tipo_gerente, login_url='/erro')
def update_user(request, id):
    user = get_object_or_404(User, pk=id)
    form = UserUpdateForm(instance=user)
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            user.save()
            return redirect('/usuario') 
        else:
            return redirect('/usuario')
    else:    
        return render(request, "monitor/update_user.html", {'form': form, 'usuario': user})

@login_required
@user_passes_test(ativo, login_url='/inativo')
@user_passes_test(tipo_gerente, login_url='/erro')
def delete_user(request, id):
    user = get_object_or_404(User, pk=id)
    if request.method == "POST":
        try:
            user.delete()
            messages.info(request, 'Usuário excluído com sucesso')
            return redirect('/usuario')
        except:
            return redirect('/erro_dadosAssociados')
    else:
        context = {'usuario': user}
        return render(request, "monitor/delete_user.html", context)

# CRUD layer
@login_required
@user_passes_test(ativo, login_url='/inativo')
@user_passes_test(tipo_gerente, login_url='/erro')
def add_layer(request):
    if request.method == "POST":
        form = LayerForm(request.POST)
        if form.is_valid():
            layer = form.save(commit=False)
            layer.save()
            return redirect('/administracao')
        else:
            return redirect('/administracao')
    else:    
        form = LayerForm()
        return render(request, "monitor/add_layer.html", {'form': form})

@login_required
@user_passes_test(ativo, login_url='/inativo')
@user_passes_test(tipo_gerente, login_url='/erro')
def update_layer(request, id):
    layer = get_object_or_404(Layer, pk=id)
    form = LayerForm(instance=layer)
    if request.method == "POST":
        form = LayerForm(request.POST, instance=layer)
        if form.is_valid():
            status = form.cleaned_data['status']
            if status == "Inativo":
                ControlPoint.objects.filter(layer=layer).update(status="Inativo")
                Camera.objects.filter(controlpoint__layer=layer).update(status="Inativo")
            layer.save()
            return redirect('/administracao') 
        else:
            return redirect('/administracao')
    else:    
        return render(request, "monitor/update_layer.html", {'form': form, 'layer': layer})

@login_required
@user_passes_test(ativo, login_url='/inativo')
@user_passes_test(tipo_gerente, login_url='/erro')
def delete_layer(request, id):
    layer = get_object_or_404(Layer, pk=id)
    if request.method == "POST":
        try:
            layer.delete()
            messages.info(request, 'Layer excluído com sucesso')
            return redirect('/administracao')
        except:
            return redirect('/erro_dadosAssociados')
    else:
        '''
        layer_list = Layer.objects.filter(pk=id)
        lista = DetectedLicensePlate.objects.filter(camera__controlpoint__layer__in=layer_list)
        logger.info(f'=====> {lista}')
        '''
        controlpoint_list = ControlPoint.objects.filter(layer=layer)
        camera_list = Camera.objects.filter(controlpoint__in=controlpoint_list)
        placa_list = DetectedLicensePlate.objects.filter(camera__in=camera_list)

        context = {
            'layer': layer,
            'controlpoint_list': controlpoint_list,
            'camera_list': camera_list,
            'placa_list': placa_list
        }
        return render(request, "monitor/delete_layer.html", context)


# CRUD Ponto de controle
@login_required
@user_passes_test(ativo, login_url='/inativo')
@user_passes_test(tipo_gerente, login_url='/erro')
def add_controlpoint(request):
    if request.method == "POST":
        form = ControlpointForm(request.POST)
        if form.is_valid():
            controlpoint = form.save(commit=False)
            controlpoint.save()
            return redirect('/administracao')
        else:
            return redirect('/administracao')
    else:    
        form = ControlpointForm()
        return render(request, "monitor/add_controlpoint.html", {'form': form})

@login_required
@user_passes_test(ativo, login_url='/inativo')
@user_passes_test(tipo_gerente, login_url='/erro')
def update_controlpoint(request, id):
    controlpoint = get_object_or_404(ControlPoint, pk=id)
    form = ControlpointForm(instance=controlpoint)
    if request.method == "POST":
        form = ControlpointForm(request.POST, instance=controlpoint)
        if form.is_valid():
            status = form.cleaned_data['status']
            if status == "Inativo":
                Camera.objects.filter(controlpoint=controlpoint).update(status="Inativo")
            controlpoint.save()
            return redirect('/administracao') 
        else:
            return redirect('/administracao')
    else:    
        return render(request, "monitor/update_controlpoint.html", {'form': form, 'controlpoint': controlpoint})

@login_required
@user_passes_test(ativo, login_url='/inativo')
@user_passes_test(tipo_gerente, login_url='/erro')
def delete_controlpoint(request, id):
    controlpoint = get_object_or_404(ControlPoint, pk=id)
    if request.method == "POST":
        try:
            controlpoint.delete()
            messages.info(request, 'Ponto de controle excluído com sucesso')
            return redirect('/administracao')
        except:
            return redirect('/erro_dadosAssociados')
    else:
        camera_list = Camera.objects.filter(controlpoint=controlpoint)
        placa_list = DetectedLicensePlate.objects.filter(camera__in=camera_list)

        context = {
            'controlpoint': controlpoint,
            'camera_list': camera_list,
            'placa_list': placa_list
        }
        return render(request, "monitor/delete_controlpoint.html", context)


# CRUD câmera
@login_required
@user_passes_test(ativo, login_url='/inativo')
@user_passes_test(tipo_gerente, login_url='/erro')
def add_camera(request):
    if request.method == "POST":
        form = CameraForm(request.POST)
        if form.is_valid():
            camera = form.save(commit=False)
            camera.save()
            return redirect('/administracao')
        else:
            return render(request, 'monitor/add_camera.html', {'form': form})
    else:    
        form = CameraForm()
        return render(request, "monitor/add_camera.html", {'form': form})

@login_required
@user_passes_test(ativo, login_url='/inativo')
@user_passes_test(tipo_gerente, login_url='/erro')
def update_camera(request, id):
    camera = get_object_or_404(Camera, pk=id)
    form = CameraForm(instance=camera)
    if request.method == "POST":
        form = CameraForm(request.POST, instance=camera)
        if form.is_valid():
            camera.save()
            return redirect('/administracao') 
        else:
            return redirect('/administracao')
    else:    
        return render(request, "monitor/update_camera.html", {'form': form, 'camera': camera})

@login_required
@user_passes_test(ativo, login_url='/inativo')
@user_passes_test(tipo_gerente, login_url='/erro')
def delete_camera(request, id):
    camera = get_object_or_404(Camera, pk=id)
    if request.method == "POST":
        try:
            camera.delete()
            messages.info(request, 'Câmera excluído com sucesso')
            return redirect('/administracao')
        except:
            return redirect('/erro_dadosAssociados')
    else:
        placa_list = DetectedLicensePlate.objects.filter(camera=camera)

        context = {
            'camera': camera,
            'placa_list': placa_list
        }
        return render(request, "monitor/delete_camera.html", context)


# CRUD alerta de veiculos
@login_required
@user_passes_test(ativo, login_url='/inativo')
@user_passes_test(tipo_analista_gerente, login_url='/erro')
def alert(request):
    context = {
        'alert_list': AlertVeiculo.objects.all(),
    }
    return render(request, "monitor/alert.html", context)

@login_required
@user_passes_test(ativo, login_url='/inativo')
@user_passes_test(tipo_analista_gerente, login_url='/erro')
def add_alert(request):
    if request.method == "POST":
        form = AlertForm(request.POST)
        if form.is_valid():
            alert = form.save(commit=False)
            alert.save()
            return redirect('/alert')
        else:
            return redirect('/alert')
    else:    
        form = AlertForm()
        return render(request, "monitor/add_alert.html", {'form': form})

@login_required
@user_passes_test(ativo, login_url='/inativo')
@user_passes_test(tipo_gerente, login_url='/erro')
def update_alert(request, id):
    alert = get_object_or_404(AlertVeiculo, pk=id)
    form = AlertForm(instance=alert)
    if request.method == "POST":
        form = AlertForm(request.POST, instance=alert)
        if form.is_valid():
            alert.save()
            return redirect('/alert') 
        else:
            return redirect('/alert')
    else:    
        return render(request, "monitor/update_alert.html", {'form': form, 'alert': alert})

@login_required
@user_passes_test(ativo, login_url='/inativo')
@user_passes_test(tipo_gerente, login_url='/erro')
def delete_alert(request, id):
    alert = get_object_or_404(AlertVeiculo, pk=id)
    try:
        alert.delete()
        messages.info(request, 'Veículo excluído com sucesso')
        return redirect('/alert')
    except:
            return redirect('/erro_dadosAssociados')
    
# Inicia o agente via SSH
def agent_start(request, tag_slug):
    try:
        logger.info(f'=====> {tag_slug}')
        camera = Camera.objects.get(tag_slug=tag_slug)
        logger.info(f'=====> {camera.id}')
        database = settings.DATABASES['default']
        logger.info(f'=====> {tag_slug}')

        
        command = 'nohup python3 -m monitorauff.app.client.agent --monitor "%s" --video "%s" --name "%s" --dbhost "%s" --dbport "%s" --dbname "%s" --dbuser "%s" --dbpwd "%s" > /dev/null 2>&1 &' % (
            request.get_host(),
            camera.rtsp_url,
            camera.tag_slug,
            database['HOST'], database['PORT'], database['NAME'], database['USER'], database['PASSWORD']
        )
        os.system('ssh %s@%s \'%s\'' % (camera.agent_user, camera.agent_server, command))
        logger.info(f'=====> start')
        return JsonResponse({'success': True})
    except Exception as error:
        return JsonResponse({'success': False, 'error': str(error)})



