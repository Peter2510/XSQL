from src.instrucciones.funcion.call_function import CallFunction
from src.instrucciones.usarDB import usarDB
from ..expresiones import binaria
from ..instrucciones.funcion import function_declaration
from src.instrucciones.crearTabla import crearTabla
from src.instrucciones.createdb import createDB
from src.instrucciones.procedure.create_procedure import ProcedureDeclaration
from src.instrucciones.procedure.call_procedure import CallProcedure
from src.instrucciones.procedure.alter_procedure import AlterProcedure
from src.instrucciones.truncate.truncateDB import truncateDB
from src.instrucciones.truncate.truncateTabla import truncateTabla
from src.instrucciones.drop.dropDB import dropDB
from src.instrucciones.drop.dropTabla import dropTable
from src.instrucciones.Alter.alterTable import alterTable
from src.instrucciones.insert.insert import insertInstruccion
from src.instrucciones.update.update import updateInstruccion

from src.ast import (
    Select, FromClause, Table,
    WhereClause, AllColumns, TableColumn,
    AliasSelect, SelectAssign, Program,
    ColumnAssignments, Update, Delete,
    SQLUnaryExpression, SQLBinaryExpression, SQLLogicalExpression
)

from src.funciones import (
    Cas, Concatenar, Contar, Hoy, Substraer, Suma
)

from .visitor import Visitor
from src.instrucciones.funcion.function_declaration import FunctionDeclaration
from src.instrucciones.funcion.alter_function import AlterFunction
from src.instrucciones.funcion.variable_declaration import VariableDeclaration
from src.instrucciones.funcion.set import Set_
from src.instrucciones.funcion.return_ import Return_
from src.instrucciones.case.else_case import ElseCase
from src.instrucciones.case.when import When
from src.instrucciones.case.stm_case import StmCase
from src.instrucciones.conditionals.else_if_ import ElseIf_
from src.instrucciones.conditionals.else_ import Else_
from src.instrucciones.conditionals.if_ import If_
from src.instrucciones.conditionals.stm_if import StmIf
from src.instrucciones.while_.stm_while import StmWhile
from src.expresiones.primitivos import Primitivo
import datetime


