from django.db import models
import time

class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)  

    def __str__(self):
        return self.nombre

class Turno(models.Model):
    ESPECIALIDADES = [
        ('kinesiologia', 'Kinesiología'),
        ('nutricion', 'Nutrición'),
        ('psicopedagogia', 'Psicopedagogía'),
    ]

    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=50, choices=ESPECIALIDADES)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.nombre} - {self.especialidad} - {self.fecha} {self.hora}"
    
    
    def clean(self):
        from django.core.exceptions import ValidationError
        # Restricción de horario: de 8 am a 8 pm
        if not (self.hora >= time(8, 0) and self.hora < time(20, 0)):
            raise ValidationError("Los turnos deben estar entre las 8:00 y las 20:00.")
        # Restricción de días: lunes a viernes
        if self.fecha.weekday() >= 5:
            raise ValidationError("Los turnos solo se pueden reservar de lunes a viernes.")
        # Verificar que no haya otro turno en la misma hora
        if Turno.objects.filter(fecha=self.fecha, hora=self.hora).exists():
            raise ValidationError("Ya existe un turno en esta fecha y hora.")
