from django.conf.urls import url
 
urlpatterns=[
	url(r'^$','gestion.views.administrar'),
	url(r'^alumnos','gestion.views.alumnos'),
	url(r'^materias','gestion.views.materias'),
	url(r'^modificarAlumno','gestion.views.modificarAlumno'),
	url(r'^eliminarAlumno','gestion.views.eliminarAlumno'),
	url(r'^modificarMateria','gestion.views.modificarMateria'),
	url(r'^eliminarMateria','gestion.views.eliminarMateria'),
	url(r'^crearAlumno','gestion.views.crearAlumno'),
	url(r'^crearMateria','gestion.views.crearMateria'),
]