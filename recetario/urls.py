"""
URL configuration for recetario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

swagger_view = get_schema_view(
    openapi.Info(
        title='Api de recetario',
        default_version='v1',
        description='Api para gestionar el uso de un recetario',
        contact=openapi.Contact(name='Roberto',
                                email='r.apaza.cornejo@gmail.com')
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # si queremos agregar un archivo con otras rutas usaremos el metodo include
    # agregar un subconjunto de rutas
    path('gestion/', include('gestion.urls')),
    path('documentacion/',swagger_view.with_ui('swagger', cache_timeout=0))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
