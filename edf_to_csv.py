import pyedflib
import numpy as np
import pandas as pd
import os

#path of edf file
path = 'C://Documents/mesa/polysomnography/edfs_test'
try:
	for filename in os.listdir(path):
		fi=filename.split(".")[0]
		f_name=path+"/"+filename
		f = pyedflib.EdfReader(f_name)
		
		#getting samples from channel 8
		sampling_freq=f.getSampleFrequency(8)
		signal_data=f.readSignal(8)
		
		#time 
		t=np.arange(0,len(signal_data))/sampling_freq
		
		#dataframe of singal and time
		df= pd.DataFrame({'Flow': signal_data,'Time': t})
		df.head()
		
		# export file locaation
		df.to_csv("F:\mesa\edf\%s.csv"% fi, index=None)
except:
	print("error in reading")
