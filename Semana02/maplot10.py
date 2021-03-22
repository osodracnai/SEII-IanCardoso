#Ian Cardoso
#11411EMT014

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


x=[0,1,2,3,4]
y=[0,2,4,6,8]

plt.figure(figsize=(2,3),dpi=300)




plt.plot(x,y, label='2x', color='red', linewidth=2, marker='.', linestyle='- -', makersize=10)
#plt.plot(x,y, 'r^--', label='2x')


x2=np.arange(0,4.5,0.5)
#plt.plot(x,x2**2, 'b', label='X^2')
plt.plot(x2[:5], x2[:5]**2, 'r',label='x2^2')
plt.plot(x2[4:]. x2[4:]**2 , 'r--')

plt.title('Our first graph', fontdict={'fontname': 'Comic Sans MS', 'fontsize':20}) 
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.xticks([0,1,2,3,4])
plt.yticks([0,2,4,6,8,10])

plt.legend()

plt.savefig('mygraph.png', dpi=300)

plt.plot(show)
