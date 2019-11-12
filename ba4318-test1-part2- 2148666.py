
# In[1]:


import pandas as pd


# In[3]:


df_brazil = pd.read_csv("sudeste.csv", usecols=["date", "temp"])


# In[5]:


df_madrid = pd.read_csv("weather_madrid_LEMD_1997_2015.csv", usecols=["CET", "Mean TemperatureC"])


# In[12]:


df_brazil_no_dup_date = df_brazil.groupby("date").mean().reset_index()


# In[14]:


df_final = pd.merge(df_brazil_no_dup_date, df_madrid, how="inner", left_on="date", right_on="CET")


# In[17]:


df_final = df_final[["date", "temp", "Mean TemperatureC"]]


# In[19]:


df_final.columns = ["date", "temp_brazil", "temp_madrid"]


# In[21]:


df_final[["temp_brazil", "temp_madrid"]].corr()


# In[22]:


# Brazil and Madrid average daily temperatures have a negative correlation of -0.03 but that can be ignored.
# As a result one can say Brazil and Madrid average daily temperatures are independent of each other.
