# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 18:44:19 2019

@author: Diego
"""

from nd2reader import ND2Reader
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 20))


with ND2Reader('../Images/Hy69/Point0005_Seq0010.nd2') as images:
    copied_images = [ im.copy() for im in images ]
    ax1.imshow(copied_images[1])

#fig, ax3 = plt.subplots()
ax2.imshow(copied_images[1])


#J = ND2Reader('../Images/Hy69/Point0005_Seq0010.nd2')
#ax2.imshow(J[0])
  


#with ND2Reader('../Images/Hy69/Point0005_Seq0011.nd2') as images:  
#    ax2.imshow(images[0])
#    print('%d x %d px' % (images.metadata['width'], images.metadata['height']))
#    print(images.metadata)
#    print("chan:", images.metadata['channels'][0])
#    for el in images.metadata:
#        print(el, "-->", images.metadata[el])
#    print(images.sizes)
# 
#fig, ax3 = plt.subplots()
#ax3.imshow(images[0])