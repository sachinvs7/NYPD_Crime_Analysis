#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
#pd.options.display.max_columns = None
#pd.options.display.max_rows = None


# In[3]:


data = pd.read_csv('../input/nypd-arrests-historic/NYPD_Arrests_Data__Historic_.csv')


# In[4]:


data.shape


# In[5]:


data.head()


# In[6]:


data.isnull().sum()


# In[7]:


data.dropna(subset = list(data.columns), inplace = True)


# In[8]:


data['ARREST_DATE'] = pd.to_datetime(data['ARREST_DATE'])


# In[9]:


data.head()


# In[10]:


data['arrest_year'] = data['ARREST_DATE'].dt.year
data['arrest_month'] = data['ARREST_DATE'].dt.month


# In[11]:


data['ARREST_BORO'].value_counts().plot(kind='pie')


# In[12]:


data['arrest_year'].value_counts()


# In[13]:


data['arrest_month'].value_counts().plot(kind='bar')


# In[14]:


data['arrest_day'] = data['ARREST_DATE'].dt.dayofweek


# In[15]:


data['arrest_day'].value_counts().plot(kind='barh')


# In[16]:


data['arrest_day'].value_counts().plot(kind='bar')


# In[17]:


data['PERP_RACE'].value_counts()


# In[18]:


data['OFNS_DESC'].value_counts().tail(15)


# In[19]:


import folium
from folium.plugins import HeatMap, HeatMapWithTime, MarkerCluster


# In[25]:


def query_heat_map(query, location=[40.650002, -73.949997]):
    train_query = data.query(query).loc[:, ['Latitude', 'Longitude']]
    if train_query.shape[0] == 0:
        print('Query fail, no data')
    m = folium.Map(location=location, zoom_start=13, tiles='CartoDB dark_matter') 
    train_query_geo_list = train_query.values.tolist()
    HeatMap(train_query_geo_list, blur=2, radius=3).add_to(m)
    m.save('NYPD_crime_brooklyn.html') 
    return m


# In[21]:


query_heat_map("ARREST_BORO=='K'")


# In[27]:


query_heat_map("ARREST_BORO=='K' & OFNS_DESC=='CRIMINAL TRESPASS'")

