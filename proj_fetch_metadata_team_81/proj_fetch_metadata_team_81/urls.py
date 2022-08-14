from django import contrib
from django import urls
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('accounts.urls', namespace='accounts')),
    path('account/',include('django.contrib.auth.urls')),
    path('upload/',include('upload.urls')),
    path('matadata/',include('matadata.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
