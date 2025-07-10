#!/usr/bin/env python
# coding: utf-8

# In[280]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



data = pd.read_csv(r"C:\Users\KimKa\Desktop\Data Projects\Trending Movies Data Project\Trending_Movies.csv")
data.head(10)
#All necessery imports and reading the first 10 lines of the data


# In[281]:


data.drop_duplicates(subset='title',inplace=True)
#dropping any duplicate movies based on the title


# In[282]:


data.info()
#checking for null values and inaccurate datatypes


# In[283]:


data['release_date']=pd.to_datetime(data['release_date'])
data.info()
#converted 'release_date' column from object datatype to datetime


# In[284]:


data= data[data['release_date']<='2025-09-07']
#filtered data to only show movies that have already been released as of 09/07/2025


# In[285]:


data.drop(columns=['original_title','overview'],inplace=True)
#removed the 'original_title' column and the 'overview' column


# In[286]:


data.dropna(subset='release_date',inplace=True)
data.isnull().sum()
#removed all rows with no release date and checked to see if there are any other empty entries within the other columns


# In[287]:


data[data['vote_count']>=1000].sort_values(by='vote_average', ascending=False).head(10)
#displayed the movies with more than 1000 votes(Engagement) that had highest voting average(Rating)


# In[288]:


breakdown= data['original_language'].value_counts().to_dict()
print(breakdown)
#grouped movies according to their language and counted them to see if any language other than english stands out


# In[289]:


def get_season(month):
    if month in [12,1,2]:
        return 'Winter'
    elif month in [3,4,5]:
        return 'Spring'
    elif month in [6,7,8]:
        return 'Summer'
    else:
        return 'Fall'
#Created a function that grouped movies into a certain season based on their release month

data['season']=data['release_date'].dt.month.map(get_season)

#Got the release months of the movies and executed the function using map() then created a new column that stores the season of a movie 




# In[329]:


seasonalAveragePopularity=data.groupby(data['season'])['popularity'].median().sort_values(ascending=False)
seasonalAveragePopularity.plot(kind='line',ylabel='Average Popularity', xlabel='Season',title='Average Popularity Score Per Season')
plt.show()

#Grouped the movies based on their release season and returned the median popularity of movies in each season then plotted it on a line graph 


# In[291]:


seasonalVoteAverage = data.groupby(data['season'])['vote_average'].mean().sort_values(ascending=False)
seasonalVoteAverage.plot(kind='line',ylabel='Vote Average',xlabel='Season',title='Vote Average Per Season')
plt.show()

#Grouped the movies based on their release season and returned the average rating of movies in each season then plotted it on a line graph 


# In[292]:


seasonalVoteAverage = data.groupby(data['season'])['vote_count'].median().sort_values(ascending=False)
seasonalVoteAverage.plot(kind='line',ylabel='Average Vote Count',xlabel='Season',title='Average Votes Per Season')
plt.show()

#Grouped the movies based on their release season and returned the median number of votes for movies in each season then plotted it on a line graph 


# In[293]:


popularMovies=data[data['popularity']>=200]
flaggedMovies=popularMovies[popularMovies['vote_count']<1000]
flaggedMovies
#Got a list of 'highly popular' movies with a low level of engagement


# In[294]:


def movie_era(year):
    if 1900 <= year <= 1930:
        return 'Silent Era'
    elif 1930 <= year <= 1960:
        return 'Golden Age'
    elif 1960 <= year <= 1980:
        return 'New Hollywood'
    elif 1980 <= year <= 2010:
        return 'Blockbuster Era'
    else: return 'Modern Era'
#Created a function that grouped movies into a certain era based on their release year

data['Era']=data['release_date'].dt.year.map(movie_era)
#Got the release year of the movies and executed the function using map() then created a new column that stores the era of a movie 
data
    


# In[295]:


data['year'] = data['release_date'].dt.year
plt.figure(figsize=(12, 6))
plt.scatter(data['year'], data['popularity'], alpha=0.4, s=10)
plt.title('Popularity vs. Release Year')
plt.xlabel('Release Year')
plt.ylabel('Popularity')
plt.grid(True)
plt.tight_layout()
plt.show()
#Checked to see if any old movies still stand out in terms of popularity in comparison with movies in other eras using a scatterplot


# In[296]:


data.loc[(data['release_date'].dt.year == 1940) & (data['popularity'] > 200), ['title','popularity']]
#Found the old movie that stood out on the scatterplot


# In[297]:


avgPopularity = data.groupby(data['Era'])['popularity'].median().sort_values(ascending=False)
avgPopularity.plot(kind='bar', xlabel='Era', ylabel='Average Popularity', title='Average Popularity Per Era')
plt.show()
#Created a bar graph that shows the average popularity of the different eras


# In[298]:


avgPopularity = data.groupby(data['Era'])['vote_count'].median().sort_values(ascending=False)
avgPopularity.plot(kind='bar', xlabel='Era', ylabel='Average Vote Count', title='Average Engagement Per Era')
plt.show()
#Created a bar graphs that shows the amount of engagement in different eras


# In[330]:


avgPopularity = data.groupby(data['Era'])['vote_average'].mean().sort_values(ascending=False)
avgPopularity.plot(kind='bar', xlabel='Era', ylabel='Vote Average ', title='Average Movie Ratings Per Era')
plt.show()
#Created a bar graphs that shows the average ratings in different eras


# In[325]:


data[['popularity','vote_average','vote_count']].corr()
#Checked the correlation between popularity, rating and engagement

