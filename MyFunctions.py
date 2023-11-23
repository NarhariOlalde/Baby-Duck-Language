
from antlr4 import *
import copy

class SemanticCube:
    """
    Clase que representa el cubo semántico utilizado en la verificación de tipos en un compilador.
    """
    def __init__(self):
        self.cube = {
            ('int', 'int', '+'): 'int',
            ('int', 'float', '+'): 'float',
            ('float', 'int', '+'): 'float',
            ('float', 'float', '+'): 'float',
            ('int', 'int', '-'): 'int',
            ('int', 'float', '-'): 'float',
            ('float', 'int', '-'): 'float',
            ('float', 'float', '-'): 'float',
            ('int', 'int', '*'): 'int',
            ('int', 'float', '*'): 'float',
            ('float', 'int', '*'): 'float',
            ('float', 'float', '*'): 'float',
            ('int', 'int', '/'): 'int',
            ('int', 'float', '/'): 'float',
            ('float', 'int', '/'): 'float',
            ('float', 'float', '/'): 'float',
            ('int', 'int', '<'): 'bool',
            ('int', 'float', '<'): 'bool',
            ('float', 'int', '<'): 'bool',
            ('float', 'float', '<'): 'bool',
            ('int', 'int', '>'): 'bool',
            ('int', 'float', '>'): 'bool',
            ('float', 'int', '>'): 'bool',
            ('float', 'float', '>'): 'bool',
            ('int', 'int', '!='): 'bool',
            ('int', 'float', '!='): 'bool',
            ('float', 'int', '!='): 'bool',
            ('float', 'float', '!='): 'bool',
            ('int', 'int', '='): 'int',
            ('int', 'float', '='): 'error',
            ('float', 'int', '='): 'float',
            ('float', 'float', '='): 'float',
        }

    def get_type(self, left, right, operator):
            """
            Devuelve el tipo resultante de aplicar el operador especificado a los operandos dados.

            Args:
                left (str): El tipo del operando izquierdo.
                right (str): El tipo del operando derecho.
                operator (str): El operador a aplicar.

            Returns:
                str: El tipo resultante de aplicar el operador a los operandos, o 'error' si no es posible.
            """
            return self.cube.get((left, right, operator), 'error')

class VariableTable:
    """
    Clase que representa una tabla de variables para un compilador.
    """
    def __init__(self):
        self.variables = {"global": {}}
        
    def set_scope(self, scope):
        if scope not in self.variables:
            self.variables[scope] = {}
    
    def add_variable(self, name, var_type, scope):
        if name in self.variables[scope]:
            raise Exception(f"Variable {name} already declared.")
        self.variables[scope][name] = {
            'type': var_type,
            'address': next(AVAIL)
        } 
    
    def get_variable_type(self, name, scope):
        return self.variables[scope][name].get('type', None)
    
    def get_variable_value(self, name, scope):
        return self.variables[scope][name].get('value', None)

    def set_variable_value(self, name, value, scope):
        self.variables[scope][name]['value'] = value
    
    def clean_variables(self, scope):
        self.variables[scope].clear()
    
    def find_scope(self, name):
        for scope in self.variables:
            if name in self.variables[scope]:
                return scope
        return None
    
class FunctionTable:
    def __init__(self):
        self.functions = {}

    def add_function(self, func_id, func_type):
        if func_id in self.functions:
            raise Exception(f"Function {func_id} already declared.")
        self.functions[func_id] = {
            "type": func_type,
            "params": {},
            "quad_count": 0,
        }
        return True

    def get_function(self, func_id):
        return self.functions.get(func_id, None)
    
    def get_function_type(self, func_id):
        return self.functions[func_id]["type"]
    
    def get_function_params(self, func_id):
        return self.functions[func_id]["params"]
    
    def get_function_param(self, func_id, param_id):
        return self.functions[func_id]["params"].get(param_id, None)
    
    def get_function_param_id(self, func_id, index):
        return list(self.functions[func_id]["params"].keys())[index]
    
    def get_function_param_type(self, func_id, param_id):
        return self.functions[func_id]["params"][param_id]
    
    def get_function_param_count(self, func_id):
        return len(self.functions[func_id]["params"])

    def clean_functions(self):
        self.functions.clear()

