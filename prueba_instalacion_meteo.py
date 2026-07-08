import warnings

warnings.filterwarnings(
    "ignore",
    message="pkg_resources is deprecated as an API.*"
)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import xarray as xr
import netCDF4
import geopandas as gpd
import cartopy
import cartopy.crs as ccrs
import contextily
import xyzservices
from tropycal import tracks

print("====================================")
print("PRUEBA DE INSTALACIÓN METEOROLÓGICA")
print("====================================")
print("NumPy:", np.__version__)
print("Pandas:", pd.__version__)
print("SciPy:", scipy.__version__)
print("Xarray:", xr.__version__)
print("netCDF4:", netCDF4.__version__)
print("GeoPandas:", gpd.__version__)
print("Cartopy:", cartopy.__version__)
print("Contextily:", contextily.__version__)
print("Tropycal: importado correctamente")
print("====================================")
print("Todo funcionando correctamente")