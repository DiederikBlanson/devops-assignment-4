import matplotlib.pyplot as plt
import numpy as np
x = np.arange(4)

plt.bar(x, height=[860, 664, 600, 599], color=(0.2, 0.4, 0.6, 0.6))
plt.ylabel('Req/Sec')
plt.xlabel('Instances')
plt.xticks(x, ['1','2','4', '8'])
plt.show()