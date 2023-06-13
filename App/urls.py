from django.conf import settings
from django.urls import path
from .views import Home , X_Rey,dashboard,all,allPatients,updatePatients,updatePatients2,deletePatients,deletePatientsDahboard
from django.conf.urls.static import static
app_name = "App"
urlpatterns  = [
    path('xray/', X_Rey, name='X_Rey'),
    path('dashboard/<str:id>/update/', updatePatients, name = "update"),
    path('update/<str:id>/', updatePatients2, name = "update2"),
    
    path('delete/<str:id>/', deletePatients, name = "delete"),
    path('dashboard/<str:id>/delete/', deletePatientsDahboard, name = "dashboard-delete"),
    
    path('dashboard/', dashboard, name='X_Rey'),
    path('all/',all,name="all"),
    path('', Home, name='home'),
    
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)