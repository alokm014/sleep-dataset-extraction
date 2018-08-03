import pyedflib
import numpy as np
import pandas as pd
import xml.etree.ElementTree as ET
import os

#path of edf file
path = 'C:\Users\user\Documents\Tensorflow-Bootcamp-master\mesa\polysomnography\edfs_test'
path1= "C:\\Users\\user\\Documents\\Tensorflow-Bootcamp-master\\mesa\\polysomnography\\annotations-events-nsrr_test"
path2= "C:\\Users\\user\\Documents\\Tensorflow-Bootcamp-master\\mesa\\polysomnography\\annotations-events-profusion_test"
li_path=[]
try:
	count=0
	
	for filename in os.listdir(path):
		print filename
		#fi=filename.split(".")[0]
		fi="edf"
		f_name=path+"\\"+filename
		name=f_name
		print name
		f = pyedflib.EdfReader(name)
		sampling_freq=f.getSampleFrequency(8)
		print sampling_freq
		signal_data=f.readSignal(8)
		t=np.arange(0,len(signal_data))/sampling_freq
		df= pd.DataFrame({'Flow': signal_data,'Epoch': t})
		#df.head()
		df.to_csv("F:\mesa\edf\%s%d.csv"% (fi,count), index=None)
		count=count+1
except:
	pass
