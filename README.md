# Covid19ML

The goal of this project is that using the data for covid for the past 2 years. We can use a regression model to predict how many new number of deaths in future dates

## Data used
The data that is being use for this project comes from [Our World in Data](https://github.com/owid/covid-19-data/tree/master/public/data).

## Looking into the dataset
We can see that 45% of the data gathered is missing. We can see which features have the most data missing in the second image below.

![alt text](https://github.com/Daniel-Aguila/Covid19ML/blob/main/Assets/missing_data/MissingDataPieGraph.png)![alt text](https://github.com/Daniel-Aguila/Covid19ML/blob/main/Assets/missing_data/missingDataByFeature.png)

### Starting to clean the data

#### Continent feature
I noticed that all the data that was missing from the continent feature, was because the continent data was being used for 'location' in those rows. So I transfered the data that was in 'location' to fill the continent data which solved that issue. For example: Some features had 'location' listed as 'Africa', while having the 'continent' feature column with NaN.
