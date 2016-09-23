import glob
import os
import sys
from skimage.io import imread
from skimage import color
import numpy as np
from scipy.stats import mode

input_path = sys.argv[1]
descriptor = sys.argv[2]

filename = []
hue = []
sat = []
val = []
hsd = []
counter = -1

for file in glob.glob(os.path.join(input_path,'*.png')):
    counter +=1

    try:
        img = color.rgb2hsv(imread(file))

        m_hue = float(mode(img[:,:,0],axis=None)[0])
        hue.append(m_hue)

        m_sat = np.median(img[:,:,1])
        sat.append(m_sat)

        m_val = np.median(img[:,:,2])
        val.append(m_val)
         
        m_hsd = np.std(img[:,:,0])
        hsd.append(m_hsd)

        filename.append(file)

        print counter, file

    except:
        print counter,file,'error'

import pandas as pd
df = pd.DataFrame({'filename':filename,
                   'hue_mode':hue,
                   'sat_median':sat,
                   'val_median':val,
                   'hsd':hsd})

#df = df[df.val>0]
df['basename'] = df.filename.apply(os.path.basename)
df['dummy'] = 5
df.dummy[df.basename=="Untitled.png"] = 1
df.dummy[df.basename=="Untitled2.png"] = 7
df.sort("hue_mode",inplace=True)
df['hue_rank'] = range(len(df.index))

df.to_csv(input_path+descriptor+'_metadata.csv',index=False)
df.to_csv(input_path+descriptor+'_metadata.txt',index=False,sep='\t')
