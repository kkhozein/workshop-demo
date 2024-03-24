# Always start by importing Pedal
from pedal import *

# example from the workshop
unit_test('cube_elements',
            ([[1, 2, 3]], [1, 8, 27]),
            ([[1]], [1]),
            ([[4, 4, 4]], [64, 64, 64]),
            ([[0]], [0]),
            ([[]], []))

# ... More instructor logic can go here ...
