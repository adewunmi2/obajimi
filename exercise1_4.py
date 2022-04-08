# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 07:37:58 2022

@author: Admin
"""

import numpy as np

data = np.linspace(0, 1, 10)
print(data)

x = np.linspace(1, 5, 100)
print(x)

matrix = []

for i in range(10):
    
    row = []
    
    for j in range(10):
        row.append(10 * (i + j))
        
    matrix.append(row)
    
print(matrix)