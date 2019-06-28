import pandas as pd

#import data
dataset = pd.read_csv("New_Olympic_Data.csv")
olym = pd.read_csv("new_olym.csv")
#genrate dataframe corresponding value of any column is nan or not 
#data = mega_dataset["Country"].notna()

#crete summer and winter dataset seprately
winter = dataset[dataset["Season"]=="Winter"]
summer = dataset[dataset["Season"]=="Summer"]

def fun(item):
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
        return "Unknown"           
summer["Category"] = summer["Sport"].apply(fun)

