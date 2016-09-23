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
hue_med = []
sat_med = []
val_med = []
hue_mode = []
sat_mode = []
val_mode = []
hsd = []
ssd = []
vsd = []

counter = -1

for root, dirs, files in os.walk(input_path):
    for file in files:
        counter +=1

        try:
            img = color.rgb2hsv(imread(root+"/"+file))

            i_hue = np.mean(img[:,:,0])
            hue.append(i_hue)

            i_sat = np.mean(img[:,:,1])
            sat.append(i_sat)

            i_val = np.mean(img[:,:,2])
            val.append(i_val)

            i_hue_med = np.median(img[:,:,0])
            hue_med.append(i_hue_med)

            i_sat_med = np.median(img[:,:,1])
            sat_med.append(i_sat_med)

            i_val_med = np.median(img[:,:,2])
            val_med.append(i_val_med)

            """
            i_hue_mode = float(mode(img[:,:,0],axis=None)[0])
            hue_mode.append(i_hue_mode)

            i_sat_mode = float(mode(img[:,:,1],axis=None)[0])
            sat_mode.append(i_sat_mode)
        
            i_val_mode = float(mode(img[:,:,2],axis=None)[0])
            val_mode.append(i_val_mode)
 
            i_hsd = np.std(img[:,:,0])
            hsd.append(i_hsd)
        
            i_ssd = np.std(img[:,:,1])
            ssd.append(i_ssd)

            i_vsd = np.std(img[:,:,2])
            vsd.append(i_vsd)
            """
            filename.append(root+"/"+file)

            print counter, file

        except:
            print counter,file,'error'

import pandas as pd
df = pd.DataFrame({'filename':filename,
                   'hue_mean':hue,
                   'sat_mean':sat,
                   'val_mean':val,
                   'hue_med':hue_med,
                   'sat_med':sat_med,
                   'val_med':val_med})
                   #'hue_mode':hue_mode,
                   #'sat_mode':sat_mode,
                   #'val_mode':val_mode,
                   #'hsd':hsd,
                   #'ssd':ssd,
                   #'vsd':vsd})


df['base'] = df.filename.apply(os.path.basename)
#df.sort("hue_mode",inplace=True)

df.to_csv(input_path+descriptor+'_metadata.csv',index=False)
#df.to_csv(input_path+descriptor+'_metadata.txt',index=False,sep='\t')
