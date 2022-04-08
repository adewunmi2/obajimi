# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 12:45:21 2022

@author: Admin
"""

import numpy as np

data = np.arange(1, 50)

data = data.reshape(7, 7)

print(data)


matrix = []

for i in range(7):
    row = []
    
    for j in range(7):
        row.append(7 * i + j)
        
    
    matrix.append(row)
    
print(matrix)

data1 = np.random.rand(8, 8)
print(data1)

data2 = np.random.randn(3)
data2 = np.random.randn(8, 8)
print(data2)

