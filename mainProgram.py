#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 18:06:56 2021

@author: dylan
"""

import numpy as np
from displayMenu import displayMenu
from dataLoad import dataLoad
from dataPlot import dataPlot
#define menu items
menuItems =  np.array(["Load data", "Filter data","Display statistics",
                       "Generate plots", "Quit"])

filename = ""
#define 

while True:
    
    choice = displayMenu(menuItems);
    #Loads data using dataLoad function
    if choice == 1:
        filename  = input("Please enter the filename to load: ")
        data = dataLoad(filename)

    #Filters data using filterData function
    elif  choice == 2: 
        if filename == "":
            print("Error: No file has been uploaded.")
            
    #Displays statistics using dataStatistics function
    elif choice == 3:
        if filename == "":
            print("Error: No file has been uploaded.")
            
    #Generates plots using dataPlot function
    elif choice == 4:
        if filename == "":
            print("Error: No file has been uploaded.")
        else: 
            dataPlot(data)
    #Quit
    elif choice == 5:
        break