class Quadruple:
    def __init__(self):
        self.quadruples = []
        self.quadruple_count = 0
    
    def push(self, quadruple):
        self.quadruples.append(quadruple)
        self.quadruple_count += 1
        

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise Exception("Stack is empty")
    
    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        raise Exception("Stack is empty")

    
variable_table = VariableTable()
function_table = FunctionTable()
semantic_cube = SemanticCube()
paramater_table = {}
local_variables = {}
varStack = []
varStackLocal = []
current_scope = "global"
quadruples = Quadruple()
PilaO = Stack()
POper = Stack()
PTypes = Stack()
PJumps = Stack()
QuadStack = Stack()
ResultStack = Stack()
param_counter = 0


#temp AVAIL
AVAIL = iter(range(1000, 2000))
memory = {}

def setScope(scope):
    global current_scope
    current_scope = scope
    variable_table.set_scope(scope)
    
    

def saveVariable(var_id):
    if var_id in variable_table.variables[current_scope] or var_id in varStack:
        raise Exception("Variable already declared")
    varStack.append(var_id)
    
    

def saveParameter(param_id, param_type):
    paramater_table[param_id] = param_type
    variable_table.add_variable(param_id, param_type, current_scope)
    
    

def saveVariableLocal(var_id):
    if var_id in variable_table.variables[current_scope] or var_id in varStackLocal:
        raise Exception("Variable already declared")
    varStackLocal.append(var_id)
    

def saveTypeLocal(var_type):
    for var_id in varStackLocal:
        local_variables[var_id] = var_type
        variable_table.add_variable(var_id, var_type, current_scope)
    varStackLocal.clear()
    
    
    
def insertVariablesLocales():
    function_table.functions[current_function]["local"] = copy.deepcopy(local_variables)
    function_table.functions[current_function]["local_count"] = len(local_variables)

def insertQuadCount():
    function_table.functions[current_function]["quad_count"] = quadruples.quadruple_count

def insertParameters():
    function_table.functions[current_function]["params"] = copy.deepcopy(paramater_table)
    function_table.functions[current_function]["param_count"] = len(paramater_table)



def saveFunction(func_id, func_type = None):
    global current_function
    current_function = func_id
    if func_id in function_table.functions:
        raise Exception("Function already declared")
    if func_type is not None:
        function_table.add_function(func_id, func_type)
    else:
        function_table.add_function(func_id, "void")
    
    

def saveType(var_type):
    for var_id in varStack:
        variable_table.add_variable(var_id, var_type, current_scope)
    varStack.clear()
    

def endScopeVars():
    local_variables.clear()
    paramater_table.clear()
    quadruples.push(["ENDFUNC", None, None, None])

def proveFunction(id):
    global current_function
    global current_scope
    if id not in function_table.functions:
        raise Exception("Function not declared")
    else:
        current_function = id

def generateERA():
    global param_counter
    param_counter = 0
    quad = ["ERA", current_function]
    quadruples.push(quad)

def arguments():
    argument = PilaO.pop()
    argument_type = PTypes.pop()
    param_id = function_table.get_function_param_id(current_function, param_counter)
    param_type = function_table.get_function_param_type(current_function, param_id)
    if argument_type != param_type:
        raise Exception("Invalid type")
    else:
        quad = ["PARAM", argument, None, param_counter]
        quadruples.push(quad)
    
def addK():
    global param_counter
    param_counter += 1

def isNull():
    if param_counter == 0 and function_table.get_function_param_count(current_function) == 0:
        quad = ["GOSUB", current_function, None, None]
        quadruples.push(quad)
    elif param_counter + 1 != function_table.get_function_param_count(current_function):
        raise Exception("Invalid number of arguments")
    else:
        quad = ["GOSUB", current_function, None, None]
        quadruples.push(quad)
        

