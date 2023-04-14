import geopandas as gpd
import pandas as pd

polygons = gpd.read_file(
    "data/philippines.shp.zip!gis_osm_buildings_a_free_1.shp", engine="pyogrio"
)
polygons.to_file("data/polygons.gpkg", driver="GPKG", engine="pyogrio")
