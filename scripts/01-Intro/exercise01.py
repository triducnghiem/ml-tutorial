import math

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

def  get_mean_std(my_list):
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

print (min)
print (max)
print (mean)
print (std)