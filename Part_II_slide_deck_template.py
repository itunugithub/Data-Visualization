#!/usr/bin/env python
# coding: utf-8

# # Part II - Trip Pattern of Users in the Ford GoBike System
# ## by Itunu Agbokeye

# ## Investigation Overview
# 
# 
# The objective of investigating this data set  is to examine the trip pattern of users in the Fordgobike  System. The main features of interest are trip period, Usertype, gender, age, Bike share for all trips.
# 
# 
# 
# ## Dataset Overview
# 
# The Fordgoike raw dataset contains 183412 rows and 16 columns. However, following the data cleaning process the date set became 174952 distinct rows and 29 features which include: duration sec, start time, end time, start station id, start station name, start station latitude, start station longitude, end station id, end station name, end station latitude, end station longitude, bike id, user type, member birth year, member gender, bike share for all trip, duration min, duration hr, start time Y, start time M, start time W, start time D, end time Y, end time M, end time W, end time D

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches
import datetime as dt
from datetime import date

get_ipython().run_line_magic('matplotlib', 'inline')

# suppress warnings from final output
import warnings
warnings.simplefilter("ignore")


# In[3]:


# load in the dataset into a pandas dataframe
Ford_df = pd.read_csv('201902-fordgobike-tripdata.csv')

Ford_df.head()

Ford_df.isnull().sum()
# In[4]:


Ford_df.dropna(inplace = True)


# In[5]:


Ford_df['start_time'] = pd.to_datetime(Ford_df['start_time'])
Ford_df['end_time'] = pd.to_datetime(Ford_df['end_time'])
Ford_df['start_station_id'] = Ford_df['start_station_id'].astype(str)
Ford_df['end_station_id'] = Ford_df['end_station_id'].astype(str)
Ford_df['bike_id'] = Ford_df['bike_id'].astype(str)
Ford_df['member_birth_year'] = Ford_df['member_birth_year'].round(0)
Ford_df['member_birth_year'] = Ford_df['member_birth_year'].astype(int)


# In[6]:


Ford_df['duration_min'] = Ford_df['duration_sec']/60
Ford_df['duration_hr'] = Ford_df['duration_sec']/3600
Ford_df['duration_min'] = Ford_df['duration_min'].astype(int)
Ford_df['duration_hr']= Ford_df['duration_hr'].astype(float).round(2)


# In[7]:


Ford_df['start_time_Y'] = Ford_df.start_time.dt.strftime('%Y');
Ford_df['start_time_M'] = Ford_df.start_time.dt.strftime('%B');
Ford_df['start_time_W'] = Ford_df.start_time.dt.strftime('%W');
Ford_df['start_time_D'] = Ford_df.start_time.dt.strftime('%A');
Ford_df['start_time_H'] = Ford_df.start_time.dt.hour
Ford_df['end_time_Y'] = Ford_df.end_time.dt.strftime('%Y');
Ford_df['end_time_M'] = Ford_df.end_time.dt.strftime('%B');
Ford_df['end_time_W'] = Ford_df.end_time.dt.strftime('%W');
Ford_df['end_time_D'] = Ford_df.end_time.dt.strftime('%A');
Ford_df['end_time_H'] = Ford_df.end_time.dt.hour


# In[8]:


current_year = date.today().year
Ford_df = Ford_df.assign(age=lambda x: current_year - x.member_birth_year)
Ford_df.age = Ford_df.age.astype(int)


# In[9]:


Ford_df.info()
Ford_df.shape


# > Note that the above cells have been set as "Skip"-type slides. That means
# that when the notebook is rendered as http slides, those cells won't show up.

# ## User Type Distribution
# There are two categories of users in the Fordgobike system (Subscribers and Customers). However, analysis showed that there are more subscribers than customers.
# 

# In[10]:


plt.figure(figsize=(5,5))
plt.title("User Type Distribution", y=1.05, fontsize=14, fontweight ='bold')
sns.countplot(data=Ford_df,x='user_type', color=sns.color_palette()[0])
plt.xlabel('Users', fontsize=12, color = 'darkblue')
plt.ylabel('Count of Users', fontsize=12, color = 'darkblue')
plt.show()


# # Gender Distribution
# The distibution shows that there are three categories of genders (Male, Female, Others). The male gender is the most dominant in the system.

# In[11]:


plt.figure(figsize=(5,5))
plt.title("Gender Distribution", y=1.05, fontsize=14, fontweight ='bold')
gender = ['Male', 'Female', 'Other']
sns.countplot(data=Ford_df,x='member_gender', color=sns.color_palette()[0], order = gender)
plt.xlabel('Gender',fontsize=12, color = 'darkblue')
plt.ylabel('Count',fontsize=12, color = 'darkblue');


