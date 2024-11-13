# Generated from ./traductorPyaJava.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,17,112,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,4,1,34,8,1,11,1,12,1,35,1,2,1,2,1,2,5,2,41,8,2,10,
        2,12,2,44,9,2,1,2,3,2,47,8,2,1,3,1,3,3,3,51,8,3,1,4,3,4,54,8,4,1,
        4,1,4,1,4,1,4,1,4,1,5,3,5,62,8,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,5,7,80,8,7,10,7,12,7,83,9,7,1,8,
        1,8,1,8,5,8,88,8,8,10,8,12,8,91,9,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,
        99,8,9,1,10,1,10,1,10,5,10,104,8,10,10,10,12,10,107,9,10,1,10,3,
        10,110,8,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,2,1,0,7,8,
        1,0,9,10,112,0,22,1,0,0,0,2,25,1,0,0,0,4,46,1,0,0,0,6,50,1,0,0,0,
        8,53,1,0,0,0,10,61,1,0,0,0,12,67,1,0,0,0,14,76,1,0,0,0,16,84,1,0,
        0,0,18,98,1,0,0,0,20,109,1,0,0,0,22,23,3,2,1,0,23,24,3,12,6,0,24,
        1,1,0,0,0,25,26,5,2,0,0,26,27,5,5,0,0,27,28,5,11,0,0,28,29,3,4,2,
        0,29,30,5,12,0,0,30,31,5,14,0,0,31,33,5,15,0,0,32,34,3,6,3,0,33,
        32,1,0,0,0,34,35,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,3,1,0,0,
        0,37,42,5,5,0,0,38,39,5,13,0,0,39,41,5,5,0,0,40,38,1,0,0,0,41,44,
        1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,47,1,0,0,0,44,42,1,0,0,0,
        45,47,1,0,0,0,46,37,1,0,0,0,46,45,1,0,0,0,47,5,1,0,0,0,48,51,3,8,
        4,0,49,51,3,10,5,0,50,48,1,0,0,0,50,49,1,0,0,0,51,7,1,0,0,0,52,54,
        5,17,0,0,53,52,1,0,0,0,53,54,1,0,0,0,54,55,1,0,0,0,55,56,5,5,0,0,
        56,57,5,1,0,0,57,58,3,14,7,0,58,59,5,15,0,0,59,9,1,0,0,0,60,62,5,
        17,0,0,61,60,1,0,0,0,61,62,1,0,0,0,62,63,1,0,0,0,63,64,5,3,0,0,64,
        65,3,14,7,0,65,66,5,15,0,0,66,11,1,0,0,0,67,68,5,4,0,0,68,69,5,11,
        0,0,69,70,5,5,0,0,70,71,5,11,0,0,71,72,3,20,10,0,72,73,5,12,0,0,
        73,74,5,12,0,0,74,75,5,15,0,0,75,13,1,0,0,0,76,81,3,16,8,0,77,78,
        7,0,0,0,78,80,3,16,8,0,79,77,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,
        81,82,1,0,0,0,82,15,1,0,0,0,83,81,1,0,0,0,84,89,3,18,9,0,85,86,7,
        1,0,0,86,88,3,18,9,0,87,85,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,
        90,1,0,0,0,90,17,1,0,0,0,91,89,1,0,0,0,92,99,5,6,0,0,93,99,5,5,0,
        0,94,95,5,11,0,0,95,96,3,14,7,0,96,97,5,12,0,0,97,99,1,0,0,0,98,
        92,1,0,0,0,98,93,1,0,0,0,98,94,1,0,0,0,99,19,1,0,0,0,100,105,3,14,
        7,0,101,102,5,13,0,0,102,104,3,14,7,0,103,101,1,0,0,0,104,107,1,
        0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,110,1,0,0,0,107,105,1,
        0,0,0,108,110,1,0,0,0,109,100,1,0,0,0,109,108,1,0,0,0,110,21,1,0,
        0,0,11,35,42,46,50,53,61,81,89,98,105,109
    ]

