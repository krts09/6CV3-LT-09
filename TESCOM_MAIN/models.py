from django.db import models

# Create your models here.


class Alumno(models.Model):
    alumno_id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nombre} {self.apellido_paterno} {self.apellido_materno}'


class TrabajoTerminal(models.Model):
    tt_id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    calificacion = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.titulo


class Profesor(models.Model):
    profesor_id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    rol = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.apellido_paterno} {self.nombre} {self.rol}'


class AlumnoTrabajoTerminal(models.Model):
    alumno_id = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    trabajo_terminal = models.ForeignKey(TrabajoTerminal, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('alumno_id', 'trabajo_terminal')


class HorarioDisponible(models.Model):
    DIAS_SEMANA = [
        ('LU','Lunes'),
        ('MA', 'Martes'),
        ('MI', 'Miercoles'),
        ('JU', 'Jueves'),
        ('VI', 'Viernes'),
    ]

    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=2, choices=DIAS_SEMANA)
    horario_inicio = models.TimeField()
    horario_fin = models.TimeField()

    class Meta:
        unique_together = ('profesor', 'dia_semana', 'horario_inicio')

    def __str__(self):
        return f'{self.profesor} {self.dia_semana}, {self.horario_inicio}, {self.horario_fin}'


class Observaciones(models.Model):
    trabajo_terminal = models.ForeignKey(TrabajoTerminal, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return f'Observación de {self.profesor} sobre {self.trabajo_terminal} el {self.fecha}'
