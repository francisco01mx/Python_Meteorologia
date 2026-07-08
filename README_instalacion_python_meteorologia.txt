INSTALACIÓN Y CONFIGURACIÓN DE PYTHON METEOROLÓGICO
Proyecto: Python_Meteorologia
Equipo: Laptop recién formateada
Fecha de elaboración: 08/07/2026

============================================================
1. RESUMEN GENERAL
============================================================

Se instaló y configuró Python en Windows para trabajar proyectos de meteorología,
climatología, mapas, trayectorias de ciclones, productos del NHC, análisis de datos
y generación de gráficas.

La instalación quedó funcional en la carpeta:

C:\Python_Meteorologia

Se creó un entorno virtual llamado:

venv_meteo

El entorno virtual sirve para instalar las librerías del proyecto sin afectar el
Python general de Windows.

============================================================
2. COMPONENTES INSTALADOS Y VERIFICADOS
============================================================

Python instalado:
- Python 3.12.10

Entorno virtual:
- C:\Python_Meteorologia\venv_meteo

Editor configurado:
- Visual Studio Code

Librerías base instaladas:
- numpy
- pandas
- matplotlib
- requests
- pillow
- openpyxl

Librerías científicas instaladas:
- scipy
- xarray
- netCDF4
- h5netcdf

Librerías geoespaciales y de mapas instaladas:
- geopandas
- cartopy
- contextily
- xyzservices

Librerías meteorológicas:
- tropycal

Librerías auxiliares:
- beautifulsoup4
- lxml
- tqdm
- setuptools-scm
- networkx

Versiones confirmadas en la prueba final:

NumPy: 2.5.1
Pandas: 3.0.3
SciPy: 1.18.0
Xarray: 2026.4.0
netCDF4: 1.7.4
GeoPandas: 1.1.4
Cartopy: 0.25.0
Contextily: 1.7.0
Tropycal: importado correctamente

============================================================
3. CARPETA PRINCIPAL DEL PROYECTO
============================================================

La carpeta principal de trabajo es:

C:\Python_Meteorologia

Estructura recomendada:

C:\Python_Meteorologia
|
|-- venv_meteo
|-- Scripts
|-- Datos
|-- Salidas
|-- Imagenes
|-- Recursos
|-- requirements.txt
|-- prueba_python.py
|-- prueba_vscode.py
|-- prueba_instalacion_meteo.py

Uso recomendado de carpetas:

Scripts:
Guardar aquí los archivos .py de trabajo.

Datos:
Guardar aquí archivos descargados, shapefiles, CSV, NetCDF, TXT, JSON, etc.

Salidas:
Guardar aquí tablas, archivos procesados y resultados intermedios.

Imagenes:
Guardar aquí mapas, gráficas y productos visuales generados.

Recursos:
Guardar aquí logotipos, plantillas, fuentes, íconos, escalas de color y otros
elementos gráficos reutilizables.

============================================================
4. CÓMO INICIAR EL ENTORNO CADA VEZ QUE SE USE
============================================================

Cada vez que se abra PowerShell o la terminal de VS Code, se debe entrar a la
carpeta del proyecto y activar el entorno virtual.

Comandos:

cd C:\Python_Meteorologia
.\venv_meteo\Scripts\activate

Cuando esté activo, la terminal debe mostrar algo parecido a:

(venv_meteo) PS C:\Python_Meteorologia>

Eso indica que se está trabajando dentro del entorno virtual correcto.

============================================================
5. CÓMO ABRIR EL PROYECTO EN VISUAL STUDIO CODE
============================================================

Desde PowerShell:

cd C:\Python_Meteorologia
.\venv_meteo\Scripts\activate
code .

Esto abrirá Visual Studio Code directamente en la carpeta del proyecto.

En VS Code se debe verificar que el intérprete seleccionado sea:

C:\Python_Meteorologia\venv_meteo\Scripts\python.exe

Debe aparecer como:

