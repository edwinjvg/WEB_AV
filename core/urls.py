from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # estas son las url que definimos en el archivo urls.py de la app packages
    path('packages/', include('apps.packages.urls')),
    # estas son las url que definimos en el archivo urls.py de la app users
    path('users/', include('apps.users.urls')),
]

# nos permite tener acceso a las imagenes que estan en la carpeta static
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)