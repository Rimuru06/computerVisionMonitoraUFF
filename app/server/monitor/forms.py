from django.contrib.auth import forms
from django import forms as forms2
from .models import User, Layer, ControlPoint, Camera, DetectedLicensePlate, AlertVeiculo



class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User

class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = ('name', 'matricula', 'email', 'username')

class LayerForm(forms2.ModelForm):
    class Meta:
        model = Layer
        fields = ('name', 'status')


class ControlpointForm(forms2.ModelForm):
    class Meta:
        model = ControlPoint
        fields = ('name', 'address', 'latitude', 'longitude', 'layer', 'status')

class CameraForm(forms2.ModelForm):
    class Meta:
        model = Camera
        fields = ('tag_slug', 'direction', 'model', 'rtsp_url', 'agent_user', 'agent_server', 'controlpoint', 'status')

class AlertForm(forms2.ModelForm):
    class Meta:
        model = AlertVeiculo
        fields = ('license_plate', 'motivo')

class UserUpdateForm(forms2.ModelForm):
    class Meta:
        model = User
        fields = ('tipoUser', 'status')

class EditCadForm(forms2.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'username', 'email', 'matricula')
        
        