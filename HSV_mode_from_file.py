import glob
import os
import sys
from skimage.io import imread
from skimage import color
import numpy as np
from scipy.stats import mode
import pandas as pd

input_path = "/Users/damoncrockett/Desktop/gujarat/images/"
input_file = sys.argv[1]
descriptor = sys.argv[2]
df = pd.read_csv(input_file)
df = df.sample(n=512)
df.reset_index(drop=True,inplace=True)

filename = []
hue = []
sat = []
val = []
hsd = []

n = len(df.index)
for i in range(n):
    try:
        file = df.filename.loc[i]
        img = color.rgb2hsv(imread(file))

        #m_hue = float(mode(img[:,:,0],axis=None)[0])
        #hue.append(m_hue)
        
        m_hue = np.median(img[:,:,0])
        hue.append(m_hue)
        
        m_sat = np.median(img[:,:,1])
        sat.append(m_sat)

        m_val = np.median(img[:,:,2])
        val.append(m_val)
        
        m_hsd = np.std(img[:,:,0])
        hsd.append(m_hsd)

        filename.append(file)

        print i, file

    except:
        print i,file,'error'

df = pd.DataFrame({'filename':filename,
                   'hue_median':hue,
                   'sat_median':sat,
                   'val_median':val,
                   'hsd':hsd})

#df = df[df.val>0]
df.to_csv(input_path+descriptor+'_metadata.csv',index=False)

#df['basename'] = df.filename.apply(os.path.basename)
#df.to_csv(input_path+descriptor+'_metadata.txt',index=False,sep='\t')
