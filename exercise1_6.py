
import numpy as np

dataset = np.arange(1, 37).reshape(6, 6)

section = dataset[3:, 2:]

print(section)

column = dataset[:4, 3]

print(column)

row = dataset[2]

print(row)

row1 = dataset[3:, :]
print(row1)