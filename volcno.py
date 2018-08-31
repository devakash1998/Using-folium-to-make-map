#code to make map using the folium library
import folium
import pandas
#creating a dataframe
data=pandas.read_csv("volcanoes.txt")

#creating a list for the longitude

long=list(data['LON'])

 #creating a list for the latitiude

lat=list(data['LAT'])

 #creating a list depicting the fname

name=list(data['NAME'])

#use the map function to generate map
#prove the location in form of a list to location
#location isof the form longitude,latitude


map=folium.Map(location=[38.58,-99.09],zoom_start=6,tiles='Mapbox Bright')

#making a feature group for Map

fg=folium.FeatureGroup(name="my map")
for l,lt,nm in zip(lat,long,name):
    fg.add_child(folium.CircleMarker(location=([l,lt]),popup=nm,radius=6,fill_color='red',fill_opacity=0.7))



map.add_child(fg)

#to add a layer contol Featur

map.add_child(folium.LayerControl())

map.save("usvolcano.html")
