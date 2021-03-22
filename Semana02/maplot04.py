#Ian Cardoso
#11411EMT014

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


x=[0,1,2,3,4]
y=[0,2,4,6,8]

plt.plot(x,y)
plt.title('Our first graph', fontdict={'fontname': 'Comic Sans MS', 'fontsize':20}) 
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.xticks([0,1,2,3,4])
plt.yticks([0,2,4,6,8,10])

plt.plot(show)
