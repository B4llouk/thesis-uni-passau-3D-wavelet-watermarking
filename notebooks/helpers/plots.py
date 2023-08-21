import ipyvolume as ipv
import numpy as np 
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

def test():
    return "hello"

def ivyplotN(data_list):
    n = len(data_list)
    widget_containers = []
    for data in data_list[:n]:  # Process only the first n data arrays
        # Normalize data for each plot
        toplot = data - np.min(data)
        toplot = toplot / np.max(toplot)

        # Create and display figure individually
        ipv.figure()
        ipv.quickvolshow(toplot, level=[0.2, 0.8], opacity=0.1, level_width=0.1, data_min=0, data_max=1)
        ipv.view(-30, 40)
        
        # Append the current widget container
        widget_containers.append(ipv.gcc())

    # Determine the number of rows and columns for the grid layout
    rows = n // 2 + n % 2
    cols = 2 if n > 1 else 1

    # Arrange widget containers in a grid layout
    grid_layout = widgets.GridspecLayout(rows, cols)
    for i, container in enumerate(widget_containers):
        grid_layout[i // cols, i % cols] = container

    return grid_layout


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