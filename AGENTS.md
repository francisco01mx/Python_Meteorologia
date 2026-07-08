\# AGENTS.md



\## Proyecto



Este repositorio corresponde al proyecto `Python\_Meteorologia`.



El objetivo principal es desarrollar scripts en Python para análisis meteorológico, climatológico, geoespacial y generación de productos gráficos, incluyendo:



\- mapas meteorológicos;

\- productos del NHC;

\- potencial ciclónico;

\- trayectorias de ciclones tropicales;

\- análisis con Tropycal;

\- mapas con Cartopy y GeoPandas;

\- manejo de datos NetCDF;

\- productos gráficos para redes sociales;

\- automatización de descargas, análisis y salidas.



\---



\## Entorno de trabajo



El proyecto usa:



\- Windows;

\- Python 3.12.10;

\- entorno virtual local: `venv\_meteo`;

\- Visual Studio Code;

\- Git y GitHub.



El entorno virtual se encuentra en:



```text

C:\\Python\_Meteorologia\\venv\_meteo

```



Para activar el entorno en PowerShell:



```powershell

cd C:\\Python\_Meteorologia

.\\venv\_meteo\\Scripts\\activate

```



\---



\## Reglas importantes



1\. No modificar directamente la carpeta `venv\_meteo`.

2\. No subir el entorno virtual al repositorio.

3\. No guardar archivos pesados innecesarios en GitHub.

4\. Usar rutas relativas cuando sea posible.

5\. Usar `pathlib.Path` para manejo de rutas.

6\. Mantener el código claro, comentado y organizado.

7\. No sobrescribir archivos importantes sin confirmación.

8\. Cuando se generen imágenes o salidas, usar nombres descriptivos con fecha u hora si aplica.

9\. Si se agregan nuevas librerías, actualizar `requirements.txt`.

10\. Antes de cambios grandes, revisar el estado con `git status`.



\---



\## Estructura del proyecto



La estructura base del proyecto es:



```text

Python\_Meteorologia

│

├── Datos

├── Imagenes

├── Recursos

├── Salidas

├── Scripts

├── venv\_meteo

│

├── AGENTS.md

├── README\_instalacion\_python\_meteorologia.txt

├── requirements.txt

├── prueba\_instalacion\_meteo.py

├── prueba\_python.py

└── prueba\_vscode.py

```



Uso recomendado de carpetas:



```text

Datos      → archivos descargados, shapefiles, CSV, TXT, NetCDF, ZIP, JSON.

Imagenes   → mapas, gráficas y productos visuales generados.

Recursos   → logos, plantillas, iconos, escalas de color, fuentes e imágenes base.

Salidas    → tablas, reportes, archivos procesados y resultados finales.

Scripts    → códigos .py de trabajo.

venv\_meteo → entorno virtual local. No modificar manualmente.

```



\---



\## Librerías principales instaladas



El entorno cuenta con librerías para análisis científico, meteorología y geoprocesamiento, entre ellas:



```text

numpy

pandas

matplotlib

scipy

xarray

netCDF4

h5netcdf

geopandas

cartopy

contextily

xyzservices

tropycal

requests

pillow

openpyxl

beautifulsoup4

lxml

tqdm

```



\---



\## Verificación del entorno



Para verificar que el entorno funciona, ejecutar:



```powershell

python prueba\_instalacion\_meteo.py

```



La prueba debe confirmar la carga de:



```text

NumPy

Pandas

SciPy

Xarray

netCDF4

GeoPandas

Cartopy

Contextily

Tropycal

```



\---



\## Tropycal



Tropycal funciona correctamente, pero puede mostrar una advertencia relacionada con `pkg\_resources`.



La advertencia no impide trabajar.



Para ocultarla en scripts que usen Tropycal, colocar al inicio:



```python

import warnings



warnings.filterwarnings(

&#x20;   "ignore",

&#x20;   message="pkg\_resources is deprecated as an API.\*"

)



from tropycal import tracks

```



\---



\## Estilo de código recomendado



Los scripts deberán seguir estas prácticas:



\- usar nombres descriptivos;

\- separar configuración, descarga de datos, procesamiento y generación de salidas;

\- evitar rutas absolutas innecesarias;

\- crear carpetas de salida si no existen;

\- incluir comentarios donde el proceso no sea obvio;

\- usar funciones cuando el script empiece a crecer;

\- evitar código duplicado;

\- manejar errores básicos de descarga o lectura de archivos;

\- generar mensajes claros en consola.



Ejemplo recomendado para rutas:



```python

from pathlib import Path



BASE\_DIR = Path(\_\_file\_\_).resolve().parents\[1]



DIR\_DATOS = BASE\_DIR / "Datos"

DIR\_IMAGENES = BASE\_DIR / "Imagenes"

DIR\_SALIDAS = BASE\_DIR / "Salidas"

DIR\_RECURSOS = BASE\_DIR / "Recursos"



DIR\_DATOS.mkdir(exist\_ok=True)

DIR\_IMAGENES.mkdir(exist\_ok=True)

DIR\_SALIDAS.mkdir(exist\_ok=True)

DIR\_RECURSOS.mkdir(exist\_ok=True)

```



\---



\## Convenciones para scripts



Guardar scripts nuevos en:



```text

Scripts

```



Usar nombres en minúsculas, descriptivos y separados por guion bajo.



Ejemplos:



```text

potencial\_ciclonico\_nhc.py

mapa\_trayectorias\_tropycal.py

descarga\_datos\_nhc.py

grafica\_temperatura\_estaciones.py

analisis\_lluvia\_municipal.py

```



\---



\## Convenciones para salidas



Las imágenes deben guardarse preferentemente en:



```text

Imagenes

```



Los archivos procesados o reportes deben guardarse en:



```text

Salidas

```



Cuando aplique, usar fecha y hora en el nombre del archivo.



Ejemplos:



```text

mapa\_potencial\_ciclonico\_20260708\_1215.png

trayectorias\_atlantico\_2025.png

resumen\_estaciones\_20260708.csv

```



\---



\## Manejo de dependencias



Después de instalar nuevas librerías, actualizar:



```powershell

pip freeze > requirements.txt

```



Para instalar dependencias desde cero:



```powershell

pip install -r requirements.txt

```



\---



\## Git



Flujo básico recomendado:



```powershell

git status

git add .

git commit -m "Descripción breve del cambio"

git push

```



Antes de modificar archivos importantes:



```powershell

git status

```



Después de terminar un avance funcional:



```powershell

git add .

git commit -m "Mensaje claro del avance"

git push

```



\---



\## Archivos que no deben subirse



El archivo `.gitignore` debe evitar subir:



```text

venv\_meteo/

\_\_pycache\_\_/

.vscode/

Datos/\*.zip

Datos/\*.nc

Datos/\*.grib

Datos/\*.tif

Imagenes/

Salidas/

\*.log

\*.tmp

```



\---



\## Prioridad del proyecto



La prioridad es producir scripts funcionales, reproducibles y claros para uso meteorológico operativo y de divulgación.



Los productos deben ser útiles para:



\- análisis técnico;

\- vigilancia meteorológica;

\- generación de mapas;

\- preparación de gráficos para redes;

\- automatización de productos;

\- documentación del flujo de trabajo.



\---



\## Nota final



Antes de hacer cambios grandes, revisar la estructura del proyecto y respetar la organización existente.



No modificar `venv\_meteo`.



No eliminar `requirements.txt`.



No eliminar `README\_instalacion\_python\_meteorologia.txt`.



No eliminar `prueba\_instalacion\_meteo.py`.

