#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Print a specific timestamp: 14:42:05.000566

from datetime import time 

t = time(14, 42, 5, 566)

print(t)


# In[15]:


# Print a specific date and timestamp: 2019/01/28 23:55:59.1023

from datetime import datetime 

dt = datetime(2019, 1, 28, 23, 55, 59, 1023)

print(dt.strftime("%Y/%m/%d %H:%M:%S.%f"))


# In[24]:


# Print today's date (current day)

from datetime import date

current_date = date.today()

print("Current year:", current_date.year)
print("Current month:", current_date.month)
print("Current day:", current_date.day)


# In[42]:


# Print a day from a datetime object: 28 January 2017
# Version 1

from datetime import date

x = date(2017, 1, 28)

print(x.strftime("%d %B %Y"))
print(x.strftime('%A'))


# In[43]:


# Print a day from a datetime object: 28 January 2017
# Version 2

date_string = "28 January 2017"

date_object = datetime.strptime(date_string, "%d %B %Y")

print(date_object.strftime("%d %B %Y"))
print(date_object.strftime('%A'))