class traductorPyaJavaParser ( Parser ):

    grammarFileName = "traductorPyaJava.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'def'", "'return'", "'print'", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'('", "')'", "','", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "DEF", "RETURN", "PRINT", 
                      "IDENTIFIER", "NUMBER", "PLUS", "MINUS", "MULTIPLY", 
                      "DIVIDE", "LPAREN", "RPAREN", "COMMA", "COLON", "NEWLINE", 
                      "WS", "INDENT" ]

    RULE_program = 0
    RULE_functionDef = 1
    RULE_parameters = 2
    RULE_statement = 3
    RULE_expressionStatement = 4
    RULE_returnStatement = 5
    RULE_printStatement = 6
    RULE_expression = 7
    RULE_term = 8
    RULE_factor = 9
    RULE_arguments = 10

    ruleNames =  [ "program", "functionDef", "parameters", "statement", 
                   "expressionStatement", "returnStatement", "printStatement", 
                   "expression", "term", "factor", "arguments" ]

    EOF = Token.EOF
    T__0=1
    DEF=2
    RETURN=3
    PRINT=4
    IDENTIFIER=5
    NUMBER=6
    PLUS=7
    MINUS=8
    MULTIPLY=9
    DIVIDE=10
    LPAREN=11
    RPAREN=12
    COMMA=13
    COLON=14
    NEWLINE=15
    WS=16
    INDENT=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionDef(self):
            return self.getTypedRuleContext(traductorPyaJavaParser.FunctionDefContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(traductorPyaJavaParser.PrintStatementContext,0)


        def getRuleIndex(self):
            return traductorPyaJavaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = traductorPyaJavaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.functionDef()
            self.state = 23
            self.printStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(traductorPyaJavaParser.DEF, 0)

        def IDENTIFIER(self):
            return self.getToken(traductorPyaJavaParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(traductorPyaJavaParser.LPAREN, 0)

        def parameters(self):
            return self.getTypedRuleContext(traductorPyaJavaParser.ParametersContext,0)


        def RPAREN(self):
            return self.getToken(traductorPyaJavaParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(traductorPyaJavaParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(traductorPyaJavaParser.NEWLINE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(traductorPyaJavaParser.StatementContext)
            else:
                return self.getTypedRuleContext(traductorPyaJavaParser.StatementContext,i)


        def getRuleIndex(self):
            return traductorPyaJavaParser.RULE_functionDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDef" ):
                listener.enterFunctionDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDef" ):
                listener.exitFunctionDef(self)




    def functionDef(self):

        localctx = traductorPyaJavaParser.FunctionDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_functionDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(traductorPyaJavaParser.DEF)
            self.state = 26
            self.match(traductorPyaJavaParser.IDENTIFIER)
            self.state = 27
            self.match(traductorPyaJavaParser.LPAREN)
            self.state = 28
            self.parameters()
            self.state = 29
            self.match(traductorPyaJavaParser.RPAREN)
            self.state = 30
            self.match(traductorPyaJavaParser.COLON)
            self.state = 31
            self.match(traductorPyaJavaParser.NEWLINE)
            self.state = 33 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self.statement()
                self.state = 35 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 131112) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(traductorPyaJavaParser.IDENTIFIER)
            else:
                return self.getToken(traductorPyaJavaParser.IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(traductorPyaJavaParser.COMMA)
            else:
                return self.getToken(traductorPyaJavaParser.COMMA, i)

        def getRuleIndex(self):
            return traductorPyaJavaParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)




    def parameters(self):

        localctx = traductorPyaJavaParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.match(traductorPyaJavaParser.IDENTIFIER)
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 38
                    self.match(traductorPyaJavaParser.COMMA)
                    self.state = 39
                    self.match(traductorPyaJavaParser.IDENTIFIER)
                    self.state = 44
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)

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


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionStatement(self):
            return self.getTypedRuleContext(traductorPyaJavaParser.ExpressionStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(traductorPyaJavaParser.ReturnStatementContext,0)


        def getRuleIndex(self):
            return traductorPyaJavaParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = traductorPyaJavaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.expressionStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.returnStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(traductorPyaJavaParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(traductorPyaJavaParser.ExpressionContext,0)


        def NEWLINE(self):
            return self.getToken(traductorPyaJavaParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(traductorPyaJavaParser.INDENT, 0)

        def getRuleIndex(self):
            return traductorPyaJavaParser.RULE_expressionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)




    def expressionStatement(self):

        localctx = traductorPyaJavaParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expressionStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 52
                self.match(traductorPyaJavaParser.INDENT)


            self.state = 55
            self.match(traductorPyaJavaParser.IDENTIFIER)
            self.state = 56
            self.match(traductorPyaJavaParser.T__0)
            self.state = 57
            self.expression()
            self.state = 58
            self.match(traductorPyaJavaParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(traductorPyaJavaParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(traductorPyaJavaParser.ExpressionContext,0)


        def NEWLINE(self):
            return self.getToken(traductorPyaJavaParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(traductorPyaJavaParser.INDENT, 0)

        def getRuleIndex(self):
            return traductorPyaJavaParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)




    def returnStatement(self):

        localctx = traductorPyaJavaParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 60
                self.match(traductorPyaJavaParser.INDENT)


            self.state = 63
            self.match(traductorPyaJavaParser.RETURN)
            self.state = 64
            self.expression()
            self.state = 65
            self.match(traductorPyaJavaParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(traductorPyaJavaParser.PRINT, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(traductorPyaJavaParser.LPAREN)
            else:
                return self.getToken(traductorPyaJavaParser.LPAREN, i)

        def IDENTIFIER(self):
            return self.getToken(traductorPyaJavaParser.IDENTIFIER, 0)

        def arguments(self):
            return self.getTypedRuleContext(traductorPyaJavaParser.ArgumentsContext,0)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(traductorPyaJavaParser.RPAREN)
            else:
                return self.getToken(traductorPyaJavaParser.RPAREN, i)

        def NEWLINE(self):
            return self.getToken(traductorPyaJavaParser.NEWLINE, 0)

        def getRuleIndex(self):
            return traductorPyaJavaParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)




    def printStatement(self):

        localctx = traductorPyaJavaParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(traductorPyaJavaParser.PRINT)
            self.state = 68
            self.match(traductorPyaJavaParser.LPAREN)
            self.state = 69
            self.match(traductorPyaJavaParser.IDENTIFIER)
            self.state = 70
            self.match(traductorPyaJavaParser.LPAREN)
            self.state = 71
            self.arguments()
            self.state = 72
            self.match(traductorPyaJavaParser.RPAREN)
            self.state = 73
            self.match(traductorPyaJavaParser.RPAREN)
            self.state = 74
            self.match(traductorPyaJavaParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(traductorPyaJavaParser.TermContext)
            else:
                return self.getTypedRuleContext(traductorPyaJavaParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(traductorPyaJavaParser.PLUS)
            else:
                return self.getToken(traductorPyaJavaParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(traductorPyaJavaParser.MINUS)
            else:
                return self.getToken(traductorPyaJavaParser.MINUS, i)

        def getRuleIndex(self):
            return traductorPyaJavaParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = traductorPyaJavaParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.term()
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 77
                _la = self._input.LA(1)
                if not(_la==7 or _la==8):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 78
                self.term()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(traductorPyaJavaParser.FactorContext)
            else:
                return self.getTypedRuleContext(traductorPyaJavaParser.FactorContext,i)


        def MULTIPLY(self, i:int=None):
            if i is None:
                return self.getTokens(traductorPyaJavaParser.MULTIPLY)
            else:
                return self.getToken(traductorPyaJavaParser.MULTIPLY, i)

        def DIVIDE(self, i:int=None):
            if i is None:
                return self.getTokens(traductorPyaJavaParser.DIVIDE)
            else:
                return self.getToken(traductorPyaJavaParser.DIVIDE, i)

        def getRuleIndex(self):
            return traductorPyaJavaParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = traductorPyaJavaParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.factor()
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9 or _la==10:
                self.state = 85
                _la = self._input.LA(1)
                if not(_la==9 or _la==10):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 86
                self.factor()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def NUMBER(self):
            return self.getToken(traductorPyaJavaParser.NUMBER, 0)

        def IDENTIFIER(self):
            return self.getToken(traductorPyaJavaParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(traductorPyaJavaParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(traductorPyaJavaParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(traductorPyaJavaParser.RPAREN, 0)

        def getRuleIndex(self):
            return traductorPyaJavaParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = traductorPyaJavaParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_factor)
        try:
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.match(traductorPyaJavaParser.NUMBER)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.match(traductorPyaJavaParser.IDENTIFIER)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.match(traductorPyaJavaParser.LPAREN)
                self.state = 95
                self.expression()
                self.state = 96
                self.match(traductorPyaJavaParser.RPAREN)
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


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(traductorPyaJavaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(traductorPyaJavaParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(traductorPyaJavaParser.COMMA)
            else:
                return self.getToken(traductorPyaJavaParser.COMMA, i)

        def getRuleIndex(self):
            return traductorPyaJavaParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)




    def arguments(self):

        localctx = traductorPyaJavaParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6, 11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.expression()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 101
                    self.match(traductorPyaJavaParser.COMMA)
                    self.state = 102
                    self.expression()
                    self.state = 107
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)

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





