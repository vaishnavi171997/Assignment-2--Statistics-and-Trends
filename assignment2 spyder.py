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

#Calculating and comparing statistical properties for five different countries comparing different indicators

#using pandas describe function to calculate statistical properties for five countries
print("\nCalculating describe of Methane emissions (% change from 1990) for five different countries")
print('\nDescribe\n',df_yr.iloc[4:,[31,107,183,259,335]].describe())

#Calculating mean using numpy for five countries
print("\nCalculating mean of Methane emissions (% change from 1990) for five different countries")
print('\nMean\n', np.mean(df_yr.iloc[4:,[31,107,183,259,335]]))

#Calculating standard deviation using numpy for five countries
print("\nCalculating Standard Deviation of Methane emissions (% change from 1990) for five different countries")
print('\nstandard Deviation\n' ,np.std(df_yr.iloc[4:,[31,107,183,259,335]]))

print("\nCalculating Kurtosis of population growth (annual %) indicator for three countries")

#Calculating kurtosis using scipy.stats for Belgium
print('\nKurtosis of Belgium :',st.kurtosis(df_co.iloc[4,4:]))

#Calculating kurtosis using scipy.stats for Bulgaria
print('Kurtosis of Bulgaria :',st.kurtosis(df_co.iloc[100,4:]))

#Calculating kurtosis using scipy.stats for Colombia
print('Kurtosis of Colombia :',st.kurtosis(df_co.iloc[200,4:]))

print("\nCalculating Skewness of population growth (annual %) indicator for three countries") 
#Calculating skewness using scipy.stats for Belgium                                                                                                                                                                                                                                                                                                                                                                                                          
print('\nskewness of Belgium :',st.skew(df_co.iloc[4,4:]))

#Calculating skewness using scipy.stats for Bulgaria                                                                                                                                                                                                                                                                                                                                                                                                            
print('skewness of Bulgaria :',st.skew(df_co.iloc[100,4:]))

#Calculating skewness using scipy.stats for Colombia                                                                                                                                                                                                                                                                                                                                                                                                          
print('skewness of colombia :',st.skew(df_co.iloc[200,4:]))

#Calculating correlation between indicators from 1966-1970 
correlation = df_co.iloc[4:,10:15]
print() #printing space
print('Pearson Correlation \n',correlation.corr())
print()
#defining correlation using kendall method
print('Kendall Correlation \n',correlation.corr(method='kendall'))

#Plotting line graph of average Methane Emission for five countries 
plt.figure(figsize=(40,40))
plt.rcParams.update({'font.size':60})
plt.plot(np.mean(df_yr.iloc[4:,[31,107,183,259,335]]),label='Methane emission',linewidth=20)
plt.xlabel('\nCountries',fontsize=60)
plt.ylabel('\nMean of Methane emissions (% change from 1990)',fontsize=60)
plt.title('Average Methane emission of five countries',fontsize=70)
plt.legend()
plt.show()

#plotting the line graph between two indicators:Co2 emissions from solid fuel consumption
#and Co2 emissions from liquid fuel consumption over the years
plt.figure(figsize=(10,8))
plt.rcParams.update({'font.size':17})
plt.plot(df_co.iloc[37,20:30],label='Co2 emissions from solid fuel consumption (% of total)',color='red',linewidth=3)
plt.plot(df_co.iloc[42,20:30],label='Co2 emissions from liquid fuel consumption (% of total)',color='blue',linewidth=3)
plt.xlabel('Years',fontsize=15)
plt.ylabel('Co2 emission Percentage',fontsize=15)
plt.title('Co2 emission over years for Belgium',fontsize=20)
plt.legend(fontsize=10,loc ='upper right')
plt.show()


#plotting pie chart of electric power consumption over the years(1976-1985)
plt.figure(figsize=(30,30))
plt.rcParams.update({'font.size':34})
years = ['1976','1977','1978','1979','1980','1981','1982','1983','1984','1985']
plt.pie(df_co.iloc[50,20:30],labels=years,autopct='%1.1f%%')
plt.legend(loc = 'upper right')
plt.title('Electric power consumption (kWh per capita)',fontsize=55)
plt.show()

#plotting graph of Energy use (kg of oil equivalent per capita)for five countries
plt.figure(figsize=(40,40))
plt.rcParams.update({'font.size':50})
plt.plot(df_co.iloc[50,20:25],label='Belgium',linewidth=15)
plt.plot(df_co.iloc[126,20:25],label='Bulgaria',linewidth=15)
plt.plot(df_co.iloc[202,20:25],label='Colombia',linewidth=15)
plt.plot(df_co.iloc[278,20:25],label='Finland',linewidth=15)
plt.plot(df_co.iloc[354,20:25],label='United Kingdom',linewidth=15)
plt.xlabel('\nYears',fontsize=65)
plt.ylabel('\nEnergy use (kg of oil equivalent per capita)',fontsize=65)
plt.title('\nEnergy use (kg of oil equivalent per capita)',fontsize=65)
plt.legend()
plt.show()
