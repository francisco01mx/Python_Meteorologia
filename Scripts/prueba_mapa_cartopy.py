from pathlib import Path

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


BASE_DIR = Path(__file__).resolve().parents[1]
DIR_IMAGENES = BASE_DIR / "Imagenes"
ARCHIVO_SALIDA = DIR_IMAGENES / "mapa_prueba_cartopy.png"


def crear_mapa() -> None:
    """Genera un mapa simple del Golfo de Mexico y el Caribe."""
    DIR_IMAGENES.mkdir(exist_ok=True)

    proyeccion = ccrs.PlateCarree()
    figura = plt.figure(figsize=(12, 8))
    eje = plt.axes(projection=proyeccion)

    eje.set_extent([-100, -50, 5, 35], crs=proyeccion)

    eje.add_feature(cfeature.OCEAN, facecolor="#b8d8ee")
    eje.add_feature(cfeature.LAND, facecolor="#e6dcc3", edgecolor="black", linewidth=0.4)
    eje.add_feature(cfeature.COASTLINE, linewidth=0.8)
    eje.add_feature(cfeature.BORDERS, linewidth=0.6)
    eje.add_feature(cfeature.STATES, linewidth=0.35, edgecolor="gray")

    grilla = eje.gridlines(
        crs=proyeccion,
        draw_labels=True,
        linewidth=0.5,
        color="gray",
        alpha=0.7,
        linestyle="--",
    )
    grilla.xlocator = MultipleLocator(10)
    grilla.ylocator = MultipleLocator(10)
    grilla.top_labels = False
    grilla.right_labels = False

    eje.set_title(
        "Mapa de prueba con Cartopy: Golfo de Mexico, Caribe y Atlantico occidental",
        fontsize=14,
        pad=16,
    )

    figura.savefig(ARCHIVO_SALIDA, dpi=150, bbox_inches="tight")
    plt.close(figura)

    print(f"Imagen guardada en: {ARCHIVO_SALIDA}")


if __name__ == "__main__":
    crear_mapa()
