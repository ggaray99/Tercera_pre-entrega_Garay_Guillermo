### Tercera Entrega Python-Coderhouse

#### Consigna

###### Objetivos generales

Desarrollar una WEB Django con patrón MVT subida a Github.
###### Se debe entregar

Link de GitHub con el proyecto totalmente subido a la plataforma.
Proyecto Web Django con patrón MVT que incluya:
-Herencia de HTML.
-Por lo menos 3 clases en models.
-Un formulario para insertar datos a todas las clases de tu models.
-Un formulario para buscar algo en la BD
-Readme que indique el orden en el que se prueban las cosas y/o donde están las funcionalidades.

Se realizo el proyecto de la pre entrega en Visual Studio Code, utilizando Python como lenguaje principal y SQLLite como BBDD. También se utilizó DBBrowser para visualizar los datos cargados.

Se tuvieron en cuenta los requisitos de la consigna, creando una WEB Django con patrón MVT llamada AppCoder en este caso.
La misma dentro cuenta con tres clases:
```
class ActivosAsignados(models.Model):
    codigo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=255)
    fecha_de_carga = models.DateField()
    usuario_asignado = models.CharField(max_length=100)
```
Esta primer clase almacenará a quien fue asignado un activo en particular.

```
	class Usuarios(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    puesto = models.CharField(max_length=40)
    sucursal = models.CharField(max_length=40)
```
Aqui cargaremos los usuarios que podran tener asignado un activo.

```
	class TipoActivos(models.Model):
    codigo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=255)
```
Y en esta ultima clase guardaremos los activos a asignar luego.

Creamos en views.py las funciones que utilizaremos tanto para poder hacer el POST en una tabla, como asi tambien las funciones para poder hacer la busqueda GET segun un codigo de un activo.

En la pagina de inicio de la WEB nos encontraremos con una barra en la parte superior donde podremos acceder a cada uno de los formularios disponibles, tanto como para cargar datos o para realizar la busqueda.

Espero que la informacion les sea de ayuda!
