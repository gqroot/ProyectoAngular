from django.shortcuts import render, redirect
from .models import Materia
from .models import Alumno
from .forms import FormMateria
from .forms import FormAlumno
from django.contrib import messages

def administrar(request):
	return render(request,'administrar.html',{})

def alumnos(request):
	obA=Alumno.objects.all()
	context={
		'alumnos':obA,
		't':'Alumnos',
	}
	return render(request,'alumnos.html',context)

def crearAlumno(request):
	obFA=FormAlumno(request.POST or None)

	context={
		'form':obFA,
		't':'Crear Alumno',
	}
	if request.method== 'POST':
		if obFA.is_valid():
			datosFA=obFA.cleaned_data

			alumno=Alumno()
			#alumno.idCA=CajaAhorros.objects.all()[0]
			alumno.nombres=datosFA.get('nombres')
			alumno.apellidos=datosFA.get('apellidos')
			alumno.cedula=datosFA.get('cedula')
			alumno.correo=datosFA.get('correo')
			alumno.telefono=datosFA.get('telefono')
			alumno.celular=datosFA.get('celular')
			alumno.direccion=datosFA.get('direccion')
			alumno.sexo=datosFA.get('sexo')
			alumno.fechaNacimiento=datosFA.get('fechaNacimiento')
			alumno.save()
			return redirect(alumnos)

	return render(request,'crear.html',context)

def materias(request):
	obM=Materia.objects.all()
	context={
		'materias':obM,
		't':'Materias',
	}
	return render(request,'materias.html',context)

def crearMateria(request):
	obFM=FormMateria(request.POST or None)

	context={
		'form':obFM,
		't':'Crear Materia',
	}
	if request.method== 'POST':
		if obFM.is_valid():
			datosFM=obFM.cleaned_data

			materia=Materia()
			#materia.idCA=CajaAhorros.objects.all()[0]
			materia.nombre=datosFM.get('nombre')
			materia.fechaInicio=datosFM.get('fechaInicio')
			materia.fechaFin=datosFM.get('fechaFin')
			materia.creditos=datosFM.get('creditos')
			materia.cupos=datosFM.get('cupos')
			materia.save()
			return redirect(materias)

	return render(request,'crear.html',context)

def modificarAlumno(request):
	alumno=Alumno.objects.get(cedula=request.GET['ced'])
	obF=FormAlumno(request.POST or None)	
	context={
		'form':obF,
		't':'MODIFICAR',
	}

	obF.fields['nombres'].initial=alumno.nombres
	obF.fields['apellidos'].initial=alumno.apellidos
	obF.fields['cedula'].initial=alumno.cedula
	obF.fields['correo'].initial=alumno.correo
	obF.fields['telefono'].initial=alumno.telefono
	obF.fields['celular'].initial=alumno.celular
	obF.fields['direccion'].initial=alumno.direccion
	obF.fields['sexo'].initial=alumno.sexo
	obF.fields['fechaNacimiento'].initial=alumno.fechaNacimiento
	obF.fields['cedula'].widget.attrs['readonly'] = True
	obF.fields['fechaNacimiento'].widget.attrs['readonly'] = True
	obF.fields['fechaNacimiento'].disabled=True

	if request.method== 'POST':
		alumno.nombres=request.POST['nombres']
		alumno.apellidos=request.POST['apellidos']
		alumno.correo=request.POST['correo']
		alumno.telefono=request.POST['telefono']
		alumno.celular=request.POST['celular']
		alumno.direccion=request.POST['direccion']
		alumno.sexo=request.POST['sexo']
		#alumno.fechaNacimiento=date(request.POST['fechaNacimiento_day']+'/'+request.POST['fechaNacimiento_month']+'/'+request.POST['fechaNacimiento_year'])
		if (alumno.save()):
			messages.add_message(request, messages.ERROR, "No se ha modificado el alumno", fail_silently=True)
		else:
			messages.add_message(request, messages.SUCCESS, "Se ha modificado el alumno", fail_silently=True)

		return redirect(alumnos)

	return render(request, 'crear.html',context)

def modificarMateria(request):
	materia=Materia.objects.get(nombre=request.GET['id'])
	obF=FormMateria(request.POST or None)	
	context={
		'form':obF,
		't':'MODIFICAR',
	}

	obF.fields['nombre'].initial=materia.nombre
	obF.fields['creditos'].initial=materia.creditos
	obF.fields['cupos'].initial=materia.cupos
	obF.fields['nombre'].widget.attrs['readonly'] = True
	obF.fields['fechaFin'].initial=materia.fechaFin
	obF.fields['fechaInicio'].initial=materia.fechaInicio
	obF.fields['fechaInicio'].widget.attrs['readonly'] = True
	obF.fields['fechaInicio'].disabled=True
	obF.fields['fechaFin'].widget.attrs['readonly'] = True
	obF.fields['fechaFin'].disabled=True

	if request.method== 'POST':
		materia.nombre=request.POST['nombre']
		materia.cupos=request.POST['cupos']
		materia.creditos=request.POST['creditos']
		#materia.fechaNacimiento=date(request.POST['fechaNacimiento_day']+'/'+request.POST['fechaNacimiento_month']+'/'+request.POST['fechaNacimiento_year'])
		if (materia.save()):
			messages.add_message(request, messages.ERROR, "No se ha modificado el materia", fail_silently=True)
		else:
			messages.add_message(request, messages.SUCCESS, "Se ha modificado el materia", fail_silently=True)

		return redirect(materias)

	return render(request, 'crear.html',context)

def eliminarAlumno(request):
	alumno = Alumno.objects.get(cedula=request.GET['ced'])
	if alumno.delete():
		messages.add_message(request, messages.SUCCESS, "Se ha eliminado el alumno", fail_silently=True)
	else:
		messages.add_message(request, messages.ERROR, "No se ha eliminado el alumno", fail_silently=True)
	return redirect(alumnos)

def eliminarMateria(request):
	materia = Materia.objects.get(nombre=request.GET['id'])
	if materia.delete():
		messages.add_message(request, messages.SUCCESS, "Se ha eliminado la materia", fail_silently=True)
	else:
		messages.add_message(request, messages.ERROR, "No se ha eliminado la materia", fail_silently=True)
	return redirect(materias)
