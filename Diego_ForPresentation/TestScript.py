# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 18:44:19 2019

@author: Diego
"""

from nd2reader import ND2Reader
import matplotlib.pyplot as plt
#%%
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 20))


with ND2Reader('../Images/Hy69/Point0005_Seq0010.nd2') as images:
    copied_images = [ im.copy() for im in images ]
    ax1.imshow(copied_images[1])
    print(type(images))
    print(images)
    print('chan:', images.metadata['channels'], type(images.metadata['channels']))
    print('chan[0]:', images.metadata['channels'][0], type(images.metadata['channels'][0]))

print("type:", type(copied_images))
print("cop_img:", copied_images)

#fig, ax3 = plt.subplots()
ax2.imshow(copied_images[1])


#J = ND2Reader('../Images/Hy69/Point0005_Seq0010.nd2')
#ax2.imshow(J[0])
  

#%%

with ND2Reader('../Images/Hy69/Point0005_Seq0010.nd2') as images:
    copied_images = [ im.copy() for im in images ]

a = copied_images[1]
print(len(a))


with ND2Reader('../Images/Hy69/Point0005_Seq0011.nd2') as images:
    copied_images = [ im.copy() for im in images ]

b = copied_images[1]
print(b)
print(len(b))
print("type:", type(b))
print(len(b[1]))


#%%

with ND2Reader('../Images/Hy69/Point0005_Seq0011.nd2') as images:  
    ax2.imshow(images[0])
    print('%d x %d px' % (images.metadata['width'], images.metadata['height']))
    print(images.metadata)
    print("chan:", images.metadata['channels'][0])
    for el in images.metadata:
        print(el, "-->", images.metadata[el])
    print(images.sizes)
 
fig, ax3 = plt.subplots()
ax3.imshow(images[0])


#%%
import numpy as np

Dict = {}

Dict[1] = np.arange(27).reshape([3,3,3])



Dict["abc"] = (1,2,3,4)

print(Dict)

for elem in Dict:
    print(elem, type(elem))

#%%
    #Resizing

import numpy as np
from nd2reader import ND2Reader
import matplotlib.pyplot as plt
from skimage.transform import resize

    
with ND2Reader('../Images/Hy69/Point0005_Seq0010.nd2') as images:
    copied_images = [ im.copy() for im in images ]
    copied_images = np.asarray(copied_images)

print(type(copied_images))
print(copied_images.shape)



img_resized = resize(copied_images, (5, 1024, 1024),anti_aliasing=True)
print(type(img_resized))

print(img_resized.shape)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 20))
ax1.imshow(copied_images[0])
ax2.imshow(img_resized[0])

print(copied_images)
#%%
import cv2   #(opencv library must be installed)
#res = cv2.resize(copied_images, dsize=(54, 140), interpolation=cv2.INTER_CUBIC)
#%%
from PIL import Image
from matplotlib import cm

im = Image.fromarray(np.uint8(cm.gist_earth(copied_images[0])*255))
img = im.resize((1024,1024), Image.ANTIALIAS) 
print("type im:", type(im))
print("type img:", type(img))
print("type copy_image:", type(copied_images))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 20))
ax1.imshow(copied_images[0])
ax2.imshow(np.asarray(img))


print(img.size)
print(len(copied_images[0]))

print(copied_images[0])
print(img)
img.show()

#%%

x = copied_images

X = np.asarray(x)


print(X[0], X.shape, X[0].shape, X[0][0,1])