#Bar plot on marks scored in cycle tests
#Three lines to make our compiler able to draw
import sys;
import matplotlib;
matplotlib.use('Agg');

import numpy as np;
import matplotlib.pyplot as plt;
tests_dict = {"Test-1":28, "Test-2":29, "Test-3":30, "Test-4":28, "Test-5":26, "Test-6":29, "Test-7":30, "Test-8":28, "Test-9":27, "Test-10":30}
cycle_tests = list(tests_dict.keys())
marks = list(tests_dict.values())
fig = plt.figure(figsize = (10, 5))
plt.bar(cycle_tests, marks, color ='blue',
        width = 0.3)
plt.xlabel("Cycle tests conducted")
plt.ylabel("Number of marks scored")
plt.title("Marks scored by me in cycle tests conducted in previous year of college")
plt.show()

#Two  lines to make our compiler able to draw
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

#OUTPUT:
#https://try.w3schools.com/try_python_img.php?id=353100264