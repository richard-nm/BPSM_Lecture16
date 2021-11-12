#!/usr/local/bin/python3
import os 
import pandas as pd

df=pd.read_csv('eukaryotes.tsv',sep="\t",na_values=['-'],engine='python')
l=df[df.apply(lambda x : x['Group'] == 'Fungi' and x['Size (Mb)'] > 100, axis=1)]
#print(list(l['#Organism/Name']))

box=['plants','animals','fungi','protists']
for i in box:
	seql=len(df[df['Group'].str.lower()==i])
#	print(str(seql)+' sequenced in '+i) 

#print(df[df.apply(lambda x: x['#Organism/Name'].startswith('Heliconius'),axis=1)])
#print(df[df['Group']=='Plants']['Center'].value_counts())
#print(df[df['SubGroup']=='Insects']['Center'].value_counts())
df['PpG']=df['Proteins']/df['Genes']
print(len(df[df['PpG']>=1.1][['#Organism/Name','PpG']]))
