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

data2= pd.read_csv(dir1+data_filename)
data2_head=data2.iloc[:9,:]
columns=list(data2.columns)
crime_counts=data2['2006']
crimes=data2['Type']
crime_counts.index=range(len(crime_counts))
fig, ax=plt.subplots(figsize=(6,8))
ax.bar(crimes, crime_counts)
ax.set_title("Crimes in Denver 2006")
ax.set_xlabel("Crime")
ax.set_ylabel("Crime Count")
ax.set_xticklabels(crimes,fontsize=7)
plt.tight_layout()
plot1_filename="Crimes2006.png"
fig.savefig(dir1+plot1_filename,dpi=dpi)

data3= pd.read_csv(dir1+data_filename)
data3_head=data3.iloc[:9,:]
columns=list(data3.columns)
crime_counts=data3['2013']
crimes=data3['Type']
crime_counts.index=range(len(crime_counts))
fig, ax=plt.subplots(figsize=(6,8))
ax.bar(crimes, crime_counts)
ax.set_title("Crimes in Denver 2013")
ax.set_xlabel("Crime")
ax.set_ylabel("Crime Count")
ax.set_xticklabels(crimes,fontsize=7)
plt.tight_layout()
plot1_filename="Crimes2013.png"
fig.savefig(dir1+plot1_filename,dpi=dpi)

dir1 = "/Users/Cait/Desktop/Matplot/"
data2_filename = "Denver Crime 2.csv"
df1=pd.read_csv(dir1+data2_filename)
df1_head=df1.iloc[:14:]
columns=list(df1.columns)
labels=df1.iloc[:,1:]
x=df1['Year'].values
y=df1.iloc[:,1:]
fig, ax=plt.subplots(figsize=(8,12))
ax.axhline(0,xmin=2001,xmax=2013)
handles=ax.plot(x,y)
ax.set_title("Crimes in Denver 2001-2013")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Crimes")
ax.legend(handles,labels,loc="upper right")
plot4_filename="Crimes 2001 - 2013"
fig.savefig(dir1+plot4_filename,dpi=dpi)
 