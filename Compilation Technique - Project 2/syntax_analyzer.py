import ply.yacc as yacc
from lexical_analyzer import tokens

# Start symbol
def p_program(p):
    '''program : statements'''
    p[0] = p[1]

# Multiple statements
def p_statements(p):
    '''statements : statement
                  | statement SEMICOLON
                  | statement SEMICOLON statements'''
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 3:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

# Individual statement
def p_statement(p):
    '''statement : print_statement
                 | cat_statement
                 | assignment
                 | expression
                 | while_loop
                 | if_block'''
    p[0] = p[1]

# Print statement
def p_print_statement(p):
    '''print_statement : PRINT LPAREN STRING RPAREN'''
    p[0] = ('print', p[3])

# Cat statement
def p_cat_statement(p):
    '''cat_statement : CAT LPAREN cat_arguments RPAREN'''
    p[0] = ('cat', p[3])

# Cat arguments
def p_cat_arguments(p):
    '''cat_arguments : expression
                     | expression COMMA cat_arguments'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

# Variable assignment
def p_assignment(p):
    '''assignment : ID ASSIGN expression'''
    p[0] = ('assign', p[1], p[3])

# Expressions
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression DIVIDE expression
                  | expression MOD expression
                  | expression GT expression
                  | expression LTE expression
                  | expression NEQ expression'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_group(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = ('number', int(p[1]))

def p_expression_string(p):
    '''expression : STRING'''
    p[0] = ('string', p[1])

def p_expression_id(p):
    '''expression : ID'''
    p[0] = ('id', p[1])

# While loop
def p_while_loop(p):
    '''while_loop : WHILE LPAREN expression RPAREN block'''
    p[0] = ('while', p[3], p[5])

# If-else block
def p_if_block(p):
    '''if_block : IF LPAREN expression RPAREN block
                | IF LPAREN expression RPAREN block ELSE block'''
    if len(p) == 6:
        p[0] = ('if', p[3], p[5], None)
    else:
        p[0] = ('if', p[3], p[5], p[7])

# Block of statements within braces
def p_block(p):
    '''block : LCURLY statements RCURLY
             | LCURLY RCURLY'''
    if len(p) == 3:  # Empty block
        p[0] = []
    else:  # Block with statements
        p[0] = p[2]

# Error handling
def p_error(p):
    print(f"Syntax error at '{p.value}' line {p.lineno}" if p else "Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Parsing function
def parse(data):
    return parser.parse(data)
