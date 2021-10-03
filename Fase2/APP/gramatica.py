# -----------------------------------------------------------------------------
#   Analizador Lexico
# -------------------------------------------------------------------------------
reserved = {
    'Elements' : 'TELEMENTS',
    'element' : 'TELEMENT',
    'type' : 'TTYPE',
    'item' : 'TITEM',
    'Carnet' : 'TCARNET',
    'DPI' : 'TDPI',
    'Nombre' : 'TNOMBRE',
    'Carrera' : 'TCARRERA',
    'Password' : 'TPASSWORD',
    'Creditos' : 'TCREDITOS',
    'Edad' : 'TEDAD',
    'Descripcion' : 'TDESCRIPCION',
    'Materia' : 'TMATERIA',
    'Fecha' : 'TFECHA',
    'Hora' : 'THORA',
    'Estado' : 'TESTADO',
    'Correo' : 'TCORREO'
 }

tokens = [
    'LQUESTION' ,'RQUESTION','DOLAR', 'ID', 'EQUALS', 'QUOTATION_MARKS', 'NUMBER','NORMSTRING', 'DATE', 'HOUR'
] + list(reserved.values())

# Tokens
t_LQUESTION  = r'\¿'
t_RQUESTION  = r'\?'
t_DOLAR  = r'\$'
t_EQUALS  = r'='
t_QUOTATION_MARKS = r'\"'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
        # print("Number: " + str(t.value))
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


def t_NORMSTRING(t):
    r'\"(\\.|[^"\\])*\"'
    # print("String: '%s'" % t.value)
    return t

def t_Date(t):
    r'\s+(?=\d{2}(?:\d{2})?/\d{1,2}/\d{1,2}\b)'
    return t

def t_HORA(t):
    r'(?=(?:\b[01]\d|2[0-3]):[0-5]\d\b)'
    return t
# def t_NAME(t):
#     r'[a-zA-Z_][a-zA-Z0-9_]*'
#     try:
#         t.value = t.value
#     except ValueError:
#         print("problemas de identificador %d", t.value)
#         t.value = 0
#     return t

# Ignored characters
t_ignore = ' \t\r\n'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import PLY.lex as lex
import re
lexer = lex.lex(reflags=re.IGNORECASE)

#----------------------------------------------------------------------------
# Analizador Sintactico
#----------------------------------------------------------------------------
from Estructuras import Lista
from Estructuras import Nodo

# Lists for save the information about users and tasks
user_list = Lista.List()
task_list = Lista.List()

# This node allows to store information about one user or task
element_node = Nodo.Nodo()

# dictionary of names
names = {}

def p_statement_group(t):
    'statement : LQUESTION TELEMENTS RQUESTION elementos LQUESTION DOLAR TELEMENTS RQUESTION'
    print('Ok')

def p_elementos_group(t):
    """elementos : elementos elemento
                 | elemento
    """
    # t[0] = t[1]
    # if len(t) == 2:
    #     t[0] = [t[1]]
    # else:
    #     t[0] = t[1]
    #     t[0].append(t[2])

def p_elemento(t):
    'elemento : LQUESTION TELEMENT  tipoElemento RQUESTION items LQUESTION DOLAR TELEMENT RQUESTION'

    if t[3] == "user":
        user_list.insertValue(element_node.Carnet, element_node.DPI, element_node.Nombre, element_node.Carrera, element_node.Password,
                              element_node.Creditos, element_node.Edad, element_node.Correo, element_node.Descripcion, element_node.Materia,
                              element_node.Fecha, element_node.Hora, element_node.Estado)
    else:
        task_list.insertValue(element_node.Carnet, element_node.DPI, element_node.Nombre, element_node.Carrera, element_node.Password,
                              element_node.Creditos, element_node.Edad, element_node.Correo, element_node.Descripcion, element_node.Materia,
                              element_node.Fecha, element_node.Hora, element_node.Estado)
    element_node.clean_values()

def p_tipoElemento(t):
    """tipoElemento : TTYPE EQUALS NORMSTRING
    """
    t[0] = t[3].replace('"', '').replace(' ', '')


def p_items(t):
    """items : items item
    """
    t[0] = t[2]

def p_items_2(t):
    """items : item
    """
    t[0] = t[1]

def p_item(t):
    """item : LQUESTION TITEM tipeItem EQUALS valueItem DOLAR RQUESTION
    """
    if t[3].lower() == "carnet":
        element_node.Carnet = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "dpi":
        element_node.DPI = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "nombre":
        element_node.Nombre = t[5].replace('"', '')
    elif t[3].lower() == "carrera":
        element_node.Carrera = t[5].replace('"', '')
    elif t[3].lower() == "password":
        element_node.Password = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "creditos":
        element_node.Creditos = t[5]
    elif t[3].lower() == "edad":
        element_node.Edad = t[5]
    elif t[3].lower() == "correo":
        element_node.Correo = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "descripcion":
        element_node.Descripcion = t[5].replace('"', '')
    elif t[3].lower() == "materia":
        element_node.Materia = t[5].replace('"', '')
    elif t[3].lower() == "fecha":
        element_node.Fecha = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "hora":
        element_node.Hora = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "estado":
        element_node.Estado = t[5].replace('"', '').replace(' ', '')

    t[0] = element_node

def p_valueItem(t):
    """valueItem : NORMSTRING
                 | NUMBER
                 """
    t[0] = t[1]

def p_tipeItem(t):
    """tipeItem : TCARNET
                | TDPI
                | TNOMBRE
                | TCARRERA
                | TPASSWORD
                | TCREDITOS
                | TEDAD
                | TDESCRIPCION
                | TMATERIA
                | TFECHA
                | THORA
                | TESTADO
                | TCORREO
                """
    t[0] = t[1]

def p_error(t):
    print("Syntax error at '%s'" % t.value)

import PLY.yacc as yacc
parser = yacc.yacc()

'''f = open("D:\Quincho\VI Semestre\EDD\LabEDD\Estudiantes.txt", "r", encoding="utf-8")
input = f.read()
print(input)
parser.parse(input)'''