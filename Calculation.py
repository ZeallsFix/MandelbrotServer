from math import pow
from math import sqrt


class Mandelbrot(object):
    """ Calculation for Mandelbrot"""
    
    def __init__(self, max_iterations, increase_per_increment, min_x_coordinate, max_x_coordinate, min_y_coordinate,
                 max_y_coordinate):
        self.max_iterations = max_iterations
        self.increase_per_increment = increase_per_increment
        self.min_x_coordinate = min_x_coordinate
        self.max_x_coordinate = max_x_coordinate
        self.min_y_coordinate = min_y_coordinate
        self.max_y_coordinate = max_y_coordinate
    
    def calculate_coordinate(self, max_iterations, increase_per_increment, min_x_coordinate, max_x_coordinate,
                             min_y_coordinate, max_y_coordinate):
        x_coordinate = min_x_coordinate
        y_coordinate = min_y_coordinate
        result_array = []
        while y_coordinate > max_y_coordinate:
            while x_coordinate > max_x_coordinate:
                result_array.append(self.complex_calculation(x_coordinate, y_coordinate, max_iterations))
                x_coordinate -= increase_per_increment
            y_coordinate -= increase_per_increment
            x_coordinate = min_x_coordinate
        return result_array
    
    def start_calc(self):
        array = self.calculate_coordinate(self.max_iterations, self.increase_per_increment, self.min_x_coordinate,
                                          self.max_x_coordinate, self.min_y_coordinate, self.max_y_coordinate)
        return array
    
    def complex_calculation(self, x_coordinate, y_coordinate, max_iterations):
        iteration = 0
        result = 0
        while iteration < max_iterations and result < float(2):
            previous_result = result
            result = previous_result + sqrt(pow(x_coordinate, 2) + pow(y_coordinate, 2))
            iteration += 1
        return iteration
    
    def return_as_json(self, array):
        return {'iterations': 'test', 'array': array}