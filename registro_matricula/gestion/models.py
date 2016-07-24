from django.db import models

class Materia(models.Model):
	nombre=models.CharField(max_length=30)
	fechaInicio=models.DateField(blank=True, null=True)
	fechaFin=models.DateField(blank=True, null=True)
	creditos=models.IntegerField()
	cupos=models.IntegerField()

	def __str__(self):
		return self.nombre

class Alumno(models.Model):
	lGenero=(
		('f','femenino'),
		('m','masculino'),
	)
	#idCA=models.ForeignKey(CajaAhorros, on_delete=models.CASCADE, default="")
	eliminado=models.BooleanField(default=False)
	nombres=models.CharField(max_length=30)
	apellidos=models.CharField(max_length=30)
	cedula=models.CharField(max_length=10, unique=True)
	correo=models.EmailField(max_length=30, blank=True, null=True)
	telefono=models.CharField(max_length=15, blank=True, null=True)
	celular=models.CharField(max_length=15, blank=True, null=True)
	direccion=models.TextField(max_length=100, default="direccion")
	sexo=models.CharField(max_length=10,choices=lGenero)
	fechaNacimiento=models.DateField(blank=True, null=True)

	def __str__(self):
		return self.cedula