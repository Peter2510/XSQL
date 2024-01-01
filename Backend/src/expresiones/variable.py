
class Variable():

    def __init__(self):
        self.id = None
        self.type = None
        self.value = None
        

    def toString(self):
        return f"{self.id} {self.type} {self.value}"