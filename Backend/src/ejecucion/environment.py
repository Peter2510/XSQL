from prettytable import PrettyTable
from src.ejecucion.datatype import *
from datetime import datetime

class Environment:
    def __init__(self, father):
        self.father = father
        self.db = None
        self.bases = []
        self.simbolos = []
        self.tablaSimbolos = []

