import ipyvolume as ipv
import numpy as np 
import matplotlib.pyplot as plt


def ivyplot(data):

    toplot= data
    toplot = toplot- np.min(toplot)
    toplot = toplot/ np.max(toplot)

#dataRoi when data size is very big
#still to implement 

    # visualize
    ipv.figure()
    ipv.quickvolshow(toplot, level=[0.2, 0.8], opacity=0.1, level_width= 0.1, data_min=0, data_max=1)
    ipv.view(-30, 40)
    ipv.show()
    return 0 


def npyplot(array): 
    # Plot the resized QR code array using Matplotlib
    plt.imshow(array, cmap='gray')
    plt.axis('off')
    plt.show()
    return 0 


def histogram(data, data2, annotations): 
    # plot a histogram of values 
    flattened_data = data.flatten()
    flattened_data2 = data2.flatten()


    # Plot histograms in the same figure
    plt.hist(flattened_data, bins=50, density=True, alpha=0.5, color='blue', label=annotations['data1'])
    plt.hist(flattened_data2, bins=50, density=True, alpha=0.5, color='orange', label=annotations['data2']) 

    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title(annotations['title'])
    plt.legend()
    plt.grid(True)
    plt.show()