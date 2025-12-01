# NYPD_Crime_Analysis

### Exploring predictive modeling concepts on 4 massive datasets sourced from the New York Police Department, available at https://www1.nyc.gov/site/nypd/stats/crime-statistics/citywide-crime-stats.page (files way too large to upload here).
### I have penned a complete breakdown of this project on my [personal website](https://sites.google.com/view/sachinvs/project_nypd_crime_analysis), showcasing my insights, applied procedures, and results.

### TL;DR:
#### 1. For the arrests dataset (~5.15 million rows by 19 columns), I wrote simple functions to quickly locate and visualize (using Folium) where arrests were made, based on custom factors. For example, all criminal trespasses relevant to Brooklyn below.
#### 2. For the shooting incidents dataset (~23,000 rows by 19 columns), I applied clustering to geocode latitude and longitude coordinate attributes into zones using k-means. I then split shooting date and timestamp attributes into different variables. Finally, I applied LightGBM classification to estimate the risk of a shooting incident resulting in victim death. Key LightGBM features are below: Test accuracy: 78%, with an unexpectedly decent F1-score of 63% without any hyperparameter tuning or probability threshold checks.
#### 3. For the complaints dataset (7.38 million rows by 35 columns), I explored deep learning with ConvLSTM2D to predict where and when future complaints might occur, focusing on spatial-temporal patterns to estimate complaints. Test accuracy achieved: 93%. Examples of ground truth and predictions are provided below.
#### 4. For the criminal court summons dataset (~ 5 million rows by 17 columns), I employed pivot table concepts to visualize which laws were violated the most over time in New York City from 2006 to 2020, creating a bar chart race.


1. Arrests: 
![Folium Viz](/Capture_folium.PNG "Screenshot")
2. Shooting incidents: 
![LightGBM features](/lgbm_importances_shootings.jpg "Screenshot")
3. Complaints:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; ![Ground truth](/download.png "Screenshot") &emsp; 

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; ![Prediction](/download_p.png "Screenshot") &emsp; 

5. Summons: 
Link to bar chart race: https://sites.google.com/view/sachinvs/project_nypd_crime_analysis
