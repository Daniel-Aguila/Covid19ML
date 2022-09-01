from xml.etree.ElementInclude import include


import tensorflow as tf
import pandas as pd
import numpy as np

#open dataset
dataset = pd.read_csv("covid-data.csv")
print(dataset.head())
print(dataset.shape) #we have 213096 rows with 67 features
print(dataset.columns.tolist())