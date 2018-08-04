import numpy as np
import pandas as pd
import xml.etree.ElementTree as ET
import os

path1= "C:\\Documents\\mesa\\polysomnography\\annotations-events-nsrr_test"
try:
	for filename1 in os.listdir(path1):
		fi2=filename1.split(".")[0]
		f_name1=path1+"\\"+filename1
		tree = ET.parse(f_name1)
		root = tree.getroot()
		ts1=[]
		ts2=[]
		ts3=[]
		ts4=[]

		for child in root.iter('ScoredEvent'):
			t1=child[0].text
			ts1.append(t1)
			t2=child[1].text
			ts2.append(t2)
			t3=child[2].text
			ts3.append(t3)
			t4=child[3].text
			ts4.append(t4)
		df1=pd.DataFrame({'Type': ts1,'Stages': ts2,'Start': ts3,'Duration':ts4,})
		df2=df1.loc[(df1['Type'] == 'Stages|Stages')]
		print df2.head()
		df2.to_csv("F:\mesa\stages\%s.csv"% (fi2), index=None)
