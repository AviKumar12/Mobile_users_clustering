import pandas as pd
import numpy as np
import csv
from sklearn.cluster import KMeans
from sklearn import preprocessing
import matplotlib.pyplot as plt
from collections import Counter
from scipy.spatial.distance import euclidean
import warnings

                                                ############################ Data-PreProcessing ##############################
data = pd.read_csv("E://users.csv")
#print data.columns
cat_num =preprocessing.LabelEncoder()

data.isgoogleaccount = cat_num.fit_transform(data.isgoogleaccount)
data.threeg = cat_num.fit_transform(data.threeg)
data.fourg = cat_num.fit_transform(data.fourg)
data.wifi = cat_num.fit_transform(data.wifi)
data.ram = cat_num.fit_transform(data.ram)

data.ostype= data['ostype'].fillna('missing')
data.displaydensity =data['displaydensity'].fillna('missing')

data.ostype = cat_num.fit_transform(data.ostype)
data.displaydensity = cat_num.fit_transform(data.displaydensity)

data.drop(data.columns[[8, 9]], axis =1, inplace=True)

                                            ################################ Clustering-Algorithm #################################
K_Means = KMeans(n_clusters = 5, random_state = None)
data = data.set_index('hiveid')
train_model = K_Means.fit(data)
labels = train_model.labels_
centroids = train_model.cluster_centers_

columns = ['pre']
labels = pd.DataFrame(labels, index = data.index, columns = columns)
df = pd.concat([data, labels], axis=1)

# import seaborn as sb
# g =sb.pairplot(df, vars = ["isgoogleaccount", "threeg", "fourg", "wifi", "ram", "ostype", "displaydensity"], hue= "pre")
# g.map_diag(plt.hist)
# g.add_legend()
                                        ################################# Cluster-Properties Identification ##############################
Group = df.groupby('pre')
df_1 = list(Group)

isgoogleaccount_freq =[]
threeg_freq =[]
fourg_freq =[]
wifi_freq =[]
ram_freq =[]
ostype_freq =[]
displaydensity_freq =[]
labe = []
for i in range(len(df_1)):
    labe.append(i)
    isgoogleaccount_freq.append(Counter(df_1[i][1]['isgoogleaccount']))
    threeg_freq.append(Counter(df_1[i][1]['threeg']))
    fourg_freq.append(Counter(df_1[i][1]['fourg']))
    wifi_freq.append(Counter(df_1[i][1]['wifi']))
    ram_freq.append(Counter(df_1[i][1]['ram']))
    ostype_freq.append(Counter(df_1[i][1]['ostype']))
    displaydensity_freq.append(Counter(df_1[i][1]['displaydensity']))
        
# print isgoogleaccount_freq
# print threeg_freq
# print fourg_freq
# print wifi_freq
# print ram_freq
# print ostype_freq
# print displaydensity_freq

var = raw_input("Please enter hiveid: ")
predict = train_model.predict(data.loc[var])
dist = []
for i in range(len(centroids)):
    dist.append(euclidean(data.loc[var], centroids[i]))

warnings.filterwarnings("ignore")
print "predicted_class:", predict
print "Distance_from_centroids: " ,dist