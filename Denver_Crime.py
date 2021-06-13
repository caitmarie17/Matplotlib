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

dir1 = "/Users/Cait/Desktop/Matplot/"
data_filename = "Denver Crime 2001-2013.csv"
data1= pd.read_csv(dir1+data_filename)
data1_head=data1.iloc[:9,:]



columns=list(data1.columns)
crime_counts=data1.sort_values(by=['2001'],ascending=True)
#print(type(crime_counts))
#print(crime_counts)
crime_year=crime_counts['2001']
#print(crime_year)
crimes=crime_counts['Type']
#print(crimes)
crime_counts.index=range(len(crime_counts))
#print(type(crimes))
#print(type(crime_counts))
fig, ax=plt.subplots(figsize=(6,8))
ax.bar(crimes, crime_year)
ax.set_title("Count of Denver Crimes by Crime Type: 2001")
ax.set_xlabel("Crime Type", fontsize=12)
ax.set_ylabel("Count")
ax.set_xticklabels(crimes,fontsize=7)
plt.tight_layout()
plot1_filename="Crimes2001.png"
fig.savefig(dir1+plot1_filename,dpi=dpi)


data2=data1
data2_head=data2.iloc[:9,:]
columns=list(data2.columns)
crime_counts=data2.sort_values(by=['2006'],ascending=True)
crime_year=crime_counts['2006']
crimes=crime_counts['Type']
crime_counts.index=range(len(crime_counts))
fig, ax=plt.subplots(figsize=(6,8))
ax.bar(crimes, crime_year)
ax.set_title("Count of Denver Crimes by Crime Type: 2006")
ax.set_xlabel("Crime Type")
ax.set_ylabel("Count")
ax.set_xticklabels(crimes,fontsize=7)
plt.tight_layout()
plot1_filename="Crimes2006.png"
fig.savefig(dir1+plot1_filename,dpi=dpi)

data3=data1
data3_head=data3.iloc[:9,:]
columns=list(data3.columns)
crime_counts=data3.sort_values(by=['2013'],ascending=True)
crime_year=crime_counts['2013']
crimes=crime_counts['Type']
crime_counts.index=range(len(crime_counts))
fig, ax=plt.subplots(figsize=(6,8))
ax.bar(crimes, crime_year)
ax.set_title("Count of Denver Crimes by Crime Type: 2013")
ax.set_xlabel("Crime Type")
ax.set_ylabel("Count")
ax.set_xticklabels(crimes,fontsize=7)
plt.tight_layout()
plot1_filename="Crimes2013.png"
fig.savefig(dir1+plot1_filename,dpi=dpi)

dir1 = "/Users/Cait/Desktop/Matplot/"
data2_filename = "Denver Crime 2.csv"
data4=pd.read_csv(dir1+data2_filename)
data4_head=data4.iloc[:14:]
columns=list(data4.columns)
labels=data4.iloc[:,1:]
x=data4['Year'].values
y=data4.iloc[:,1:]
fig, ax=plt.subplots(figsize=(12,8))
ax.axhline(0,xmin=2001,xmax=2013)
handles=ax.plot(x,y)
ax.set_title("Crimes in Denver 2001-2013")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Crimes")
ax.legend(handles,labels,loc="upper right", bbox_to_anchor=(1,1.05),ncol=2, fancybox=True, shadow=True)
plot4_filename="Crimes 2001 - 2013"
fig.savefig(dir1+plot4_filename,dpi=dpi)