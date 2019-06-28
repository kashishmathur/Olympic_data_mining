# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 18:58:06 2019

@author: Lakshya
"""


import pandas as pd

dataset = pd.read_csv("dataset.csv")
olympics = pd.read_csv("new_olympic.csv")

'''dividing the athleter dataset into summer and winter season'''
summer = dataset[dataset["Season"] == "Summer"]
winter = dataset[dataset["Season"] == "Winter"]