venv_meteo (Python 3.12.10)

============================================================
6. CÓMO EJECUTAR UN SCRIPT
============================================================

Ejemplo:

python prueba_instalacion_meteo.py

Para ejecutar cualquier otro archivo:

python nombre_del_script.py

Ejemplo:

python potencial_ciclonico_nhc.py

============================================================
7. ARCHIVO REQUIREMENTS.TXT
============================================================

Se generó el archivo:

requirements.txt

Este archivo contiene la lista de librerías instaladas en el entorno.

Para actualizarlo después de instalar nuevas librerías:

pip freeze > requirements.txt

Para reinstalar las mismas librerías en otra computadora o en un nuevo entorno:

pip install -r requirements.txt

============================================================
8. PRUEBA FINAL REALIZADA
============================================================

Se creó y ejecutó el archivo:

prueba_instalacion_meteo.py

El resultado fue:

====================================
PRUEBA DE INSTALACIÓN METEOROLÓGICA
====================================
NumPy: 2.5.1
Pandas: 3.0.3
SciPy: 1.18.0
Xarray: 2026.4.0
netCDF4: 1.7.4
GeoPandas: 1.1.4
Cartopy: 0.25.0
Contextily: 1.7.0
Tropycal: importado correctamente
====================================
Todo funcionando correctamente

Esto confirma que el entorno está listo para trabajos meteorológicos y geoespaciales.

============================================================
9. NOTA SOBRE TROPYCAL
============================================================

Tropycal funciona correctamente, pero puede mostrar una advertencia relacionada
con pkg_resources:

pkg_resources is deprecated as an API

Esta advertencia no impide trabajar. No es un error crítico.

Para ocultarla en scripts donde se use Tropycal, se puede colocar al inicio:

import warnings

warnings.filterwarnings(
    "ignore",
    message="pkg_resources is deprecated as an API.*"
)

from tropycal import tracks

============================================================
10. COMANDOS IMPORTANTES
============================================================

Ver versión de Python:

python --version

Ver versión de pip:

pip --version

Ver librerías instaladas:

pip list

Guardar entorno:

pip freeze > requirements.txt

Instalar librerías desde requirements.txt:

pip install -r requirements.txt

Activar entorno:

.\venv_meteo\Scripts\activate

Salir del entorno virtual:

deactivate

Abrir VS Code:

code .

============================================================
11. FLUJO DE TRABAJO RECOMENDADO
============================================================

1. Abrir PowerShell o VS Code.
2. Entrar a la carpeta:

   cd C:\Python_Meteorologia

3. Activar entorno:

   .\venv_meteo\Scripts\activate

4. Abrir VS Code si no está abierto:

   code .

5. Guardar scripts en la carpeta Scripts.
6. Guardar datos descargados en la carpeta Datos.
7. Guardar imágenes generadas en Imagenes.
8. Guardar productos o archivos finales en Salidas.
9. Al instalar nuevas librerías, actualizar:

   pip freeze > requirements.txt

============================================================
12. PROYECTOS QUE YA SE PUEDEN RETOMAR
============================================================

Con esta instalación ya se pueden trabajar proyectos como:

- mapas del NHC
- potencial ciclónico
- trayectorias históricas de ciclones
- análisis con Tropycal
- mapas con Cartopy
- shapefiles con GeoPandas
- mapas base con OpenStreetMap/contextily
- análisis de series meteorológicas
- datos NetCDF con xarray y netCDF4
- productos gráficos para redes sociales
- scripts de automatización meteorológica

============================================================
13. RECOMENDACIÓN FINAL
============================================================

No conviene instalar más librerías sin necesidad inmediata.

Antes de continuar, se recomienda:

1. Mantener este archivo como respaldo.
2. Mantener actualizado requirements.txt.
3. Instalar Git y conectar la carpeta con GitHub.
4. Después, conectar el flujo de trabajo con Codex.

Fin del documento.
