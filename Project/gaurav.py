# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 17:16:58 2019

@author: GRV
"""

# -*- coding: utf-8 -*-
"""
punit
1352 sector 23A gudgaav
23 market
Created on Wed Jun 19 08:28:21 2019

@author: GRV
"""
#from pandas.core.reshape.concat import concat
#from pandas.core.reshape.melt import melt, lreshape, wide_to_long
#from pandas.core.reshape.reshape import pivot_simple as pivot, get_dummies
#from pandas.core.reshape.merge import merge, merge_ordered, merge_asof
#from pandas.core.reshape.pivot import pivot_table, crosstab
#from pandas.core.reshape.tile import cut, qcut
"""
# OLYMPICS HISTORY

* According to historical records, the first ancient Olympic Games can be 

traced back to 776 BC. They were dedicated to the Olympian gods and were staged

on the ancient plains of Olympia. They continued for nearly 12 centuries, 

until Emperor Theodosius decreed in 393 A.D. that all such "pagan cults" be banned.


This is a historical dataset on the modern Olympic Games, including all the Games from Athens 1896 to Rio 2016.


This dataset provides an opportunity to ask questions about how the Olympics 

have evolved over time, including questions about the participation and performance of women, different nations, and different sports and events.


THE FILE athlete_events.csv CONTAINS 271116 ROWS AND 15 COLUMNS. EACH ROW 

CORRESPONDS TO AN INDIVIDUAL ATHLETE COMPETING IN AN INDIVIDUAL OLYMPIC EVENT 

(ATHLETE-EVENTS). THE COLUMNS ARE:


ID - Unique number for each athlete

Name - Athlete's name

Sex - M or F

Age - Integer

Height - In centimeters

Weight - In kilograms

Team - Team name

NOC - National Olympic Committee 3-letter code

Games - Year and season

Year - Integer

Season - Summer or Winter

City - Host city

Sport - Sport

Event - Event

Medal - Gold, Silver, Bronze, or NA



noc_regions.csv-

NOC (National Olympic Committee 3 letter code)

Country name 

Notes



Project Tasks-


A---> DATA ANALYSIS AND VISUALIZATION


Data is given for both summer and winter olympics combined. So perform

following tasks separately for both unless mentioned to perform in combine 

form -


1. Fetch the participant who won the most medals with their sports and country

(Consider as whole no male and female distinguish needed)


2. Visualize Athlete participation count over years.


3. Visualize the Athlete Participation by gender over years.


4. Visualize the Gender Distribution in the games.


5. Visualize the number of countries participated in the games.


6.Visualize the highest number of participation nation wise.


7. Visualize the countries that Hosted the games for the highest number of times.


8. Visualize the cities that hosted the games for the highest number of times.


9. Visualize the average age, height and weight of the athletes for various 

   sports categories. (3 separate representation)

   

10. Visualize the total unique sports activities over years in Olympics.


11. Visualize the event ratio by gender.


12. Visualize the events by genders over years.


13. Fetch the discontinued sports in olympics 2016.


14. Revenue Categories - 


