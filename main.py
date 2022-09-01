from cProfile import label
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
def missingData(dataset):
    return dataset.isnull().sum()
missing_data_values = missingData(dataset=dataset)

print("Missing data\n", missing_data_values)

#percentage of missing data
def missingDataPercentage(dataset):
    total_cells = np.product(dataset.shape)
    total_missing = missing_data_values.sum()   
    return round((total_missing/total_cells)*100,2)

missing_data_percentage = missingDataPercentage(dataset=dataset)
print("Percentage of missing data: " + str(missing_data_percentage) + "%")

#pi plot of missing data...for drama 
def piePlotMissingData(dataset):
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
print(dataset['location'].unique()) #shows all the unique values

location_dictionary_replacement = {
    'Afghanistan': 0,
}
#since there is no location missing, we can drop the continent column as location is more specific and is still able to give data on
#geographical location
#dataset = dataset.drop(columns=['continent'])

#moving on to date column
print(dataset['date'].dtype) # shows it is an object

print(dataset[dataset['location'] == 'Africa'])