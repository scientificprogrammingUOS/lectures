class Matrix:

    # use-case 1
    def __init__(self, iterable):
        """constructor, expects a non-ill-formed iterator of ints or floats"""
        #TODO: check for non-ill-formedness & if every cell is int or fload
        self._data = .....

    @staticmethod
    def filled(rows, cols, value):
        
        #TODO: fill the data by using the parameters rows, cols and value.
        # data = ....
        
        return Matrix(data)


    # use-case 2
    def __str__(self):
        """proper string representation"""
        
        string = "["
        #TODO: fill the variable "string" such that the pytest passes. 
        # The string-representation ends every line but the last with a comma and a \n, 
        # and starts each line but the first with a space.
        return string
      
    
    # use-case 3
    @property
    def data(self):
        """returns a copy of the data"""
        
        #TODO what does this method need to return?
        return ...


    # use-case 4
    def __getitem__(self, coords):
        """gets a cell, by comma-separated cell-coords"""
        
        #TODO what does this method need to return?
        return ...

    def __setitem__(self, coords, value):
        """sets a cell, by comma-separated cell-coords"""
        
        #TODO what does this method need to set?
        self....  = value


    # use-case 5
    @property
    def T(self):
        """Transposes a Matrix"""
        
        #TODO how do you transpose a matrix?
        return Matrix(...)


    # use-case 6
    def __add__(self, other):
        """Adds two matrices"""
        
        #TODO how do you add two matrices?
        new_data = ....
        return Matrix(new_data)


    # use-case 7
    def __rmul__(self, other):
        """Scalar multiplication"""
        
        #TODO how does scalar multiplication work?
        new_data = ...
        return Matrix(new_data)


    # use-case 8
    def __mul__(self, other):
        """matrix multiplication"""
        
        #TODO how does matrix-multiplication work?
        new_data = ... 
        return Matrix(new_data)
