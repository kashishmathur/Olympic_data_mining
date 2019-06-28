# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 22:19:58 2019

@author: GRV
"""
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot
import plotly.io as pio
init_notebook_mode(connected=True)
from Olympic_data import winter,summer,dataset,olym
import folium


def map1():
        
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
    
    m.save("map.html")   

#####################################################################################################
#1. Fetch the participant who won the most medals with their sports and country
def won_most_medal():
    
    winter_participent = winter[winter["Medal"]!="Loss"].groupby(["Name","Sport","region"])["Medal"].count().sort_values().tail(1)
    summer_participent = summer[summer["Medal"]!="Loss"].groupby(["Name","Sport","region"])["Medal"].count().sort_values().tail(1)
    # for winter
    print("Highest Medal Won Athlete In Winter Olympics : ")
    print("Athlete : ",winter_participent.index[0][0])
    print("Sport : ",winter_participent.index[0][1])
    print("Country : ",winter_participent.index[0][2])
    print("Medals : ",winter_participent.values[0])
    #for summer
    print("\nHighest Medal Won Athlete In summer Olympics : ")
    print("Athlete : ",summer_participent.index[0][0])
    print("Sport : ",summer_participent.index[0][1])
    print("Country : ",summer_participent.index[0][2])
    print("Medals : ",summer_participent.values[0])
     
    return (winter_participent.index[0][0],winter_participent.index[0][1])
#####################################################################################################
#2. Visualize Athlete participation count over years.
#for summer
def Athlt_pc_yr():
    
    year_participent_summer = summer.groupby("Year")["Name"].count()
    data = [go.Bar(
                x = year_participent_summer.index,
                y = year_participent_summer.values,
                name = "Athlete",
                marker = dict(color = 'rgba(255, 0, 255, 1)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Athlete")]

    layout = go.Layout(title = 'In Summer Athlete Participation Over Years',
                   xaxis=dict(
                           title='Year',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(107, 107, 107)'
                                      ),
                           tickfont=dict(
                                      size=14,
                                      color='rgb(107, 107, 107)'
                                      )
                           ),
                   yaxis=dict(
                           title='Number Of Athlete',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(107, 107, 107)'
                                      ),
                           tickfont=dict(
                                       size=14,
                                       color='rgb(107, 107, 107)'
                                       )
                           ),
                    margin = dict(
                                l=150,
                                r=100,
                                t=100,
                                b=150
                                ),
                    showlegend = True
                    )
    fig1 = go.Figure(data = data, layout = layout)
    graph1 = plot(fig1 ,filename = "a.html" ,  output_type = "div")

#for winter

    
    year_participent_winter = winter.groupby("Year")["Name"].count()
    data = [go.Bar(
                x = year_participent_winter.index,
                y = year_participent_winter.values,
                name = "Athlete",
                marker = dict(color = 'rgba(255, 0, 255, 1)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Athlete")]

    layout = go.Layout(title = 'In Winter Athlete Participation Over Years',
                   xaxis=dict(
                           title='Year',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(107, 107, 107)'
                                      ),
                           tickfont=dict(
                                      size=14,
                                      color='rgb(107, 107, 107)'
                                      )
                           ),
                   yaxis=dict(
                           title='Number Of Athlete',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(107, 107, 107)'
                                      ),
                           tickfont=dict(
                                       size=14,
                                       color='rgb(107, 107, 107)'
                                       )
                           ),
                    margin = dict(
                                l=150,
                                r=100,
                                t=100,
                                b=150
                                ),
                    showlegend = True
                    )
    fig2 = go.Figure(data = data, layout = layout)
    graph2 = plot(fig2 ,filename = "b.html" , output_type = "div")
    
    return graph1,graph2

#####################################################################################################
#3. Visualize the Athlete Participation by gender over years.
#for summer
def athlt_pc_gn_yr():

    year_m_participent_summer = summer[summer["Sex"]=="M"].groupby("Year")["Sex"].count()
    year_f_participent_summer = summer[summer["Sex"]=="F"].groupby("Year")["Sex"].count()
    
    summ = year_m_participent_summer + year_f_participent_summer
    summ = summ.fillna(0)
    
    scaled_pcount_f = ( year_f_participent_summer - min(summ)) / (max(summ) - min(summ)) + 0.1
    scaled_pcount_m = (year_m_participent_summer - min(summ)) / (max(summ) - min(summ)) + 0.1

    trace0 = go.Scatter(
            x= year_f_participent_summer.index,
            y= year_f_participent_summer,
            mode='markers',
            marker=dict(
                    
                    size=scaled_pcount_f*50,
                    symbol='circle-open',
                    line=dict(
                            width=4
                            ),
                            color='#2c73d2'
                            ),
                            name='Female Athletes',
                            #text='Year: x <br> Total: y',
                            #hoverinfo='text'
                            hovertemplate = 'Year:%{x} <br> Total:%{y}'
                    
    )

    trace1 = go.Scatter(
            x= year_m_participent_summer.index,
            y= year_m_participent_summer,
            mode='markers',
            marker=dict(
                    size=scaled_pcount_m*50,
                    symbol='circle-open',
                    line=dict(
                            width=4
                            ),
                            color='#f9f871'),
                            name='Male Athletes',
                            #text=['Year:%{x}' , '<br> Total:%{y}'],
                            #hoverinfo='text',
                            hovertemplate = 'Year:%{x} <br> Total:%{y}'
    )
                    
    layout1 = go.Layout(
            title='Athlete Participation - Summer Olympics',
            titlefont=dict(
                    size=36,
                    color='#4b8480'
                    ),
                    xaxis=dict(
                            title='Year',
                            color='#4b8480',
                            titlefont=dict(
                                    size=20
                                    ),
                                    showline=True,
                                    linewidth=1,
                                    linecolor='#4b8480',
                                    showgrid=False
                                    ),
                                    yaxis=dict(
                                            title='Number of Participation',
                                            color='#4b8480',
                                            titlefont=dict(
                                                    size=20
                                                    ),
                                                    showline=True,
                                                    linewidth=1,
                                                    linecolor='#4b8480',
                                                    showgrid=False,
                                                    zeroline=False,
                                                    ),
                                                    legend=dict(orientation='h')
    )

    data1 = [trace0, trace1]

    fig1 = go.Figure(data=data1, layout=layout1)
    graph1 = plot(fig1 ,filename = "c.html" , output_type = "div")
    
#winter


    gender_ym_w = winter[winter["Sex"] == "M"].groupby(["Year"])["Sex"].count()
    gender_yf_w = winter[winter["Sex"] == "F"].groupby(["Year"])["Sex"].count()
    
    
    summ = gender_ym_w + gender_yf_w
    summ = summ.fillna(0)
    
    scaled_pcount_f = (gender_yf_w - min(summ)) / (max(summ) - min(summ)) + 0.1
    scaled_pcount_m = (gender_ym_w - min(summ)) / (max(summ) - min(summ)) + 0.1

    trace0 = go.Scatter(
            x=gender_yf_w.index,
            y=gender_yf_w,
            mode='markers',
            marker=dict(
                    
                    size=scaled_pcount_f*50,
                    symbol='circle-open',
                    line=dict(
                            width=4
                            ),
                            color='#2c73d2'
                            ),
                            name='Female Athletes',
                            #text='Year: x <br> Total: y',
                            #hoverinfo='text'
                            hovertemplate = 'Year:%{x} <br> Total:%{y}'
                    
    )

    trace1 = go.Scatter(
            x=gender_ym_w.index,
            y=gender_ym_w,
            mode='markers',
            marker=dict(
                    size=scaled_pcount_m*50,
                    symbol='circle-open',
                    line=dict(
                            width=4
                            ),
                            color='#f9f871'),
                            name='Male Athletes',
                            #text=['Year:%{x}' , '<br> Total:%{y}'],
                            #hoverinfo='text',
                            hovertemplate = 'Year:%{x} <br> Total:%{y}'
    )
                    
    layout1 = go.Layout(
            title='Athlete Participation - Winter Olympics',
            titlefont=dict(
                    size=36,
                    color='#4b8480'
                    ),
                    xaxis=dict(
                            title='Year',
                            color='#4b8480',
                            titlefont=dict(
                                    size=20
                                    ),
                                    showline=True,
                                    linewidth=1,
                                    linecolor='#4b8480',
                                    showgrid=False
                                    ),
                                    yaxis=dict(
                                            title='Number of Participation',
                                            color='#4b8480',
                                            titlefont=dict(
                                                    size=20
                                                    ),
                                                    showline=True,
                                                    linewidth=1,
                                                    linecolor='#4b8480',
                                                    showgrid=False,
                                                    zeroline=False,
                                                    ),
                                                    legend=dict(orientation='h')
    )

    data1 = [trace0, trace1]

    fig2 = go.Figure(data=data1, layout=layout1)
    
    graph2 = plot(fig2 ,filename = "d.html" , output_type = "div")
    return graph1,graph2
    
###############################################################################################
#4. Visualize the Gender Distribution in the games.
#for summer
def gn_ditb_gm():
    
    sport_m_participent_summer = summer[dataset["Sex"]=="M"].groupby("Sport")["Sex"].count()
    sport_f_participent_summer = summer[dataset["Sex"]=="F"].groupby("Sport")["Sex"].count()
    # or
    #sport_m_participent_summer = summer.groupby("Sport")["Sex"].value_counts().unstack()
    data1 = go.Bar(
                y = sport_m_participent_summer.index,
                x = sport_m_participent_summer.values,
                name = "Male",
                marker = dict(color = 'rgba(0, 126, 133, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Male Athlete",
                orientation = "h")
    data2 = go.Bar(
                y = sport_f_participent_summer.index,
                x = sport_f_participent_summer.values,
                name = "Female",
                marker = dict(color = 'rgba(31, 244, 255, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Female Athlete",
                orientation = "h")               

    layout = go.Layout(title = 'In Summer Athlete Participation By Gender Over Games',
                   xaxis=dict(
                           title='Number Of Athlete',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                      size=14,
                                      color='rgb(0,0,0)'
                                      ),
                           tickangle=-45,
                           ),
                   yaxis=dict(
                           title='Game',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                       size=14,
                                       color='rgb(0,0,0)'
                                       )
                           ),
                    margin = dict(
                                l=150,
                                r=100,
                                t=100,
                                b=150
                                ),
                   legend=dict(
#                           x=0,
#                           y=1.0,
                           bgcolor='rgba(255, 255, 255, 0)',
                           bordercolor='rgba(255, 255, 255, 0)'
                           ),  
                   barmode='group',
                   bargap=0.15,
                   bargroupgap=0.1,
                   height = 800
                   )
    data = [data1,data2]                       
    fig1 = go.Figure(data = data, layout = layout)
    

#for winter

    
    sport_m_participent_winter = winter[dataset["Sex"]=="M"].groupby("Sport")["Sex"].count()
    sport_f_participent_winter = winter[dataset["Sex"]=="F"].groupby("Sport")["Sex"].count()
    data1 = go.Bar(
                y = sport_m_participent_winter.index,
                x = sport_m_participent_winter.values,
                name = "Male",
                marker = dict(color = 'rgba(0, 126, 133, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Male Athlete",
                orientation = "h")
    data2 = go.Bar(
                y = sport_f_participent_winter.index,
                x = sport_f_participent_winter.values,
                name = "Female",
                marker = dict(color = 'rgba(31, 244, 255, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Female Athlete",
                orientation = "h")               

    layout = go.Layout(title = 'In Winter Athlete Participation By Gender Over Games',
                   xaxis=dict(
                           title='Number Of Athlete',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                      size=10,
                                      color='rgb(0,0,0)'
                                      ),
                           tickangle=-45,
                           ),
                   yaxis=dict(
                           title='Game',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                       size=10,
                                       color='rgb(0,0,0)'
                                       )
                           ),
                    margin = dict(
                                l=150,
                                r=100,
                                t=100,
                                b=150
                                ),
                   legend=dict(
#                           x=0,
#                           y=1.0,
                           bgcolor='rgba(255, 255, 255, 0)',
                           bordercolor='rgba(255, 255, 255, 0)'
                           ),  
                   barmode='group',
                   bargap=0.15,
                   bargroupgap=0.1       
                   )
    data = [data1,data2]                       
    fig2 = go.Figure(data = data, layout = layout)
    graph1 = plot(fig1,filename = "e.html",output_type = "div")
    graph2 = plot(fig2,filename = "f.html",output_type = "div")
    
    return graph1,graph2
############################################################################################
#5. Visualize the number of countries participated in the games.
#for winter
def cntry_pc_gm():
    
    country_participent_winter = winter.groupby("Sport")["region"].unique()
    count_country_winter = [len(x) for x in country_participent_winter]
    country_name_winter = [list(x) for x in country_participent_winter]
    data = [go.Bar(
                x = country_participent_winter.index,
                y = count_country_winter,
                name = "Male",
                marker = dict(color = 'rgba(0, 126, 133, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = country_name_winter,
                textposition = 'auto') ]           

    layout = go.Layout(title = 'Country participation in games over years in Winter',
                   xaxis=dict(
                           title='Numbers Of Country',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                      size=10,
                                      color='rgb(0,0,0)'
                                      ),
                           tickangle=-45,
                           ),
                   yaxis=dict(
                           title='Sport',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                       size=10,
                                       color='rgb(0,0,0)'
                                       )
                           ) ,
                    margin = dict(
                                l=150,
                                r=100,
                                t=100,
                                b=150
                                )
                   )                       
    fig2 = go.Figure(data = data, layout = layout)
    
    
#for summer

    
    country_participent_summer = summer.groupby("Sport")["region"].unique()
    count_country_summer = [len(x) for x in country_participent_summer]
    country_name_summer = [list(x) for x in country_participent_summer]
    data = [go.Bar(
                x = country_participent_summer.index,
                y = count_country_summer,
                name = "Country",
                marker = dict(color = 'rgba(0, 126, 133, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = country_name_summer) ]           

    layout = go.Layout(title = 'Country participation in games over years in Summer',
                   xaxis=dict(
                           title='Numbers Of Country',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                      size=10,
                                      color='rgb(0,0,0)'
                                      ),
                           tickangle=-45,
                           ),
                   yaxis=dict(
                           title='Sport',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                       size=10,
                                       color='rgb(0,0,0)'
                                       )
                           ),
                    margin = dict(
                                l=150,
                                r=100,
                                t=100,
                                b=150
                                ),
                    showlegend = True
                   )       
    updatemenus=list([
            dict(
                    buttons=list([   
                            dict(
                                    args=['type', 'bar'],
                                    label='3D Surface',
                                    method='restyle'
                                    ),
                                    dict(
                                            args=['type', 'bar'],
                                            label='Heatmap',
                                            method='restyle'
                                            )             
                                    ]),
                                    direction = 'up',
                                    pad = {'r': 10, 't': 10},
                                    showactive = True,
                                    x = 0.1,
                                    xanchor = 'left',
                                    y = 1.1,
                                    yanchor = 'top' 
                             ),
                    ])
    annotations = list([
            dict(text='Trace type:', x=0, y=1.085, yref='paper', align='left', showarrow=False)
    ])
    layout['updatemenus'] = updatemenus
    layout['annotations'] = annotations
    fig1 = go.Figure(data = data, layout = layout)
    graph1 = plot(fig1,filename = "g.html",output_type = "div")
    graph2 = plot(fig2,filename = "h.html",output_type = "div")
    
    return graph1,graph2

###########################################################################################
#6.Visualize the highest number of participation nation wise.
def hst_pc_nt():
    
    nation_s = summer.groupby("Year")["region"].value_counts().unstack()
    high_year_s = nation_s.max(axis = 1)
    high_value_s = nation_s.idxmax(axis = 1)
    
    nation_w = winter.groupby("Year")["region"].value_counts().unstack()
    high_year_w = nation_w.max(axis = 1)
    high_value_w = nation_w.idxmax(axis = 1)
    
    fig = {
            "data" : [
                    
                    {
                            
                            "labels": high_value_s,
                            "values": high_year_s,
                            "domain": {"column": 0},
                            #"text":["Summer"],
                            "hoverinfo":"label+percent",
                            "hole": .4,
                            "type": "pie"
                            
                            
                            },
                    {
                            
                            "labels": high_value_w,
                            "values": high_year_w,
                            #"text":["Winter"],
                            #"textposition":"inside",
                            "domain": {"column": 1},
                            "hoverinfo":"label+percent",
                            "hole": .4,
                            "type": "pie",
                            
                            }],
            "layout" : {
                    
                    "title":"Paticipation of countries",
                    "grid": {"rows": 1, "columns": 2},
                    "annotations": [
                            
                            {
                                    
                                    "font": {
                                            "size": 20
                                            },
                                            "showarrow": False,
                                            "text": "Summer",
                                            "x": 0.20,
                                            "y": 0.5
                                            },
                                            {
                                                    "font": {
                                                            "size": 20
                                                            },
                                                            "showarrow": False,
                                                            "text": "Winter",
                                                            "x": 0.8,
                                                            "y": 0.5
                                                            }
                                                    ]
                    }
            }
    
    
    graph1 = plot(fig, filename="i.html" , output_type = "div")
    return graph1

###########################################################################################
#7. Visualize the countries that Hosted the games for the highest number of times.
#for summer
def hst_host_cnty():

    freq = summer.Country.value_counts().reset_index().rename(columns={'index': 'x'})

    data1 = go.Bar(y=freq['x'][0:20],
                   x=freq['Country'][0:20], 
                   marker=dict(color='#CF1020'),
                   orientation = "h",
                   name = "Country"
                   )
    data2 = {
            "geo": "geo3",
            "lon": summer['longitude'],
            "lat": summer['latitude'],

      "text":freq["x"],
      "name" : "Country ",
      "locations" : freq['x'],
      "hoverinfo" : "lon+lat+location",
      "connectgaps" :True,
   
      "locationmode":'country names', 
              
      "marker": {
              "symbol":0,
              "size": 4,
              "sizeref":50,
              "opacity": 0.8,
              "color": '#CF1020',
              "colorscale": 'Earth',
              "sizemode" : "area",
    
                },
   
        "mode": "markers",
        "type": "scattergeo"
  
    }

    data = [data1,data2]
    
    
    layout = {
            "plot_bgcolor": 'black',
            "paper_bgcolor": 'black',
            "titlefont": {
                    "size": 20,
                    "family": "Raleway"
                    },
                    "font": {
                            "color": 'white'
                            },
                            "dragmode": "zoom",
                            "geo3": {
                                    "domain": {
                                            "x": [0, 0.55],
                                            "y": [0, 1]
                                            },
                                    "lakecolor": "rgba(127,205,255,1)",
                                    "oceancolor": "rgb(6,66,115)",
                                    "landcolor": "rgb(250, 250, 250)",
                                    "projection": {"type": "equirectangular"
                                                   
                                            },
                                                   "lonaxis" : dict(
                                                           showgrid = True,
                                                           gridcolor = 'rgb(102, 102, 102)',
                                                           gridwidth = 0.5
                                                           ),
                                                           "lataxis" : dict(
                                                                   showgrid = True,
                                                                   gridcolor = 'rgb(102, 102, 102)',
                                                                   gridwidth = 0.5
                                                                   ),
                                                                   
                                                                   "scope": "world",
                                                                   "showcoastlines":True,
                                                                   "coastlinecolor":"#444",
                                                                   "showcountries" : True,
                                                                    "countrycolor" : "rgb(217, 217, 217)",
                                                                    "showlakes": True,
                                                                    "showocean": True,
                                                                    "showland": True,
                                                                    "bgcolor": 'black'
                                                                    },
          
            "margin": {
                    "r": 10,
                    "t": 10,
                    "b": 10,
                    "l": 20
                    },
                    
            "showlegend": True,
            "title": "<br>Olympic Game Hosting Country",
                    "xaxis": {
                            "anchor": "y",
                            "domain": [0.65, 1]
                            },    
                    "yaxis": {
                            "anchor": "x",
                            "domain": [0.1, 0.85],
                            "showgrid": True
                            }
                    }
                    
    annotations = { "text": "Source: Olympic",
                                   "showarrow": False,
                                   "xref": "paper",
                                   "yref": "paper",
                                   "x": 1,
                                   "y": 0}

    layout['annotations'] = [annotations]


    fig1 = go.Figure(data=data, layout=layout)
    

#for winter
    
    freq = winter.Country.value_counts().reset_index().rename(columns={'index': 'x'})

    data1 = go.Bar(y=freq['x'][0:20],
                   x=freq['Country'][0:20], 
                   marker=dict(color='#CF1020'),
                   orientation = "h",
                   name = "Country"
                   )
    data2 = {
            "geo": "geo3",
#            "lon": winter['longitude'],
#            "lat": winter['latitude'],

      "text":freq["x"],
      "name" : "Country ",
      "locations" : freq['x'],
      "hoverinfo" : "lon+lat+location",
      "connectgaps" :True,
   
      "locationmode":'country names', 
              
      "marker": {
              "symbol":0,
              "size": 4,
              "sizeref":50,
              "opacity": 0.8,
              "color": '#CF1020',
              "colorscale": 'Earth',
              "sizemode" : "area",
    
                },
   
        "mode": "markers",
        "type": "scattergeo"
  
    }

    data = [data1,data2]
    
    
    layout = {
            "plot_bgcolor": 'black',
            "paper_bgcolor": 'black',
            "titlefont": {
                    "size": 20,
                    "family": "Raleway"
                    },
                    "font": {
                            "color": 'white'
                            },
                            "dragmode": "zoom",
                            "geo3": {
                                    "domain": {
                                            "x": [0, 0.55],
                                            "y": [0, 1]
                                            },
                                    "lakecolor": "rgba(127,205,255,1)",
                                    "oceancolor": "rgb(6,66,115)",
                                    "landcolor": "rgb(250, 250, 250)",
                                    "projection": {"type": "equirectangular"
                                                   
                                            },
                                                   "lonaxis" : dict(
                                                           showgrid = True,
                                                           gridcolor = 'rgb(102, 102, 102)',
                                                           gridwidth = 0.5
                                                           ),
                                                           "lataxis" : dict(
                                                                   showgrid = True,
                                                                   gridcolor = 'rgb(102, 102, 102)',
                                                                   gridwidth = 0.5
                                                                   ),
                                                                   
                                                                   "scope": "world",
                                                                   "showcoastlines":True,
                                                                   "coastlinecolor":"#444",
                                                                   "showcountries" : True,
                                                                    "countrycolor" : "rgb(217, 217, 217)",
                                                                    "showlakes": True,
                                                                    "showocean": True,
                                                                    "showland": True,
                                                                    "bgcolor": 'black'
                                                                    },
          
            "margin": {
                    "r": 10,
                    "t": 10,
                    "b": 10,
                    "l": 20
                    },
                    
            "showlegend": True,
            "title": "<br>Olympic Game Hosting Country",
                    "xaxis": {
                            "anchor": "y",
                            "domain": [0.65, 1]
                            },    
                    "yaxis": {
                            "anchor": "x",
                            "domain": [0.1, 0.85],
                            "showgrid": True
                            }
                    }
                    
    annotations = { "text": "Source: Olympic",
                                   "showarrow": False,
                                   "xref": "paper",
                                   "yref": "paper",
                                   "x": 1,
                                   "y": 0}

    layout['annotations'] = [annotations]


    fig2 = go.Figure(data=data, layout=layout)
    graph1 = plot(fig1,filename = "j.html",output_type = "div")
    graph2 = plot(fig2,filename = "k.html",output_type = "div")
    
    return graph1,graph2
###########################################################################################
#8. Visualize the cities that hosted the games for the highest number of times.
def hst_host_city():
    
    host_city_s = olym[olym["Season"] == "Summer"]["City"].value_counts()
    host_city_w = olym[olym["Season"] == "Winter"]["City"].value_counts()
    
    
    fig = {
            "data" : [
                    
                    {
                            
                            "labels": host_city_s.index,
                            "values": host_city_s,
                            "domain": {"column": 0},
                            #"text":["Summer"],
                            "hoverinfo":"label+percent",
                            "hole": .4,
                            "type": "pie"
                            
                            
                            },
                    {
                            
                            "labels": host_city_w.index,
                            "values": host_city_w,
                            #"text":["Winter"],
                            #"textposition":"inside",
                            "domain": {"column": 1},
                            "hoverinfo":"label+percent",
                            "hole": .4,
                            "type": "pie",
                            
                            }],
            "layout" : {
                    
                    "title":"Global Emissions 1896-2016",
                    "grid": {"rows": 1, "columns": 2},
                    "annotations": [
                            
                            {
                                    
                                    "font": {
                                            "size": 20
                                            },
                                            "showarrow": False,
                                            "text": "Summer",
                                            "x": 0.20,
                                            "y": 0.5
                                            },
                                            {
                                                    "font": {
                                                            "size": 20
                                                            },
                                                            "showarrow": False,
                                                            "text": "Winter",
                                                            "x": 0.8,
                                                            "y": 0.5
                                                            }
                                                    ]
                    }
            }
    
    graph1 = plot(fig, filename="m.html",output_type = "div")
    return graph1

###########################################################################################
#9. Visualize the average age, height and weight of the athletes for various 
#   sports categories. (3 separate representation)
#for summer
def avg_AHV():
    
    average_age = summer.groupby("Sport")["Age"].mean() 
    height = summer.groupby("Sport")["Height"].mean()
    weight = summer.groupby("Sport")["Weight"].mean()
    data = [go.Bar(
                x = average_age.index,
                y = average_age.values,
                name = "Age",
                marker = dict(color = 'rgba(218, 70, 47, 1)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                ) ,
         go.Bar(
                x = height.index,
                y = height.values,
                name = "Height",
                marker = dict(color = 'rgba(218, 178, 47, 1)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                ),
         go.Bar(
                x = weight.index,
                y = weight.values,
                name = "Weight",
                marker = dict(color = 'rgba(107, 218, 47, 1)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                )
        ]  


    layout = go.Layout(title = 'In Summer average age, height and weight of the athletes for various sports categories',
                   xaxis=dict(
                           title='Sport',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                      size=10,
                                      color='rgb(0,0,0)'
                                      ),
                           tickangle=-45,
                           ),
                   yaxis=dict(
                           title='Aerage Age , Height ,Weight',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                       size=10,
                                       color='rgb(0,0,0)'
                                       )
                           ),
                    margin = dict(
                                l=150,
                                r=100,
                                t=100,
                                b=150
                                ),
                    showlegend = True
                   )       

    fig1 = go.Figure(data = data, layout = layout)
    
    
#for winter

    
    average_age = winter.groupby("Sport")["Age"].mean() 
    height = winter.groupby("Sport")["Height"].mean()
    weight = winter.groupby("Sport")["Weight"].mean()
    data = [go.Bar(
                x = average_age.index,
                y = average_age.values,
                name = "Age",
                marker = dict(color = 'rgba(218, 70, 47, 1)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                ) ,
         go.Bar(
                x = height.index,
                y = height.values,
                name = "Height",
                marker = dict(color = 'rgba(218, 178, 47, 1)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                ),
         go.Bar(
                x = weight.index,
                y = weight.values,
                name = "Weight",
                marker = dict(color = 'rgba(107, 218, 47, 1)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                )
        ]  


    layout = go.Layout(title = 'In Winter average age, height and weight of the athletes for various sports categories',
                   xaxis=dict(
                           title='Sport',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                      size=10,
                                      color='rgb(0,0,0)'
                                      ),
                           tickangle=-45,
                           ),
                   yaxis=dict(
                           title='Aerage Age , Height ,Weight',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                       size=10,
                                       color='rgb(0,0,0)'
                                       )
                           ),
                    margin = dict(
                                l=150,
                                r=100,
                                t=100,
                                b=150
                                ),
                    showlegend = True
                   )       

    fig2 = go.Figure(data = data, layout = layout)
    
    graph1 = plot(fig1,filename = "n.html",output_type = "div")
    graph2 = plot(fig2,filename = "o.html",output_type = "div")
    
    return graph1,graph2
    

###########################################################################################
#10. Visualize the total unique sports activities over years in Olympics.
#for summer
def uniq_spt_yr():
    
    unique_sport = summer.groupby("Year")["Sport"].unique()
    count_unique_sport = [len(x) for x in unique_sport]
    sport_unique_sport = [list(x) for x in unique_sport]
    data = [go.Bar(
                x = unique_sport.index,
                y = count_unique_sport,
                name = "Unique Sport",
                marker = dict(color = 'rgba(0, 126, 133, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = sport_unique_sport,
                textposition = 'auto') ]           

    layout = go.Layout(title = 'In summer total unique sports activities over years in Olympics',
                   xaxis=dict(
                           title='Year',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                      size=10,
                                      color='rgb(0,0,0)'
                                      ),
                           tickangle=-45,
                           ),
                   yaxis=dict(
                           title='Unique Sport',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                       size=10,
                                       color='rgb(0,0,0)'
                                       )
                           ) ,
                    margin = dict(
                                l=150,
                                r=100,
                                t=100,
                                b=150
                                )
                   )                       
    fig1 = go.Figure(data = data, layout = layout)
    
#for winter


    unique_sport = winter.groupby("Year")["Sport"].unique()
    count_unique_sport = [len(x) for x in unique_sport]
    sport_unique_sport = [list(x) for x in unique_sport]
    data = [go.Bar(
                x = unique_sport.index,
                y = count_unique_sport,
                name = "Unique Sport",
                marker = dict(color = 'rgba(0, 126, 133, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = sport_unique_sport,
                textposition = 'auto') ]           

    layout = go.Layout(title = 'In winter total unique sports activities over years in Olympics',
                   xaxis=dict(
                           title='Year',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                      size=10,
                                      color='rgb(0,0,0)'
                                      ),
                           tickangle=-45,
                           ),
                   yaxis=dict(
                           title='Unique Sport',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                       size=10,
                                       color='rgb(0,0,0)'
                                       )
                           ) ,
                    margin = dict(
                                l=150,
                                r=100,
                                t=100,
                                b=150
                                )
                   )                       

    fig2 = go.Figure(data = data, layout = layout)
    
    graph1 = plot(fig1,filename = "n.html",output_type = "div")
    graph2 = plot(fig2,filename = "o.html",output_type = "div")
    
    return graph1,graph2

###########################################################################################
    
#11. Visualize the event ratio by gender.
#for summer
def event_rto_gn():
    
    event_ratio = summer.groupby("Event")["Sex"].value_counts().unstack()
    data = [go.Bar(
                x = event_ratio.index,
                y = event_ratio["M"],
                name = "Male",
                marker = dict(color = 'rgba(0, 126, 133, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Male",
                textposition = 'auto'),
         go.Bar(
                x = event_ratio.index,
                y = event_ratio["F"],
                name = "Female",
                marker = dict(color = 'rgba(107, 218, 47, 1)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Female",
                textposition = 'auto')       ]           

    layout = go.Layout(title = 'In summer event ratio by gender',
                   xaxis=dict(
                           title='Event',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                      size=10,
                                      color='rgb(0,0,0)'
                                      ),
                           tickangle=-45,
                           ),
                   yaxis=dict(
                           title='Athlete',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                       size=10,
                                       color='rgb(0,0,0)'
                                       )
                           ) ,
                    margin = dict(
                                l=150,
                                r=100,
                                t=100,
                                b=150
                                ),
                    barmode='stack'
                   )                       
    fig1 = go.Figure(data = data, layout = layout)
    

#for winter

    
    event_ratio = winter.groupby("Event")["Sex"].value_counts(normalize = True).unstack()
    data = [go.Bar(
                x = event_ratio.index,
                y = event_ratio["M"],
                name = "Male",
                marker = dict(color = 'rgba(0, 126, 133, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Male",
                textposition = 'auto'),
         go.Bar(
                x = event_ratio.index,
                y = event_ratio["F"],
                name = "Female",
                marker = dict(color = 'rgba(107, 218, 47, 1)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Female",
                textposition = 'auto')       ]           

    layout = go.Layout(title = 'In winter event ratio by gender',
                   xaxis=dict(
                           title='Event',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                      size=10,
                                      color='rgb(0,0,0)'
                                      ),
                           tickangle=-45,
                           ),
                   yaxis=dict(
                           title='Athlete',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                       size=10,
                                       color='rgb(0,0,0)'
                                       )
                           ) ,
                    margin = dict(
                                l=150,
                                r=100,
                                t=100,
                                b=150
                                ),
                    barmode='group'
                   )                       

    fig2 = go.Figure(data = data, layout = layout)
    
    graph1 = plot(fig1,filename = "n.html",output_type = "div")
    graph2 = plot(fig2,filename = "o.html",output_type = "div")
    
    return graph1,graph2

###########################################################################################
#12. Visualize the events by genders over years.
#for summer
def event_gn_yr():
    
    year_ratio_m = summer[summer["Sex"]=="M"].groupby("Year")["Event"].value_counts().unstack().sum(axis=1)
    year_ratio_f = summer[summer["Sex"]=="F"].groupby("Year")["Event"].value_counts().unstack().sum(axis=1)

    data = [go.Bar(
                x = year_ratio_m.index,
                y = year_ratio_m.values,
                name = "Male",
                marker = dict(color = 'rgba(0, 126, 133, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Male",
                textposition = 'auto'),
         go.Bar(
                x = year_ratio_f.index,
                y = year_ratio_f.values,
                name = "Female",
                marker = dict(color = 'rgba(107, 218, 47, 1)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Female",
                textposition = 'auto')       ]           

    layout = go.Layout(title = 'In summer event ratio by gender over year',
                   xaxis=dict(
                           title='Year',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                      size=10,
                                      color='rgb(0,0,0)'
                                      ),
                           tickangle=-45,
                           ),
                   yaxis=dict(
                           title='Athlete In Event',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                       size=10,
                                       color='rgb(0,0,0)'
                                       )
                           ) ,
                    margin = dict(
                                l=150,
                                r=100,
                                t=100,
                                b=150
                                )
                    
                   )                       

    fig1 = go.Figure(data = data, layout = layout)
    #plot(fig1)
    
#winter
    year_ratio_m = winter[winter["Sex"]=="M"].groupby("Year")["Event"].value_counts().unstack().sum(axis=1)
    year_ratio_f = winter[winter["Sex"]=="F"].groupby("Year")["Event"].value_counts().unstack().sum(axis=1)
    
    data = [go.Bar(
                x = year_ratio_m.index,
                y = year_ratio_m.values,
                name = "Male",
                marker = dict(color = 'rgba(0, 126, 133, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Male",
                textposition = 'auto'),
         go.Bar(
                x = year_ratio_f.index,
                y = year_ratio_f.values,
                name = "Female",
                marker = dict(color = 'rgba(107, 218, 47, 1)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Female",
                textposition = 'auto')       ]           

    layout = go.Layout(title = 'In Winter event ratio by gender over year',
                   xaxis=dict(
                           title='Year',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                      size=10,
                                      color='rgb(0,0,0)'
                                      ),
                           tickangle=-45,
                           ),
                   yaxis=dict(
                           title='Athlete In Event',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                       size=10,
                                       color='rgb(0,0,0)'
                                       )
                           ) ,
                    margin = dict(
                                l=150,
                                r=100,
                                t=100,
                                b=150
                                )
                    
                   )                       

    fig2 = go.Figure(data = data, layout = layout)
    #plot(fig2)
    graph1 = plot(fig1,filename = "n.html",output_type = "div")
    graph2 = plot(fig2,filename = "o.html",output_type = "div")
    
    return graph1,graph2
    
"""
###########################################################################################
#13. Fetch the discontinued sports in olympics 2016.
#for summer
def dis_spt_yr2016():
    total_sport_summer = set(summer[summer["Year"]!=2016]["Sport"].unique())
    total_sport_2016_summer = set(summer[summer["Year"]==2016]["Sport"].unique())
    discontinued_summer_sport_2016 = list(total_sport_summer - total_sport_2016_summer)
    html1 = '<input value="{discontinued_summer_sport_2016}" name="d1" type="text" />'
    return html1.format(location = location)
    #print("Discontinued Sport  In Summer 2016 ",discontinued_summer_sport_2016)
    