def addMultDiv(operator):
    POper.push(operator)
    
    

def addSumSub(operator):
    POper.push(operator)
    
    

def addCompare(operator):
    POper.push(operator)
    
    

def addPrint():
    POper.push("print")
    
def printExp():
    if not POper.is_empty():
        if POper.peek() == "print":
            operand = PilaO.pop()
            print_ = POper.pop()
            quad = [print_, operand, None, None]
            quadruples.push(quad)
            
        else:
            raise Exception("Missing print")
    else:
        raise Exception("Missing print")

def sumRes():
    if not POper.is_empty():
        
        if POper.peek() == "+" or POper.peek() == "-":
            right_operand = PilaO.pop()
            right_type = PTypes.pop()
            left_operand = PilaO.pop()
            left_type = PTypes.pop()
            operator = POper.pop()
            result_type = semantic_cube.get_type(left_type, right_type, operator)
            if result_type != "error":
                result = next(AVAIL)
                quad = [operator, left_operand, right_operand, result]
                quadruples.push(quad)
                PilaO.push(result)
                PTypes.push(result_type)
                #If any of the operands is a temporal, free it
                
            else:
                raise Exception("Invalid type")

def multDiv():
    if not POper.is_empty():
        if POper.peek() == "*" or POper.peek() == "/":
            right_operand = PilaO.pop()
            right_type = PTypes.pop()
            left_operand = PilaO.pop()
            left_type = PTypes.pop()
            operator = POper.pop()
            result_type = semantic_cube.get_type(left_type, right_type, operator)
            if result_type != "error":
                result = next(AVAIL)
                quad = [operator, left_operand, right_operand, result]
                quadruples.push(quad)
                PilaO.push(result)
                PTypes.push(result_type)
                #If any of the operands is a temporal, free it?
                
            else:
                raise Exception("Invalid type")

def compareExp():
    
    if not POper.is_empty():
        
        if POper.peek() == "<" or POper.peek() == ">" or POper.peek() == "!=":
            right_operand = PilaO.pop()
            right_type = PTypes.pop()
            left_operand = PilaO.pop()
            left_type = PTypes.pop()
            operator = POper.pop()
            result_type = semantic_cube.get_type(left_type, right_type, operator)
            if result_type != "error":
                result = next(AVAIL)
                quad = [operator, left_operand, right_operand, result]
                quadruples.push(quad)
                PilaO.push(result)
                PTypes.push(result_type)
                #If any of the operands is a temporal, free it
            else:
                raise Exception("Invalid type")
                
    

def addParenthesis():
    POper.push("(")


def closeParenthesis():
    if not POper.is_empty():
        if POper.peek() == "(":
            POper.pop()
            
        else:
            raise Exception("Missing parenthesis")
    else:
        raise Exception("Missing parenthesis")

def addBrackets():
    POper.push("[")

def closeBrackets():
    if not POper.is_empty():
        if POper.peek() == "[":
            POper.pop()
            
        else:
            raise Exception("Missing brackets")
    else:
        raise Exception("Missing brackets")

def gosubFunction(func_id):
    if func_id in function_table.functions:
        quad = ["GOSUB", func_id]
        quadruples.push(quad)
        
        
        
    else:
        raise Exception("Function not declared")

def addKey():
    POper.push("{")

def closeKey():
    if not POper.is_empty():
        if POper.peek() == "{":
            POper.pop()
            
        else:
            raise Exception("Missing key")
    else:
        raise Exception("Missing key")


