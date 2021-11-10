# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 13:43:55 2021
@author: Asus
"""
import numpy as np
def dataStatistics(data,statistic): #the function is declared
    tm = data[:,0] 
# tm - represents an array with all the values from the first column from the data matrix (temeperatures)
    gm = data[:,1] 
# gm - represents an array with all the values from the second column from the data matrix (growth rates)
    if statistic == 'Temperature Mean':
        result = np.mean(tm)
# if asked for Temperature Mean, the mean of all the elements from tm is taken
    if statistic == 'Growth Rate Mean':
        result = np.mean(gm)
# if asked for Growth Rate Mean, the mean of all the elements from gm is taken
    if statistic == 'Std Temperature':
        result = np.std(tm)
# if asked for Std Temperature, the std deviation of all the elements from tm is taken
    if statistic == 'Std Growth Rate':
        result = np.std(gm)
#if asked for Std Growth Rate, the std deviation of all the elements from gm is taken
    if statistic == 'Mean Cold Growth Rate':
        result = np.mean(gm[tm<=20])
# tm<=20 will be a new array, to which a new array gm corresponds, the code will take the average value of the new values from gm
    if statistic == 'Mean Hot Growth Rate':
        result = np.mean(gm[tm>=50])
# same as in the previous line, but here the new array tm, will contain the values >= 50
    if statistic == 'Rows':
        result = data.shape[0]
# data.shape will be a new array with 2 values (nr of rows, nr of columns), and the first one data.shape[0] will give the number of rows
    return result
        
print(dataStatistics(np.array([[39.122, 0.81021, 1],
[13.534, 0.5742, 1],
[56.137, 0.20517, 1],
[50.019, 0.4754, 1],
[24.297, 0.86149, 1],
[37.183, 0.85134, 1],
[59.239, 0.058406, 1],
[45.784, 0.62541 ,1],
[51.948, 0.39315 ,1],
[42.34 ,0.73713 ,1],
[25.387, 0.8774 ,1],
[57.187, 0.388 ,2],
[37.458, 0.7095, 2],
[46.419, 0.64312, 2],
[38.838, 0.70335, 2],
[11.293, 0.12138, 2],
[32.327, 0.67083, 2],
[42.315, 0.69079, 2],
[36.06 ,0.70488 ,2],
[28.616, 0.62475, 2],
[56.857, 0.39398, 2],
[51.477, 0.54097, 2],
[52.454, 0.51267, 2],
[28.627, 0.62481, 2],
[39.659, 0.70214, 2],
[53.628, 0.48291, 2],
[56.675, 0.40291, 2],
[43.423, 0.68051, 2],
[20.339, 0.42761, 2],
[42.693, 0.68262, 2],
[13.603, 0.20598, 2],
[30.336, 0.64974, 2],
[43.347, 0.67488, 2],
[56.686, 0.39765, 2],
[50.548, 0.55905, 2],
[34.227, 0.6929 ,2],
[47.837, 0.61363, 2],
[30.852, 0.65929, 2],
[51.329, 0.50498, 3],
[29.501, 0.77894, 3],
[34.895, 0.80504, 3],
[44.74 ,0.68839 ,3],
[51.718, 0.49269, 3],
[40.481, 0.76205, 3],
[38.737, 0.78338, 3],
[26.302, 0.73795, 3],
[32.821, 0.80721, 3],
[45.69 ,0.66843 ,3],
[54.22 ,0.40582 ,3],
[46.043, 0.66109, 3],
[10.931, 0.27471, 3],
[43.739, 0.70429, 3],
[31.925, 0.79482, 3],
[31.891, 0.79544, 3],
[15.852, 0.45917, 3],
[50.734, 0.52373, 3],
[26.243, 0.73048, 3],
[22.311, 0.65362, 3],
[14.769, 0.17958, 4],
[17.326, 0.23037, 4],
[41.557, 0.38979, 4],
[52.966, 0.26035, 4],
[58.711, 0.15578, 4]]), 'Mean Hot Growth Rate'))
    
    
            
        
    