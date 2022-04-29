#HISTOGRAM PLOTTING RANDOMLY

#Three lines used to make our compiler able to draw
import sys;
import matplotlib;
matplotlib.use('Agg');

import matplotlib.pyplot as plt;
import numpy as np;
x = np.random.normal(200, 10, 300)
plt.hist(x)
plt.show()

#Two lines used to make our compiler able to draw
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

#OUTPUT:
#https://try.w3schools.com/try_python_img.php?id=353562490