import pyedflib
import numpy as np
import pandas as pd
import xml.etree.ElementTree as ET
import os

#path of edf file
path = 'C://Documents/mesa/polysomnography/edfs_test'
try:
	count=0
	
	for filename in os.listdir(path):
		print filename
		#fi=filename.split(".")[0]
		fi="edf"
		f_name=path+"/"+filename
		print name
		f = pyedflib.EdfReader(f_name)
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
