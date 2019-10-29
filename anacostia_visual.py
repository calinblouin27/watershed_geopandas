# Import libraries
import geopandas as gpd
import matplotlib.pyplot as plt


# Import shapefiles
watershed = gpd.read_file('C:/Users/cblou/geopandas/Watersheds.shp')
waterbodies = gpd.read_file('C:/Users/cblou/geopandas/Waterbodies.shp')

#isolate Anacostia watershed from all other watersheds in district
anacostia = watershed[watershed.NAME == 'Washington Metropolitan']
anacostia_outline = anacostia.plot(color = 'white', edgecolor = 'black' )

# intersecting the two shapefiles to remove unwanted parts of waterbody shapefile
anacostia_watershed = gpd.overlay(anacostia,waterbodies, how = 'intersection')
anacostia_watershed.plot(edgecolor = 'black', figsize = (20,20))

#overlay the two shapefiles to show entire watershed and the pieces of the anacostia
fig, ax = plt.subplots(1) 
anacostia.plot(ax=ax, color = 'white', edgecolor = 'black')
anacostia_watershed.plot(ax=ax)
