from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('turnos.urls')),  # Incluye las URLs de la aplicación turnos
    path('api/auth/', include('django.contrib.auth.urls')),
]