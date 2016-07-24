from rest_framework import serializers
from gestion.models import Materia

class MateriaSerializable(serializers.ModelSerializer):
	class Meta:
		model= Materia
		fields=['nombre','fechaInicio','fechaFin','creditos','cupos']
	

