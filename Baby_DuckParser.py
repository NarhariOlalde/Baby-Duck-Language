# Generated from Baby_Duck.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


from MyFunctions import *
    
def serializedATN():
    return [
        4,1,38,305,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,1,0,1,0,1,0,1,0,5,0,39,8,0,10,0,12,0,
        42,9,0,1,0,5,0,45,8,0,10,0,12,0,48,9,0,1,0,1,0,1,0,1,0,1,1,1,1,1,
        1,5,1,57,8,1,10,1,12,1,60,9,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,
        2,3,2,71,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,5,4,
        85,8,4,10,4,12,4,88,9,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,
        1,5,5,5,101,8,5,10,5,12,5,104,9,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,128,
        8,6,10,6,12,6,131,9,6,3,6,133,8,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,141,
        8,6,10,6,12,6,144,9,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,165,8,7,10,7,12,7,168,9,7,
        3,7,170,8,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,
        184,8,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,192,8,8,1,8,5,8,195,8,8,10,8,
        12,8,198,9,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,3,9,215,8,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,5,11,235,8,11,10,11,12,
        11,238,9,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,
        12,250,8,12,1,12,1,12,1,12,1,12,3,12,256,8,12,3,12,258,8,12,1,13,
        1,13,1,13,1,13,1,13,1,13,3,13,266,8,13,5,13,268,8,13,10,13,12,13,
        271,9,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,3,14,282,8,
        14,5,14,284,8,14,10,14,12,14,287,9,14,1,14,1,14,1,14,1,15,1,15,1,
        15,1,15,1,15,5,15,297,8,15,10,15,12,15,300,9,15,1,15,1,15,1,15,1,
        15,0,0,16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,2,2,0,2,2,
        8,8,1,0,24,25,315,0,32,1,0,0,0,2,53,1,0,0,0,4,70,1,0,0,0,6,72,1,
        0,0,0,8,78,1,0,0,0,10,94,1,0,0,0,12,112,1,0,0,0,14,152,1,0,0,0,16,
        176,1,0,0,0,18,203,1,0,0,0,20,219,1,0,0,0,22,231,1,0,0,0,24,257,
        1,0,0,0,26,269,1,0,0,0,28,285,1,0,0,0,30,298,1,0,0,0,32,33,6,0,-1,
        0,33,34,5,9,0,0,34,35,6,0,-1,0,35,36,5,33,0,0,36,40,5,31,0,0,37,
        39,3,8,4,0,38,37,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,
        0,41,46,1,0,0,0,42,40,1,0,0,0,43,45,3,12,6,0,44,43,1,0,0,0,45,48,
        1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,49,1,0,0,0,48,46,1,0,0,0,
        49,50,5,7,0,0,50,51,6,0,-1,0,51,52,3,2,1,0,52,1,1,0,0,0,53,54,5,
        17,0,0,54,58,6,1,-1,0,55,57,3,4,2,0,56,55,1,0,0,0,57,60,1,0,0,0,
        58,56,1,0,0,0,58,59,1,0,0,0,59,61,1,0,0,0,60,58,1,0,0,0,61,62,5,
        18,0,0,62,63,6,1,-1,0,63,64,6,1,-1,0,64,3,1,0,0,0,65,71,3,6,3,0,
        66,71,3,18,9,0,67,71,3,20,10,0,68,71,3,14,7,0,69,71,3,16,8,0,70,
        65,1,0,0,0,70,66,1,0,0,0,70,67,1,0,0,0,70,68,1,0,0,0,70,69,1,0,0,
        0,71,5,1,0,0,0,72,73,5,33,0,0,73,74,5,23,0,0,74,75,3,30,15,0,75,
        76,6,3,-1,0,76,77,5,31,0,0,77,7,1,0,0,0,78,79,5,6,0,0,79,80,5,33,
        0,0,80,86,6,4,-1,0,81,82,5,30,0,0,82,83,5,33,0,0,83,85,6,4,-1,0,
        84,81,1,0,0,0,85,88,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,89,1,
        0,0,0,88,86,1,0,0,0,89,90,5,32,0,0,90,91,5,2,0,0,91,92,6,4,-1,0,
        92,93,5,31,0,0,93,9,1,0,0,0,94,95,5,6,0,0,95,96,5,33,0,0,96,102,
        6,5,-1,0,97,98,5,30,0,0,98,99,5,33,0,0,99,101,6,5,-1,0,100,97,1,
        0,0,0,101,104,1,0,0,0,102,100,1,0,0,0,102,103,1,0,0,0,103,105,1,
        0,0,0,104,102,1,0,0,0,105,106,5,32,0,0,106,107,5,2,0,0,107,108,6,
        5,-1,0,108,109,6,5,-1,0,109,110,6,5,-1,0,110,111,5,31,0,0,111,11,
        1,0,0,0,112,113,7,0,0,0,113,114,5,33,0,0,114,115,6,6,-1,0,115,116,
        6,6,-1,0,116,117,5,15,0,0,117,132,6,6,-1,0,118,119,5,33,0,0,119,
        120,5,32,0,0,120,121,5,2,0,0,121,129,6,6,-1,0,122,123,5,30,0,0,123,
        124,5,33,0,0,124,125,5,32,0,0,125,126,5,2,0,0,126,128,6,6,-1,0,127,
        122,1,0,0,0,128,131,1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,0,130,
        133,1,0,0,0,131,129,1,0,0,0,132,118,1,0,0,0,132,133,1,0,0,0,133,
        134,1,0,0,0,134,135,5,16,0,0,135,136,6,6,-1,0,136,137,6,6,-1,0,137,
        138,5,19,0,0,138,142,6,6,-1,0,139,141,3,10,5,0,140,139,1,0,0,0,141,
        144,1,0,0,0,142,140,1,0,0,0,142,143,1,0,0,0,143,145,1,0,0,0,144,
        142,1,0,0,0,145,146,3,22,11,0,146,147,5,20,0,0,147,148,6,6,-1,0,
        148,149,6,6,-1,0,149,150,6,6,-1,0,150,151,5,31,0,0,151,13,1,0,0,
        0,152,153,5,33,0,0,153,154,6,7,-1,0,154,155,5,15,0,0,155,156,6,7,
        -1,0,156,169,6,7,-1,0,157,158,3,30,15,0,158,166,6,7,-1,0,159,160,
        5,30,0,0,160,161,6,7,-1,0,161,162,3,30,15,0,162,163,6,7,-1,0,163,
        165,1,0,0,0,164,159,1,0,0,0,165,168,1,0,0,0,166,164,1,0,0,0,166,
        167,1,0,0,0,167,170,1,0,0,0,168,166,1,0,0,0,169,157,1,0,0,0,169,
        170,1,0,0,0,170,171,1,0,0,0,171,172,5,16,0,0,172,173,6,7,-1,0,173,
        174,6,7,-1,0,174,175,5,31,0,0,175,15,1,0,0,0,176,177,5,14,0,0,177,
        178,5,15,0,0,178,179,6,8,-1,0,179,183,6,8,-1,0,180,184,3,30,15,0,
        181,182,5,37,0,0,182,184,6,8,-1,0,183,180,1,0,0,0,183,181,1,0,0,
        0,184,185,1,0,0,0,185,196,6,8,-1,0,186,187,5,30,0,0,187,191,6,8,
        -1,0,188,192,3,30,15,0,189,190,5,37,0,0,190,192,6,8,-1,0,191,188,
        1,0,0,0,191,189,1,0,0,0,192,193,1,0,0,0,193,195,6,8,-1,0,194,186,
        1,0,0,0,195,198,1,0,0,0,196,194,1,0,0,0,196,197,1,0,0,0,197,199,
        1,0,0,0,198,196,1,0,0,0,199,200,5,16,0,0,200,201,6,8,-1,0,201,202,
        5,31,0,0,202,17,1,0,0,0,203,204,5,12,0,0,204,205,5,15,0,0,205,206,
        6,9,-1,0,206,207,3,30,15,0,207,208,5,16,0,0,208,209,6,9,-1,0,209,
        210,6,9,-1,0,210,214,3,22,11,0,211,212,5,13,0,0,212,213,6,9,-1,0,
        213,215,3,22,11,0,214,211,1,0,0,0,214,215,1,0,0,0,215,216,1,0,0,
        0,216,217,5,31,0,0,217,218,6,9,-1,0,218,19,1,0,0,0,219,220,5,10,
        0,0,220,221,6,10,-1,0,221,222,5,15,0,0,222,223,6,10,-1,0,223,224,
        3,30,15,0,224,225,5,16,0,0,225,226,6,10,-1,0,226,227,6,10,-1,0,227,
        228,3,22,11,0,228,229,5,31,0,0,229,230,6,10,-1,0,230,21,1,0,0,0,
        231,232,5,17,0,0,232,236,6,11,-1,0,233,235,3,4,2,0,234,233,1,0,0,
        0,235,238,1,0,0,0,236,234,1,0,0,0,236,237,1,0,0,0,237,239,1,0,0,
        0,238,236,1,0,0,0,239,240,5,18,0,0,240,241,6,11,-1,0,241,23,1,0,
        0,0,242,243,5,15,0,0,243,244,6,12,-1,0,244,245,3,30,15,0,245,246,
        5,16,0,0,246,247,6,12,-1,0,247,258,1,0,0,0,248,250,7,1,0,0,249,248,
        1,0,0,0,249,250,1,0,0,0,250,255,1,0,0,0,251,252,5,3,0,0,252,256,
        6,12,-1,0,253,254,5,33,0,0,254,256,6,12,-1,0,255,251,1,0,0,0,255,
        253,1,0,0,0,256,258,1,0,0,0,257,242,1,0,0,0,257,249,1,0,0,0,258,
        25,1,0,0,0,259,260,3,24,12,0,260,265,6,13,-1,0,261,262,5,21,0,0,
        262,266,6,13,-1,0,263,264,5,22,0,0,264,266,6,13,-1,0,265,261,1,0,
        0,0,265,263,1,0,0,0,266,268,1,0,0,0,267,259,1,0,0,0,268,271,1,0,
        0,0,269,267,1,0,0,0,269,270,1,0,0,0,270,272,1,0,0,0,271,269,1,0,
        0,0,272,273,3,24,12,0,273,274,6,13,-1,0,274,27,1,0,0,0,275,276,3,
        26,13,0,276,281,6,14,-1,0,277,278,5,24,0,0,278,282,6,14,-1,0,279,
        280,5,25,0,0,280,282,6,14,-1,0,281,277,1,0,0,0,281,279,1,0,0,0,282,
        284,1,0,0,0,283,275,1,0,0,0,284,287,1,0,0,0,285,283,1,0,0,0,285,
        286,1,0,0,0,286,288,1,0,0,0,287,285,1,0,0,0,288,289,3,26,13,0,289,
        290,6,14,-1,0,290,29,1,0,0,0,291,292,3,28,14,0,292,293,6,15,-1,0,
        293,294,5,1,0,0,294,295,6,15,-1,0,295,297,1,0,0,0,296,291,1,0,0,
        0,297,300,1,0,0,0,298,296,1,0,0,0,298,299,1,0,0,0,299,301,1,0,0,
        0,300,298,1,0,0,0,301,302,3,28,14,0,302,303,6,15,-1,0,303,31,1,0,
        0,0,24,40,46,58,70,86,102,129,132,142,166,169,183,191,196,214,236,
        249,255,257,265,269,281,285,298
    ]

