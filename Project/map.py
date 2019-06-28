# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 09:04:08 2019

@author: GRV
"""

# import libraries
import folium
import pandas as pd
from Olympic_data import winter,summer
#from PIL import Image
##
#img=Image.open("newplot.png")
## Make a data frame with dots to show on the map
#data = pd.DataFrame({
#'lat':[-58, 2, 145, 30.32, -4.03, -73.57, 36.82, -38.5],
#'lon':[-34, 49, -38, 59.93, 5.33, 45.52, -1.29, -12.97],
#'name':['Buenos Aires', 'Paris', 'melbourne', 'St Petersbourg', 'Abidjan', 'Montreal', 'Nairobi', 'Salvador']
#})
#data
#
## Make an empty map
#m = folium.Map(location=[20, 0], tiles="Mapbox Bright", zoom_start=2)
#
## I can add marker one by one on the map
#for i in range(0,len(data)):
#    folium.Marker([data.iloc[i]['lon'], data.iloc[i]['lat']], popup=data.iloc[i]['name']).add_to(m)
#
## Save it as html
#m.save('312_markers_on_folium_map1.html')
#
#
## Libraries
#import pandas as pd
#from mpl_toolkits.basemap import Basemap
#import matplotlib.pyplot as plt
# 
## Set the dimension of the figure
#my_dpi=96
#plt.figure(figsize=(2600/my_dpi, 1800/my_dpi), dpi=my_dpi)
# 
## read the data (on the web)
#data = pd.read_csv('http://python-graph-gallery.com/wp-content/uploads/TweetSurfData.csv', sep=";")
# 
## Make the background map
#m=Basemap(llcrnrlon=-180, llcrnrlat=-65,urcrnrlon=180,urcrnrlat=80)
#m.drawmapboundary(fill_color='#A6CAE0', linewidth=0)
#m.fillcontinents(color='grey', alpha=0.3)
#m.drawcoastlines(linewidth=0.1, color="white")
# 
## prepare a color for each point depending on the continent.
#data['labels_enc'] = pd.factorize(data['homecontinent'])[0]
# 
## Add a point per position
#m.scatter(data['homelon'], data['homelat'], s=data['n']/6, alpha=0.4, c=data['labels_enc'], cmap="Set1")
# 
## copyright and source data info
#plt.text( -170, -58,'Where people talk about #Surf\n\nData collected on twitter by @R_Graph_Gallery during 300 days\nPlot realized with Python and the Basemap library', ha='left', va='bottom', size=9, color='#555555' )
# 
## Save as png
#plt.savefig('#315_Tweet_Surf_Bubble_map1.png', bbox_inches='tight')
#            
#            
            
            
            
m = folium.Map(
    location=[45.372, -11.6972],
    zoom_start=2,
    tiles='Stamen Terrain'
)
a = olym[["latitude","longitude"]].values.tolist()
b = olym["City"].values.T.tolist()
for i in range(0,len(a)):
    print(i)
    folium.Marker(
            location=a[i],
            popup=b[i],
            icon=folium.Icon(icon='cloud')
    ).add_to(m)

m.save('markers_on_folium_map1.html')           

#
#z = "No.of Olympic\ngaurav"
#m = folium.Map(
#    location=[46.3014, -123.7390],
#    zoom_start=7,
#    tiles='Stamen Terrain'
#)
#folium.Marker(
#    location=[47.3489, -124.708],
#    popup=folium.Popup(max_width=450).add_child(
#        folium.Vega(img, width=450, height=250))
#).add_to(m)
#
#folium.Marker(
#    location=[44.639, -124.5339],
#    popup=folium.Popup(max_width=450).add_child(
#        folium.Vega(img, width=450, height=250))
#).add_to(m)
#
#folium.Marker(
#    location=[46.216, -124.1280],
#    popup=folium.Popup(max_width=450).add_child(
#        folium.Vega(img, width=450, height=250))
#).add_to(m)


#
#summer_city = summer[summer["City"]=="Paris"].groupby("Year")["Event"].count()
#winter_city = winter[winter["City"]=="Paris"].groupby("Year")["Event"].count()
#data = [go.Bar(
#                x = summer_city.index,
#                y = summer_city.values,
#                name = "Athlete",
#                marker = dict(color = 'rgba(255, 0, 255, 1)',
#                              line=dict(color='rgb(0,0,0)',width=1.5)),
#                text = "Athlete",
##                grid =  {"column": 0}
#                ),
#                go.Bar(
#                x = winter_city.index,
#                y = winter_city.values,
#                name = "Athlete",
#                marker = dict(color = 'rgba(255, 0, 255, 1)',
#                              line=dict(color='rgb(0,0,0)',width=1.5)),
#                text = "Athlete",
##                grid =  {"column": 1}
#                )]
#
#layout = go.Layout(title = 'In Summer Athlete Participation Over Years',
#                   xaxis=dict(
#                           title='Year',
#                           titlefont=dict(
#                                       size=16,
#                                       color='rgb(107, 107, 107)'
#                                      ),
#                           tickfont=dict(
#                                      size=14,
#                                      color='rgb(107, 107, 107)'
#                                      )
#                           ),
#                   yaxis=dict(
#                           title='Number Of Athlete',
#                           titlefont=dict(
#                                       size=16,
#                                       color='rgb(107, 107, 107)'
#                                      ),
#                           tickfont=dict(
#                                       size=14,
#                                       color='rgb(107, 107, 107)'
#                                       )
#                           ),
#                    margin = dict(
#                                l=150,
#                                r=100,
#                                t=100,
#                                b=150
#                                ),
#                    showlegend = True
#                    )
#fig = go.Figure(data = data, layout = layout)
#plot(fig)
#
#






#
#
#
#
#
#folium.Marker(
#    location=[45.3288, -121.6625],
#    popup='Mt. Hood Meadows',
#    icon=folium.Icon(icon='cloud')
#).add_to(m)
#
#folium.Marker(
#    location=[45.3311, -121.7113],
#    popup='Timberline Lodge',
#    icon=folium.Icon(color='green')
#).add_to(m)
#
#folium.Marker(
#    location=[45.3300, -121.6823],
#    popup='Some Other Location',
#    icon=folium.Icon(color='red', icon='info-sign')
#).add_to(m)
#
#
#plot(a)            
#            
#            
#
#
#olym[["latitude","longitude"]].values.tolist()
#a=[list(l) for l in zip(*olym[["latitude","longitude"]].values)]        
#            
#            
#            
            
