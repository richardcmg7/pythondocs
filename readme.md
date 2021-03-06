# Generarador de documentos

## Contenido
- [Instalacion](#install)
- [Motivación](#motivation)
- [Como Usarlo](#description)

<p align=""center">
    Esta aplicación apoya la generación de documentos "Manual de uso de infraestructura y confidencialidad"
</p>


<a name="install"></a>
## Instalacion

<a name="motivation"></a>
## Motivación

Dentro del proceso de desarrollo de software, el desarrollo de scripts aportan para el mejoramiento de la productividad. 
Esta aplicación tiene como fin apoyar en el desarrollo de documentos necesarios en el desarrollo de la gestion de proyectos en Tecnoparque.

<a name="description"></a>
## Como usarlo

El repositorio se encuentra en una primera etapa y será actualizado constantemente.

Se cuenta con 3 crud basicos para el proceso de generación de los documentos.

* Gestion de proyectos
* Gestion de talentos
* Gestion de expertos

Cada uno de los pasos definen el contenido que estara dentro del documento.

En general tiene las opciones de agregar - editar* - eliminar - seleccionar y - Salir con lo seleccionado.

Los diferentes registros se guardaran en un documento con extension .csv persistiendo en el script dichos datos.

### ** Debes tener instalada la version de python 3 para poder ejecutar la aplicación **

- Descarga o clona el repo: `git clone https://github.com/richardcmg7/pythondocs.git`
- Actualiza el nombre del gestor en el documento : `test_infraestructura.py` 
- Ejecutar con `python3 test_infraestructura.py` o `python test_infraestructura` según como tenga instalado el interprete de python.
- Seguir las instrucciones detenidamente.
    * Administrador de proyectos:
        El menu presenta diferentes opciones. Seleccionar la opcion. recuerda para finalizar debe dar en salir con el elemento seleccionado.
    * Gestion de talentos.
        Para el documento de confidencialidad deben pasar 3 de ellos(Titular, interlocutor, ejecutor). Utiliza el formato `1,2,1`
    * Gestion de expertos
        Seleccionar todos los expertos que iran en el documento. Utilizar la opcion salir para devolver los expertos seleccionados. Utiliza la forma: `0,1,2,3,4..`
## Versiones

Las actualizaciones se desarrollaran a traves de los diferentes realeases.

* Realease V1.0 - Version de inicio: Generador de base, funcionando con reglas estrictas. 
## Creadores

**Richard Saavedra**
@ Tecnoparque nodo neiva

