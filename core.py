import math
import matplotlib.pyplot as plt
import pandas as pd

## Variables
x0 = 10
v0 = 0
mass = 5
g = -9.81
t_max = 1
delta_t = 0.01
precision = 100

## core calculations
x = [x0]
v = [v0]
t_array = range(0, int(t_max*precision), int(delta_t*precision))

for i in range(1, len(t_array)):
    v.append(v[i-1] + g*delta_t)
    x.append(x[i-1] + v[i-1]*delta_t + g*math.pow(delta_t, 2))


import pdb; pdb.set_trace()