def assignExpression(id):
    global current_scope
    operand = PilaO.pop()
    if operand in variable_table.variables[current_scope]:
        typeOfAsssignValue = variable_table.get_variable_type(operand, current_scope)
    else:
        typeOfAsssignValue = identifyNumberType(operand)
    idType = variable_table.get_variable_type(id, current_scope)
    if operand in variable_table.variables[current_scope]:
        operand = operand
    else:
        operand = parseNumber(operand)
    if semantic_cube.get_type(idType, typeOfAsssignValue, '=') == "error":
        raise Exception("Invalid type")
    else:
        quad = ["=", operand, None, id]
        quadruples.push(quad)

def stackConstant(number):
    result = parseNumber(number)
    PilaO.push(result)
    PTypes.push(identifyNumberType(number))

def stackId(id):
    PilaO.push(id)
    PTypes.push(variable_table.get_variable_type(id, current_scope))

def identifyNumberType(num_str):
    try:
        int(num_str)
        return "int"
    except ValueError:
        try:
            float(num_str)
            return "float"
        except ValueError:
            return "Not a valid number"

def parseNumber(num_str):
    if type(num_str) is int or type(num_str) is float:
        return num_str
    try:
        return int(num_str)
    except ValueError:
        try:
            return float(num_str)
        except ValueError:
            return "Not a valid number"
    
def endGlobal():
    function_table.clean_functions()
    variable_table.clean_variables("global")

def csTrue():
    exp_type = PTypes.pop()
    if exp_type != "bool":
        raise Exception("Invalid type")
    else:
        result = PilaO.pop()
        quad = ["GOTOF", result, None, None]
        quadruples.push(quad)
        PJumps.push(quadruples.quadruple_count - 1)

def GOTO():
    quad = ["GOTO", None]
    quadruples.push(quad)
    false = PJumps.pop()
    PJumps.push(quadruples.quadruple_count - 1)
    FILL(false, quadruples.quadruple_count)

def FILL(end, fill):
    if quadruples.quadruples[end][0] == "GOTO":
        quadruples.quadruples[end][1] = fill
    elif quadruples.quadruples[end][0] == "GOTOF":
        quadruples.quadruples[end][3] = fill

def pJumpF():
    end = PJumps.pop()
    FILL(end, quadruples.quadruple_count)

def saveString(string):
    PilaO.push(string)
    PTypes.push("string")

def whileLoop():
    PJumps.push(quadruples.quadruple_count)

def functionGoto():
    quad = ["GOTO", None]
    quadruples.push(quad)
    PJumps.push(quadruples.quadruple_count - 1)

def expresionWhile():
    exp_type = PTypes.pop()
    if exp_type != "bool":
        raise Exception("Invalid type")
    else:
        result = PilaO.pop()
        quad = ["GOTOF", result, None, None]
        quadruples.push(quad)
        PJumps.push(quadruples.quadruple_count - 1)

def endWhile():
    end = PJumps.pop()
    returnToWhile = PJumps.pop()
    quad = ["GOTO", returnToWhile]
    quadruples.push(quad)
    FILL(end, quadruples.quadruple_count)

