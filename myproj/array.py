class Array(object):
    def __init__(self, array_string):
        self.array_string = array_string

    def sum(self, size):
        numbers = [int(number) for number in self.array_string.split(' ')]
        if size != len(numbers):
            raise Exception('array size is not matched')
        return sum(numbers)
