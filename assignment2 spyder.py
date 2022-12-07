# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 10:53:24 2022

@author: HP
"""
#Importing pandas package to read the file,for deriving pandas features and stats properties
import pandas as pd
#Importing numpy to read statistical properties
import numpy as np
#Importing matplotlib package for data plotting and visualization
import matplotlib.pyplot as plt
#Importing scipy functions to calculate skewnwss and kurtoisis
import scipy.stats as st


#defining function to produce two dataframes,one with countries as columns and one with years as coulmns
def readcsv(input_file,countries):
    data = pd.read_csv(input_file)
    #replacing the null values with zeroes using fillna() method
    dropping_values = data.fillna(0) 
    test = dropping_values[dropping_values['Country Name'].isin(countries)]
    df_countries = pd.DataFrame(test)
    print(df_countries)
    #transposing data to derive dataframe with years as columns
    transpose=pd.DataFrame.transpose(test)
    header = transpose.iloc[0].values.tolist()
    transpose.columns = header
    transpose = transpose.iloc[0:]
    df_years = transpose
    print(transpose)
    return df_countries,df_years


#calling the function to produce two dataframes by choosing few countries
df_co,df_yr=readcsv('API_19_DS2_en_csv_v2_4700503-Copy.csv',['Belgium','Bulgaria','Colombia','Finland','United Kingdom'])

#Deriving statistical properties
#using pandas describe function to derive statistical properties
print('Describe\n',df_yr.iloc[4:,10:20].describe())

#Calculating mean using numpy
print('Mean\n', np.mean(df_yr.iloc[4:,10:20]))

#Calculating standard deviation using numpy
print('standard Deviation\n' ,np.std(df_yr.iloc[4:,10:20]))

#Calculating kurtosis using scipy.stats 
print('Kurtosis',st.kurtosis(df_co.iloc[4,4:]))

#Calculating skewness using scipy.stats                                                                                                                                                                                                                                                                                                                                                                                                             
print('skewness',st.skew(df_co.iloc[4,4:]))

#Calculating correlation between indicators from 1966-1970 
correlation = df_co.iloc[4:,10:15]
print() #printing space
print('Pearson Correlation \n',correlation.corr())
print()
#defining correlation using kendall method
print('Kendall Correlation \n',correlation.corr(method='kendall'))