class C3DVisitor(Visitor):
    def __init__(self, environment):
        super().__init__(environment)
        self.temp = 0
        self.label = 0
        self.code = ""

    def visit(self, node, environment):

        if isinstance(node, binaria.Binaria):
            return self.visitBinaria(node, environment)
        elif isinstance(node, Cas):
            return self.visitCas(node, environment)
        elif isinstance(node, Concatenar):
            return self.visitConcatenar(node, environment)
        elif isinstance(node, Contar):
            return self.visitContar(node, environment)
        elif isinstance(node, Hoy):
            return self.visitHoy(node, environment)
        elif isinstance(node, Substraer):
            return self.visitSubstraer(node, environment)
        elif isinstance(node, Suma):
            return self.visitSuma(node, environment)
        elif isinstance(node, crearTabla):
            return self.visitCrearTabla(node, environment)
        elif isinstance(node, createDB):
            return self.visitCreateDB(node, environment)
        elif isinstance(node, truncateDB):
            return self.visitTruncateDB(node, environment)
        elif isinstance(node, truncateTabla):
            return self.visitTruncateTabla(node, environment)
        elif isinstance(node, dropDB):
            return self.visitDropDB(node, environment)
        elif isinstance(node, dropTable):
            return self.visitDropTable(node, environment)
        elif isinstance(node, alterTable):
            return self.visitAlterTable(node, environment)
        elif isinstance(node, insertInstruccion):
            return self.visitInsertInstruccion(node, environment)
        elif isinstance(node, updateInstruccion):
            return self.visitUpdateInstruccion(node, environment)
        elif isinstance(node, StmWhile):
            return self.visitWhile(node, environment)

        elif isinstance(node, binaria.Binaria):
            return self.visitLogico(node, environment)

        elif isinstance(node, Primitivo):
            return self.visitPrimitivo(node, environment)

        elif isinstance(node, binaria.Binaria):
            return self.visitRelacional(node, environment)

        elif isinstance(node, function_declaration.FunctionDeclaration):
            return self.visitFunctionDeclaration(node, environment)

        elif isinstance(node, AlterFunction):
            return self.visitAlterFunction(node, environment)

        elif isinstance(node, CallFunction):
            return self.visitCallFunction(node, environment)

        elif isinstance(node, Return_):
            return self.visitReturn(node, environment)

        elif isinstance(node, Set_):
            return self.visitSet(node, environment)

        elif isinstance(node, VariableDeclaration):
            return self.visitVariableDeclaration(node, environment)

        elif isinstance(node, Else_):
            return self.visitElse(node, environment)

        elif isinstance(node, ElseIf_):
            return self.visitElseIf(node, environment)

        elif isinstance(node, If_):
            return self.visitIf(node, environment)

        elif isinstance(node, StmIf):
            return self.visitStmIf(node, environment)

        elif isinstance(node, ElseCase):
            return self.visitElseCase(node, environment)

        elif isinstance(node, StmCase):
            return self.visitStmCase(node, environment)

        elif isinstance(node, When):
            return self.visitWhen(node, environment)

        elif isinstance(node, Program):
            return self.visitProgram(node, environment)

        return "fn()"

    def new_temp(self):
        temp_str = f"t{self.temp}"
        self.temp += 1
        return temp_str

    def new_label(self):
        label_str = f"L{self.label}"
        self.label += 1
        return label_str

    def next_label(self, value):
        return f"L{self.label + value}"

    def append(self, code):
        if code is not None and len(code) > 0:
            self.code += f"{code}\n"

    def visitFunctionDeclaration(self, node: FunctionDeclaration, environment):
        self.append(f"{node.id}:")
        self.append("BEGIN")
        self.body_code(node.body, environment)
        self.append("END")

    def visitAlterFunction(self, node: AlterFunction, environment):
        self.append(f"{node.id}:")
        self.append("BEGIN")
        self.body_code(node.body, environment)
        self.append("END")

    def visitVariableDeclaration(self, node: VariableDeclaration, environment):
        # variable_type = node.type
        # node_expr = None
        # if isinstance(variable_type, String_):
        #     type_str = str(variable_type.type)
        #     variable_type.size.accept(self, environment)
        #     node_expr = variable_type.size
        #     variable_type = str(f"{type_str}")
        # else:
        #     variable_type = str(node.type)
        #
        # node.nd = self.graph.newItem(f"{node.id} {variable_type}")
        # if node_expr is not None and node_expr.nd is not None:
        #     self.graph.newLink(node.nd, node_expr.nd)
        pass

    def visitSet(self, node: Set_, environment):
        expr_code = self.visit(node.valor, environment)
        self.append("{} = {}".format(node.id, expr_code))

    def visitReturn(self, node: Return_, environment):
        # node.nd = self.graph.newItem("RETURN")
        # node_expr = node.instruction.nd if node.instruction.nd is not None else self.graph.newItem("expr")
        # self.graph.newLink(node.nd, node_expr)
        pass

    def visitStmIf(self, node, environment):
        self.visit(node.get_if(), environment)

        if node.list_elseif is not None:
            for stmt_else in node.list_elseif:
                self.visit(stmt_else, environment)

        if node.else_ is not None:
            self.visit(node.else_, environment)

    def visitIf(self, node: If_, environment):
        expr_code = self.visit(node.condition, environment)
        if_false_label = self.new_label()
        end_if_label = self.next_label(1)  # Usar la misma lógica que en visitElse
        self.append("ifFalse {} goto {}".format(expr_code, if_false_label))
        self.body_code(node.instructions, environment)
        self.append(f"goto {end_if_label}")
        self.append(f"{if_false_label}:")

    def visitElseIf(self, node: ElseIf_, environment):
        expr_code = self.visit(node.condition, environment)
        elif_false_label = self.new_label()
        end_elif_label = self.next_label(1)  # Usar la misma lógica que en visitElse
        self.append("ifFalse {} goto {}".format(expr_code, elif_false_label))
        self.body_code(node.instructions, environment)
        self.append(f"goto {end_elif_label}")
        self.append(f"{elif_false_label}:")

    def visitElse(self, node: Else_, environment):
        else_label = self.new_label()
        self.append(f"{else_label}:")
        self.body_code(node.instructions, environment)
        self.append(f"{self.next_label(0)}:")

    def body_code(self, instructions, environment):
        for stmt in instructions:
            if isinstance(stmt, list):
                for stmt_lst in stmt:
                    self.visit(stmt_lst, environment)
            else:
                self.visit(stmt, environment)
        pass

    def visitWhen(self, node: When, environment):
        # node.nd = self.graph.newItem("WHEN")
        # node.condition.accept(self, environment)
        # node_expr = node.condition.nd if node.condition.nd is not None else self.graph.newItem("expr")
        # self.graph.newLink(node.nd, node_expr)
        # self.body_node(node.nd, node.instructions, environment, True)
        pass

    def visitElseCase(self, node: ElseCase, environment):
        # node.nd = self.graph.newItem("ELSE_CASE")
        # self.body_node(node.nd, node.instructions, environment, True)
        pass

    def visitStmCase(self, node: StmCase, environment):
        # node.nd = self.graph.newItem("STMT_CASE")
        #
        # for when_stmt in node.list_when:
        #     self.graph.newLink(node.nd, self.node_none(when_stmt))
        #
        # if node.else_case is not None:
        #     self.graph.newLink(node.nd, self.node_none(node.else_case))
        pass

    def visitWhile(self, node: StmWhile, environment):
        # node.nd = self.graph.newItem("WHILE")
        # node_expr = node.condicion.nd if node.condicion.nd is not None else self.graph.newItem("expr")
        # self.graph.newLink(node.nd, node_expr)
        # self.body_node(node.nd, node.instrucciones, environment)
        pass

    def visitBinaria(self, node, environment):
        left_code = self.visit(node.opIzq, environment)
        right_code = self.visit(node.opDer, environment)
        t = self.new_temp()
        self.append(f"{t} = {left_code} {node.tipoOp} {right_code}")
        return t

    def visitPrimitivo(self, node: Primitivo, environment):
        if not isinstance(node.valor, (int, str, float, bool, datetime.date, datetime.datetime)):
            node.valor.accept(self, environment)
            return node.valor.code if node.valor is not None else ""
        else:
            return f"{node.valor}"

    def visitContar(self, node, environment):
        return str(node)

    def visitSuma(self, node, environment):
        return str(node)

    def visitSubstraer(self, node, environment):
        return str(node)

    def visitHoy(self, node, environment):
        return str(node)

    def visitConcatenar(self, node, environment):
        return str(node)

    def visitCas(self, node, environment):
        return str(node)

    def visitCallFunction(self, node, environment):
        return f"{node.id}"