# ## Trip Duration Distribution
# 
# The analysis of the Fordgobike system, shows that most of the trips taken last for 5 to 10 minutes, However the highest trip count last for 7 minutes

# In[12]:


binsize = 2
bins = np.arange(0,Ford_df['age'].max()+binsize, binsize)
plt.figure(figsize=(10,5))
plt.title('Trip Duration Distribution', y=1.05, fontsize=14, fontweight ='bold')
plt.hist(data=Ford_df, x= 'duration_min', bins=bins)
plt.xlabel('Duration(min)', fontsize=12, color = 'darkblue')
plt.ylabel('Trip Count', fontsize=12, color = 'darkblue')
plt.xticks([5,10,15,20,25,30,35,40,45,50])
plt.show()


# ## Age Distribution
# 
# The age distribution of the data set shows that 33 years is the dominant age while the mean age is 37 years.
# 
# 

# In[13]:


binsize = 5
bins = np.arange(0,Ford_df['age'].max()+binsize, binsize)
plt.figure(figsize=(10,5))
plt.title("Age Distribution of Riders", y=1.05, fontsize=14, fontweight ='bold')
plt.hist(x ='age',data=Ford_df, bins=bins)
plt.xlabel("Rider's Age", fontsize=12, color = 'darkblue')
plt.ylabel('Trip Count', fontsize=12, color = 'darkblue')
plt.xticks([10,20,30,40,50,60,70,80,90,100])
plt.show()


# ## User Type/ Trip Distribution
# 
# From the user type/trip distribution, it can be concluded that Thursdays and Tuesdays recorded higher number of daily trips while Saturday and Sundays recorded lesser trips.
# The subscriber make very low trips on Saturdays and Sundays, they make most of their tripson Monday to Friday and the peak periods are mornings between the hours of 7-9 and evenings between the hours of 16 - 19. For customers, they make trips all the days of the week, however we can deduce that they make more weekend trips betweeen the hours of 10 - 15. On Mondays to Fridays trips are significant in the morning at 8 and in the evening at the 17th hour

# In[14]:


plt.figure(figsize=(10,5))
plt.subplot(2,1,1)
plt.suptitle('User Type/Trip Period Distribution', y=1.05, fontsize=14, fontweight ='bold')
subscriber_data = Ford_df.query('user_type == "Subscriber"')
subscriber = subscriber_data.groupby(['start_time_D', 'start_time_H']).size().reset_index(name='count').pivot(index='start_time_D', columns ='start_time_H', values = 'count')
sns.heatmap(subscriber, cmap = 'magma_r')
plt.xlabel('Hours', fontsize=12, color = 'darkblue')
plt.ylabel('Week', fontsize=12, color = 'darkblue')
plt.title('Subscriber')


plt.figure(figsize=(10,5))
plt.subplot(2,1,1)
customer_data = Ford_df.query('user_type == "Customer"')
customer = customer_data.groupby(['start_time_D', 'start_time_H']).size().reset_index(name='count').pivot(index='start_time_D', columns ='start_time_H', values = 'count')
sns.heatmap(customer, cmap = 'magma_r')
plt.xlabel('Hours', fontsize=12, color = 'darkblue')
plt.ylabel('Week', fontsize=12, color = 'darkblue')
plt.title('Customer')
plt.show()

### Generate Slideshow
Once you're ready to generate your slideshow, use the `jupyter nbconvert` command to generate the HTML slide show.  !jupyter nbconvert Part_II_slide_deck_template.ipynb --to slides --post serve
# In[ ]:


# Use this command if you are running this file in local
get_ipython().system('jupyter nbconvert Part_II_slide_deck_template.ipynb --to slides --post serve --no-input --no-prompt')


# > In the classroom workspace, the generated HTML slideshow will be placed in the home folder. 
# 
# > In local machines, the command above should open a tab in your web browser where you can scroll through your presentation. Sub-slides can be accessed by pressing 'down' when viewing its parent slide. Make sure you remove all of the quote-formatted guide notes like this one before you finish your presentation! At last, you can stop the Kernel. 

# ### Submission
# If you are using classroom workspace, you can choose from the following two ways of submission:
# 
# 1. **Submit from the workspace**. Make sure you have removed the example project from the /home/workspace directory. You must submit the following files:
#    - Part_I_notebook.ipynb
#    - Part_I_notebook.html or pdf
#    - Part_II_notebook.ipynb
#    - Part_I_slides.html
#    - README.md
#    - dataset (optional)
# 
# 
# 2. **Submit a zip file on the last page of this project lesson**. In this case, open the Jupyter terminal and run the command below to generate a ZIP file. 
# ```bash
# zip -r my_project.zip .
# ```
# The command abobve will ZIP every file present in your /home/workspace directory. Next, you can download the zip to your local, and follow the instructions on the last page of this project lesson.
# 

# In[ ]:




