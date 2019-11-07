# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 18:44:19 2019

@author: Diego
"""

from nd2reader import ND2Reader
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 20))


with ND2Reader('../Images/Hy69/Point0005_Seq0010.nd2') as images:
  ax1.imshow(images[0])
  
with ND2Reader('../Images/Hy69/Point0005_Seq0011.nd2') as images:  
  ax2.imshow(images[0])