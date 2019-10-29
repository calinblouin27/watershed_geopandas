# Import libraries
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import descartes
from shapely.geometry import Point, Polygon


# Import shapefiles
watershed = gpd.read_file('shapefiles/Watersheds.shp')
waterbodies = gpd.read_file('shapefiles/Waterbodies.shp')

#import the data from the .csv
df = pd.read_csv('data/turbidity.csv')
crs = {'init':'epsg:4326'}

#Create Points with Lat and long
geometry = [Point(xy) for xy in zip(df["Longitude"], df["Latitude"])]
geo_df = gpd.GeoDataFrame(df, crs=crs, geometry=geometry)

#isolate just anacostia watershed 
anacostia = watershed[watershed.NAME == 'Washington Metropolitan']
anacostia_watershed = gpd.overlay(anacostia,waterbodies, how = 'intersection')


#plot anacostia watershed and turbidity values over one another. (test) 
fig, ax = plt.subplots(figsize=(20,20)) 
anacostia_watershed.plot(ax=ax, alpha = 0.4, color="grey")
geo_df[geo_df['Turbidity']<=10].plot(ax=ax, color="blue")
geo_df[geo_df['Turbidity']>=11].plot(ax=ax, color="red")