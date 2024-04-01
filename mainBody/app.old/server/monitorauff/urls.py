from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # django admin
    path('admin/', admin.site.urls),
    # user management    
    path("", include("monitor.urls", namespace="monitor")),
    path('accounts/', include('django.contrib.auth.urls')),    
]
