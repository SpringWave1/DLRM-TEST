# coding:utf-8

"""
Author: roguesir
Date: 2017/8/30
GitHub: https://roguesir.github.com
Blog: http://blog.csdn.net/roguesir
"""

import numpy as np
import matplotlib.pyplot as plt

x1 = [4,16,36,64]
y1 = [100,0,0,0]

x = np.arange(0, 80)
l1 = plt.plot(x1, y1, 'b--')

plt.plot(x1, y1, 'bo-')
plt.title('Learning Reward')
plt.xlabel('Number of Agents')
plt.ylabel('Reward')
plt.legend()
plt.show()