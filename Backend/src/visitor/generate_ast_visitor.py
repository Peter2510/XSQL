import gvgen
from .visitor import Visitor
from src.instrucciones.crearTabla import crearTabla
from src.instrucciones.createdb import createDB
from src.instrucciones.funcion.function_declaration import FunctionDeclaration
from src.instrucciones.funcion.alter_function import AlterFunction
from src.instrucciones.procedure.create_procedure import ProcedureDeclaration
from src.instrucciones.procedure.call_procedure import CallProcedure
from src.instrucciones.funcion.call_function import CallFunction
from src.instrucciones.procedure.alter_procedure import AlterProcedure
from src.instrucciones.truncate.truncateDB import truncateDB
from src.instrucciones.truncate.truncateTabla import truncateTabla
from src.instrucciones.drop.dropDB import dropDB
from src.instrucciones.drop.dropTabla import dropTable
from src.instrucciones.Alter.alterTable import alterTable
from src.instrucciones.usarDB import usarDB
from src.ast import (Select, Delete, FromClause, WhereClause, SQLUnaryExpression, SQLBinaryExpression,
                     SQLLogicalExpression, AliasSelect, TableColumn, Update)
from src.funciones import (Cas, Concatenar, Contar, Hoy, Substraer, Suma)
from src.instrucciones.insert.insert import insertInstruccion
from src.instrucciones.update.update import updateInstruccion
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
from src.instrucciones.funcion.string_ import String_
from src.expresiones.primitivos import Primitivo
import datetime

# from src.expresiones.binaria import Binaria


