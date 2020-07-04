import numpy as np
import pandas as pd

df = pd.read_csv('GMS_input.csv')

lat_raw = np.asarray(df['latitude'])
lon_raw = np.asarray(df['longitude'])
name = np.asarray(df['name'])

latitude = []
longitude = []
for i in range(len(lat_raw)):

    # Latitude #
    sep_gra_lat = lat_raw[i].split('°' or 'º')
    gra_lat = int(sep_gra_lat[0])
    sep_min_lat = sep_gra_lat[1].split('\'')
    min_lat = int(sep_min_lat[0])
    sep_seg_lat = sep_min_lat[1].split('\"')
    mer_lat = sep_seg_lat[-1]
    seg_lat = float(sep_seg_lat[0])
    lat = (gra_lat + min_lat/60 + seg_lat/3600)
    if(mer_lat == "S"):
        lat = lat*(-1)
    latitude.append(lat)
    # Longitude
    sep_gra_lon = lon_raw[i].split('°' or 'º')
    gra_lon = int(sep_gra_lon[0])
    sep_min_lon = sep_gra_lon[1].split('\'')
    min_lon = int(sep_min_lon[0])
    sep_seg_lon = sep_min_lon[1].split('\"')
    mer_lon = sep_seg_lon[1]
    seg_lon = float(sep_seg_lon[0])
    lon = (gra_lon + min_lon/60 + seg_lon/3600)
    if(mer_lon == "W" or mer_lon == "O"):
        lon = lon*(-1)
    longitude.append(lon)

df1 = pd.DataFrame(list(zip(latitude, longitude, name)), columns = ['Latitude (º)', 'Longitude (º)', 'Name'])
df1.to_csv('Coordinates_DecimalDegrees_output.csv', encoding = 'utf-8-sig')