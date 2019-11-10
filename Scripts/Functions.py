# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 14:30:51 2019
Contains main functions used for Final Project
@author: Diego
"""

import numpy as np
import matplotlib.pyplot as plt
from nd2reader import ND2Reader
import os #For ScanFolder function
from skimage.transform import resize #For AdjustResolution function
import matplotlib.colors as clrs



def ScanFolder(Path):
    FileList = os.listdir(Path)
    for element in FileList:
        if not element.endswith(".nd2"):
            FileList.remove(element)
    return FileList


def GetIterables(FileList):
    FullName = FileList[0]
    Idx_EndOfStem = FullName.find("_")
    stem = FullName[:Idx_EndOfStem]
    NumberOfChannels = sum(stem in element for element in FileList)
    StemList = [element[:Idx_EndOfStem] for element in FileList] #Different <stem> strings correspond to different FOVs, get a list of stems
    StemList = list(set(StemList)) #(remove repeated entires) #Contains the names of the different fields of view (FOVs)
    #NumberOfFOVs = len(StemList)
    return NumberOfChannels, StemList#, NumberOfFOVs


def LoadImagesInFOV(Path, FileList, NumberOfChannels, stem):
    FilesToRead = list(FileList) #If we do only FilesToRead = FileList, then modifying FilesToRead also modifies FileList --> wtf?! python is stupid sometimes. The list() command helps to tell python that the two lists should be allocated in independent memory slots
    for FileName in FileList: #If we iterate through the elements of FilesToRead, then something goes wrong. Apparently you cannot iterate through a list and modify it at the same time. Again, python be stupid
        if not stem in FileName:
            FilesToRead.remove(FileName)
    StackCollection = {} #Dictionary that stores the image stacks corresponding to different channels
    for FileName in FilesToRead:
        with ND2Reader(Path + FileName) as stack:
            ImageStack = [ im.copy() for im in stack ]
            StackCollection[stack.metadata['channels'][0]] = np.asarray(ImageStack)
    return StackCollection
    

def AdjustResolution(ImageStacks):
    SizeList = [ np.asarray(ImageStacks[channel].shape) for channel in ImageStacks ]
    xSizes = [entry[1] for entry in SizeList]
    ySizes = [entry[2] for entry in SizeList]
    Xmin = np.min(xSizes)
    Ymin = np.min(ySizes)
    nFrames = SizeList[0][0]    #Consider adding code to check if all stacks have the same number of frames as they should
    if (xSizes > Xmin).any() or (ySizes > Ymin).any():
        print("need to compress")
        for channel in ImageStacks:
            resizedStack = resize(ImageStacks[channel], (nFrames, Xmin, Ymin),anti_aliasing=True)
            ImageStacks[channel] = resizedStack
    return ImageStacks


#def OverlayChannels(ImageStacks): #add extra argument that maps the different possible channel to its corresponding display color
    #pass
    




#%% #Test the functions
    
Path = "../Images/Hy69/"
L = ScanFolder(Path)
print(L)
nCh, sList = GetIterables(L)

SC = LoadImagesInFOV(Path, L, nCh, "Point0005")

#fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 20))
#ax1.imshow(SC["BF"][0])
#ax2.imshow(SC["GFP"][0])

fig, axes = plt.subplots(2, 2, figsize=(20, 20))
axes[0][0].imshow(SC["BF"][0])
axes[0][0].set_title("Image0005 - Bright field")

axes[1][0].imshow(SC["GFP"][0])
axes[1][0].set_title("Image0005 - GFP channel")



sL = AdjustResolution(SC)

#fig, (ax3, ax4) = plt.subplots(1, 2, figsize=(20, 20))
#ax3.imshow(sL["BF"][0])
#ax4.imshow(sL["GFP"][0])



axes[0][1].imshow(sL["BF"][0])
axes[0][1].set_title("Image0005 - Bright field - resized")

axes[1][1].imshow(sL["GFP"][0])
axes[1][1].set_title("Image0005 - GFP channel")


#OverlayChannels(sL)