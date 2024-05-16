import os
import pandas as pd
import numpy as np

from matdata.preprocess import *

print('Starting...')

root     = os.path.abspath('../')
data     = os.path.join(root, 'data')
res_path = os.path.join(root, 'results')
prg_path = os.path.join(root, 'programs')

dir_path = os.path.join(data, 'NEW_DATA', 'Weeplaces')

file = os.path.join(dir_path, 'weeplace_checkins.csv')
df = pd.read_csv(file)

file = os.path.join(dir_path, 'weeplace_friends.csv')
df_friends = pd.read_csv(file)

print('1 - files read.')

df,_,_ = organizeFrame(df)

df['categories'] = df['category']
#df[['category','subcategory']] = df['categories'].str.split(":", expand=True)
#df
temp = df['categories'].str.split(":", expand=True)
temp[0] = temp[0].replace('Homes, Work, Others', 'Home / Work / Other')
temp[0] = temp[0].replace('Nightlife Spots', 'Nightlife')
temp[0] = temp[0].replace('Travel Spots', 'Travel')
temp[0] = temp[0].replace('Colleges & Universities', 'College & Education')

temp = temp.fillna('?')
#temp = temp.replace(None, '?')

df[['category','category2','category3']] = temp

#df['datetime'] = df['datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')
df['datetime'] = pd.to_datetime(df['datetime'])
df['week'] = df['datetime'].dt.isocalendar().week
#df['datetime'] = df['datetime'].str.replace('T', ' ')

df['tid'] = df.groupby(df[['userid', 'week']].apply(frozenset, axis=1)).ngroup() + 1

print('2 - data cleanup.')

df['friends'] = ''
#from tqdm.auto import tqdm
#def setFriends(name, group):
#    ls = list(group['userid2'].to_numpy())
#    ls.sort()
#    #print(name, '||', ' '.join(ls))
#    df.loc[df['userid'] == name, 'friends'] = ' '.join(ls)
#    return 0
#list(map(lambda name, group: setFriends(name, group), df_friends.groupby('userid1').groups.items() ))

for name, group in df_friends.groupby('userid1'):
    ls = list(group['userid2'].to_numpy())
    ls.sort()
    #print(name, '||', ' '.join(ls))
    df.loc[df['userid'] == name, 'friends'] = ' '.join(ls)
    
print('3 - friends column.')

print(df.columns)

df.drop(['categories', 'week'], axis=1, inplace=True)

df.set_axis(\
[
    'label', 'placeid', 'datetime', 'lat', 'lon', 'city', 'category', 'space', 'category2', 'category3', 'tid', 'friends'
]
, axis=1, inplace=True)

df.replace(',','_', regex=True, inplace=True)

print(df.columns)
print('4 - reorganized columns.')

print('# trajs: >= 5 | < 5', np.bincount(df.groupby(['label'])['tid'].nunique() < 5))
df_ = df.groupby(by='label', as_index=False).agg({'tid': pd.Series.nunique})
index_names = df[df['label'].isin(df_[df_['tid'] < 5]['label'])].index
df.drop(index_names, inplace=True)

print('5 - Drop classes with less than 5 trajectories.')

cols = ['tid', 'label', 'placeid', 'datetime', 'lat', 'lon', 'space', 'city', 'category', 'category2', 'category3', 'friends']
# 1. Unir os datasets:
trainAndTestSplit(dir_path, df[cols], train_size=0.7)

print("6 - 70/30 Done.")

train, test = kfold_trainAndTestSplit(dir_path, 5, df, fileprefix='specific_', columns_order=cols, verbose=True)

print("7 - 5-fold Done.")