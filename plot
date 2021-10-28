import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def dataPlot(data):
 
objects = ('Salmonella enterica', 'Bacillus cereus', 'Listeria', 'Brochothrix thermosphacta')
y_pos = np.arange(len(objects))
performance = [25,20,15,10,5,0]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Count')
plt.title('Number of bacteria')

plt.show()
