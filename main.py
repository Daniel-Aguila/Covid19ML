import string
import tensorflow as tf
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)  

#open dataset
dataset = pd.read_csv("covid-data.csv")
print(dataset.head())
print(dataset.shape) #we have 213096 rows with 67 features
print(dataset.columns.tolist(), "\n") #list the features
#number of missing data
def missingData():
    return dataset.isnull().sum()
missing_data_values = missingData()

#print("Missing data\n", missing_data_values)

#percentage of missing data
def missingDataPercentage():
    total_cells = np.product(dataset.shape)
    total_missing = missing_data_values.sum()   
    return round((total_missing/total_cells)*100,2)

missing_data_percentage = missingDataPercentage()
print("Percentage of missing data: " + str(missing_data_percentage) + "%")

#pi plot of missing data...for drama 
def piePlotMissingData():
    total_cells = np.product(dataset.shape)
    total_missing = missing_data_values.sum()  
    labels = ['Missing','Total']
    data = [total_missing,total_cells]
    colors = sns.color_palette("hls", 8)
    plt.pie(data,labels=labels, colors=colors,autopct='%.0f%%')
    plt.show()

                            #ANALYZE THE DATA AND ... JUST LOOK AT IT

#iso_code will be possibly drop as it is easier to read location and it provides the same information
#print(dataset['iso_code'][0:10]) #ISO gives AFG as a code for Afghanistan
#print(dataset['location'].unique()) #shows all the unique values

#iso_code is also dropped since location is enough for geographical location
dataset = dataset.drop(columns=['iso_code'])

print(dataset['continent'].unique())
dataset['continent'] = dataset['continent'].fillna(dataset['location']) #A lot of continents that were "NaN" was because 
#the location was used as the continent, so we just switched over the location to the continent data

#moving on to date column
print(dataset['date'].dtype) # shows it is an object, we need it as a date type
print(len(dataset['date'].unique())) #shows that at the time of writing the code Sept 1st, the days since the data was written shows
#974 days, and the length of the unique values is 974 days. After checking all 974 date entries. They follow the same format even though
#it is object, so this makes it switching to date type on pandas easier.
dataset['date'] = pd.to_datetime(dataset['date'],format="%Y-%m-%d")
print(dataset['date'].dtype) #now we have a datetime64 type and not an object type

#Graphic visuals of countries in respect to total_cases to date
def TrackFeatureByCountryGraph(country: string, track_feature: string):
    gk = dataset.groupby("location")
    gk = gk.get_group(country)
    plt.xlabel("Date")
    plt.ylabel(track_feature)
    plt.title(country + "'s total number of Covid19 " + track_feature + " over time")
    plt.grid(True)
    plt.fill_between(gk['date'],gk[track_feature])
    plt.show()
TrackFeatureByCountryGraph('Mexico','total_deaths') #type whatever country you want
missing_data_values = missingData()
print(missing_data_values)

dataset = dataset.drop(920) #dropped the index (920) for location Africa, since the first case of covid19 in africa was not the 13th of february 2020, but the 14th
#and so a lot of the data was missing for the row[s] since data was not being collected

total_Cases_is_null = dataset.loc[dataset['total_cases'].isnull()]
print(total_Cases_is_null.head())

#change location from quantative to numerical values
def QuantativeToNumerical(feature: string, dataset):
    dictionary_replacement_value = {}
    for index, value in enumerate(dataset[feature].unique()):
        dictionary_replacement_value[value] = index
    dataset[feature] = dataset[feature].replace(dictionary_replacement_value)
    return dataset

#QuantativeToNumerical is a slow function (Might be better to create the dictionary list on one's own)
#dataset = QuantativeToNumerical("location",dataset) #while we work on the data base it is easier to not change them to numerical values yet
