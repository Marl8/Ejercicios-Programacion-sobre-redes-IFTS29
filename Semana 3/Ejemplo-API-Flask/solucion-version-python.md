## Cambio de versiones de Python en Proyectos

**Solución para que funcione Flask** 

El problema es que la versión 3.11 está instalada como Global y luego instalé la 3.14. Para que funcione Flask debo usar la que esta como versión Global, osea la 3.11.

- Presiona F1.

- Escribe ``Python: Select Interpreter``.

- Elige la opción que dice Python 3.11.x.

````bash

# Para instalar en la 3.14 globalmente
py -3.14 -m pip install flask

````

Para ver las librerías instaladas en cada versión

Para ver lo de la 3.11:

````bash

py -3.11 -m pip list

````
Para ver lo de la 3.14:

````bash

py -3.14 -m pip list

````

O Opción 2: Crear un entorno Virtual

**1.** Crear entorno con la versión que vas a usar:

````bash
python3.14 -m venv venv
````

**2.** Activar:

````bash
source venv/Scripts/activate
````

**3.** Ver versión de Python:

````bash
python --version
````

**3.** Instalar cosas:

````bash
pip install flask
````

**4.** Salir:

````bash
deactivate
````
Crear un archivo tipo ``Package.json`` el Javascript con toas las dependencias instaladas

````bash
pip freeze > requirements.txt
````

Para correr la aplicación:

````bash
python run.py
````