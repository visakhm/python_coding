# Data analysis using python 
# starting with some examples to understand how and what type of analysis can be done with the data
# The same example can be found some where else as well, can be a copy
# This is just to share some knowledge. 

# Analysis example - Diabetes data from kaggle ( example can be found on a page - towardsdatascience(tds)
#https://towardsdatascience.com/a-beginners-guide-to-data-analysis-in-python-188706df5447)

# We will try to see how the example code given works and try to come up with some more analysis as well. 

# import necessary libraries for python like reading the data, creating data frames etc. 

import pandas as pd



# read the data and create a data frame 
# we will try to do that dynamically meaning, the user can give a location of his choice to the variable below and then load the data , create a df

path = 'location'
df = pd.read_csv(path)


