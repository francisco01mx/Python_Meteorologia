from datetime import datetime, timezone
from pathlib import Path

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator


BASE_DIR = Path(__file__).resolve().parents[1]
DIR_IMAGENES = BASE_DIR / "Imagenes"
ARCHIVO_SALIDA = DIR_IMAGENES / "mapa_base_cartopy_v2.png"

TITULO = "Mapa base - Golfo de México, Caribe y Atlántico occidental"
EXTENSION_MAPA = [-100, -55, 5, 35]
LONGITUDES_GRILLA = range(-100, -54, 10)
LATITUDES_GRILLA = range(10, 36, 10)


def crear_mapa() -> None:
    """Genera un mapa base con Cartopy y lo guarda como PNG."""
    DIR_IMAGENES.mkdir(exist_ok=True)

    fecha_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    texto_fuente = f"Fuente: Natural Earth / Cartopy | Elaborado: {fecha_utc}"

    proyeccion = ccrs.PlateCarree()
    fig = plt.figure(figsize=(16, 9), facecolor="white")
    ax = fig.add_subplot(1, 1, 1, projection=proyeccion)

    fig.subplots_adjust(left=0.06, right=0.98, top=0.88, bottom=0.12)

    ax.set_extent(EXTENSION_MAPA, crs=proyeccion)
    ax.set_facecolor("#cfe8f3")

    ax.add_feature(cfeature.OCEAN, facecolor="#cfe8f3", zorder=0)
    ax.add_feature(cfeature.LAND, facecolor="#eadfc8", edgecolor="#5c5448", linewidth=0.4, zorder=1)
    ax.add_feature(cfeature.LAKES, facecolor="#cfe8f3", edgecolor="#8bb8cc", linewidth=0.3, zorder=2)
    ax.add_feature(cfeature.COASTLINE, edgecolor="#2f2f2f", linewidth=0.9, zorder=3)
    ax.add_feature(cfeature.BORDERS, edgecolor="#5a5a5a", linewidth=0.6, zorder=3)
    ax.add_feature(cfeature.STATES, edgecolor="#7a7a7a", linewidth=0.35, zorder=3)

    grilla = ax.gridlines(
        crs=proyeccion,
        draw_labels=True,
        x_inline=False,
        y_inline=False,
        linewidth=0.55,
        color="#687985",
        alpha=0.55,
        linestyle="--",
        zorder=4,
    )
    grilla.xlocator = FixedLocator(list(LONGITUDES_GRILLA))
    grilla.ylocator = FixedLocator(list(LATITUDES_GRILLA))
    grilla.top_labels = False
    grilla.right_labels = False
    grilla.xlabel_style = {"size": 10, "color": "#333333"}
    grilla.ylabel_style = {"size": 10, "color": "#333333"}

    fig.suptitle(TITULO, fontsize=18, fontweight="bold", y=0.95)
    fig.text(
        0.5,
        0.045,
        texto_fuente,
        ha="center",
        va="center",
        fontsize=10,
        color="#444444",
    )

    fig.savefig(ARCHIVO_SALIDA, dpi=180, facecolor=fig.get_facecolor())
    plt.close(fig)

    print(f"Imagen guardada en: {ARCHIVO_SALIDA}")


if __name__ == "__main__":
    crear_mapa()
