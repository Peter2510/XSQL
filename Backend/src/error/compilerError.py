class CompilerError:

    def __init__(self, type, descrip, line, column):
        self.type = type
        self.desc = descrip
        self.line = line
        self.column = column

    def __str__(self) -> str:
        return 'ERROR ' + self.type + ' - ' + self.desc + ' [' + str(self.line) + ', ' + str(self.column) + '];'
    
    def toString(self):
        return self.type + ' - ' + self.desc + ' [' + str(self.line) + ', ' + str(self.column) + '];'
    
