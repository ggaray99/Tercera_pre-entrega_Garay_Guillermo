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

        # Crear una nueva instancia del modelo ActivosAsignados
        asignacion = ActivosAsignados(
            codigo=codigo,
            descripcion=descripcion,
            fecha_de_carga=fecha_de_carga,
            usuario_asignado=usuario_asignado
        )

        # Guardar el objeto en la base de datos
        asignacion.save()

        # Redirigir a otra página después de guardar
        return redirect('inicio')

    # Si no es una solicitud POST, simplemente renderizar el formulario
    return render(request, "AppCoder/asignarActivos.html")

def asignarUsuarios(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        puesto = request.POST.get('puesto')
        sucursal = request.POST.get('sucursal')

        # Crear una nueva instancia del modelo Usuarios
        usuario = Usuarios(
            nombre=nombre,
            apellido=apellido,
            puesto=puesto,
            sucursal=sucursal
        )

        # Guardar el objeto en la base de datos
        usuario.save()

        # Redirigir a otra página después de guardar
        return redirect('inicio')

    # Si no es una solicitud POST, simplemente renderizar el formulario
    return render(request, "AppCoder/usuarios.html")

def asignarTipoActivos(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        descripcion = request.POST.get('descripcion')

        # Crear una nueva instancia del modelo TipoActivos
        tipo_activo = TipoActivos(
            codigo=codigo,
            descripcion=descripcion
        )

        # Guardar el objeto en la base de datos
        tipo_activo.save()

        # Redirigir a otra página después de guardar
        return redirect('inicio')

    # Si no es una solicitud POST, simplemente renderizar el formulario
    return render(request, "AppCoder/activos.html")


def busqueda_activo (request):
    return render(request,"AppCoder/busquedaactivo.html")


def buscar_activos(request):
    if request.method == 'GET':
        codigo = request.GET.get('codigo')

        # Verificar si codigo no es None antes de realizar la consulta
        if codigo is not None:
            activos = TipoActivos.objects.filter(codigo__icontains=codigo)
            return render(request, 'AppCoder/busquedaactivo.html', {'activos': activos})
    
    # Si codigo es None o si la solicitud no es GET, simplemente renderizar la página de búsqueda
    return render(request, 'AppCoder/busquedaactivo.html')
