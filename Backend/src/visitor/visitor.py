from src.ast.node import *
from src.ast.symTable import SymTable


class Visitor:
    global_symtable: SymTable
    ambit_symtable: SymTable
    correct: bool = True
    filename: str

    def __init__(self, filename: str, ambit: SymTable = None):
        if ambit:
            self.ambit_symtable = ambit
        else:
            self.ambit_symtable = SymTable('base')
        self.global_symtable = SymTable('base')
        self.filename = filename
        
    def visit(self, node):
        if isinstance(node, Program):
            self.visitProgram(node)
        # elif isinstance(node, Identifier):
        #     self.visitIdentifier(node)
        # elif isinstance(node, VariableDeclarator):
        #     self.visitVariableDeclarator(node)
        # elif isinstance(node, BinaryExpression):
        #     self.visitBinaryExpression(node)
        # elif isinstance(node, LogicalExpression):
        #     self.visitLogicalExpression(node)
        # elif isinstance(node, Assignment):
        #     self.visitAssignment(node)
        # elif isinstance(node, CallFunction):
        #     self.visitCallFunction(node)
        # elif isinstance(node, functionParam):
        #     self.visitfunctionParam(node)
        # elif isinstance(node, returnStmt):
        #     self.visitreturnStmt(node)
        # elif isinstance(node, functionDeclaration):
        #     self.visitfunctionDeclaration(node)
        # elif isinstance(node, IfStmt):
        #     self.visitIfStmt(node)
        # elif isinstance(node, whileStmt):
        #     self.visitwhileStmt(node)
        # elif isinstance(node, DibujarAST):
        #     self.visitDibujarAST(node)
        # elif isinstance(node, DibujarEXP):
        #     self.visitDibujarEXP(node)
        # elif isinstance(node, DibujarTS):
        #     self.visitDibujarTS(node)
            