def solveQuadruples():
    cont = 0
    cont_quad = 0
    temp_quads = copy.deepcopy(quadruples.quadruples)
    for quad in quadruples.quadruples:
        print(f'Original Quad: {cont_quad}, Quad:{quad}')
        cont_quad += 1
    cont_quad = 0
    while True:
        if cont >= quadruples.quadruple_count:
            break
        quad = temp_quads[cont]
        if not QuadStack.is_empty() and (quad[1] == QuadStack.peek() or quad[2] == QuadStack.peek()):
            if quad[1] == QuadStack.peek():
                quad[1] = ResultStack.pop()
                QuadStack.pop()
            elif quad[2] == QuadStack.peek():
                quad[2] = ResultStack.pop()
                QuadStack.pop()
                quad[1] = ResultStack.pop()
                QuadStack.pop()
        
        try: 
            if type(quadruples.quadruples[cont][1]) is str:
                quad[1] = variable_table.get_variable_value(quadruples.quadruples[cont][1], current_scope)
                
            if type(quadruples.quadruples[cont][2]) is str:
                quad[2] = variable_table.get_variable_value(quadruples.quadruples[cont][2], current_scope)
        except:
            pass
        if quad[0] == "GOTOF":
            print(f'Quad:{cont_quad} Operator:{quad[0]} To:{quad[3]}')
            if quad[1] == False:
                cont = quad[3]
            else:
                cont += 1
        elif quad[0] == "GOTO":
            print(f'Quad:{cont_quad} Operator:{quad[0]} To:{quad[1]}')
            cont = quad[1]
        elif quad[0] == "print":
            print(f'Quad:{cont_quad} {quad[0]} {quad[1]}')
            print(quad[1])
            cont += 1
        elif quad[0] == "ENDFUNC":
            print(f'Quad:{cont_quad} {quad[0]}')
            cont += 1
        elif quad[0] == "GOSUB":
            print(f'Quad:{cont_quad} {quad[0]} To:{quad[1]}')
            cont += 1
        elif quad[0] == "ERA":
            print(f'Quad:{cont_quad} {quad[0]} Of:{quad[1]}')
            cont += 1    
        elif quad[0] == "PARAM":
            print(f'Quad:{cont_quad} {quad[0]} Of:{quad[1]} To:{quad[3]}')
            cont += 1
        else:
            if quad[0] == "+":
                result = quad[1] + quad[2]
                QuadStack.push(quad[3])
                quad[3] = result
                ResultStack.push(result)
                print(f'Quad:{cont_quad} Left:{quad[1]} Right:{quad[2]} Operator:{quad[0]} Result:{quad[3]}')
            if quad[0] == "-":
                result = quad[1] - quad[2]
                QuadStack.push(quad[3])
                quad[3] = result
                ResultStack.push(result)
                print(f'Quad:{cont_quad} Left:{quad[1]} Right:{quad[2]} Operator:{quad[0]} Result:{quad[3]}')
            if quad[0] == "*":
                result = quad[1] * quad[2]
                QuadStack.push(quad[3])
                quad[3] = result
                ResultStack.push(result)
                print(f'Quad:{cont_quad} Left:{quad[1]} Right:{quad[2]} Operator:{quad[0]} Result:{quad[3]}')
            if quad[0] == "/":
                result = quad[1] / quad[2]
                QuadStack.push(quad[3])
                quad[3] = result
                ResultStack.push(result)
                print(f'Quad:{cont_quad} Left:{quad[1]} Right:{quad[2]} Operator:{quad[0]} Result:{quad[3]}')
            if quad[0] == "<":
                result = quad[1] <= quad[2]
                QuadStack.push(quad[3])
                quad[3] = result
                ResultStack.push(result)
                print(f'Quad:{cont_quad} Left:{quad[1]} Right:{quad[2]} Operator:{quad[0]} Result:{quad[3]}')
            if quad[0] == ">":
                result = quad[1] >= quad[2]
                QuadStack.push(quad[3])
                quad[3] = result
                ResultStack.push(result)
                print(f'Quad:{cont_quad} Left:{quad[1]} Right:{quad[2]} Operator:{quad[0]} Result:{quad[3]}')
            if quad[0] == "!=":
                result = quad[1] != quad[2]
                QuadStack.push(quad[3])
                quad[3] = result
                ResultStack.push(result)
                print(f'Quad:{cont_quad} Left:{quad[1]} Right:{quad[2]} Operator:{quad[0]} Result:{quad[3]}')
            if quad[0] == "=":
                variable_table.get_variable_type(quad[3], variable_table.find_scope(quad[3]))
                if variable_table.get_variable_type(quad[3], variable_table.find_scope(quad[3])) == "int":
                    result = int(quad[1])
                else:
                    result = float(quad[1])
                variable_table.set_variable_value(quad[3], result, variable_table.find_scope(quad[3]))
                print(f'Quad:{cont_quad} Assign:{quad[1]} Operator:{quad[0]} To:{quad[3]}')
            cont += 1
        cont_quad += 1
    cont = 0
        
