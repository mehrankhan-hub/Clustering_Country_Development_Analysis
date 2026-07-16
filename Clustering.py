import pandas as pd
import pickle as pkl
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('Country-data.csv')


x = df[['child_mort','exports','health','imports','income',
        'inflation','life_expec','total_fer','gdpp']]


kmean = KMeans(n_clusters=3,random_state=42)

kmean.fit(x)
print(kmean.predict(x))
#print(kmean.cluster_centers_)
res = kmean.labels_
result = [
    "Low-income" if i == 0 else "High-income" if i == 1 else "Middle-income" for i in res]
df['result'] = result
#print(kmean.labels_)
pd.set_option('display.max_columns', None)
#print(df[['country','child_mort','exports','health','imports','income',
#          'inflation','life_expec','total_fer','gdpp','result']].head(20))

#print(df[df['result']=='High-income'])



with open('Country-data.pkl', 'wb') as f:
    pkl.dump(kmean,f)



print('Saved')