class Baby_DuckParser ( Parser ):

    grammarFileName = "Baby_Duck.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'float'", "'int'", "'var'", "'main'", "'void'", "'program'", 
                     "'while'", "'do'", "'if'", "'else'", "'print'", "'('", 
                     "')'", "'{'", "'}'", "'['", "']'", "'*'", "'/'", "'='", 
                     "'+'", "'-'", "'>'", "'<'", "'!='", "'.'", "','", "';'", 
                     "':'" ]

    symbolicNames = [ "<INVALID>", "TYPE_CONDITIONAL", "TYPE", "CTE", "FLOAT", 
                      "INT", "VAR", "MAIN", "VOID", "PROGRAM", "WHILE", 
                      "DO", "IF", "ELSE", "PRINT_WORD", "OPEN_PAREN", "CLOSE_PAREN", 
                      "OPEN_KEY", "CLOSE_KEY", "OPEN_BRACKET", "CLOSE_BRACKET", 
                      "MULT", "DIV", "EQUAL", "ADD", "SUB", "GREATER", "LESS", 
                      "DIFFERENT", "DOT", "COMMA", "SEMICOLON", "COLON", 
                      "ID", "LETTER", "DECIMAL", "NUMBER", "STRING", "WS" ]

    RULE_programa = 0
    RULE_body_end = 1
    RULE_statement = 2
    RULE_assign = 3
    RULE_vars = 4
    RULE_vars_func = 5
    RULE_funcs = 6
    RULE_f_call = 7
    RULE_print_ = 8
    RULE_condition = 9
    RULE_cycle = 10
    RULE_body = 11
    RULE_factor = 12
    RULE_termino = 13
    RULE_exp = 14
    RULE_expresion = 15

    ruleNames =  [ "programa", "body_end", "statement", "assign", "vars", 
                   "vars_func", "funcs", "f_call", "print_", "condition", 
                   "cycle", "body", "factor", "termino", "exp", "expresion" ]

    EOF = Token.EOF
    TYPE_CONDITIONAL=1
    TYPE=2
    CTE=3
    FLOAT=4
    INT=5
    VAR=6
    MAIN=7
    VOID=8
    PROGRAM=9
    WHILE=10
    DO=11
    IF=12
    ELSE=13
    PRINT_WORD=14
    OPEN_PAREN=15
    CLOSE_PAREN=16
    OPEN_KEY=17
    CLOSE_KEY=18
    OPEN_BRACKET=19
    CLOSE_BRACKET=20
    MULT=21
    DIV=22
    EQUAL=23
    ADD=24
    SUB=25
    GREATER=26
    LESS=27
    DIFFERENT=28
    DOT=29
    COMMA=30
    SEMICOLON=31
    COLON=32
    ID=33
    LETTER=34
    DECIMAL=35
    NUMBER=36
    STRING=37
    WS=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRAM(self):
            return self.getToken(Baby_DuckParser.PROGRAM, 0)

        def ID(self):
            return self.getToken(Baby_DuckParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(Baby_DuckParser.SEMICOLON, 0)

        def MAIN(self):
            return self.getToken(Baby_DuckParser.MAIN, 0)

        def body_end(self):
            return self.getTypedRuleContext(Baby_DuckParser.Body_endContext,0)


        def vars_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Baby_DuckParser.VarsContext)
            else:
                return self.getTypedRuleContext(Baby_DuckParser.VarsContext,i)


        def funcs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Baby_DuckParser.FuncsContext)
            else:
                return self.getTypedRuleContext(Baby_DuckParser.FuncsContext,i)


        def getRuleIndex(self):
            return Baby_DuckParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = Baby_DuckParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            functionGoto()
            self.state = 33
            self.match(Baby_DuckParser.PROGRAM)
            setScope("global")
            self.state = 35
            self.match(Baby_DuckParser.ID)
            self.state = 36
            self.match(Baby_DuckParser.SEMICOLON)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 37
                self.vars_()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==8:
                self.state = 43
                self.funcs()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self.match(Baby_DuckParser.MAIN)
            pJumpF()
            self.state = 51
            self.body_end()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_endContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_KEY(self):
            return self.getToken(Baby_DuckParser.OPEN_KEY, 0)

        def CLOSE_KEY(self):
            return self.getToken(Baby_DuckParser.CLOSE_KEY, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Baby_DuckParser.StatementContext)
            else:
                return self.getTypedRuleContext(Baby_DuckParser.StatementContext,i)


        def getRuleIndex(self):
            return Baby_DuckParser.RULE_body_end

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody_end" ):
                listener.enterBody_end(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody_end" ):
                listener.exitBody_end(self)




    def body_end(self):

        localctx = Baby_DuckParser.Body_endContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_body_end)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(Baby_DuckParser.OPEN_KEY)
            addKey()
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8589956096) != 0):
                self.state = 55
                self.statement()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
            self.match(Baby_DuckParser.CLOSE_KEY)
            closeKey()
            solveQuadruples()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(Baby_DuckParser.AssignContext,0)


        def condition(self):
            return self.getTypedRuleContext(Baby_DuckParser.ConditionContext,0)


        def cycle(self):
            return self.getTypedRuleContext(Baby_DuckParser.CycleContext,0)


        def f_call(self):
            return self.getTypedRuleContext(Baby_DuckParser.F_callContext,0)


        def print_(self):
            return self.getTypedRuleContext(Baby_DuckParser.Print_Context,0)


        def getRuleIndex(self):
            return Baby_DuckParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = Baby_DuckParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.condition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 67
                self.cycle()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 68
                self.f_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 69
                self.print_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(Baby_DuckParser.ID, 0)

        def EQUAL(self):
            return self.getToken(Baby_DuckParser.EQUAL, 0)

        def expresion(self):
            return self.getTypedRuleContext(Baby_DuckParser.ExpresionContext,0)


        def SEMICOLON(self):
            return self.getToken(Baby_DuckParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return Baby_DuckParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = Baby_DuckParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            localctx._ID = self.match(Baby_DuckParser.ID)
            self.state = 73
            self.match(Baby_DuckParser.EQUAL)
            self.state = 74
            self.expresion()
            assignExpression((None if localctx._ID is None else localctx._ID.text))
            self.state = 76
            self.match(Baby_DuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self._TYPE = None # Token

        def VAR(self):
            return self.getToken(Baby_DuckParser.VAR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(Baby_DuckParser.ID)
            else:
                return self.getToken(Baby_DuckParser.ID, i)

        def COLON(self):
            return self.getToken(Baby_DuckParser.COLON, 0)

        def TYPE(self):
            return self.getToken(Baby_DuckParser.TYPE, 0)

        def SEMICOLON(self):
            return self.getToken(Baby_DuckParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Baby_DuckParser.COMMA)
            else:
                return self.getToken(Baby_DuckParser.COMMA, i)

        def getRuleIndex(self):
            return Baby_DuckParser.RULE_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars" ):
                listener.enterVars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars" ):
                listener.exitVars(self)




    def vars_(self):

        localctx = Baby_DuckParser.VarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(Baby_DuckParser.VAR)
            self.state = 79
            localctx._ID = self.match(Baby_DuckParser.ID)
            saveVariable((None if localctx._ID is None else localctx._ID.text))
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 81
                self.match(Baby_DuckParser.COMMA)
                self.state = 82
                localctx._ID = self.match(Baby_DuckParser.ID)
                saveVariable((None if localctx._ID is None else localctx._ID.text))
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
            self.match(Baby_DuckParser.COLON)
            self.state = 90
            localctx._TYPE = self.match(Baby_DuckParser.TYPE)
            saveType((None if localctx._TYPE is None else localctx._TYPE.text))
            self.state = 92
            self.match(Baby_DuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vars_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self._TYPE = None # Token

        def VAR(self):
            return self.getToken(Baby_DuckParser.VAR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(Baby_DuckParser.ID)
            else:
                return self.getToken(Baby_DuckParser.ID, i)

        def COLON(self):
            return self.getToken(Baby_DuckParser.COLON, 0)

        def TYPE(self):
            return self.getToken(Baby_DuckParser.TYPE, 0)

        def SEMICOLON(self):
            return self.getToken(Baby_DuckParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Baby_DuckParser.COMMA)
            else:
                return self.getToken(Baby_DuckParser.COMMA, i)

        def getRuleIndex(self):
            return Baby_DuckParser.RULE_vars_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars_func" ):
                listener.enterVars_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars_func" ):
                listener.exitVars_func(self)




    def vars_func(self):

        localctx = Baby_DuckParser.Vars_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vars_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(Baby_DuckParser.VAR)
            self.state = 95
            localctx._ID = self.match(Baby_DuckParser.ID)
            saveVariableLocal((None if localctx._ID is None else localctx._ID.text))
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 97
                self.match(Baby_DuckParser.COMMA)
                self.state = 98
                localctx._ID = self.match(Baby_DuckParser.ID)
                saveVariableLocal((None if localctx._ID is None else localctx._ID.text))
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 105
            self.match(Baby_DuckParser.COLON)
            self.state = 106
            localctx._TYPE = self.match(Baby_DuckParser.TYPE)
            saveTypeLocal((None if localctx._TYPE is None else localctx._TYPE.text))
            insertVariablesLocales()
            insertQuadCount()
            self.state = 110
            self.match(Baby_DuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._TYPE = None # Token
            self._ID = None # Token

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(Baby_DuckParser.ID)
            else:
                return self.getToken(Baby_DuckParser.ID, i)

        def OPEN_PAREN(self):
            return self.getToken(Baby_DuckParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(Baby_DuckParser.CLOSE_PAREN, 0)

        def OPEN_BRACKET(self):
            return self.getToken(Baby_DuckParser.OPEN_BRACKET, 0)

        def body(self):
            return self.getTypedRuleContext(Baby_DuckParser.BodyContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(Baby_DuckParser.CLOSE_BRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(Baby_DuckParser.SEMICOLON, 0)

        def VOID(self):
            return self.getToken(Baby_DuckParser.VOID, 0)

        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(Baby_DuckParser.TYPE)
            else:
                return self.getToken(Baby_DuckParser.TYPE, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(Baby_DuckParser.COLON)
            else:
                return self.getToken(Baby_DuckParser.COLON, i)

        def vars_func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Baby_DuckParser.Vars_funcContext)
            else:
                return self.getTypedRuleContext(Baby_DuckParser.Vars_funcContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Baby_DuckParser.COMMA)
            else:
                return self.getToken(Baby_DuckParser.COMMA, i)

        def getRuleIndex(self):
            return Baby_DuckParser.RULE_funcs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncs" ):
                listener.enterFuncs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncs" ):
                listener.exitFuncs(self)




    def funcs(self):

        localctx = Baby_DuckParser.FuncsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            _la = self._input.LA(1)
            if not(_la==2 or _la==8):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 113
            localctx._ID = self.match(Baby_DuckParser.ID)
            saveFunction((None if localctx._ID is None else localctx._ID.text), (None if localctx._TYPE is None else localctx._TYPE.text))
            setScope((None if localctx._ID is None else localctx._ID.text))
            self.state = 116
            self.match(Baby_DuckParser.OPEN_PAREN)
            addParenthesis()
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 118
                localctx._ID = self.match(Baby_DuckParser.ID)
                self.state = 119
                self.match(Baby_DuckParser.COLON)
                self.state = 120
                localctx._TYPE = self.match(Baby_DuckParser.TYPE)
                saveParameter((None if localctx._ID is None else localctx._ID.text), (None if localctx._TYPE is None else localctx._TYPE.text))
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==30:
                    self.state = 122
                    self.match(Baby_DuckParser.COMMA)
                    self.state = 123
                    localctx._ID = self.match(Baby_DuckParser.ID)
                    self.state = 124
                    self.match(Baby_DuckParser.COLON)
                    self.state = 125
                    localctx._TYPE = self.match(Baby_DuckParser.TYPE)
                    saveParameter((None if localctx._ID is None else localctx._ID.text), (None if localctx._TYPE is None else localctx._TYPE.text))
                    self.state = 131
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 134
            self.match(Baby_DuckParser.CLOSE_PAREN)
            closeParenthesis()
            insertParameters()
            self.state = 137
            self.match(Baby_DuckParser.OPEN_BRACKET)
            addBrackets()
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 139
                self.vars_func()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 145
            self.body()
            self.state = 146
            self.match(Baby_DuckParser.CLOSE_BRACKET)
            closeBrackets()
            endScopeVars()
            setScope("global")
            self.state = 150
            self.match(Baby_DuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class F_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(Baby_DuckParser.ID, 0)

        def OPEN_PAREN(self):
            return self.getToken(Baby_DuckParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(Baby_DuckParser.CLOSE_PAREN, 0)

        def SEMICOLON(self):
            return self.getToken(Baby_DuckParser.SEMICOLON, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Baby_DuckParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(Baby_DuckParser.ExpresionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Baby_DuckParser.COMMA)
            else:
                return self.getToken(Baby_DuckParser.COMMA, i)

        def getRuleIndex(self):
            return Baby_DuckParser.RULE_f_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_call" ):
                listener.enterF_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_call" ):
                listener.exitF_call(self)




    def f_call(self):

        localctx = Baby_DuckParser.F_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_f_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            localctx._ID = self.match(Baby_DuckParser.ID)
            proveFunction((None if localctx._ID is None else localctx._ID.text))
            self.state = 154
            self.match(Baby_DuckParser.OPEN_PAREN)
            generateERA()
            addParenthesis()
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8640299016) != 0):
                self.state = 157
                self.expresion()
                arguments()
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==30:
                    self.state = 159
                    self.match(Baby_DuckParser.COMMA)
                    addK()
                    self.state = 161
                    self.expresion()
                    arguments()
                    self.state = 168
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 171
            self.match(Baby_DuckParser.CLOSE_PAREN)
            closeParenthesis()
            isNull()
            self.state = 174
            self.match(Baby_DuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._STRING = None # Token

        def PRINT_WORD(self):
            return self.getToken(Baby_DuckParser.PRINT_WORD, 0)

        def OPEN_PAREN(self):
            return self.getToken(Baby_DuckParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(Baby_DuckParser.CLOSE_PAREN, 0)

        def SEMICOLON(self):
            return self.getToken(Baby_DuckParser.SEMICOLON, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Baby_DuckParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(Baby_DuckParser.ExpresionContext,i)


        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(Baby_DuckParser.STRING)
            else:
                return self.getToken(Baby_DuckParser.STRING, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Baby_DuckParser.COMMA)
            else:
                return self.getToken(Baby_DuckParser.COMMA, i)

        def getRuleIndex(self):
            return Baby_DuckParser.RULE_print_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_" ):
                listener.enterPrint_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_" ):
                listener.exitPrint_(self)




    def print_(self):

        localctx = Baby_DuckParser.Print_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_print_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(Baby_DuckParser.PRINT_WORD)
            self.state = 177
            self.match(Baby_DuckParser.OPEN_PAREN)
            addParenthesis()
            addPrint()
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 15, 24, 25, 33]:
                self.state = 180
                self.expresion()
                pass
            elif token in [37]:
                self.state = 181
                localctx._STRING = self.match(Baby_DuckParser.STRING)
                saveString((None if localctx._STRING is None else localctx._STRING.text))
                pass
            else:
                raise NoViableAltException(self)

            printExp()
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 186
                self.match(Baby_DuckParser.COMMA)
                addPrint()
                self.state = 191
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3, 15, 24, 25, 33]:
                    self.state = 188
                    self.expresion()
                    pass
                elif token in [37]:
                    self.state = 189
                    localctx._STRING = self.match(Baby_DuckParser.STRING)
                    saveString((None if localctx._STRING is None else localctx._STRING.text))
                    pass
                else:
                    raise NoViableAltException(self)

                printExp()
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 199
            self.match(Baby_DuckParser.CLOSE_PAREN)
            closeParenthesis()
            self.state = 201
            self.match(Baby_DuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(Baby_DuckParser.IF, 0)

        def OPEN_PAREN(self):
            return self.getToken(Baby_DuckParser.OPEN_PAREN, 0)

        def expresion(self):
            return self.getTypedRuleContext(Baby_DuckParser.ExpresionContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(Baby_DuckParser.CLOSE_PAREN, 0)

        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Baby_DuckParser.BodyContext)
            else:
                return self.getTypedRuleContext(Baby_DuckParser.BodyContext,i)


        def SEMICOLON(self):
            return self.getToken(Baby_DuckParser.SEMICOLON, 0)

        def ELSE(self):
            return self.getToken(Baby_DuckParser.ELSE, 0)

        def getRuleIndex(self):
            return Baby_DuckParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = Baby_DuckParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(Baby_DuckParser.IF)
            self.state = 204
            self.match(Baby_DuckParser.OPEN_PAREN)
            addParenthesis()
            self.state = 206
            self.expresion()
            self.state = 207
            self.match(Baby_DuckParser.CLOSE_PAREN)
            closeParenthesis()
            csTrue()
            self.state = 210
            self.body()
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 211
                self.match(Baby_DuckParser.ELSE)
                GOTO()
                self.state = 213
                self.body()


            self.state = 216
            self.match(Baby_DuckParser.SEMICOLON)
            pJumpF()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CycleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(Baby_DuckParser.WHILE, 0)

        def OPEN_PAREN(self):
            return self.getToken(Baby_DuckParser.OPEN_PAREN, 0)

        def expresion(self):
            return self.getTypedRuleContext(Baby_DuckParser.ExpresionContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(Baby_DuckParser.CLOSE_PAREN, 0)

        def body(self):
            return self.getTypedRuleContext(Baby_DuckParser.BodyContext,0)


        def SEMICOLON(self):
            return self.getToken(Baby_DuckParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return Baby_DuckParser.RULE_cycle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCycle" ):
                listener.enterCycle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCycle" ):
                listener.exitCycle(self)




    def cycle(self):

        localctx = Baby_DuckParser.CycleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_cycle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(Baby_DuckParser.WHILE)
            whileLoop()
            self.state = 221
            self.match(Baby_DuckParser.OPEN_PAREN)
            addParenthesis()
            self.state = 223
            self.expresion()
            self.state = 224
            self.match(Baby_DuckParser.CLOSE_PAREN)
            closeParenthesis()
            expresionWhile()
            self.state = 227
            self.body()
            self.state = 228
            self.match(Baby_DuckParser.SEMICOLON)
            endWhile()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_KEY(self):
            return self.getToken(Baby_DuckParser.OPEN_KEY, 0)

        def CLOSE_KEY(self):
            return self.getToken(Baby_DuckParser.CLOSE_KEY, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Baby_DuckParser.StatementContext)
            else:
                return self.getTypedRuleContext(Baby_DuckParser.StatementContext,i)


        def getRuleIndex(self):
            return Baby_DuckParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = Baby_DuckParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(Baby_DuckParser.OPEN_KEY)
            addKey()
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8589956096) != 0):
                self.state = 233
                self.statement()
                self.state = 238
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 239
            self.match(Baby_DuckParser.CLOSE_KEY)
            closeKey()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._CTE = None # Token
            self._ID = None # Token

        def OPEN_PAREN(self):
            return self.getToken(Baby_DuckParser.OPEN_PAREN, 0)

        def expresion(self):
            return self.getTypedRuleContext(Baby_DuckParser.ExpresionContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(Baby_DuckParser.CLOSE_PAREN, 0)

        def CTE(self):
            return self.getToken(Baby_DuckParser.CTE, 0)

        def ID(self):
            return self.getToken(Baby_DuckParser.ID, 0)

        def ADD(self):
            return self.getToken(Baby_DuckParser.ADD, 0)

        def SUB(self):
            return self.getToken(Baby_DuckParser.SUB, 0)

        def getRuleIndex(self):
            return Baby_DuckParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = Baby_DuckParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 257
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.match(Baby_DuckParser.OPEN_PAREN)
                addParenthesis()
                self.state = 244
                self.expresion()
                self.state = 245
                self.match(Baby_DuckParser.CLOSE_PAREN)
                closeParenthesis()
                pass
            elif token in [3, 24, 25, 33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==24 or _la==25:
                    self.state = 248
                    _la = self._input.LA(1)
                    if not(_la==24 or _la==25):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 255
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 251
                    localctx._CTE = self.match(Baby_DuckParser.CTE)
                    stackConstant((None if localctx._CTE is None else localctx._CTE.text))
                    pass
                elif token in [33]:
                    self.state = 253
                    localctx._ID = self.match(Baby_DuckParser.ID)
                    stackId((None if localctx._ID is None else localctx._ID.text))
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._MULT = None # Token
            self._DIV = None # Token

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Baby_DuckParser.FactorContext)
            else:
                return self.getTypedRuleContext(Baby_DuckParser.FactorContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(Baby_DuckParser.MULT)
            else:
                return self.getToken(Baby_DuckParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(Baby_DuckParser.DIV)
            else:
                return self.getToken(Baby_DuckParser.DIV, i)

        def getRuleIndex(self):
            return Baby_DuckParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)




    def termino(self):

        localctx = Baby_DuckParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_termino)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 259
                    self.factor()
                    multDiv()
                    self.state = 265
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [21]:
                        self.state = 261
                        localctx._MULT = self.match(Baby_DuckParser.MULT)
                        addMultDiv((None if localctx._MULT is None else localctx._MULT.text))
                        pass
                    elif token in [22]:
                        self.state = 263
                        localctx._DIV = self.match(Baby_DuckParser.DIV)
                        addMultDiv((None if localctx._DIV is None else localctx._DIV.text))
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 271
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

            self.state = 272
            self.factor()
            multDiv()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ADD = None # Token
            self._SUB = None # Token

        def termino(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Baby_DuckParser.TerminoContext)
            else:
                return self.getTypedRuleContext(Baby_DuckParser.TerminoContext,i)


        def ADD(self, i:int=None):
            if i is None:
                return self.getTokens(Baby_DuckParser.ADD)
            else:
                return self.getToken(Baby_DuckParser.ADD, i)

        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(Baby_DuckParser.SUB)
            else:
                return self.getToken(Baby_DuckParser.SUB, i)

        def getRuleIndex(self):
            return Baby_DuckParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)




    def exp(self):

        localctx = Baby_DuckParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 275
                    self.termino()
                    sumRes()
                    self.state = 281
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [24]:
                        self.state = 277
                        localctx._ADD = self.match(Baby_DuckParser.ADD)
                        addSumSub((None if localctx._ADD is None else localctx._ADD.text))
                        pass
                    elif token in [25]:
                        self.state = 279
                        localctx._SUB = self.match(Baby_DuckParser.SUB)
                        addSumSub((None if localctx._SUB is None else localctx._SUB.text))
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 287
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

            self.state = 288
            self.termino()
            sumRes()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._TYPE_CONDITIONAL = None # Token

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Baby_DuckParser.ExpContext)
            else:
                return self.getTypedRuleContext(Baby_DuckParser.ExpContext,i)


        def TYPE_CONDITIONAL(self, i:int=None):
            if i is None:
                return self.getTokens(Baby_DuckParser.TYPE_CONDITIONAL)
            else:
                return self.getToken(Baby_DuckParser.TYPE_CONDITIONAL, i)

        def getRuleIndex(self):
            return Baby_DuckParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)




    def expresion(self):

        localctx = Baby_DuckParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 291
                    self.exp()
                    compareExp()

                    self.state = 293
                    localctx._TYPE_CONDITIONAL = self.match(Baby_DuckParser.TYPE_CONDITIONAL)
                    addCompare((None if localctx._TYPE_CONDITIONAL is None else localctx._TYPE_CONDITIONAL.text)) 
                self.state = 300
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

            self.state = 301
            self.exp()
            compareExp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





