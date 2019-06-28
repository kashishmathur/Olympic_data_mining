# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 18:03:52 2019

@author: Lakshya
"""


""" Libraries """
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from difflib import SequenceMatcher


import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


from library import dataset,olympics,summer,winter
  

#1. Fetch the participant who won the most medals with their sports and country
def a():
    top_medal_s = summer.groupby(["Name" , "region" , "Sport"])["Medal"].count()
    top_medal_s = top_medal_s.sort_values(ascending = False).head(1)
    print("Name : ",top_medal_s.index[0][0])
    print("Team : ",top_medal_s.index[0][1])
    print("Sport : ",top_medal_s.index[0][2])
    print("Medal :",top_medal_s.values[0])
a()    

def b():
    top_medal_w = winter.groupby(["Name" , "region" , "Sport"])["Medal"].count()
    top_medal_w = top_medal_w.sort_values(ascending = False).head(1)
    print("Name : ",top_medal_w.index[0][0])
    print("Team : ",top_medal_w.index[0][1])
    print("Sport : ",top_medal_w.index[0][2])
    print("Medal :",top_medal_w.values[0])
b()


#2. Visualize Athelete participation count over years.

def c():
    year_s = summer["Year"].value_counts()
    #plt.bar(year_s.index , year_s)
    #plt.legend("Summer" , loc = "upperleft")
    data = [go.Bar(
                x = year_s.index,
                y = year_s,
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
                                )
                    )
    fig = go.Figure(data = data, layout = layout)
    plot(fig)


c()

def d():
    year_w = winter["Year"].value_counts()
    #plt.bar(year_w.index , year_w)
    #plt.legend("Winter" , loc = "upperleft")
    data = [go.Bar(
                x = year_w.index,
                y = year_w,
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
                                )
                    )
    fig = go.Figure(data = data, layout = layout)
    plot(fig)
d()  


#3. Visualize the Athelete Participation by gender over years.
'''
gender_ym_s = summer[summer["Sex"] == "M"].groupby(["Year"])["Sex"].count()
gender_yf_s = summer[summer["Sex"] == "F"].groupby(["Year"])["Sex"].count()
plt.bar(gender_ym_s.index , gender_ym_s, edgecolor = 'black')
plt.bar(gender_yf_s.index , gender_yf_s , edgecolor = 'black')
plt.legend(["Male" , "Female"] , loc = "upperleft")

gender_ym_w = winter[winter["Sex"] == "M"].groupby(["Year"])["Sex"].count()
gender_yf_w = winter[winter["Sex"] == "F"].groupby(["Year"])["Sex"].count()
plt.bar(gender_ym_w.index , gender_ym_w, edgecolor = 'black')
plt.bar(gender_yf_w.index , gender_yf_w, edgecolor = 'black')
plt.legend(["Male" , "Female"] , loc = "upperleft")
'''
def e():
    gender_ym_s = summer[summer["Sex"] == "M"].groupby(["Year"])["Sex"].count()
    gender_yf_s = summer[summer["Sex"] == "F"].groupby(["Year"])["Sex"].count()
    
    summ = gender_ym_s + gender_yf_s
    summ = summ.fillna(0)
    
    scaled_pcount_f = (gender_yf_s - min(summ)) / (max(summ) - min(summ)) + 0.1
    scaled_pcount_m = (gender_ym_s - min(summ)) / (max(summ) - min(summ)) + 0.1

    trace0 = go.Scatter(
            x=gender_yf_s.index,
            y=gender_yf_s,
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
            x=gender_ym_s.index,
            y=gender_ym_s,
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

    plot(fig1)
    
    
    
e()

def g():
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

    fig1 = go.Figure(data=data1, layout=layout1)

    plot(fig1)
    
    
    
    
g()    
    

#4. Visualize the Gender Distribution in the games.
"""
gender_s = summer["Sex"].value_counts()
gender_w = winter["Sex"].value_counts()

