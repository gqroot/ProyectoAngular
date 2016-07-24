from gestion.models import Materia
from .serializable import MateriaSerializable
from rest_framework import viewsets

class MateriaViewSet(viewsets.ModelViewSet):
	serializer_class=MateriaSerializable
	queryset=Materia.objects.filter(cupos__lte=29)
	
