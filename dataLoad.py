#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 11:41:57 2021

@author: dylan
"""
import numpy as np
#loads data
def dataLoad(filename):
    data = np.loadtxt(filename)
    #creates a matrix of the same shape as the data
    boolv = np.ones(np.shape(data)[0],dtype=bool)
    #begins a for loop to test each loop
    for i in range(len(data)):
        #checks each temperature in each row in the proper range
        if data[i,0] > 60 or data[i,0] < 10:
            #Prints error message
            print("Error: Temperature in row "\
                  +str(i+1)\
                  +" is outside experiment range.")
            #makes row false
            boolv[i] = False 
        #checks each Growth rate for being positive.
        if data[i,1] <= 0: 
            #error message
            print("Error: Growth rate in row "\
                  +str(i+1)\
                  +" must be a positive number.")
            #makes row false
            boolv[i] = False
        #checks each Bacteria row assign proper values.
        if data[i,2] > 4 or data[i,2] < 1:
            #error message
            print("Error: Bacteria in row "\
                  +str(i+1)\
                  + " must be an approved value(1,2,3,4).")
            #makes row false
            boolv[i] = False
    #creates new vector(data) without rows with errors.       
    data = data[boolv]
    return data