plt.bar(gender_s.index , gender_s)
plt.bar(gender_w.index , gender_w)
plt.legend({"Summer","Winter"} , loc = "upperleft")
"""
#or
'''
gender_m_s = summer[summer["Sex"] == "M"].groupby(["Sport"])["Sex"].count()
gender_f_s = summer[summer["Sex"] == "F"].groupby(["Sport"])["Sex"].count()
plt.bar(gender_m_s.index , gender_m_s)
plt.bar(gender_f_s.index , gender_f_s)
plt.xticks(rotation = 90)
plt.legend({"Male","Female"} , loc = "upperleft")
'''
def h():
    gender_m_s = summer[summer["Sex"] == "M"].groupby(["Sport"])["Sex"].count()
    gender_f_s = summer[summer["Sex"] == "F"].groupby(["Sport"])["Sex"].count()
    
    data1 = go.Bar(
                x = gender_m_s.values,
                y = gender_m_s.index,
                name = "Male",
                marker = dict(color = 'rgba(0, 126, 133, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Male Athlete",
                orientation = "h")
    data2 = go.Bar(
                x = gender_f_s.values,
                y = gender_f_s.index,
                name = "Female",
                marker = dict(color = 'rgba(31, 244, 255, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Female Athlete",
                orientation = "h")               

    layout = go.Layout(title = 'In Summer Athlete Participation By Gender Over Games',
                       width = 1800,
                       height = 800,
                   xaxis=dict(
                           title='Number Of Athlete',
                           titlefont=dict(
                                       size=20,
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
                                       size=20,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                       size=14,
                                       color='rgb(0,0,0)'
                                       )
                           ),
                    margin = dict(
                                l=230,
                                r=100,
                                t=70,
                                b=100
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
    fig = go.Figure(data = data, layout = layout)
    plot(fig)



    gender_m_w = winter[winter["Sex"] == "M"].groupby(["Sport"])["Sex"].count()
    gender_f_w = winter[winter["Sex"] == "F"].groupby(["Sport"])["Sex"].count()
    
    data1 = go.Bar(
                x = gender_m_w.values,
                y = gender_m_w.index,
                name = "Male",
                marker = dict(color = 'rgba(0, 255, 255, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Male Athlete",
                orientation = 'h')
    data2 = go.Bar(
                x = gender_f_w.values,
                y = gender_f_w.index,
                name = "Female",
                marker = dict(color = 'rgba(255, 0, 255, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Female Athlete",
                orientation = 'h')               

    layout = go.Layout(title = 'In Winter Athlete Participation By Gender Over Games',
                       width = 1800,
                   xaxis=dict(
                           title='Number Of Athlete',
                           titlefont=dict(
                                       size=25,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                      size=15,
                                      color='rgb(0,0,0)'
                                      ),
                           tickangle=-45,
                           ),
                   yaxis=dict(
                           title='Game',
                           titlefont=dict(
                                       size=25,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                       size=15,
                                       color='rgb(0,0,0)'
                                       )
                           ),
                    margin = dict(
                                l=200,
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
    fig = go.Figure(data = data, layout = layout)
    plot(fig)

h()
    
    

#5. Visualize the number of countries participated in the games.

def j():
    game_s = summer.groupby(["Sport"])["region"].unique()
    count_country_summer = [len(x) for x in game_s]
    country_name_summer = [list(x) for x in game_s]

    #length = [len(x) for x in game_s]
    #plt.bar(game_s.index , [len(x) for x in game_s])
    #plt.legend({"Summer"} , loc = "upperleft")
    #plt.xticks(rotation = 70)
    data = [go.Bar(
                x = game_s.index,
                y = count_country_summer,
                name = "Summer",
                marker = dict(color = 'rgba(0, 126, 133, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = country_name_summer,
                textposition = 'auto') ]           

    layout = go.Layout(title = 'In Summer Countries Participation',
                   xaxis=dict(
                           title='Country',
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
                           title='Number of participation',
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
    fig = go.Figure(data = data, layout = layout)
    plot(fig)




    game_w = winter.groupby(["Sport"])["region"].unique()
    #plt.bar(game_w.index , [len(x) for x in game_w])
    #plt.legend({"Winter"} , loc = "upperleft")
    #plt.xticks(rotation = 90)
    count_country_winter = [len(x) for x in game_w]
    country_name_winter = [list(x) for x in game_w]
    data = [go.Bar(
                x = game_w.index,
                y = count_country_winter,
                name = "Winter",
                marker = dict(color = 'rgba(0, 126, 133, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = country_name_winter,
                textposition = 'auto') ]           

    layout = go.Layout(title = 'In Summer Countries Participation',
                   xaxis=dict(
                           title='Country',
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
                           title='Number of Participation',
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
    fig = go.Figure(data = data, layout = layout)
    plot(fig)

j()


#6.Visualize the highest number of participation nation wise.

def l():
    
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
                    
                    "title":"Prticipation of countries",
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
    plot(fig)

    

#7. Visualize the countries that Hosted the games for the highest number of times.
#for summer
def smr_hst_host_cnty():

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


    fig = go.Figure(data=data, layout=layout)
    plot(fig, filename = "Mixed Subplots Volcano")
 
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


    fig = go.Figure(data=data, layout=layout)
    plot(fig, filename = "Mixed Subplots Volcano")

###########################################################################################
#8. Visualize the cities that hosted the games for the highest number of times.
def hst_host_city():
    
    host_city_s = olympics[olympics["Season"] == "Summer"]["City"].value_counts()
    host_city_w = olympics[olympics["Season"] == "Winter"]["City"].value_counts()
    #high_year = host_country_s.max(axis = 1)
    #high_value = host_country_s.idxmax(axis = 1)
    
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
    plot(fig)


#9. Visualize the average age, height and weight of the atheletes for various sports 
#   categories. (3 seperate representation)

def p():
    age_summer = summer.groupby("Sport")[["Age" , "Height" , "Weight"]].mean()
    
    data1 = go.Bar(
                x = age_summer.index,
                y = age_summer["Age"],
                name = "Age",
                marker = dict(color = 'rgba(0, 255, 255, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Average",
                textposition = 'auto')
                
    data2 = go.Bar(
                x = age_summer.index,
                y = age_summer["Height"],
                name = "Height",
                marker = dict(color = 'rgba(255, 0, 255, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Average",
                textposition = 'auto')
                
    data3 = go.Bar(
                x = age_summer.index,
                y = age_summer["Weight"],
                name = "weight",
                marker = dict(color = 'rgba(255, 255, 0, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Average",
                textposition = 'auto')
                
                
    layout = go.Layout(title = 'Average age, height and weight in Sports for Summer season',
                   xaxis=dict(
                           title='Sports',
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
                           title="Average",
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
    data = [data1 , data2 , data3]
    fig = go.Figure(data = data, layout = layout)
    plot(fig)
    



    age_winter = winter.groupby("Sport")[["Age" , "Height" , "Weight"]].mean()
    
    data1 = go.Bar(
                x = age_winter.index,
                y = age_winter["Age"],
                name = "Age",
                marker = dict(color = 'rgba(0, 255, 255, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Average",
                textposition = 'auto')
                
    data2 = go.Bar(
                x = age_winter.index,
                y = age_winter["Height"],
                name = "Height",
                marker = dict(color = 'rgba(255, 0, 255, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Average",
                textposition = 'auto')
                
    data3 = go.Bar(
                x = age_winter.index,
                y = age_winter["Weight"],
                name = "weight",
                marker = dict(color = 'rgba(255, 255, 0, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Average",
                textposition = 'auto')
                
                
    layout = go.Layout(title = 'Average age, height and weight in Sports for Winter season',
                   xaxis=dict(
                           title='Sports',
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
                           title="Average",
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
    data = [data1 , data2 , data3]
    fig = go.Figure(data = data, layout = layout)
    plot(fig)
    
p()


#10. Visualize the total unique sports activities over years in Olympics.

def r():
    unique_sport_summer = summer.groupby("Year")["Sport"].unique()
    count_sport_summer = [len(x) for x in unique_sport_summer]
    sport_name_summer = [list(x) for x in unique_sport_summer]
    
    unique_sport_winter = winter.groupby("Year")["Sport"].unique()
    count_sport_winter = [len(x) for x in unique_sport_winter]
    sport_name_winter = [list(x) for x in unique_sport_winter]
    
    data1 = [go.Bar(
                x = unique_sport_summer.index,
                y = count_sport_summer,
                name = "Summer",
                marker = dict(color = 'rgba(0, 255, 255, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = sport_name_summer,
                textposition = 'auto')]
                
    data2 = [go.Bar(
                x = unique_sport_winter.index,
                y = count_sport_winter,
                name = "Winter",
                marker = dict(color = 'rgba(255, 0, 255, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = sport_name_winter,
                textposition = 'auto')]
                
    layout = go.Layout(title = 'Unique number of Sports',
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
                           title='Number Of Sports',
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
    #data = [data1,data2]                       
    fig = go.Figure(data = data1, layout = layout)
    plot(fig)
    
    fig = go.Figure(data = data2, layout = layout)
    plot(fig)

r()

#11. Visualize the event ratio by gender.

def s():
    event_summer = summer.groupby("Event")["Sex"].value_counts().unstack()
    
    data1 = go.Bar(
                x = event_summer.index,
                y = event_summer["F"],
                name = "Female",
                marker = dict(color = 'rgba(0, 255, 255, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "F",
                textposition = 'auto')
                
    data2 = go.Bar(
                x = event_summer.index,
                y = event_summer["M"],
                name = "Male",
                marker = dict(color = 'rgba(255, 0, 255, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Male",
                textposition = 'auto')
                
    layout = go.Layout(title = 'Event Ratio by gender',
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
                           title='Ratio',
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
    fig = go.Figure(data = data, layout = layout)
    plot(fig)

s()    

def t():
    event_winter = winter.groupby("Event")["Sex"].value_counts().unstack()
    
    data1 = go.Bar(
                x = event_winter.index,
                y = event_winter["F"],
                name = "Female",
                marker = dict(color = 'rgba(0, 255, 255, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "F",
                textposition = 'auto')
                
    data2 = go.Bar(
                x = event_winter.index,
                y = event_winter["M"],
                name = "Male",
                marker = dict(color = 'rgba(255, 0, 255, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Male",
                textposition = 'auto')
                
    layout = go.Layout(title = 'Event Ratio by gender',
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
                           title='Ratio',
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
    fig = go.Figure(data = data, layout = layout)
    plot(fig)

t()    

#12. Visualize the events by genders over years.

def u():
    events_gender_summer_m = summer[summer["Sex"] == "M"].groupby("Year")["Event"].value_counts().unstack()
    events_gender_summer_f = summer[summer["Sex"] == "F"].groupby("Year")["Event"].value_counts().unstack()
    summ_m = events_gender_summer_m.sum(axis = 1)
    summ_f = events_gender_summer_f.sum(axis = 1)
    
    data1 = go.Bar(
                x = events_gender_summer_m.index,
                y = summ_m,
                name = "Male",
                marker = dict(color = 'rgba(0, 255, 255, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Event",
                textposition = 'auto')
                
    data2 = go.Bar(
                x = events_gender_summer_f.index,
                y = summ_f,
                name = "Female",
                marker = dict(color = 'rgba(255, 0, 255, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Event",
                textposition = 'auto')
                
    layout = go.Layout(title = 'Number of events by genders in Summer',
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
                           title='Number of events',
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
    fig = go.Figure(data = data, layout = layout)
    plot(fig)

u()

def v():
    events_gender_winter_m = winter[winter["Sex"] == "M"].groupby("Year")["Event"].value_counts().unstack()
    events_gender_winter_f = winter[winter["Sex"] == "F"].groupby("Year")["Event"].value_counts().unstack()
    summ_m = events_gender_winter_m.sum(axis = 1)
    summ_f = events_gender_winter_f.sum(axis = 1)
    
    data1 = go.Bar(
                x = events_gender_winter_m.index,
                y = summ_m,
                name = "Male",
                marker = dict(color = 'rgba(0, 255, 255, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Event",
                textposition = 'auto')
                
    data2 = go.Bar(
                x = events_gender_winter_f.index,
                y = summ_f,
                name = "Female",
                marker = dict(color = 'rgba(255, 0, 255, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Event",
                textposition = 'auto')
                
    layout = go.Layout(title = 'Number of events by genders in Winters',
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
                           title='Number of events',
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
    fig = go.Figure(data = data, layout = layout)
    plot(fig)

v()

#13. Fetch the discontinued sports in olympics 2016.

def w():
    unique_sport_s = list(summer[summer["Year"] != 2016]["Sport"].unique())
    unique_2016_s = list(summer[summer["Year"] == 2016]["Sport"].unique())
    discontinued_sport_s = list(set(unique_sport_s) - set(unique_2016_s))
    
    print(discontinued_sport_s)
    
    unique_sport_w = list(winter[winter["Year"] != 2016]["Sport"].unique())
    unique_2016_w = list(winter[winter["Year"] == 2016]["Sport"].unique())
    discontinued_sport_w = list(set(unique_sport_w) - set(unique_2016_w))
        
    print(discontinued_sport_w)

w()

'''
14. Revenue Categories - 

Category ---------->   Sports
A                      Acquatics, Atheletes, Gymnastics
B                      Cycling, Tennis
C                      Archery, Badminton, Boxing, Judo, Rowing, Shooting, Table Tennis, Weightlifting
D                      Canoeing, Equestrianism, Sailing, Fencing, Taekwondo, Triathlon, Wrestling
E                      Modern Pentathlon, Golf

    Visualize the sports ratio in each revenue category.
'''

def x():
    A = ["Acquatics", "Atheletes", "Gymnastics"]
    B = ["Cycling", "Tennis"]
    C = ["Archery", "Badminton", "Boxing", "Judo", "Rowing", "Shooting", "Table Tennis", "Weightlifting"]
    D = ["Canoeing", "Equestrianism", "Sailing", "Fencing", "Taekwondo", "Triathlon", "Wrestling"]
    E = ["Modern Pentathlon", "Golf"]
    
    def cate(item):
        if item in A:
            return "A"
        elif item in B:
            return "B"
        elif item in C:
            return "C"
        elif item in D:
            return "D"
        elif item in E:
            return "E"
        else:
            return np.nan
    
            
    summer["Category"] = summer["Sport"].apply(cate)
    
    sport_ratio_s = summer.groupby("Category")["Sport"].value_counts(normalize = True).unstack()
    
    data1 = go.Bar(
                y = sport_ratio_s.columns,
                x = sport_ratio_s.iloc[0,:].values,
                name = "A",
                marker = dict(color = 'rgba(0, 255, 255, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "A",
                textposition = 'auto',
                orientation = "h")
                
    data2 = go.Bar(
                y = sport_ratio_s.columns,
                x = sport_ratio_s.iloc[1,:].values,
                name = "B",
                marker = dict(color = 'rgba(255, 0, 255, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "B",
                textposition = 'auto',
                orientation = "h")
                
    data3 = go.Bar(
                y = sport_ratio_s.columns,
                x = sport_ratio_s.iloc[2,:].values,
                name = "C",
                marker = dict(color = 'rgba(255, 255, 0, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "C",
                textposition = 'auto',
                orientation = "h")
                
    data4 = go.Bar(
                y = sport_ratio_s.columns,
                x = sport_ratio_s.iloc[3,:].values,
                name = "D",
                marker = dict(color = 'rgba(120, 0, 255, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "D",
                textposition = 'auto',
                orientation = "h")
                
    data5 = go.Bar(
                y = sport_ratio_s.columns,
                x = sport_ratio_s.iloc[4,:].values,
                name = "E",
                marker = dict(color = 'rgba(255, 0, 100, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "E",
                textposition = 'auto',
                orientation = "h")
                
    layout = go.Layout(title = 'Sports ratio in revenue category',
                   xaxis=dict(
                           title='Ratio',
                           titlefont=dict(
                                       size=20,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                      size=20,
                                      color='rgb(0,0,0)'
                                      ),
                           #tickangle=-45,
                           ),
                   yaxis=dict(
                           title='Sport',
                           titlefont=dict(
                                       size=20,
                                       color='rgb(0,0,0)'
                                      ),
                           tickfont=dict(
                                       size=20,
                                       color='rgb(0,0,0)'
                                       )
                           ),
                    margin = dict(
                                l=220,
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
    data = [data1,data2,data3,data4,data5]                       
    fig = go.Figure(data = data, layout = layout)
    plot(fig)

    
        
x()

def y():
    A = ["Acquatics", "Atheletes", "Gymnastics"]
    B = ["Cycling", "Tennis"]
    C = ["Archery", "Badminton", "Boxing", "Judo", "Rowing", "Shooting", "Table Tennis", "Weightlifting"]
    D = ["Canoeing", "Equestrianism", "Sailing", "Fencing", "Taekwondo", "Triathlon", "Wrestling"]
    E = ["Modern Pentathlon", "Golf"]
    
    def cate(item):
        if item in A:
            return "A"
        elif item in B:
            return "B"
        elif item in C:
            return "C"
        elif item in D:
            return "D"
        elif item in E:
            return "E"
        else:
            return np.nan
    
            
    winter["Category"] = winter["Sport"].apply(cate)
    '''
    sport_ratio_w = winter.groupby("Category")["Sport"].value_counts(normalize = True).unstack()
    
    data1 = go.Bar(
                x = sport_ratio_w.columns,
                y = sport_ratio_w.iloc[0,:].values,
                name = "A",
                marker = dict(color = 'rgba(0, 255, 255, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "A",
                textposition = 'auto')
                
    data2 = go.Bar(
                x = sport_ratio_w.columns,
                y = sport_ratio_w.iloc[1,:].values,
                name = "B",
                marker = dict(color = 'rgba(255, 0, 255, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "B",
                textposition = 'auto')
                
    data3 = go.Bar(
                x = sport_ratio_w.columns,
                y = sport_ratio_w.iloc[2,:].values,
                name = "C",
                marker = dict(color = 'rgba(255, 255, 0, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "C",
                textposition = 'auto')
                
    data4 = go.Bar(
                x = sport_ratio_w.columns,
                y = sport_ratio_w.iloc[3,:].values,
                name = "D",
                marker = dict(color = 'rgba(120, 0, 255, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "D",
                textposition = 'auto')
                
    data5 = go.Bar(
                x = sport_ratio_w.columns,
                y = sport_ratio_w.iloc[4,:].values,
                name = "E",
                marker = dict(color = 'rgba(255, 0, 100, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "E",
                textposition = 'auto')
                
    layout = go.Layout(title = 'Sports ratio in revenue category',
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
                           title='Ratio',
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
    data = [data1,data2,data3,data4,data5]                       
    fig = go.Figure(data = data, layout = layout)
    plot(fig)
    '''
    
        

y()

#15. Visualize the medals won in each revenue category.

def z():
    
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

    title='Total medals won by categories',
    titlefont=dict(
            size=36,
            color='#4b8480'
            ),

    )
    fig = go.Figure(data=data1,layout=layout1)
    plot(fig)
    
z()      

def aa():
       
    
#16. Fetch the medal tally for each sports categories
 
def ab():
    medal_summer = summer.groupby("Category")["Medal"].value_counts().unstack()
    
    
    medal_summer['Total'] = medal_summer['Bronze'] + medal_summer['Silver'] + medal_summer['Gold']
    medal_summer.insert(loc=0, column="Category", value=medal_summer.index)
    #medal_summer.insert(loc = 5 , column="Total" , value=[11,22,15,13,18])

# take only ones with 10 or more medals
    medal_summer_s = medal_summer[medal_summer['Total'] >= 10].sort_values(by='Total').copy()

# now onto the plot
    data_m = []

    for i in range(medal_summer_s.shape[0]):
        trace = go.Scatter(
                x=list(range(1, medal_summer_s.iloc[i,5]+1)),
                y=[medal_summer_s.iloc[i,0]] * medal_summer_s.iloc[i,5],
                mode='markers',
                marker=dict(
                        size=30,
                        symbol=100, #"circle-open"
                        color=['#A48E65'] * medal_summer_s.iloc[i,1]+\
                               ['#D5A419'] * medal_summer_s.iloc[i,2]+\
                                ['#DFE0DF'] * medal_summer_s.iloc[i,4],
                                 line=dict(color='white',
                                           width=2)
                                 ),
                                 showlegend=False,
                                 text=str(medal_summer_s.iloc[i,0]) +\
                                 '<br>won ' +\
                                 str(medal_summer_s.iloc[i, 5]) +\
                                 ' medals in total.',
                                 hoverinfo='text'
                                 )
        data_m.append(trace)

    layout_m = go.Layout(
            title='Medals won by Categories',
            titlefont=dict(
                    size=24,
                    color='#4b8480'
                    ),
                    height=800, 
                    hovermode='closest', 
                    yaxis=dict(
                            color='#4b8480',
                            automargin=True,
                            ), 
                            xaxis=dict(
                                    color='#4b8480',
                                    showgrid=False,
                                    zeroline=False))
    fig_m = go.Figure(data=data_m, layout=layout_m)
    plot(fig_m)

    
ab()    
    
    
    
#18. Fetch the top 100 atheletes with the highest total medal first seperate for both seasons and then in combined form.

def ac():
    athlete_s = summer.groupby("Name")["Medal"].value_counts().unstack()
    top_athlete_s = sorted(athlete_s.sum(axis = 1) , reverse = True)[0:100]
    print(top_athlete_s)
    
    athlete_w = winter.groupby("Name")["Medal"].value_counts().unstack()
    top_athlete_w = sorted(athlete_w.sum(axis = 1),reverse = True)[0:100]
    print(top_athlete_w)
    
    athlet = dataset.groupby("Name")["Medal"].value_counts().unstack()
    top_athlete = sorted(athlet.sum(axis = 1) , reverse = True)[0:100]

    
#19. Fetch the countries with their total medals in combined of both seasons.

def ad():
    total_medal_country = dataset.groupby("Country")["Medal"].value_counts().unstack()
    total_medal = total_medal_country.sum(axis = 1)
    



