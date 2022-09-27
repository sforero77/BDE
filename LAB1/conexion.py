import json
import psycopg2
import geojson

conn = psycopg2.connect(host="localhost", database="LAB1", user="sebas", password="sebas")
print(conn)

cur = conn.cursor()
print(cur)

with open('/home/sebas/Documentos/Bases Datos Espaciales/LAB1/museum.geojson') as f:
    gj = geojson.load(f)

#for feature in gj['features']:
#    print(feature['geometry'])
#    print(json.dumps(feature['geometry']['type']=='Point'))

for feature in gj['features']:
    if feature['geometry']['type']=='Point':
        #cur.execute("INSERT INTO museum (name, geom_point) VALUES (%s, ST_GeomFromGeoJSON(%s))", (feature['properties']['name'], json.dumps(feature['geometry'])))
        print("INSERT INTO museum (name, geom) VALUES (%s, ST_GeomFromGeoJSON(%s))", (feature['properties']['name'], json.dumps(feature['geometry'])))
    elif feature['geometry']['type']=='Polygon':
        print("INSERT INTO museum (name, geom) VALUES (%s, ST_GeomFromGeoJSON(%s))", (feature['properties']['name'], json.dumps(feature['geometry'])))
        #cur.execute("INSERT INTO museum (name, geom) VALUES (%s, ST_GeomFromGeoJSON(%s))", (feature['properties']['name'], json.dumps(feature['geometry'])))
    else:
        print("hay otro tipo de dato")


#for feature in gj['features']:
#    cur.execute("INSERT INTO museum (name, geom) VALUES (%s, ST_GeomFromGeoJSON(%s))", (feature['properties']['name'], json.dumps(feature['geometry'])))
conn.commit()       
cur.close()
conn.close()


