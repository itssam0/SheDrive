from django.urls import path
from WebApp import views

urlpatterns = [ 
    path('index/', views.index, name="index"),
    path('signinCond/', views.signinCond, name="signinCond"),
    path('pasajera/<str:identificacion>/', views.pasajera, name="pasajera"),
    path('logout/', views.logout_view, name='logout')
]
