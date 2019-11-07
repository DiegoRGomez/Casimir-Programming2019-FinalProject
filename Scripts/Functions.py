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
    StackCollection = {} #Dictionary that stores the stacks corresponding to different channels
    for FileName in FilesToRead:
        with ND2Reader(Path + FileName) as stack:
            
            StackCollection[stack.metadata['channels'][0]] = stack

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 20))
    ax1.imshow(SC["BF"][0])
    ax2.imshow(SC["GFP"][0])
    return StackCollection
    

Path = "../Images/Hy69/"
L = ScanFolder(Path)
print(L)
#nCh, sList, nFOVs = GetIterables(L)
nCh, sList = GetIterables(L)
#print(Nch)
#print(sList)

SC = LoadImagesInFOV(Path, L, nCh, "Point0006")

#fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 20))
#ax1.imshow(SC["BF"])
#ax2.imshow(SC["GFP"])