#functional

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)
    
    
    # How does this solution ensure data immutability? because you can track the changes (append)
    # Is this solution a pure function? Why or why not? yes because the values will not change on return
    # Is this solution a higher order function? Why or why not? yes, sorted is higher order
    # Would it have been easier to solve this problem using a different programming style? probably not
    # Why in particular is functional programming a helpful paradigm when solving this problem? it is more maintainable
    
#OOP

class Podracer:

    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    # Define a repair() method that will update the condition of the podracer to "repaired".
    def repair(self):
        self.condition = "repaired"


# Define a new class, AnakinsPod that inherits the Podracer class.


class AnakinsPod(Podracer):

    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price)

    # but also contains a special method called boost that will multiply max_speed by 2.
    def boost(self):
        self.max_speed *= 2


# Define another class that inherits Podracer and call this one SebulbasPod.
class SebulbasPod(Podracer):

    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price)


#This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".

    def flame_jet(self, other):
        other.condition = "trashed"
