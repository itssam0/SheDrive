from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Agendamientoviaje(models.Model):
    id_agenda = models.IntegerField(db_column='Id_agenda', primary_key=True)  
    identificacion_usu = models.OneToOneField('Usuaria', models.DO_NOTHING, db_column='Identificacion_usu')  
    id_viaje = models.OneToOneField('Viaje', models.DO_NOTHING, db_column='Id_viaje')  
    fecha = models.DateField(db_column='Fecha')  
    hora = models.TimeField(db_column='Hora')  

    class Meta:
        db_table = 'agendamientoviaje'


class Carro(models.Model):
    placa_carro = models.CharField(db_column='Placa_Carro', primary_key=True, max_length=6)  
    marca = models.CharField(db_column='Marca', max_length=50)  
    modelo = models.CharField(db_column='Modelo', max_length=50)  
    papeles = models.CharField(db_column='Papeles', max_length=100)  

    class Meta:
        db_table = 'carro'


class Conductora(models.Model):
    identificacion_cond = models.IntegerField(db_column='Identificacion_cond', primary_key=True)  
    nombre_cond = models.CharField(db_column='Nombre_cond', max_length=50)  
    correo = models.CharField(db_column='Correo', max_length=100)  
    contraseña = models.CharField(db_column='Contraseña', max_length=50) 
    celular = models.IntegerField(db_column='Celular')  
    placa_carro = models.OneToOneField(Carro, models.DO_NOTHING, db_column='placa_carro')

    class Meta:
        db_table = 'conductora'


class Usuaria(models.Model):
    identificacion_usu = models.IntegerField(db_column='Identificacion_usu', primary_key=True) 
    nombre_usu = models.CharField(db_column='Nombre_usu', max_length=50)  
    correo = models.CharField(db_column='Correo', max_length=100)  
    contraseña = models.CharField(db_column='Contraseña', max_length=50)  
    celular = models.IntegerField(db_column='Celular')  

    class Meta:
        db_table = 'usuaria'


class Viaje(models.Model):
    id_viaje = models.IntegerField(db_column='Id_viaje', primary_key=True)  
    identificacion_usu = models.ForeignKey('Usuaria', on_delete=models.CASCADE, related_name='viajes')
    identificacion_cond = models.ForeignKey('Conductora', on_delete=models.CASCADE, related_name='viajes')
    origen = models.CharField(db_column='Origen', max_length=50)  
    destino = models.CharField(db_column='Destino', max_length=50)  
    precio = models.IntegerField(db_column='Precio')  
    distancia = models.IntegerField(db_column='Distancia')  
    tiempo = models.CharField(db_column='Tiempo', max_length=50)  

    class Meta:
        db_table = 'viaje'