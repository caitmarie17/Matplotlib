#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 12:38:15 2021

@author: Cait
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
dpi = 300

#f = open("/Users/Cait/Desktop/Matplot/Denver Crime 2001-2013.csv","r")
dir1 = "/Users/Cait/Desktop/Matplot/"
data_filename = "Denver Crime 2001-2013.csv"
data1= pd.read_csv(dir1+data_filename)
data1_head=data1.iloc[:9,:]
columns=list(data1.columns)
crime_counts=data1['2001']
crimes=data1['Type']
crime_counts.index=range(len(crime_counts))
fig, ax=plt.subplots(figsize=(6,8))
ax.bar(crimes, crime_counts)
ax.set_title("Crimes in Denver 2001")
ax.set_xlabel("Crime")
ax.set_ylabel("Crime Count")
ax.set_xticklabels(crimes,fontsize=7)
plt.tight_layout()
plot1_filename="Crimes2001.png"
fig.savefig(dir1+plot1_filename,dpi=dpi)

