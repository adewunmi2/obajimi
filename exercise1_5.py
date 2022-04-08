# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 05:16:23 2022

@author: Admin
"""

import numpy as np

x = np.array([[23, 34, 54, 34,56], [33, 56, 78, 65, 78], [41, 32, 11, 34, 56]])
x = x.reshape(3,5)
print(x)

data = np.arange(128, 256).reshape(16, 8)
print(data)

data1 = np.arange(0.05, 5.05, 0.05).reshape(10, 10)
print(data1)