from rest_framework import serializers
from .models import Turno
from .models import Especialidad
from rest_framework import serializers
from django.contrib.auth.models import User


class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = '__all__'
    def validate(self, data):
        from datetime import time
        fecha = data.get('fecha')
        hora = data.get('hora')

        #  hora dentro del rango permitido
        if not (time(8, 0) <= hora < time(20, 0)):
            raise serializers.ValidationError("Los turnos deben estar entre las 8:00 y las 20:00.")
        
        # fecha en un día laboral
        if fecha.weekday() >= 5:
            raise serializers.ValidationError("Los turnos solo se pueden reservar de lunes a viernes.")
        
        # que no haya otro turno en la misma hora
        if Turno.objects.filter(fecha=fecha, hora=hora).exists():
            raise serializers.ValidationError("Ya existe un turno en esta fecha y hora.")

        return data

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = ['id', 'nombre']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']