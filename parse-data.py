# leipzig 1912 csv in geo-json umwandeln
# adaption von https://github.com/gboeing/urban-data-science/blob/3faf7e028d48cb03ddb999c5a910213c5384e7dc/17-Leaflet-Web-Mapping/leaflet-simple-demo/pandas-to-geojson.ipynb

import pandas as pd
import numpy as np
import utm
import json

# einlesen der csv-datei
df = pd.read_csv("Leipzig-1912-komplett-flat.csv", delimiter=";", header=0)

print('We have {} rows'.format(len(df)))

# df_geo als subset aller daten, die gültige geodaten haben
df_geo = df.dropna(subset=['ETRS_UTM33N_X', 'ETRS_UTM33N_Y'], axis=0, inplace=False)

print('We have {} geotagged rows'.format(len(df_geo)))

print(df_geo.tail())
# zählen der einzelnen gewerbetypen
# print(df_geo['Gewerbetyp'].value_counts())

# UTM in WGS84 umrechnen und in neue spalten schreiben

df_geo[['lat', 'lon']] = df_geo.apply(lambda row: pd.Series(utm.to_latlon(row['ETRS_UTM33N_X'], row['ETRS_UTM33N_Y'], 33, 'N')), axis=1)


def df_to_geojson(df, properties, lat='lat', lon='lon'):
    """
    Turn a dataframe containing point data into a geojson formatted python dictionary

    df : the dataframe to convert to geojson
    properties : a list of columns in the dataframe to turn into geojson feature properties
    lat : the name of the column in the dataframe that contains latitude data
    lon : the name of the column in the dataframe that contains longitude data
    """

    # create a new python dict to contain our geojson data, using geojson format
    geojson = {'type': 'FeatureCollection', 'features': []}

    # loop through each row in the dataframe and convert each row to geojson format
    for _, row in df.iterrows():
        # create a feature template to fill in
        feature = {'type': 'Feature',
                   'properties': {},
                   'geometry': {'type': 'Point',
                                'coordinates': []}}

        # fill in the coordinates
        feature['geometry']['coordinates'] = [row[lon], row[lat]]

        # for each column, get the value and add it as a new feature property
        for prop in properties:
            feature['properties'][prop] = row[prop]

        # add this feature (aka, converted dataframe row) to the list of features inside our dict
        geojson['features'].append(feature)

    return geojson


useful_columns = ['Firma', 'Gewerbetyp']
geojson_dict = df_to_geojson(df_geo, properties=useful_columns)
geojson_str = json.dumps(geojson_dict, indent=2)

# save the geojson result to a file
output_filename = 'dataset.js'
with open(output_filename, 'w') as output_file:
    output_file.write('var dataset = {};'.format(geojson_str))

# how many features did we save to the geojson file?
print('{} geotagged features saved to file'.format(len(geojson_dict['features'])))
