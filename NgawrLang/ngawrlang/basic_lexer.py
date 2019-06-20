from sly import Lexer

class BasicLexer(Lexer):
    tokens = { NAME, NUMBER, STRING, IF, THEN, ELSE, FOR, FUN, TO, ARROW, EQEQ, PRINT }
    ignore = '\t '

    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';' }

    # Define tokens
    IF = r'UPAMA'
    THEN = r'SAK WISE'
    ELSE = r'SAK LIYANE'
    FOR = r'KANGGO'
    FUN = r'FUNGSI'
    TO = r'KANGGE'
    PRINT = r'CETAK'
    ARROW = r'->'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'

    EQEQ = r'=='

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'#.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def newline(self,t ):
        self.lineno = t.value.count('\n')
