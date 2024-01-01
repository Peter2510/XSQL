from src.ejecucion.type import Type

class SymTable:
    def __init__(self,upperAmbit=None):
        self.symbolVars = {}
        self.symbolFuncs = {}
        self.symbolProc = {}
        self.upperAmbit = upperAmbit

    def getSymbolVars(self):
        return self.symbolVars

    def addUpperAmbit(self, upperTable):
        self.upperAmbit = upperTable

    def getVariable(self, id, childTable=None):
        variable = self.symbolVars.get(id)
        if variable is not None:
            return variable
        elif self.upperAmbit is not None and self.upperAmbit.getVariable(id):
            return self.upperAmbit.getVariable(id)
        return None

    def getFunction(self, id, globalTable=None):
        funcs = self.symbolFuncs.get(id)
        if funcs is not None and funcs.get(id) is not None:
            return funcs[id]
        elif self.upperAmbit is not None and self.upperAmbit.getFunction(id):
            return self.upperAmbit.getFunction(id)
        return None

    def addVariable(self, variable):
        if self.isInsertableVar(variable.id.name):
            self.symbolVars[variable.id.name] = variable
            return True
        return False

    def addFunc(self, func):
        if self.isInsertableFunc(func):
            if self.symbolFuncs.get(func.id) is None:
                self.symbolFuncs[func.id] = {}
            self.symbolFuncs[func.id][func.nameForTable] = func
            return True
        return False

    def isInsertableVar(self, id):
        return self.symbolVars.get(id) is None

    def isInsertableFunc(self, func):
        funcs = self.symbolFuncs.get(func)
        if funcs is None:
            return True
        return funcs.get(id) is None

    def itExistsThisFunctionId(self, id):
        funcs = self.symbolFuncs.get(id)
        if funcs is not None:
            return True
        if self.upperAmbit is None:
            return False
        return self.upperAmbit.itExistsThisFunctionId(id)