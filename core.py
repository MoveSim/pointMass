import math
import matplotlib.pyplot as plt
import pandas as pd

## Variables
x0 = 10
v0 = 0
mass = 5
g = -9.81
t_max = 10
delta_t = 0.001
precision = 1000

## core calculations
x = [x0]
v = [v0]
t_array = range(0, int(t_max*precision), int(delta_t*precision))

for i in range(1, len(t_array)):
    v.append(v[i-1] + g*delta_t)
    x.append(max(0, x[i-1] + v[i-1]*delta_t + g*math.pow(delta_t, 2)))

x = pd.DataFrame(x)
x.reset_index(x.index/precision)

x.plot()
plt.show()

import pdb; pdb.set_trace()