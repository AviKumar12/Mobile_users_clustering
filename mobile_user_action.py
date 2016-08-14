import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from collections import Counter

data = pd.read_csv('E://useractions.csv')
                                                    ############################# App Trend ###########################
event_type_count = Counter(data['event_type'])

Group = data.groupby(data['a_others'])
df = list(Group)

Apps_Installed = []
Apps_Launched= []
Apps_Uninstalled = []
hive_id = []
for i in range(len(df)):
    count_1 = 0
    count_2 = 0
    count_3 = 0
    hive_id.append(df[i][0])
    indx = df[i][1].index.tolist()
   
    for j in indx:
        if df[i][1]['event_type'][j]== 'Apps Installed':
            count_1 = count_1+1
        elif df[i][1]['event_type'][j] == 'Apps Launched':
            count_2 = count_2+1
        elif df[i][1]['event_type'][j] == 'Apps UnInstalled':
            count_3 = count_3+1
    Apps_Installed.append(count_1)
    Apps_Launched.append(count_2)
    Apps_Uninstalled.append(count_3)
    
columns = ['hiveid', 'Apps_Installed', 'Apps_Launched', 'Apps_Uninstalled']
df_1 = pd.DataFrame(columns = columns)
df_1['hiveid'] = pd.Series(hive_id)
df_1['Apps_Installed'] = pd.DataFrame(Apps_Installed)
df_1['Apps_Uninstalled'] = pd.DataFrame(Apps_Uninstalled)
df_1['Apps_Launched'] = pd.DataFrame(Apps_Launched)

                                                    ################################# Top Apps ######################################
package_name_count = Counter(data['a_packagename'])

apps = []
count = []
for i in range(len(package_name_count.items())):
    apps.append(package_name_count.items()[i][0])
    count.append(package_name_count.items()[i][1])

columns = ['apps', 'count']
df_2 = pd.DataFrame(columns = columns)
df_2['apps'] = pd.Series(apps)
df_2['count'] = pd.DataFrame(count)

                                            ############################## E-commerce Apps ##############################
import re

co = []
brand = []
for i in range(len(apps)):
    try:
        m = re.match(r"(\w+)\.(\w+)", apps[i])
        co.append(m.group(1))
        brand.append(m.group(2))
    except:
        pass

amazon = []
for i in range(len(data)):
    if data['a_packagename'][i]== 'in.amazon.mShop.android.shopping' or data['a_packagename'][i]== 'com.snapdeal.main' or data['a_packagename'][i]=='net.one97.paytm' or data['a_packagename'][i]=='com.abof.android' or data['a_packagename'][i]== 'com.alibaba.aliexpresshd' or data['a_packagename'][i] == 'com.craftsvilla.app' or data['a_packagename'][i] == 'com.flipkart.android' or data['a_packagename'][i] == 'com.homeshop18.activity' or data['a_packagename'][i] == 'com.jabong.android' or data['a_packagename'][i]== 'com.myntra.android' or data['a_packagename'][i]== 'com.voonik.android':
        amazon.append(data['a_others'][i])

E-commerce = len(np.unique(amazon))
                                        ########################################### Correlation ############################  
df_1['Apps_Installed_cat']= pd.cut(df_1['Apps_Installed'], 4, labels=False)
df_1['Apps_Uninstalled_cat']= pd.cut(df_1['Apps_Uninstalled'], 4, labels=False)
df_1['Apps_Launched_cat']= pd.cut(df_1['Apps_Launched'], 4, labels=False)

user_data= pd.read_csv("E://users.csv")
from sklearn import preprocessing

cat_num =preprocessing.LabelEncoder()

user_data.isgoogleaccount = cat_num.fit_transform(user_data.isgoogleaccount)
user_data.threeg = cat_num.fit_transform(user_data.threeg)
user_data.fourg = cat_num.fit_transform(user_data.fourg)
user_data.wifi = cat_num.fit_transform(user_data.wifi)
user_data.ram = cat_num.fit_transform(user_data.ram)

user_data.ostype= user_data['ostype'].fillna('missing')
user_data.displaydensity =user_data['displaydensity'].fillna('missing')

user_data.ostype = cat_num.fit_transform(user_data.ostype)
user_data.displaydensity = cat_num.fit_transform(user_data.displaydensity)

combined_data = pd.merge(df_1, user_data, how ='left', on='hiveid')

from scipy.stats.stats import pearsonr  

combined_data= combined_data.dropna()

print pearsonr(combined_data['Apps_Installed_cat'], combined_data['threeg'])
print pearsonr(combined_data['Apps_Uninstalled_cat'], combined_data['threeg'])
print pearsonr(combined_data['Apps_Launched_cat'], combined_data['threeg'])

print pearsonr(combined_data['Apps_Installed_cat'], combined_data['isgoogleaccount'])
print pearsonr(combined_data['Apps_Uninstalled_cat'], combined_data['isgoogleaccount'])
print pearsonr(combined_data['Apps_Launched_cat'], combined_data['isgoogleaccount'])

print pearsonr(combined_data['Apps_Installed_cat'], combined_data['fourg'])
print pearsonr(combined_data['Apps_Uninstalled_cat'], combined_data['fourg'])
print pearsonr(combined_data['Apps_Launched_cat'], combined_data['fourg'])

print pearsonr(combined_data['Apps_Installed_cat'], combined_data['wifi'])
print pearsonr(combined_data['Apps_Uninstalled_cat'], combined_data['wifi'])
print pearsonr(combined_data['Apps_Launched_cat'], combined_data['wifi'])

print pearsonr(combined_data['Apps_Installed_cat'], combined_data['ram'])
print pearsonr(combined_data['Apps_Uninstalled_cat'], combined_data['ram'])
print pearsonr(combined_data['Apps_Launched_cat'], combined_data['ram'])

print pearsonr(combined_data['Apps_Installed_cat'], combined_data['ostype'])
print pearsonr(combined_data['Apps_Uninstalled_cat'], combined_data['ostype'])
print pearsonr(combined_data['Apps_Launched_cat'], combined_data['ostype'])

print pearsonr(combined_data['Apps_Installed_cat'], combined_data['displaydensity'])
print pearsonr(combined_data['Apps_Uninstalled_cat'], combined_data['displaydensity'])
print pearsonr(combined_data['Apps_Launched_cat'], combined_data['displaydensity'])