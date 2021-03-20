import copy

class Array():
    '''This class is a demonstration of basic Algebra on 2d matrix
    '''
    def __init__(self, m = 0, n = 0):
        '''Constructor methods to initialize the instance with given input

        Parameters:
        -----------
        m: int
            Number of rows
        n: int
            Number of columns

        Raise:
        ValueError: when m or n is negative int
        '''
        if m <0 or not isinstance(m, int) \
            or n < 0 or not isinstance(n, int):
            raise ValueError("Number of rows or columns must be a non-negative integer!")
            return
        self.arr = []

    def create_array(self, input_array)
        '''Creates a copy array of input_array
        '''
        self.arr = copy.deepcopy(input_array)

    def transpose(self):
        '''transposes the array
        
        Returns
        -------
        array
            An array that is the result of tranposing the original one
        '''
        arr = []
        #here do your transpose

        return arr

    def multiplication(self, arr_2):
        '''multiplies two matrices

        Parameters:
        -----------
        arr_2: Array
            An instance of Array to be multiplied with
        
        Returns:
        --------
        array
            Results of the multiplication

        Raise:
        ------
        InputError if it's wrong input!
        '''
        result = []
        #Do you task here
        return result

#Here is where you write the script to play with

original_array = [[1.1, 2.2, 3], [2.0, 5.6, 7.8]]

# do the transpose

# do the multiplication