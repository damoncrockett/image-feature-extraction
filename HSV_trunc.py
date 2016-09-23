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


counter = -1

for file in glob.glob(os.path.join(input_path,'*.png')):
    counter +=1

    try:
        img = color.rgb2hsv(imread(file))

        m_hue = float(mode(img[:,:,0],axis=None)[0])
        hue.append(m_hue)

        i_sat = np.mean(img[:,:,1])
        sat.append(i_sat)

        i_val = np.mean(img[:,:,2])
        val.append(i_val)

        filename.append(file)

        print counter, file

    except:
        print counter,file,'error'

import pandas as pd
df = pd.DataFrame({'filename':filename,
				   'hue_mode':hue,
                   'sat_mean':sat,
                   'val_mean':val})
                
df['base'] = df.filename.apply(os.path.basename)
#df.sort("hue_mode",inplace=True)

df.to_csv(input_path+descriptor+'_metadata.csv',index=False)
#df.to_csv(input_path+descriptor+'_metadata.txt',index=False,sep='\t')
