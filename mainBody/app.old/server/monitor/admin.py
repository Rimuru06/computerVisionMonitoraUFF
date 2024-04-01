from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .forms import UserCreationForm, UserChangeForm
from .models import User, Layer, ControlPoint, Camera, DetectedLicensePlate, Veiculo

# admin.site.register(User, auth_admin.UserAdmin)
admin.site.register(Layer)
admin.site.register(ControlPoint)
admin.site.register(Camera)
admin.site.register(DetectedLicensePlate)
admin.site.register(Veiculo)

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    '''
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Campos personalizados", {"fields":("tipoUser","matricula",)}),
    )
    '''