class Variable:
    """
    A symbolic representation of a variable that supports arithmetic operations.
    
    Attributes:
        __coefficient (int, float): The numerical coefficient of the variable.
        __variable (str): The symbolic name of the variable.
    """

    __slots__ = ["__coefficient", "__variable"]

    def __init__(self, coefficient, variable):
        """
        Initialize a Variable instance with a coefficient and a symbolic name.
        
        Args:
            coefficient (int, float): The coefficient of the variable.
            variable (str): The symbolic name representing the variable.
        """
        self.__coefficient = coefficient
        self.__variable = variable

    def get_coefficient(self):
        """Return the coefficient of the variable."""
        return self.__coefficient

    def get_variable(self):
        """Return the symbolic name of the variable."""
        return self.__variable

    def __add__(variable_one, variable_two):
        """
        Add two Variables if they share the same symbolic name.
        If they do not share the same symbolic name, return a symbolic expression showing their addition.
        
        Args:
            variable_one (Variable): The first variable.
            variable_two (Variable): The second variable.
        
        Returns:
            str: The result of the addition, either simplified or as a symbolic expression.
        """
        if variable_one.get_variable() == variable_two.get_variable():
            result = variable_one.get_coefficient() + variable_two.get_coefficient()
            return f"{result}{variable_one.get_variable()}"
        else:
            return f"{variable_one.get_coefficient()}{variable_one.get_variable()} + {variable_two.get_coefficient()}{variable_two.get_variable()}"

    def __sub__(variable_one, variable_two):
        """
        Subtract two Variables if they share the same symbolic name.
        If they do not share the same symbolic name, return a symbolic expression showing their subtraction.
        
        Args:
            variable_one (Variable): The first variable.
            variable_two (Variable): The second variable.
        
        Returns:
            str: The result of the subtraction, either simplified or as a symbolic expression.
        """
        if variable_one.get_variable() == variable_two.get_variable():
            result = variable_one.get_coefficient() - variable_two.get_coefficient()
            return f"{result}{variable_one.get_variable()}"
        else:
            return f"{variable_one.get_coefficient()}{variable_one.get_variable()} - {variable_two.get_coefficient()}{variable_two.get_variable()}"

    def __mul__(variable_one, variable_two):
        """
        Multiply two Variables.
        
        Args:
            variable_one (Variable): The first variable.
            variable_two (Variable): The second variable.
        
        Returns:
            str: The product of the variables, either simplified or as a symbolic expression.
        """
        result = variable_one.get_coefficient() * variable_two.get_coefficient()
        if variable_one.get_variable() == variable_two.get_variable():
            return f"{result}{variable_one.get_variable()}"
        else:
            return f"{result}{variable_one.get_variable()}{variable_two.get_variable()}"

    def __floordiv__(variable_one, variable_two):
        """
        Divide two Variables using floor division.
        
        Args:
            variable_one (Variable): The numerator variable.
            variable_two (Variable): The denominator variable.
        
        Returns:
            str: The quotient, either as an integer or a symbolic fraction.
        """
        if variable_one.get_variable() == variable_two.get_variable():
            result = variable_one.get_coefficient() // variable_two.get_coefficient()
            return f"{result}"
        else:
            term_one = f"{variable_one.get_coefficient()}{variable_one.get_variable()}"
            term_two = f"{variable_two.get_coefficient()}{variable_two.get_variable()}"
            return f"{term_one}/{term_two}"
        

    def __pow__(variable_one, exponent):
        """
        Raise a Variable to a given power.
        
        Args:
            variable_one (Variable): The base variable.
            exponent (int): The exponent to which the variable is raised.
        
        Returns:
            str: The variable raised to the given power, represented in symbolic form.
        """
        variable_one_coefficient = variable_one.get_coefficient()
        variable_one_variable = variable_one.get_variable()
        return f"{variable_one_coefficient}{variable_one_variable}^{exponent}"
    

var1 = Variable(3,"X")
print(var1 ** 2)