# Covid19ML

The goal of this project is that using the data for covid for the past 2 years. We can use a regression model to predict how many new number of deaths in future dates

## Data used
The data that is being use for this project comes from [Our World in Data](https://github.com/owid/covid-19-data/tree/master/public/data).

## Looking into the dataset
We can see that 45% of the data gathered is missing. We can see which features have the most data missing in the second image below.

(Pie graph showing how much of the total data is missing)
![alt text](https://github.com/Daniel-Aguila/Covid19ML/blob/main/Assets/missing_data/MissingDataPieGraph.png)

(Bar graphs showing how many values per feature is missing in numerical terms)
![alt text](https://github.com/Daniel-Aguila/Covid19ML/blob/main/Assets/missing_data/missingDataByFeature.png)

(This image shows how much percentage is missing per feature. How to read: "a xx.xx" is read as "xx.xx%". First part)
![alt text](https://github.com/Daniel-Aguila/Covid19ML/blob/main/Assets/missing_data/missingDataPerFeature_1.png)

(This image shows how much percentage is missing per feature. Second part)
![alt text](https://github.com/Daniel-Aguila/Covid19ML/blob/main/Assets/missing_data/missingDataPerFeature_2.png)

### Starting to clean the data

#### Continent feature
I noticed that all the data that was missing from the continent feature, was because the continent data was being used for 'location' in those rows. So I transfered the data that was in 'location' to fill the continent data which solved that issue. For example: Some features had 'location' listed as 'Africa', while having the 'continent' feature column with NaN.
#### Excess_mortality and related features
The excess_mortality features are interesting to look at as most of their information in all 213k of the data gather is either missing or could be classify as invalid due to how countries go about reporting it. According to [Our World in Data excess mortality explanation](https://github.com/owid/covid-19-data/tree/master/public/data/excess_mortality) A lot of countries in the lower to middle income don't really report their deaths, and even in the richer countries that do report deaths, a lot of them can be inaccurate on their respective date. Deaths can happen at a completely different time then the one listed. For this reason, the four features which have 96.6% of data missing will be deleted 
'excess_mortality_cumulative_absolute','excess_mortality_cumulative','excess_mortality','excess_mortality_cumulative_per_million' will be dropped from the dataset.
