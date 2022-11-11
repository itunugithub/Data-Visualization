# Trip Pattern of Users in the Ford GoBike System
## by Itunu Agbokeye


## Dataset

The fordgobike data set includes information about individual rides made in a bike-sharing system covering the greater San Francisco Bay Area.
The raw dataset contains 183412 rows and 16 columns. However, following the data cleaning process the date set became 174952 distinct rows and 29 features some of which include: duration sec, start time, end time, start station id, start station name, start station latitude, start station longitude, end station id, end station name, end station latitude, end station longitude, bike id, user type, member birth year, member gender, bike share for all trip, duration min, duration hr.
The main features of interest are trip period, Usertype, gender, age, Bike share for all trips.Some transformation was done such as changing data types where apllicable, converting duration_sec to minutes and hour, converting the start_time and end_time to year, month, week, day and hours. This was done to make the analysis seamless



## Summary of Findings

The exploration process of fordgobike data set gives an overview of the lifestyle and preference of users in the system. The Fordgobike 
system consist of different users (the subscribers and the customers) of different genders; male , female and others.  While a higher percentage of users are subscribers, the majority of users are also male. This was visually represented by a bar chart

For the trip periods,Tuesdays and Thursdays recorded higher number of daily trips while Saturday and Sundays recorded lesser trips. The majority of trips were made between the 8th and 17th hours. A significant number of trips were also made during the 7th, 9th, 16th, and 18th hours. Most trips last between 5 and 10 minutes, with the more trip at 7 minutes.



## Key Insights for Presentation

I started by looking at the distribution of the main variable of interest, then went further to investigate relationships between different variables by representing them visually. Below are some key insight generated

- Most of the Subscribers take more of work trips from Mondays to Friday because their peak periods are mornings when going to work between the hours of 7-9 and evenings when returning between the hours of 16 - 19. Customers take more of weekend trip due to the day and period.
- The age distribution of the data set shows that 33 years is the dominant age while the mean age is 37 years.
- Majority of trips taken lasted for 5 to 10 minutes
- The most dominant age is 33 years while the mean age is 37 years.
- The bike share for all trips reveals that the majority of the rides were not shared.

