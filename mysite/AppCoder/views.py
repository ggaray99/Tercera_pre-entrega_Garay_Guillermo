from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from .models import ActivosAsignados, Usuarios, TipoActivos
from django.shortcuts import render, redirect

# Create your views here.
def inicio(request):
    miHtml = open("C:/Users/ggaray/Desktop/Pre-Entrega 3/mysite/AppCoder/templates/AppCoder/index.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)



def asignarActivos(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        descripcion = request.POST.get('descripcion')
        fecha_de_carga = request.POST.get('fecha_de_carga')
        usuario_asignado = request.POST.get('usuario_asignado')

        asignacion = ActivosAsignados(
            codigo=codigo,
            descripcion=descripcion,
            fecha_de_carga=fecha_de_carga,
            usuario_asignado=usuario_asignado
        )

        asignacion.save()

        return redirect('inicio')

    return render(request, "AppCoder/asignarActivos.html")

def asignarUsuarios(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        puesto = request.POST.get('puesto')
        sucursal = request.POST.get('sucursal')

        usuario = Usuarios(
            nombre=nombre,
            apellido=apellido,
            puesto=puesto,
            sucursal=sucursal
        )

        usuario.save()

        return redirect('inicio')

    return render(request, "AppCoder/usuarios.html")

def asignarTipoActivos(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        descripcion = request.POST.get('descripcion')

        tipo_activo = TipoActivos(
            codigo=codigo,
            descripcion=descripcion
        )

        tipo_activo.save()

        return redirect('inicio')

    return render(request, "AppCoder/activos.html")


def busqueda_activo (request):
    return render(request,"AppCoder/busquedaactivo.html")


def buscar_activos(request):
    if request.method == 'GET':
        codigo = request.GET.get('codigo')

        if codigo is not None:
            activos = TipoActivos.objects.filter(codigo__icontains=codigo)
            return render(request, 'AppCoder/busquedaactivo.html', {'activos': activos})
    
    return render(request, 'AppCoder/busquedaactivo.html')
