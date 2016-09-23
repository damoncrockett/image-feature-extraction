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

for root, dirs, files in os.walk(input_path):
    for name in files:
        try:
            counter +=1

            img = color.rgb2hsv(imread(os.path.join(root,name)))

            i_hue = np.mean(img[:,:,0])
            hue.append(i_hue)

            i_sat = np.mean(img[:,:,1])
            sat.append(i_sat)

            i_val = np.mean(img[:,:,2])
            val.append(i_val)

            i_hsd = np.std(img[:,:,0])
            hsd.append(i_hsd)
         
            filename.append(os.path.join(root,name))

            print counter, os.path.join(root,name)
 
        except:
            print counter, os.path.join(root,name), "error"
             
import pandas as pd
df = pd.DataFrame({'filename':filename,
                   'hue_mean':hue,
                   'sat_mean':sat,
                   'val_mean':val,
                   'hsd':hsd})

df['base'] = df.filename.apply(os.path.basename)
df.to_csv(input_path+descriptor+'_metadata.csv',index=False)
