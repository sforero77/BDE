import json
import psycopg2
import geojson

conn = psycopg2.connect(host="localhost", database="LAB1", user="sebas", password="sebas")
print(conn)

cur = conn.cursor()
print(cur)

with open('export.geojson') as f:
    gj = geojson.load(f)

#for feature in gj['features']:
#    print(feature["properties"]["name"])
    

for feature in gj['features']:
    cur.execute("INSERT INTO museum (name, geom) VALUES (%s, ST_GeomFromGeoJSON(%s))", (feature['properties']['name'], json.dumps(feature['geometry'])))
conn.commit()       

cur.close()
conn.close()


