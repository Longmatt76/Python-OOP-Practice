

"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    """ builds the constructor, start indicates the starting number"""

    def __init__(self, start):
        self.start = start
        self.counter = start

    """builds a readable string of info when debugging or accessing via console"""
    
    def __repr__(self) -> str:
        return f"SerialGenerator start={self.start} next={self.start +1}"

    """increments by one for each time the funcion is called """

    def generate(self):
        self.start += 1
        return self.start

    """resets the count to the initial value"""

    def reset(self):
        self.start = self.counter
        return self.start