#for winter

    total_sport_winter = set(winter[winter["Year"]!=2016]["Sport"].unique())
    total_sport_2016_winter = set(winter[winter["Year"]==2016]["Sport"].unique())
    discontinued_winter_sport_2016 = list(total_sport_winter - total_sport_2016_winter)
    html2 = '<input value="{discontinued_winter_sport_2016}" name="d2" type="text" />'
    #print("Discontinued Sport  In Winter 2016 ",discontinued_winter_sport_2016)
    
    #return html1,html2
    
"""
###########################################################################################
#14. Revenue Categories - 
#Category ---------->   Sports
#A                      Acquatics, Athletes, Gymnastics
#B                      Cycling, Tennis
#C                      Archery, Badminton, Boxing, Judo, Rowing, Shooting, Table Tennis, Weightlifting
#D                      Canoeing, Equestrianism, Sailing, Fencing, Taekwondo, Triathlon, Wrestling
#E                      Modern Pentathlon, Golf
#Visualize the sports ratio in each revenue category
#for summer
def smr_revenue_cat():
    
    revenue_sport_ratio = summer.groupby("Category")["Sport"].value_counts(normalize = True).unstack(level=0)
    revenue_sport_ratio1 = summer.groupby("Category")["Sport"].value_counts()
    summer_ratio_c =list(zip(*list(revenue_sport_ratio.index)))
    data = [go.Bar(
                x = list(revenue_sport_ratio.index),
                y = revenue_sport_ratio["A"],
                name = "A",
                marker = dict(color = 'rgba(218, 70, 47, 1)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "A",
                textposition = "auto"),
                
         go.Bar(x = list(revenue_sport_ratio.index),
                y = revenue_sport_ratio["B"],
                name = "B",
                marker = dict(color = 'rgba(169, 139, 20, 1)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "B",
                textposition = "auto"),
         go.Bar(x = list(revenue_sport_ratio.index),
                y = revenue_sport_ratio["C"],
                name = "C",
                marker = dict(color = 'rgba(25, 169, 20, 1)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "C",
                textposition = "auto"),
         go.Bar(x = list(revenue_sport_ratio.index),
                y = revenue_sport_ratio["D"],
                name = "D",
                marker = dict(color = 'rgba(52, 20, 169, 1)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "D",
                textposition = "auto"),
         go.Bar(x = list(revenue_sport_ratio.index),
                y = revenue_sport_ratio["E"],
                name = "E",
                marker = dict(color = 'rgba(169, 20, 20, 1)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "E",
                textposition = "auto")]  


    layout = go.Layout(title = 'In Summer average age, height and weight of the athletes for various sports categories',
                   xaxis=dict(
                           title='Sport',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                      size=10,
                                      color='rgb(0,0,0)'
                                      ),
                           tickangle=-45,
                           ),
                   yaxis=dict(
                           title='Aerage Age , Height ,Weight',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                       size=10,
                                       color='rgb(0,0,0)'
                                       )
                           ),
                    margin = dict(
                                l=150,
                                r=100,
                                t=100,
                                b=150
                                ),
                    showlegend = True
                   )       

    fig = go.Figure(data = data, layout = layout)
    graph1 = plot(fig, filename = "p.html" , output_type = "div")
    return graph1
    
"""
#for winter
def wtr_revn_cat():
    def fun_winter(item):
        if item in ["Acquatics"," Athletes", "Gymnastics"]:
            return "A"
        elif item in ["Cycling", "Tennis"]:
            return "B"
        elif item in ["Archery", "Badminton", "Boxing", "Judo", "Rowing", "Shooting", "Table Tennis", "Weightlifting"]:
            return "C"
        elif item in ["Canoeing", "Equestrianism", "Sailing", "Fencing", "Taekwondo", "Triathlon", "Wrestling"]:
            return "D"
        elif item in ["Modern Pentathlon"," Golf"]:
            return "E"
        else:
            return np.nan
    
    winter["Category"] = winter["Sport"].apply(lambda x: fun_winter(x))
    
    
