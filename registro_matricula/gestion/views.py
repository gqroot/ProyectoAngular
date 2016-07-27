from django.shortcuts import render, render_to_response, redirect
from .models import Materia, Alumno
from .forms import FormMateria, FormAlumno, FormLogin, EditarContrasenaForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse,HttpResponseRedirect

@login_required(login_url='/administrar/ingresar/')
def administrar(request):
	return render(request,'administrar.html',{})

def alumnos(request):
	obA=Alumno.objects.all()

	if request.GET.get('o'):
		obA=Alumno.objects.order_by(request.GET['o'])

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

	if request.GET.get('o'):
		obM=Materia.objects.order_by(request.GET['o'])

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
			messages.add_message(request, messages.ERROR, "Alumno no actualizado", fail_silently=True)
		else:
			messages.add_message(request, messages.SUCCESS, "Alumno actualizado", fail_silently=True)

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
			messages.add_message(request, messages.ERROR, "Materia no actualizada", fail_silently=True)
		else:
			messages.add_message(request, messages.SUCCESS, "Materia actualizada", fail_silently=True)

		return redirect(materias)

	return render(request, 'crear.html',context)

def eliminarAlumno(request):
	alumno = Alumno.objects.get(cedula=request.GET['ced'])
	if alumno.delete():
		messages.add_message(request, messages.SUCCESS, "Alumno eliminado", fail_silently=True)
	else:
		messages.add_message(request, messages.ERROR, "Alumno no eliminado", fail_silently=True)
	return redirect(alumnos)

def eliminarMateria(request):
	materia = Materia.objects.get(nombre=request.GET['id'])
	if materia.delete():
		messages.add_message(request, messages.SUCCESS, "Materia eliminada", fail_silently=True)
	else:
		messages.add_message(request, messages.ERROR, "Materia no eliminada", fail_silently=True)
	return redirect(materias)

def ingresar(request):
    
    obF = FormLogin(request.POST or None)
    context={
    	'form':obF,
    	'ms':'Por favor digíte su nombre de usuario y contraseña para ingresar',
    }

    next = ""
    if request.GET:  
        next = request.GET['next']
    if request.method == 'POST':
        if obF.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    if next == "":
                        return redirect(administrar)
                    else:
                        return redirect(next)
                else:
                	messages.add_message(request, messages.ERROR, 'Usuario inactivo', fail_silently=True)
                	return render(request,'login.html',context)
            else:
            	messages.add_message(request, messages.ERROR, 'El nombre de usuario o la contraseña que ingresaste son incorrectos', fail_silently=True)
            	return render(request,'login.html',context)
    return render(request,'login.html', context)

@login_required(login_url='/administrar/ingresar/')
def perfil(request):
    perfil = request.user
    form = EditarContrasenaForm
    if request.method == 'POST':
        form = EditarContrasenaForm(request.POST)
        if form.is_valid():
            request.user.password = make_password(form.cleaned_data['password'])
            request.user.save()
            messages.add_message(request, messages.SUCCESS, "La contraseña ha sido cambiado con exito!.", fail_silently=True)
            messages.add_message(request, messages.SUCCESS, "Es necesario introducir los datos para entrar.", fail_silently=True)
            return render_to_response('index.html', RequestContext(request, locals()))
        else:
            messages.add_message(request, messages.WARNING, "Datos incorrectos.", fail_silently=True)
    else:
        form = EditarContrasenaForm()

    context={
    	'perfil':perfil,
    	'form':form,
    }
        
    return render(request, 'perfil.html', context)

@login_required(login_url='')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/administrar')
