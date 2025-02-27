class Variable:
    """
    A symbolic representation of a variable that supports arithmetic operations.
    """

    __slots__ = ["__coefficient", "__variable"]

    def __init__(self, coefficient, variable):
        """Initialize a Variable with a coefficient and symbolic name."""
        self.__coefficient = coefficient
        self.__variable = variable

    def get_coefficient(self):
        """Return the coefficient of the variable."""
        return self.__coefficient

    def get_variable(self):
        """Return the symbolic variable."""
        return self.__variable

    def __add__(variable_one, variable_two):
        """Add two Variables if they share the same symbolic name."""
        if variable_one.get_variable() == variable_two.get_variable():
            result = variable_one.get_coefficient() + variable_two.get_coefficient()
            return f"{result}{variable_one.get_variable()}"
        raise ValueError("Cannot add variables with different symbolic names.")