"""
########################################################################################
#15. Visualize the medals won in each revenue category.
#for summer
def won_mdl_ech_ctg():
    total_medal_summer = summer.groupby("Category")["Medal"].value_counts().unstack()
    total_medal_s = total_medal_summer.sum(axis = 1)
    
    data1 = [go.Pie(

    labels=total_medal_s.index,
    values=total_medal_s,
    hoverinfo='label+percent',
    textinfo='value',
    marker=dict(line=dict(color='#000000', width=2))

    )]

    layout1 = go.Layout(

    title='Total medals won by revenue categories',
    titlefont=dict(
            size=36,
            color='#4b8480'
            ),

    )
    fig = go.Figure(data=data1,layout=layout1)
    graph = plot(fig, filename = "q.html" , output_type = "div")  
    return graph
"""
########################################################################################
#16. Fetch the medal tally for each sports categories
    
#for summer
def smr_mdl_ech_spt_ctg():
    medal_summer = summer.groupby("Sport")["Medal"].value_counts().unstack()
    return medal_summer
#for winter
def wtr_mdl_ech_spt_ctg():
    medal_winter = winter.groupby("Sport")["Medal"].value_counts().unstack()    
    return medal_winter

"""
########################################################################################
#17. Visualize the above results.
#for summer  
def rslt_mdl_ech_spt_ctg():
    
    summer_sport_revenue_medal = summer.groupby("Category")["Medal"].value_counts().unstack()
    data = [go.Bar(
                x = list(summer_sport_revenue_medal.index),
                y = summer_sport_revenue_medal["Gold"],
                name = "Gold",
                marker = dict(color = 'rgba(218, 70, 47, 1)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text =  "Gold"),
                
         go.Bar(
                y = summer_sport_revenue_medal["Silver"],
                x = list(summer_sport_revenue_medal.index),
                name = "Silver",
                marker = dict(color = 'rgba(169, 139, 20, 1)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text =  "Silver"),
         go.Bar(
                y = summer_sport_revenue_medal["Bronze"],
                x = list(summer_sport_revenue_medal.index),
                name = "Bronze",
                marker = dict(color = 'rgba(25, 169, 20, 1)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text =  "Bronze")
         ]  


    layout = go.Layout(title = 'In Summer medal tally for each sports categories',
                   xaxis=dict(
                           title='Sport',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                      size=10,
                                      color='rgb(0,0,0)'
                                      ),
                           tickangle=-45,
                           ),
                   yaxis=dict(
                           title='Total Medal',
                           titlefont=dict(
                                       size=16,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                       size=10,
                                       color='rgb(0,0,0)'
                                       )
                           ),
                    margin = dict(
                                l=150,
                                r=100,
                                t=100,
                                b=150
                                ),
                    showlegend = True,
                    
                   )       

    fig1 = go.Figure(data = data, layout = layout)
  
    graph1 = plot(fig1,filename = "r.html",output_type = "div" )  
    return graph1
    
########################################################################################
#18. Fetch the top 10 athletes with the highest total medal first seperate for both seasons and then in combined form.
#for summer
def top_10_athlt():
    
    summer_melals = summer.groupby("Name")["Medal"].value_counts().unstack(fill_value=0)
    summer_melals['Total'] = summer_melals['Bronze'] + summer_melals['Silver'] + summer_melals['Gold']
    f10meds = summer_melals[[ 'Loss', 'Bronze', 'Silver', 'Gold', 'Total']]
    f10meds.insert(loc=0, column="Category", value=f10meds.index)
    f10meds =  f10meds.sort_values("Total",ascending = True).tail(10)
    data_m = []

    for i in range(f10meds.shape[0]):
        trace = go.Scatter(
                x=list(range(1, f10meds.iloc[i,5]+1)),
                y=[f10meds.iloc[i,0]] * f10meds.iloc[i,5],
                mode='markers',
                name = "B",
                marker=dict(
                        size=30,
                        #            symbol = 300,
                        color=['#A48E65'] * f10meds.iloc[i,2]+\
                               ["#DFE0DF"] * f10meds.iloc[i,3]+\
                                ['#D5A419'] * f10meds.iloc[i,4],
                                 line=dict(color='white',
                                           width=1)
                                 ),
                 showlegend=False,
                 text=str(f10meds.iloc[i,0]) +\
                 '<br>won ' +\
                 str(f10meds.iloc[i, 5]) +\
                 ' medals in total.',
                 hoverinfo='text'
                 )
        data_m.append(trace)

    layout_m = go.Layout(
            title='Top Olympic Medalists In Summer',
            titlefont=dict(
                    size=24,
                    color='#4b8480'
                    ),
                    height=700, 
                    width = 800,
                    hovermode='closest', 
                    yaxis=dict(
                            fixedrange = False,
                            color='#4b8480',
                            automargin=True,
                            ), 
                            xaxis=dict(
                                    color='#4b8480',
                                    showgrid=False,
                                    zeroline=False,
                                    )
                            )
    fig1 = go.Figure(data=data_m, layout=layout_m)
    
    
#for winter

    winter_melals = winter.groupby("Name")["Medal"].value_counts().unstack(fill_value=0)
    winter_melals['Total'] = winter_melals['Bronze'] + winter_melals['Silver'] + winter_melals['Gold']
    f10meds = winter_melals[[ 'Loss', 'Bronze', 'Silver', 'Gold', 'Total']]
    f10meds.insert(loc=0, column="Category", value=f10meds.index)
    f10meds =  f10meds.sort_values("Total",ascending = True).tail(10)
    data_m = []

    for i in range(f10meds.shape[0]):
        trace = go.Scatter(
                x=list(range(1, f10meds.iloc[i,5]+1)),
                y=[f10meds.iloc[i,0]] * f10meds.iloc[i,5],
                mode='markers',
                name = "B",
                marker=dict(
                        size=30,
                        #            symbol = 300,
                        color=['#A48E65'] * f10meds.iloc[i,2]+\
                               ["#DFE0DF"] * f10meds.iloc[i,3]+\
                                ['#D5A419'] * f10meds.iloc[i,4],
                                 line=dict(color='white',
                                           width=1)
                                 ),
                 showlegend=False,
                 text=str(f10meds.iloc[i,0]) +\
                 '<br>won ' +\
                 str(f10meds.iloc[i, 5]) +\
                 ' medals in total.',
                 hoverinfo='text'
                 )
        data_m.append(trace)

    layout_m = go.Layout(
            title='Top Olympic Medalists In Winter',
            titlefont=dict(
                    size=24,
                    color='#4b8480'
                    ),
                    height=700, 
                    width = 600,
                    hovermode='closest', 
                    yaxis=dict(
                            fixedrange = False,
                            color='#4b8480',
                            automargin=True,
                            ), 
                            xaxis=dict(
                                    color='#4b8480',
                                    showgrid=False,
                                    zeroline=False,
                                    )
                            )
    fig2 = go.Figure(data=data_m, layout=layout_m)
    
    
#for mega_data

    
    all_melals = dataset.groupby("Name")["Medal"].value_counts().unstack(fill_value=0)
    all_melals['Total'] = all_melals['Bronze'] + all_melals['Silver'] + all_melals['Gold']
    f10meds = all_melals[[ 'Loss', 'Bronze', 'Silver', 'Gold', 'Total']]
    f10meds.insert(loc=0, column="Category", value=f10meds.index)
    f10meds =  f10meds.sort_values("Total",ascending = True).tail(10)
    data_m = []

    for i in range(f10meds.shape[0]):
        trace = go.Scatter(
                x=list(range(1, f10meds.iloc[i,5]+1)),
                y=[f10meds.iloc[i,0]] * f10meds.iloc[i,5],
                mode='markers',
                name = "B",
                marker=dict(
                        size=30,
                        #            symbol = 300,
                        color=['#A48E65'] * f10meds.iloc[i,2]+\
                               ["#DFE0DF"] * f10meds.iloc[i,3]+\
                                ['#D5A419'] * f10meds.iloc[i,4],
                                 line=dict(color='white',
                                           width=1)
                                 ),
                 showlegend=False,
                 text=str(f10meds.iloc[i,0]) +\
                 '<br>won ' +\
                 str(f10meds.iloc[i, 5]) +\
                 ' medals in total.',
                 hoverinfo='text'
                 )
        data_m.append(trace)

    layout_m = go.Layout(
            title='Top 10 Olympic Medalists ',
            titlefont=dict(
                    size=24,
                    color='#4b8480'
                    ),
                    height=700, 
                    width = 800,
                    hovermode='closest', 
                    yaxis=dict(
                            fixedrange = False,
                            color='#4b8480',
                            automargin=True,
                            ), 
                            xaxis=dict(
                                    color='#4b8480',
                                    showgrid=False,
                                    zeroline=False,
                                    )
                            )
    fig3 = go.Figure(data=data_m, layout=layout_m)
    
    graph1 = plot(fig1,filename = "t.html",output_type = "div")
    graph2 = plot(fig2,filename = "u.html",output_type = "div")
    graph3 = plot(fig3,filename = "v.html",output_type = "div")
    
    return graph1,graph2,graph3
    
########################################################################################
#19. Fetch the countries with their total medals in combined of both seasons.
#for mega_data
def cnty_wt_ttl_mdl():
    combined_melals = dataset.groupby("region")["Medal"].value_counts().unstack()
    combined_melals["total"] = combined_melals.apply(np.sum,axis=1)