class GenerateASTVisitor(Visitor):
    def __init__(self, environment):
        super().__init__(environment)
        self.graph = gvgen.GvGen()
        self.root = self.graph.newItem("XSQL")

    def get_graph(self):
        return self.graph

    def visitProgram(self, node, environment):
        for stmt in node.statements:
            self.graph.newLink(self.root, self.node_none(stmt))

    def visitFromClause(self, node: FromClause, environment):
        from_clause_node = self.graph.newItem("FROM")
        for table in node.tables:
            table_node = self.graph.newItem(table.id)
            self.graph.newLink(from_clause_node, table_node)

        node.nd = from_clause_node

    def visitWhereClause(self, node: WhereClause, environment):
        where_clause_node = self.graph.newItem("WHERE")
        self.graph.newLink(where_clause_node, node.expr.nd)
        node.nd = where_clause_node

    def visitAllColumns(self, node, environment):
        node.nd = self.graph.newItem("*")

    def visitAliasSelect(self, node: AliasSelect, environment):
        node.nd = self.graph.newItem(node.id)
        self.graph.newLink(node.nd, node.expr.nd)

    def visitTableColumn(self, node: TableColumn, environment):
        node.nd = self.graph.newItem(f"{node.table}.{node.id}")

    def visitSQLBinaryExpression(self, node: SQLBinaryExpression, environment):
        node.nd = self.graph.newItem(node.operator)
        self.graph.newLink(node.nd, node.left.nd)
        self.graph.newLink(node.nd, node.right.nd)

    def visitSQLLogicalExpression(self, node, environment):
        self.visitSQLBinaryExpression(node, environment)

    def visitSQLUnaryExpression(self, node: SQLUnaryExpression, environment):
        if not isinstance(node.argument, (int, str, float, bool, datetime.date, datetime.datetime)):
            node.nd = node.argument.nd if (
                    node.argument is not None and node.argument.nd is not None) else self.graph.newItem(
                "Call")
        else:
            node.nd = self.graph.newItem(f"{node.argument}")

    def visitCas(self, node: Cas, environment):
        node.nd = self.graph.newItem("CAS")
        self.graph.newLink(node.nd, node.expr.nd)

    def visitConcatenar(self, node: Concatenar, environment):
        node.nd = self.graph.newItem("CONCATENA")
        for expr in node.expr_lst:
            self.graph.newLink(node.nd, expr.nd)

    def visitContar(self, node: Contar, environment):
        node.nd = self.graph.newItem("CONTAR")

    def visitHoy(self, node: Hoy, environment):
        node.nd = self.graph.newItem("HOY")

    def visitSubstraer(self, node: Substraer, environment):
        node.nd = self.graph.newItem("SUBSTRAER")
        self.graph.newLink(node.nd, node.value.nd)

    def visitSuma(self, node: Suma, environment):
        node.nd = self.graph.newItem("SUMA")
        if not isinstance(node.value, int):
            self.graph.newLink(node.nd, node.value.nd)
        else:
            node_suma = self.graph.newItem(node.value)
            self.graph.newLink(node.nd, node_suma)

    def visitSelect(self, node: Select, environment):
        select_node = self.graph.newItem("SELECT")
        columns_node = self.graph.newItem("COLUMNS")
        self.graph.newLink(select_node, columns_node)
        for column in node.columns:
            self.graph.newLink(columns_node, column.nd)

        if node.from_clause is not None:
            self.graph.newLink(select_node, node.from_clause.nd)

        if node.where_clause is not None:
            self.graph.newLink(select_node, node.where_clause.nd)

        node.nd = select_node

    def visitDelete(self, node: Delete, environment):
        node.nd = self.graph.newItem("DELETE")

        from_node = self.graph.newItem("FROM")
        node_id = self.graph.newItem(node.table)
        self.graph.newLink(from_node, node_id)
        self.graph.newLink(node.nd, from_node)
        self.graph.newLink(node.nd, node.where_clause.nd)

    def visitCrearTabla(self, node: crearTabla, environment):
        node.nd = self.graph.newItem(f"CREAR TABLA: {node.nombre}")

        for column in node.listaAtributos:
            column_str = [str(item) for item in column]
            node_column = self.graph.newItem(" ".join(column_str))
            self.graph.newLink(node.nd, node_column)

    def visitCreateDB(self, node: createDB, environment):
        node.nd = self.graph.newItem(f"CREAR DB: {node.nombre}")

    def set_param(self, param, environment):
        node_type = param.type
        node_expr = None
        if isinstance(node_type, String_):
            type_str = str(node_type.type)
            node_type.size.accept(self, environment)
            node_expr = node_type.size
            node_type = str(f"{type_str}")
        else:
            node_type = str(param.type)

        node_param = self.graph.newItem(f"{param.id} {node_type}")
        if node_expr is not None and node_expr.nd is not None:
            self.graph.newLink(node_param, node_expr.nd)

        return node_param

    def visitFunctionDeclaration(self, node: FunctionDeclaration, environment):
        node.nd = self.graph.newItem(f"DECL {node.id}()")

        node_params = self.graph.newItem("PARAMS")
        self.graph.newLink(node.nd, node_params)
        for param in node.params:
            node_param = self.set_param(param, environment)
            self.graph.newLink(node_params, node_param)

        self.body_node(node.nd, node.body, environment, True)

    def visitAlterFunction(self, node: AlterFunction, environment):
        node.nd = self.graph.newItem(f"ALTER {node.id}")

        node_params = self.graph.newItem("PARAMS")
        self.graph.newLink(node.nd, node_params)
        for param in node.params:
            node_param = self.set_param(param, environment)
            self.graph.newLink(node_params, node_param)

        self.body_node(node.nd, node.body, environment, True)

    def visitCreateProcedure(self, node: ProcedureDeclaration, environment):
        node.nd = self.graph.newItem(f"PROCEDURE {node.id}")

        node_params = self.graph.newItem("PARAMS")
        self.graph.newLink(node.nd, node_params)
        for param in node.params:
            node_param = self.set_param(param, environment)
            self.graph.newLink(node_params, node_param)

        self.body_node(node.nd, node.body, environment, True)

    def visitCallProcedure(self, node: CallProcedure, environment):
        node.nd = self.graph.newItem(f"CALL PROCEDURE {node.id}")

        node_params = self.graph.newItem("PARAMS")
        self.graph.newLink(node.nd, node_params)
        for _param in node.parametros:
            _param.accept(self, environment)
            node_param = self.node_none(_param)
            self.graph.newLink(node_params, node_param)

    def visitCallFunction(self, node: CallFunction, environment):
        node.nd = self.graph.newItem(f"CALL FUNCTION {node.id}")

        node_params = self.graph.newItem("PARAMS")
        self.graph.newLink(node.nd, node_params)
        for _param in node.parametros:
            _param.accept(self, environment)
            node_param = self.node_none(_param)
            self.graph.newLink(node_params, node_param)

    def visitAlterProcedure(self, node: AlterProcedure, environment):
        node.nd = self.graph.newItem(f"ALTER {node.id}")

        node_params = self.graph.newItem("PARAMS")
        self.graph.newLink(node.nd, node_params)
        for param in node.params:
            node_param = self.set_param(param, environment)
            self.graph.newLink(node_params, node_param)

        self.body_node(node.nd, node.body, environment, True)

    def visitTruncateDB(self, node: truncateDB, environment):
        node.nd = self.graph.newItem("TRUNCATE DB")

        node_id = self.graph.newItem(f"{node.nombre}")
        self.graph.newLink(node.nd, node_id)

    def visitTruncateTabla(self, node: truncateTabla, environment):
        node.nd = self.graph.newItem("TRUNCATE TABLA")

        node_id = self.graph.newItem(f"{node.nombre}")
        self.graph.newLink(node.nd, node_id)

    def visitDropDB(self, node: dropDB, environment):
        node.nd = self.graph.newItem("TRUNCATE DB")

        node_id = self.graph.newItem(f"{node.nombre}")
        self.graph.newLink(node.nd, node_id)

    def visitDropTable(self, node: dropTable, environment):
        node.nd = self.graph.newItem("TRUNCATE TABLA")

        node_id = self.graph.newItem(f"{node.nombre}")
        self.graph.newLink(node.nd, node_id)

    def visitAlterTable(self, node: alterTable, environment):
        node.nd = self.graph.newItem("ALTER TABLA")

        node_id = self.graph.newItem(f"{node.nombre}")
        self.graph.newLink(node.nd, node_id)
        op = node.opcionAlter
        text = "ADD COLUMN" if isinstance(op, list) else "DROP COLUMN"
        name = op[0] if isinstance(op, list) else op
        node_op = self.graph.newItem(f"{text} {name}")
        self.graph.newLink(node.nd, node_op)

    def visitUsar(self, node: usarDB, environment):
        node.nd = self.graph.newItem("USAR DB")

        node_id = self.graph.newItem(f"{node.nombre}")
        self.graph.newLink(node.nd, node_id)

    def visitInsertInstruccion(self, node: insertInstruccion, environment):
        node.nd = self.graph.newItem("INSERT")

        node_columns = self.graph.newItem("COLUMNAS")
        self.graph.newLink(node.nd, node_columns)
        try:
            for column in node.atributos:
                node_col = self.graph.newItem(str(column))
                self.graph.newLink(node_columns, node_col)

            node_valores = self.graph.newItem("VALORES")
            self.graph.newLink(node.nd, node_valores)
            for value in node.parametros:
                node_value = self.graph.newItem(str(value))
                self.graph.newLink(node_valores, node_value)
        except Exception as e:
            print('insert ast', e)

    def visitUpdate(self, node: Update, environment):
        node.nd = self.graph.newItem("UPDATE")

        node_id = self.graph.newItem(node.table)
        self.graph.newLink(node.nd, node_id)
        try:
            node_set = self.graph.newItem("SET")
            self.graph.newLink(node.nd, node_set)
            for assign in node.assignments:
                node_assign = self.graph.newItem("=")
                node_id = assign.column_ref.nd
                node_expr = assign.expr.nd
                self.graph.newLink(node_set, node_assign)
                self.graph.newLink(node_assign, node_id)
                self.graph.newLink(node_assign, node_expr)

            node_where = node.where_clause.nd
            self.graph.newLink(node.nd, node_where)

        except Exception as e:
            print('update ast', e)

    def visitVariableDeclaration(self, node: VariableDeclaration, environment):
        variable_type = node.type
        node_expr = None
        if isinstance(variable_type, String_):
            type_str = str(variable_type.type)
            variable_type.size.accept(self, environment)
            node_expr = variable_type.size
            variable_type = str(f"{type_str}")
        else:
            variable_type = str(node.type)

        node.nd = self.graph.newItem(f"{node.id} {variable_type}")
        if node_expr is not None and node_expr.nd is not None:
            self.graph.newLink(node.nd, node_expr.nd)

    def visitSet(self, node: Set_, environment):
        node.nd = self.graph.newItem(f"SET VARIABLE {node.id}")
        node.valor.accept(self, environment)
        node_expr = node.valor.nd if node.valor.nd is not None else self.graph.newItem("expr")
        self.graph.newLink(node.nd, node_expr)

    def visitReturn(self, node: Return_, environment):
        node.nd = self.graph.newItem("RETURN")
        node_expr = node.instruction.nd if node.instruction.nd is not None else self.graph.newItem("expr")
        self.graph.newLink(node.nd, node_expr)

    def visitIf(self, node: If_, environment):
        node.nd = self.graph.newItem("IF")
        node.condition.accept(self, environment)
        node_expr = node.condition.nd if node.condition.nd is not None else self.graph.newItem("expr")
        self.graph.newLink(node.nd, node_expr)

        self.body_node(node.nd, node.instructions, environment, True)

    def visitElseIf(self, node: ElseIf_, environment):

        node.nd = self.graph.newItem("ELSE IF")
        node.condition.accept(self, environment)
        node_expr = node.condition.nd if node.condition.nd is not None else self.graph.newItem("expr")
        self.graph.newLink(node.nd, node_expr)

        self.body_node(node.nd, node.instructions, environment, True)

    def visitElse(self, node: Else_, environment):
        node.nd = self.graph.newItem("ELSE")
        self.body_node(node.nd, node.instructions, environment, True)

    def body_node(self, parent_node, instructions, environment, visit=False):
        node_body = self.graph.newItem("BODY")
        self.graph.newLink(parent_node, node_body)
        for stmt in instructions:
            if isinstance(stmt, list):
                for stmt_lst in stmt:
                    if visit:
                        stmt_lst.accept(self, environment)
                    self.graph.newLink(node_body, self.node_none(stmt_lst))
            else:
                if visit:
                    stmt.accept(self, environment)
                    if isinstance(stmt, (StmWhile, StmIf)):
                        self.visit(stmt, environment)
                self.graph.newLink(node_body, self.node_none(stmt))

    def node_none(self, node):
        if node is None or node.nd is None:
            return self.graph.newItem("STMT")

        return node.nd

    def visitStmIf(self, node: StmIf, environment):
        node.nd = self.graph.newItem("STMT IF")
        self.graph.newLink(node.nd, self.node_none(node.get_if()))
        if node.list_elseif is not None:
            for else_lst in node.list_elseif:
                self.graph.newLink(node.nd, self.node_none(else_lst))

        if node.else_ is not None:
            self.graph.newLink(node.nd, self.node_none(node.else_))

    def visitWhen(self, node: When, environment):
        node.nd = self.graph.newItem("WHEN")
        node.condition.accept(self, environment)
        node_expr = node.condition.nd if node.condition.nd is not None else self.graph.newItem("expr")
        self.graph.newLink(node.nd, node_expr)
        self.body_node(node.nd, node.instructions, environment, True)

    def visitElseCase(self, node: ElseCase, environment):
        node.nd = self.graph.newItem("ELSE_CASE")
        self.body_node(node.nd, node.instructions, environment, True)

    def visitStmCase(self, node: StmCase, environment):
        node.nd = self.graph.newItem("STMT_CASE")

        for when_stmt in node.list_when:
            self.graph.newLink(node.nd, self.node_none(when_stmt))

        if node.else_case is not None:
            self.graph.newLink(node.nd, self.node_none(node.else_case))

    def visitWhile(self, node: StmWhile, environment):
        node.nd = self.graph.newItem("WHILE")
        node_expr = node.condicion.nd if node.condicion.nd is not None else self.graph.newItem("expr")
        self.graph.newLink(node.nd, node_expr)
        self.body_node(node.nd, node.instrucciones, environment)

    def visitBinaria(self, node, environment):
        node.nd = self.graph.newItem(node.tipoOp)
        self.graph.newLink(node.nd, self.node_none(node.opIzq))
        self.graph.newLink(node.nd, self.node_none(node.opDer))

    def visitPrimitivo(self, node: Primitivo, environment):
        if not isinstance(node.valor, (int, str, float, bool, datetime.date, datetime.datetime)):
            node.valor.accept(self, environment)
            node.nd = node.valor.nd if (
                    node.valor is not None and node.valor.nd is not None) else self.graph.newItem(
                "Call")
        else:
            node.nd = self.graph.newItem(f"{node.valor}")
