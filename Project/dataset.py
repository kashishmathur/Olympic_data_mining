# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 11:22:01 2019

@author: HP
"""

'''dataset'''
olympics = pd.read_csv("olym.csv" , encoding = "latin-1")
olympics = olympics.iloc[:,0:7]
olympics = olympics[olympics["Summer (Olympiad)"].notnull() | olympics["Winter"].notnull()]
olympics["Year"] = olympics["Year"].fillna(method = 'ffill')
olympics = olympics.append({"City" : "Stockholm" , "Country" : "Sweden" , "Summer (Olympiad)" : "XVI" , "Year" : 1956 , "latitude" : "59.3326" , "longitude" : "18.0649"},ignore_index = True)

'''noc datset'''
noc = pd.read_csv("noc_regions.csv")
noc = noc.append({'NOC': "SGP" , 'region' : "Singapore" , 'notes' : np.nan}, ignore_index=True)
noc_tuv = noc[noc["NOC"] == "TUV"]
noc.loc[noc_tuv.index[0]]["region"] = "Tuvalu"


'''athlete dataset'''
athlete = pd.read_csv("athlete_events.csv")
athlete = athlete[athlete["Year"] != 1906]

athlete_city = list(athlete["City"].unique())
olym_city = list(olympics["City"].unique())
new = {}
for item in athlete_city:
    if item not in olym_city:
        maxx = 0.0
        for value in olym_city:
            ratio = difflib.SequenceMatcher(None,item,value).ratio()
            if ratio > maxx:
                maxx = ratio
                name = value
        new[item] = name
        
athlete["City"] = athlete["City"].replace(new.keys() , new.values())        
            
    


'''merged dataset'''
data = pd.merge(athlete , noc , how = "left" , on = "NOC")
dataset = pd.merge(data , olympics , how = "left" , on = ["City","Year"])
dataset = dataset[(dataset["NOC"] != "ROT") & (dataset["NOC"] != "UNK" )]

#handling nan values in age, height, and weight
mean = dataset.groupby(["Year" , "Sport"])[["Age" , "Height" , "Weight"]].mean()   
column = ["Age" , "Height" , "Weight"]
for item in column:
    for i in dataset.index:
        if str(dataset[item][i]) == "nan":
            dataset.loc[i , item] = mean[item][(dataset["Year"][i],dataset["Sport"][i])]
    

#dataset = dataset.iloc[]

sport_group = dataset.groupby("Sport")[["Height" , "Weight"]].mean()
for i in dataset.index:
    if str(dataset["Height"][i]) == "nan":
        dataset.loc[i,"Height"] = sport_group["Height"][dataset["Sport"][i]]
    if str(dataset["Weight"][i]) == "nan":
        dataset.loc[i,"Weight"] = sport_group["Weight"][dataset["Sport"][i]]

x = pd.read_csv("height_weight.csv") 
for i in dataset.index:
    if (str(dataset["Height"][i]) == "nan") & (dataset["region"][i] in x["Country"].values):
        dataset.loc[i,"Height"] = x["Median height, cm"][x.index[x["Country"] == dataset["region"][i]][0]]
    if (str(dataset["Weight"][i]) == "nan") & (dataset["region"][i] in x["Country"].values):
        dataset.loc[i,"Weight"] = x["Average weight"][x.index[x["Country"] == dataset["region"][i]][0]]
        
country_group = dataset.groupby("region")[["Height" , "Weight"]].mean()
for i in dataset.index:
    if str(dataset["Height"][i]) == "nan":
        dataset.loc[i,"Height"] = country_group["Height"][dataset["region"][i]]
    if str(dataset["Weight"][i]) == "nan":
        dataset.loc[i,"Weight"] = country_group["Weight"][dataset["region"][i]]
        
dataset["Age"] = dataset["Age"].astype(int)
dataset["Height"] = round(dataset["Height"],2)
dataset["Weight"] = round(dataset["Weight"],2)
dataset["Medal"] = dataset["Medal"].fillna("Loss")
dataset["Country"] =dataset["Country"].apply(lambda x: x.replace("\xa0",""))

        
'''
#sport = pd.read_csv("sports.csv")      
p = dataset.groupby(["Sport" , "Country"])["Weight"].mean().unstack()
q = dataset.groupby(["Sport" , "region"])["Height"].mean()

for i in dataset.index:
    if (str(dataset["Weight"][i]) == "nan") & (str(p[dataset["region"][i]][dataset["Sport"][i]]) != "nan"):
        dataset.loc[i,"Weight"] = p[dataset["region"][i]][dataset["Sport"][i]]
    if (str(dataset["Height"][i]) == "nan") & (str(q[dataset["region"][i]][dataset["Sport"][i]]) != "nan"):
        dataset.loc[i,"Height"] = q[dataset["region"][i]][dataset["Sport"][i]]
'''
