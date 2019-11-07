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
    return NumberOfChannels, StemList


L = ScanFolder("../Images/Hy69/")
print(L)
Nch, sList = GetIterables(L)
print(Nch)
print(sList)