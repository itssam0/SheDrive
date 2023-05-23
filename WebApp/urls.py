from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from WebApp import views

urlpatterns = [ 
    path('index/', views.index, name="index"),
    path('signinCond/', views.signinCond, name="signinCond"),
    path('pasajera/<str:identificacion>/', views.pasajera, name="pasajera"),
    path('signupC/', views.signupC, name='signupC'),
    path('conductoras/<str:identificacion_cond>/', views.conductoras, name='conductoras'),
    path('solicitar-viaje/', views.solicitar_viaje, name='solicitar_viaje'),
    #path('aprobar-viaje/<int:viaje_id>/', views.aprobar_viaje, name='aprobar_viaje'),
    path('logout/', views.logout_view, name='logout')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
