import glob
import os
import sys
from skimage.io import imread
from skimage import color
import numpy as np

input_path = sys.argv[1]
descriptor = sys.argv[2]

filename = []
hue = []
sat = []
val = []
hsd = []
counter = -1

for file in glob.glob(os.path.join(input_path,'*.jpg')):
    counter +=1

    try:
        img = color.rgb2hsv(imread(file))

        m_hue = np.mean(img[:,:,0])
        hue.append(m_hue)

        #m_sat = np.mean(img[:,:,1])
        #sat.append(m_sat)

        #m_val = np.mean(img[:,:,2])
        #val.append(m_val)
         
        #m_hsd = np.std(img[:,:,0])
        #hsd.append(m_hsd)

        filename.append(file)

        print counter, file

    except Exception as e:
        print e

import pandas as pd
df = pd.DataFrame({'filename':filename,
                   'hue':hue})
                   #'sat':sat})
                   #'val':val})
                   #'hsd':hsd})

#df = df[df.val>0]
#df['basename'] = df.filename.apply(os.path.basename)

df.to_csv(input_path+descriptor+'_metadata.csv',index=False)
#df.to_csv(input_path+descriptor+'_metadata.txt',index=False,sep='\t')
