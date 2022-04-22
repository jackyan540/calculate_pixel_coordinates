import numpy as np

def calc_pixels(dims, corner_points):
    #Get height and width dimensions
    height = dims[0]
    width = dims[1]
    
    #Get x-coordinates and y-coordinates of the corner points
    x, y = zip(*corner_points)

    #Create array of unique x-coordinates (cols) and y-coordinates (rows) for the eventual solution
    cols = np.linspace(np.unique(x)[0], np.unique(x)[1], width)
    rows = np.linspace(np.unique(y)[0], np.unique(y)[1], height)

    #Create a coordinate matrix of all the x-coordinates and all the y-coordinates
    xs, ys = np.meshgrid(cols, rows)
    
    #Round any decimal values to 3 decimal places
    xs = xs.round(3)
    ys = ys.round(3)

    #Create a 2-Dimensional array of all the points for the eventual solution
    pts = np.vstack(([xs], [ys])).T.reshape(height * width, 2)

    #Sort the points according to largest y-coordinate (and then smallest x-coordinate in case of a tie)
    sorted_pts = pts[np.lexsort(([pts[:,0], -pts[:,1]]))]

    #Reshape the sorted points to the desired solution array dimensions and return the solution
    return np.reshape(sorted_pts, (height, width, 2)).tolist()