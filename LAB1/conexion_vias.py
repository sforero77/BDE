import json
import psycopg2
import geojson

conn = psycopg2.connect(host="localhost", database="LAB1", user="sebas", password="sebas")
print(conn)

cur = conn.cursor()
print(cur)

with open('/home/sebas/Documentos/Bases Datos Espaciales/LAB1/calles.geojson') as f:
    gj = geojson.load(f)

#for feature in gj['features']:
#    print(feature['geometry'])
#    print(json.dumps(feature['geometry']['type']=='Point'))

for feature in gj['features']:
    if feature['geometry']['type']=='LineString':
        #print("({}, ST_GeomFromGeoJSON{},{})".format(feature['properties']['name'], json.dumps(feature['geometry']), feature['properties']['highway']))
        #print("INSERT INTO autopista (name, geometria, feature) VALUES ('{}', ST_GeomFromGeoJSON('{}'),'{}')".format(feature['properties']['name'], json.dumps(feature['geometry']), feature['properties']['highway']))
        cur.execute("INSERT INTO autopista (name, geometria, feature) VALUES ('{}', ST_GeomFromGeoJSON('{}'),'{}')".format(feature['properties']['name'], json.dumps(feature['geometry']), feature['properties']['highway']))
        #print( feature['properties']['name'])
    elif feature['geometry']['type']=='Polygon':
        #print("({}, ST_GeomFromGeoJSON{},{})".format(feature['properties']['name'], json.dumps(feature['geometry']), feature['properties']['highway']))
        #print(feature['properties']['name'])
        #print("INSERT INTO autopista (name, geometria, feature) VALUES ('{}', ST_GeomFromGeoJSON('{}'),'{}')".format(feature['properties']['name'], json.dumps(feature['geometry']), feature['properties']['highway']))
        cur.execute("INSERT INTO autopista (name, geometria_pol, feature) VALUES ('{}', ST_GeomFromGeoJSON('{}'),'{}')".format(feature['properties']['name'], json.dumps(feature['geometry']), feature['properties']['highway']))
        #print( feature['properties']['name'])
    else:
        print("hay otro tipo de dato")


#for feature in gj['features']:
#    cur.execute("INSERT INTO museum (name, geom) VALUES (%s, ST_GeomFromGeoJSON(%s))", (feature['properties']['name'], json.dumps(feature['geometry'])))
conn.commit()       
cur.close()
conn.close()


