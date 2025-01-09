import ply.lex as lex

# Daftar token
tokens = (
    'PRINT', 'CAT', 'NUMBER', 'ASSIGN', 'MOD', 'NEQ', 'WHILE', 'IF', 'ELSE', 'STRING',
    'LPAREN', 'RPAREN', 'LCURLY', 'RCURLY', 'SEMICOLON', 'COMMA', 'PLUS', 'LTE', 'ID',
    'DIVIDE', 'GT', 'ARROW'
)

# Definisi token
t_ASSIGN = r'<-'  # This matches the <-

# Other token definitions...
t_MOD = r'%'
t_NEQ = r'!='
t_GT = r'>'
t_STRING = r'\"([^"\\]|(\\.)|(\n))*\"'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_SEMICOLON = r';'
t_COMMA = r','
t_PLUS = r'\+'
t_DIVIDE = r'/'
t_LTE = r'<='
t_NUMBER = r'\d+'

# Define ID handling and keyword mapping
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value == 'if':
        t.type = 'IF'
    elif t.value == 'else':
        t.type = 'ELSE'
    elif t.value == 'while':
        t.type = 'WHILE'
    elif t.value == 'cat':
        t.type = 'CAT'
    elif t.value == 'print':
        t.type = 'PRINT'
    return t

# Ignore whitespace and comments
t_ignore = ' \t'
t_ignore_COMMENT = r'\#.*'

# Handling newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

# Build lexer
lexer = lex.lex()
