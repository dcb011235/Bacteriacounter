import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

  
def dataPlot(data):
   
    objects = ['Salmonella enterica', 'Bacillus cereus', 'Listeria', 'Brochothrix thermosphacta']
 
    data = np.asarray(data)
  
    #Histogram
    test = data[:,2]
    y_pos = np.arange(len(objects))+1
    


    plt.hist(test, bins='auto', color='purple',align='mid', alpha=0.5)
    plt.xticks(y_pos, objects, rotation=45)
    

    
    plt.ylabel('Amount')
    plt.title('Number of bacteria')

    plt.show()
