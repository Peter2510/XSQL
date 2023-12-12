class SymbolTable(list):
    def __init__(self, parent=None):
        super().__init__()
        if parent:
            self.extend(parent)

    def add(self, variable):
        self.append(variable)

    def get_by_id(self, id):
        return next((v for v in self if v.id == id), None)

    def contains(self, id):
        return any(v.id == id for v in self)