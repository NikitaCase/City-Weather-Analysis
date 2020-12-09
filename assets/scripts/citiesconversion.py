## This script converts the cities.csv file to an html table 

#import dependency
import pandas as pd 

#read csv into pandas 
cities_df = pd.read_csv('assets/Resources/cities.csv')

#convert to html
filepath = 'cities-table.html'
cities_df = cities_df.to_html(filepath)

