import glob
import os
import sys
from skimage.io import imread
from skimage import color
import numpy as np
import pandas as pd

data = pd.read_csv("/Users/damoncrockett/Desktop/la/la_sliced/256/slice_metadata.csv")
data = data.sample(n=1548576)
data.reset_index(drop=True,inplace=True)

hue = []
sat = []
val = []

n = len(data.index)
for i in range(n):
    try:
        img = color.rgb2hsv(imread(data.filename.loc[i]))

        m_hue = np.mean(img[:,:,0])
        hue.append(m_hue)

        m_sat = np.mean(img[:,:,1])
        sat.append(m_sat)

        m_val = np.mean(img[:,:,2])
        val.append(m_val)

        print i

    except:
        print i,'error'
        hue.append("missing")
        sat.append("missing")
        val.append("missing")

data['hue'] = hue
data['sat'] = sat
data['val'] = val

data.to_csv("/Users/damoncrockett/Desktop/la/la_sliced/256/sample_slice_metadata.csv",
          index=False)