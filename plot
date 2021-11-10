import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt



  
def dataPlot(data):
   
    objects = ['Salmonella enterica', 'Bacillus cereus', 'Listeria', 'Brochothrix thermosphacta']
 
    data = np.asarray(data)
  
    #Histogram
    test = data[:,2]
    y_pos = np.arange(len(objects))+1
    


    plt.hist(test, bins='auto', color='purple', edgecolor='indigo', linewidth=3, align='mid', alpha=0.5)
    plt.xticks(y_pos, objects, rotation=45)
    

    
    plt.ylabel('Amount', fontsize=14, fontweight='bold')
    plt.xlabel('Bacteria type', fontsize=14, fontweight='bold')
    plt.title('Number of bacteria', fontsize=24, color="purple", fontstyle='italic', fontweight='demi')

    plt.show()

    
 #line plot

# Using Numpy to create an array 

 
    
    #for data[:,2] in range() :
        #growthrate1 == data(:,1)
    sorted1 = data[np.argsort(data[:, 2])]
    sorted2 = sorted1[np.argsort(sorted1[:,0])]
    tm = sorted2[:,0]
    g = sorted2[:,1]
    ty = sorted2[:,2]
    
    
    
    bacteria1 = 1
    mask = ty == bacteria1
    bacteria2 = 2
    mask1 = ty == bacteria2
    bacteria3 = 3
    mask2 = ty == bacteria3
    bacteria4 = 4
    mask3 = ty == bacteria4
    
    
    plt.scatter(tm[mask],g[mask], color='navy', label='Salmonella enterica')
    plt.plot(tm[mask],g[mask], color='royalblue')
    plt.scatter(tm[mask1], g[mask1], color='darkred', label='Bacillus cereus')
    plt.plot(tm[mask1], g[mask1], color='lightcoral')
    plt.scatter(tm[mask2], g[mask2], color='darkgreen', label='Listeria')
    plt.plot(tm[mask2], g[mask2], color='seagreen')
    plt.scatter(tm[mask3], g[mask3], color='magenta', label='Brochotrix thermosphacta')
    plt.plot(tm[mask3], g[mask3], color='orchid')
    
    plt.xlabel("Temperature", fontsize=14)
    plt.ylabel("Growth rate", fontsize=14)
    plt.title("Growth rate by temperature", fontsize=20, color="darkblue", alpha=0.8, fontstyle='italic', fontweight='demibold')
    plt.legend(bbox_to_anchor=(1.05, 1.0) )
    
    plt.show()
   
    
