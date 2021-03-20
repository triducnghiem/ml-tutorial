import math
import numpy as np

def get_min_max(my_list):
    '''Finds min and max values of the given list

    Parameters:
    -----------
    my_list: list
        List of numbers
    
    Returns:
    --------
    tuple (min, max)
        A tuple contains min and max values
    '''
    min = math.inf
    max = -math.inf
    #Here is where you write your code
    
    #Returns the found values
    return (min, max)

def get_mean_std(my_list):
    '''Finds mean and standard deviation of the list

    Parameters:
    -----------
    my_list: list
        List of numbers
    
    Returns:
    --------
    tuple (mean, std)
        A tuple contains mean and standard deviation values
    '''
    mean = 0
    std = 0
    #Here is where you write your code
    
    #Returns values
    return (mean, std)

#Test 
my_list = [6, 4, 2, 10, 15, 30, 46, 49]
min, max = get_min_max(my_list)
mean, std = get_mean_std(my_list)

np_list = np.array(my_list)
cr_min = np_list.min()
cr_max = np_list.max()
cr_mean = np_list.mean()
cr_std = np_list.std()

epsilon = 0.001
if abs(min - cr_min) > epsilon:
    print ("You are so dump! Expected min: {} but get {}".format(cr_min, min))
else:
    print ("Correct! min = {}".format(min))
if abs(max - cr_max) > epsilon:
    print ("You are so dump! Expected max: {} but get {}".format(cr_max, max))
else:
    print ("Correct! max = {}".format(max))
if abs(mean - cr_mean) > epsilon:
    print ("You are so dump! Expected mean: {} but get {}".format(cr_mean, mean))
else:
    print ("Correct! mean = {}".format(mean))
if abs(std - cr_std) > epsilon:
    print ("You are so dump! Expected min: {} but get {}".format(cr_std, std))
else:
    print ("Correct! std = {}".format(std))