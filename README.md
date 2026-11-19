# Python_Meteorologia

Entorno y scripts de Python para análisis meteorológico y geoespacial: mapas, datos NetCDF y productos de ciclones tropicales.

**Este repositorio no es un producto oficial** del Servicio Meteorológico Nacional (SMN), de la CONAGUA, del National Hurricane Center (NHC) ni de ninguna otra agencia. No sustituye avisos, alertas ni boletines oficiales.

Proyecto de [weather.francisco](https://github.com/francisco01mx/weather-francisco).

## Qué contiene

- Guía de instalación del entorno en Windows (`README_instalacion_python_meteorologia.txt`) y notas de trabajo (`AGENTS.md`).
- `requirements.txt` con el entorno verificado en julio de 2026: Python 3.12, NumPy, Pandas, SciPy, Xarray, netCDF4, GeoPandas, Cartopy, Contextily y Tropycal, entre otras librerías.
- Scripts para comprobar la instalación: `prueba_instalacion_meteo.py`, `prueba_python.py` y `prueba_vscode.py`.
- Un script de trabajo en `Scripts/prueba_mapa_cartopy.py`, que genera un mapa base del Golfo de México, el Caribe y el Atlántico occidental con Cartopy y Natural Earth.

Las carpetas locales de datos, imágenes y salidas no se versionan. El visor meteorológico completo está en [weather-francisco](https://github.com/francisco01mx/weather-francisco).

## Cómo usarlo

```powershell
python -m venv venv_meteo
.\venv_meteo\Scripts\activate
pip install -r requirements.txt
python prueba_instalacion_meteo.py
```

La guía de instalación describe el flujo original en `C:\Python_Meteorologia`.

— weather.francisco
