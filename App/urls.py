from django.conf import settings
from django.urls import path
from .views import Home , X_Rey
from django.conf.urls.static import static
urlpatterns  = [
    path('xray/', X_Rey, name='X_Rey'),
    path('', Home, name='home'),
    
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)