"""

import pandas as pd
import numpy as np
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.plotly as py
from PIL import Image
init_notebook_mode(connected=True)
import difflib


athlete_events = pd.read_csv("athlete_events.csv")
noc_regions = pd.read_csv("noc_regions.csv")
olym = pd.read_csv("olym.csv",encoding='latin1')

#check uniqe values of noc
name_of_noc=noc_regions["NOC"].unique()
dataset = pd.merge(athlete_events,noc_regions,how="left",on="NOC")
mega_dataset = pd.merge(dataset,olym,on=["City","Year"],how="left")

#remove NOC = (TUV,UNK,ROT,SGP) rows which are 370
mega_dataset = mega_dataset[(mega_dataset["NOC"]!="TUV") & (mega_dataset["NOC"]!="UNK") & (mega_dataset["NOC"]!="ROT")&(mega_dataset["NOC"]!="SGP")]
mega_dataset.isnull().any(axis=0)

#crete summer and winter dataset seprately
winter = mega_dataset[mega_dataset["Season"]=="Winter"]
summer = mega_dataset[mega_dataset["Season"]=="Summer"]

#1. Fetch the participant who won the most medals with their sports and country
winter_participent = winter.groupby(["Name","Sport","region"])["Medal"].count().sort_values().tail(1)
summer_participent = summer.groupby(["Name","Sport","region"])["Medal"].count().sort_values().tail(1)
# for winter
print("Highest Medals Won by Athlete In Winter Olympics : ")
print("Athlete : ",winter_participent.index[0][0])
print("Sport : ",winter_participent.index[0][1])
print("Country : ",winter_participent.index[0][2])
print("Medals : ",winter_participent.values[0])
#for summer
print("\nHighest Medals Won by Athlete In summer Olympics : ")
print("Athlete : ",summer_participent.index[0][0])
print("Sport : ",summer_participent.index[0][1])
print("Country : ",summer_participent.index[0][2])
print("Medals : ",summer_participent.values[0])
#####################################################################################################
#2. Visualize Athlete participation count over years.
#for summer
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
                                )
                    )
fig = go.Figure(data = data, layout = layout)
plot(fig)

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
                                )
                    )
fig = go.Figure(data = data, layout = layout)
plot(fig)
#####################################################################################################
#3. Visualize the Athlete Participation by gender over years.
#for summer
year_m_participent_summer = summer[mega_dataset["Sex"]=="M"].groupby("Year")["Sex"].count()
year_f_participent_summer = summer[mega_dataset["Sex"]=="F"].groupby("Year")["Sex"].count()
data1 = go.Bar(
                x = year_m_participent_summer.index,
                y = year_m_participent_summer.values,
                name = "Male",
                marker = dict(color = 'rgba(255, 0, 255, 1)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Male Athlete")
data2 = go.Bar(
                x = year_f_participent_summer.index,
                y = year_f_participent_summer.values,
                name = "Female",
                marker = dict(color = 'rgba(255, 0, 255, 1)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Female Athlete")               

layout = go.Layout(title = 'In Summer Athlete Participation By Gender Over Years',
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


#for winter
year_m_participent_winter = winter[mega_dataset["Sex"]=="M"].groupby("Year")["Sex"].count()
year_f_participent_winter = winter[mega_dataset["Sex"]=="F"].groupby("Year")["Sex"].count()
data1 = go.Bar(
                x = year_m_participent_winter.index,
                y = year_m_participent_winter.values,
                name = "Male",
                marker = dict(color = 'rgba(255, 0, 255, 1)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Male Athlete")
data2 = go.Bar(
                x = year_f_participent_winter.index,
                y = year_f_participent_winter.values,
                name = "Female",
                marker = dict(color = 'rgba(255, 0, 255, 1)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Female Athlete")               

layout = go.Layout(title = 'In Winter Athlete Participation By Gender Over Years',
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
###############################################################################################
#4. Visualize the Gender Distribution in the games.
#for summer
sport_m_participent_summer = summer[mega_dataset["Sex"]=="M"].groupby("Sport")["Sex"].count()
sport_f_participent_summer = summer[mega_dataset["Sex"]=="F"].groupby("Sport")["Sex"].count()
# or
#sport_m_participent_summer = summer.groupby("Sport")["Sex"].value_counts().unstack()
data1 = go.Bar(
                x = sport_m_participent_summer.index,
                y = sport_m_participent_summer.values,
                name = "Male",
                marker = dict(color = 'rgba(0, 126, 133, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Male Athlete")
data2 = go.Bar(
                x = sport_f_participent_summer.index,
                y = sport_f_participent_summer.values,
                name = "Female",
                marker = dict(color = 'rgba(31, 244, 255, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Female Athlete")               

layout = go.Layout(title = 'In Summer Athlete Participation By Gender Over Games',
                   xaxis=dict(
                           title='Game',
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
                           title='Number Of Athlete',
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
                   bargroupgap=0.1       
                   )
data = [data1,data2]                       
fig = go.Figure(data = data, layout = layout)
plot(fig)
#for winter
sport_m_participent_winter = winter[mega_dataset["Sex"]=="M"].groupby("Sport")["Sex"].count()
sport_f_participent_winter = winter[mega_dataset["Sex"]=="F"].groupby("Sport")["Sex"].count()
data1 = go.Bar(
                x = sport_m_participent_winter.index,
                y = sport_m_participent_winter.values,
                name = "Male",
                marker = dict(color = 'rgba(0, 126, 133, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Male Athlete")
data2 = go.Bar(
                x = sport_f_participent_winter.index,
                y = sport_f_participent_winter.values,
                name = "Female",
                marker = dict(color = 'rgba(31, 244, 255, 0.53)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "Female Athlete")               

layout = go.Layout(title = 'In Winter Athlete Participation By Gender Over Games',
                   xaxis=dict(
                           title='Game',
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
                           title='Number Of Athlete',
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
############################################################################################
#5. Visualize the number of countries participated in the games.
#for winter
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

layout = go.Layout(title = 'In Winter Athlete Participation By Gender Over Games',
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
fig = go.Figure(data = data, layout = layout)
plot(fig)
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

layout = go.Layout(title = 'In Summer Athlete Participation By Gender Over Games',
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
fig = go.Figure(data = data, layout = layout)
plot(fig)

###########################################################################################
#6.Visualize the highest number of participation nation wise.
year_list = sorted(list(summer["Year"].unique()))
l = summer.groupby(["Year","region"])["Name"].count()
nation_participent_summer = [summer[summer["Year"]==name].groupby("region")["Name"].count() for name in year_list]
a = summer[summer["Year"]==1992].groupby("region")["Name"].count().max().values
summer["Name"].unstack()

aac=pd.pivot_table(summer, 'Year', 'Name', 'Country')

d
from collections import Counter
acc=pd.pivot_table(summer,index=['Year','Country'],values=['Name'],aggfunc=Counter)
###########################################################################################
#7. Visualize the countries that Hosted the games for the highest number of times.
host_country = summer["Country"].value_counts()

###########################################################################################
#8. Visualize the cities that hosted the games for the highest number of times.

###########################################################################################

l=mega_dataset[["City","Country"]]
lu=len(l["City"])
lc=list(l["Country"].unique())

l[l["City"]=="Los Angeles"]["Country"]









plt.savefig('sinewave.png')
logo = Image.open('sinewave.png')
logo.show()

import plotly
import jupyter
import flask

mega_dataset.isnull().any(axis=0)
l=dataset["NOC"].unique()


import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.plotly as py
init_notebook_mode(connected=True)


trace1 = go.Bar(
                x = sport_m_participent_summer.index,
                y = sport_m_participent_summer.values,
                name = "citations",
                marker = dict(color = 'rgba(255, 0, 255, 1)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = "M")
trace2 = go.Bar(
                x = sport_f_participent_summer.index,
                y = sport_f_participent_summer.values,
                name = "citations",
                marker = dict(color = 'rgba(255, 174, 255, 0.5)',
                             line=dict(color='rgb(0,0,0)',width=3)),
                text = "Ffffffffffffffffffffffffffffffffffffffffffffffffffffffff")
                

data = [trace1,trace2]
layout = go.Layout(barmode = "group")
fig = go.Figure(data = data, layout = layout)
plot(fig)
