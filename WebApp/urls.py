from django.urls import path
from WebApp import views

urlpatterns = [ 
    path('index/', views.index, name="index"),
    path('signinCond/', views.signinCond, name="signinCond"),
    path('pasajera/', views.pasajera, name="pasajera"),
]
