# Generated from traductor.g4 by ANTLR 4.13.2
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
        4,1,32,101,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,3,4,3,39,8,3,11,3,12,3,40,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,3,5,55,8,5,1,6,1,
        6,1,6,1,6,1,7,1,7,1,7,3,7,64,8,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,3,11,
        86,8,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,94,8,11,10,11,12,11,97,
        9,11,1,12,1,12,1,12,0,1,22,13,0,2,4,6,8,10,12,14,16,18,20,22,24,
        0,4,1,0,11,14,1,0,19,22,1,0,23,28,2,0,17,18,29,31,96,0,26,1,0,0,
        0,2,30,1,0,0,0,4,34,1,0,0,0,6,38,1,0,0,0,8,42,1,0,0,0,10,54,1,0,
        0,0,12,56,1,0,0,0,14,60,1,0,0,0,16,65,1,0,0,0,18,70,1,0,0,0,20,72,
        1,0,0,0,22,85,1,0,0,0,24,98,1,0,0,0,26,27,3,2,1,0,27,28,3,6,3,0,
        28,29,3,4,2,0,29,1,1,0,0,0,30,31,5,4,0,0,31,32,5,5,0,0,32,33,5,6,
        0,0,33,3,1,0,0,0,34,35,5,7,0,0,35,36,5,5,0,0,36,5,1,0,0,0,37,39,
        3,10,5,0,38,37,1,0,0,0,39,40,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,
        41,7,1,0,0,0,42,43,5,9,0,0,43,44,5,30,0,0,44,45,5,10,0,0,45,46,3,
        6,3,0,46,47,5,7,0,0,47,48,5,9,0,0,48,9,1,0,0,0,49,55,3,14,7,0,50,
        55,3,8,4,0,51,55,3,16,8,0,52,55,3,12,6,0,53,55,3,20,10,0,54,49,1,
        0,0,0,54,50,1,0,0,0,54,51,1,0,0,0,54,52,1,0,0,0,54,53,1,0,0,0,55,
        11,1,0,0,0,56,57,5,29,0,0,57,58,5,1,0,0,58,59,3,22,11,0,59,13,1,
        0,0,0,60,63,5,8,0,0,61,64,5,31,0,0,62,64,3,22,11,0,63,61,1,0,0,0,
        63,62,1,0,0,0,64,15,1,0,0,0,65,66,3,18,9,0,66,67,5,29,0,0,67,68,
        5,1,0,0,68,69,3,22,11,0,69,17,1,0,0,0,70,71,7,0,0,0,71,19,1,0,0,
        0,72,73,5,15,0,0,73,74,3,22,11,0,74,75,5,16,0,0,75,76,3,6,3,0,76,
        77,5,7,0,0,77,78,5,15,0,0,78,21,1,0,0,0,79,80,6,11,-1,0,80,86,3,
        24,12,0,81,82,5,2,0,0,82,83,3,22,11,0,83,84,5,3,0,0,84,86,1,0,0,
        0,85,79,1,0,0,0,85,81,1,0,0,0,86,95,1,0,0,0,87,88,10,3,0,0,88,89,
        7,1,0,0,89,94,3,22,11,4,90,91,10,2,0,0,91,92,7,2,0,0,92,94,3,22,
        11,3,93,87,1,0,0,0,93,90,1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,
        96,1,0,0,0,96,23,1,0,0,0,97,95,1,0,0,0,98,99,7,3,0,0,99,25,1,0,0,
        0,6,40,54,63,85,93,95
    ]

class traductorParser ( Parser ):

    grammarFileName = "traductor.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "'Inicio'", "'Funcion'", 
                     "'principal'", "'Fin'", "'Escribir'", "'Repetir'", 
                     "'Veces'", "'entero'", "'texto'", "'booleano'", "'flotante'", 
                     "'Si'", "'Entonces'", "'verdadero'", "'falso'", "'+'", 
                     "'-'", "'*'", "'/'", "'>'", "'<'", "'>='", "'<='", 
                     "'=='", "'!='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INICIO", "FUNCION", "PRINCIPAL", "FIN", "ESCRIBIR", 
                      "REPITE", "VECES", "ENTERO", "TEXTO", "BOOLEANO", 
                      "FLOTANTE", "SI", "ENTONCES", "VERDADERO", "FALSO", 
                      "MAS", "MENOS", "MULTIPLICACION", "DIVISION", "MAYOR", 
                      "MENOR", "MAYORIGUAL", "MENORIGUAL", "IGUALIGUAL", 
                      "DIFERENTE", "ID", "NUMERO", "CADENA", "ESPACIOS" ]

    RULE_programa = 0
    RULE_inicioFuncion = 1
    RULE_finFuncion = 2
    RULE_cuerpo = 3
    RULE_repetir = 4
    RULE_instruccion = 5
    RULE_asignacion = 6
    RULE_escribir = 7
    RULE_definicionVariable = 8
    RULE_tipoVariable = 9
    RULE_condicion = 10
    RULE_expresion = 11
    RULE_valor = 12

    ruleNames =  [ "programa", "inicioFuncion", "finFuncion", "cuerpo", 
                   "repetir", "instruccion", "asignacion", "escribir", "definicionVariable", 
                   "tipoVariable", "condicion", "expresion", "valor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    INICIO=4
    FUNCION=5
    PRINCIPAL=6
    FIN=7
    ESCRIBIR=8
    REPITE=9
    VECES=10
    ENTERO=11
    TEXTO=12
    BOOLEANO=13
    FLOTANTE=14
    SI=15
    ENTONCES=16
    VERDADERO=17
    FALSO=18
    MAS=19
    MENOS=20
    MULTIPLICACION=21
    DIVISION=22
    MAYOR=23
    MENOR=24
    MAYORIGUAL=25
    MENORIGUAL=26
    IGUALIGUAL=27
    DIFERENTE=28
    ID=29
    NUMERO=30
    CADENA=31
    ESPACIOS=32

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inicioFuncion(self):
            return self.getTypedRuleContext(traductorParser.InicioFuncionContext,0)


        def cuerpo(self):
            return self.getTypedRuleContext(traductorParser.CuerpoContext,0)


        def finFuncion(self):
            return self.getTypedRuleContext(traductorParser.FinFuncionContext,0)


        def getRuleIndex(self):
            return traductorParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = traductorParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.inicioFuncion()
            self.state = 27
            self.cuerpo()
            self.state = 28
            self.finFuncion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InicioFuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INICIO(self):
            return self.getToken(traductorParser.INICIO, 0)

        def FUNCION(self):
            return self.getToken(traductorParser.FUNCION, 0)

        def PRINCIPAL(self):
            return self.getToken(traductorParser.PRINCIPAL, 0)

        def getRuleIndex(self):
            return traductorParser.RULE_inicioFuncion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInicioFuncion" ):
                listener.enterInicioFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInicioFuncion" ):
                listener.exitInicioFuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInicioFuncion" ):
                return visitor.visitInicioFuncion(self)
            else:
                return visitor.visitChildren(self)




    def inicioFuncion(self):

        localctx = traductorParser.InicioFuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_inicioFuncion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(traductorParser.INICIO)
            self.state = 31
            self.match(traductorParser.FUNCION)
            self.state = 32
            self.match(traductorParser.PRINCIPAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FinFuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FIN(self):
            return self.getToken(traductorParser.FIN, 0)

        def FUNCION(self):
            return self.getToken(traductorParser.FUNCION, 0)

        def getRuleIndex(self):
            return traductorParser.RULE_finFuncion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinFuncion" ):
                listener.enterFinFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinFuncion" ):
                listener.exitFinFuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFinFuncion" ):
                return visitor.visitFinFuncion(self)
            else:
                return visitor.visitChildren(self)




    def finFuncion(self):

        localctx = traductorParser.FinFuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_finFuncion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(traductorParser.FIN)
            self.state = 35
            self.match(traductorParser.FUNCION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CuerpoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(traductorParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(traductorParser.InstruccionContext,i)


        def getRuleIndex(self):
            return traductorParser.RULE_cuerpo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCuerpo" ):
                listener.enterCuerpo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCuerpo" ):
                listener.exitCuerpo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCuerpo" ):
                return visitor.visitCuerpo(self)
            else:
                return visitor.visitChildren(self)




    def cuerpo(self):

        localctx = traductorParser.CuerpoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_cuerpo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 37
                self.instruccion()
                self.state = 40 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 536935168) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepetirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPITE(self, i:int=None):
            if i is None:
                return self.getTokens(traductorParser.REPITE)
            else:
                return self.getToken(traductorParser.REPITE, i)

        def NUMERO(self):
            return self.getToken(traductorParser.NUMERO, 0)

        def VECES(self):
            return self.getToken(traductorParser.VECES, 0)

        def cuerpo(self):
            return self.getTypedRuleContext(traductorParser.CuerpoContext,0)


        def FIN(self):
            return self.getToken(traductorParser.FIN, 0)

        def getRuleIndex(self):
            return traductorParser.RULE_repetir

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepetir" ):
                listener.enterRepetir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepetir" ):
                listener.exitRepetir(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepetir" ):
                return visitor.visitRepetir(self)
            else:
                return visitor.visitChildren(self)




    def repetir(self):

        localctx = traductorParser.RepetirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_repetir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(traductorParser.REPITE)
            self.state = 43
            self.match(traductorParser.NUMERO)
            self.state = 44
            self.match(traductorParser.VECES)
            self.state = 45
            self.cuerpo()
            self.state = 46
            self.match(traductorParser.FIN)
            self.state = 47
            self.match(traductorParser.REPITE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def escribir(self):
            return self.getTypedRuleContext(traductorParser.EscribirContext,0)


        def repetir(self):
            return self.getTypedRuleContext(traductorParser.RepetirContext,0)


        def definicionVariable(self):
            return self.getTypedRuleContext(traductorParser.DefinicionVariableContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(traductorParser.AsignacionContext,0)


        def condicion(self):
            return self.getTypedRuleContext(traductorParser.CondicionContext,0)


        def getRuleIndex(self):
            return traductorParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = traductorParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_instruccion)
        try:
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.escribir()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.repetir()
                pass
            elif token in [11, 12, 13, 14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.definicionVariable()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 4)
                self.state = 52
                self.asignacion()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 5)
                self.state = 53
                self.condicion()
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


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(traductorParser.ID, 0)

        def expresion(self):
            return self.getTypedRuleContext(traductorParser.ExpresionContext,0)


        def getRuleIndex(self):
            return traductorParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = traductorParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(traductorParser.ID)
            self.state = 57
            self.match(traductorParser.T__0)
            self.state = 58
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EscribirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ESCRIBIR(self):
            return self.getToken(traductorParser.ESCRIBIR, 0)

        def CADENA(self):
            return self.getToken(traductorParser.CADENA, 0)

        def expresion(self):
            return self.getTypedRuleContext(traductorParser.ExpresionContext,0)


        def getRuleIndex(self):
            return traductorParser.RULE_escribir

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEscribir" ):
                listener.enterEscribir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEscribir" ):
                listener.exitEscribir(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEscribir" ):
                return visitor.visitEscribir(self)
            else:
                return visitor.visitChildren(self)




    def escribir(self):

        localctx = traductorParser.EscribirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_escribir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(traductorParser.ESCRIBIR)
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 61
                self.match(traductorParser.CADENA)
                pass

            elif la_ == 2:
                self.state = 62
                self.expresion(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinicionVariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipoVariable(self):
            return self.getTypedRuleContext(traductorParser.TipoVariableContext,0)


        def ID(self):
            return self.getToken(traductorParser.ID, 0)

        def expresion(self):
            return self.getTypedRuleContext(traductorParser.ExpresionContext,0)


        def getRuleIndex(self):
            return traductorParser.RULE_definicionVariable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinicionVariable" ):
                listener.enterDefinicionVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinicionVariable" ):
                listener.exitDefinicionVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinicionVariable" ):
                return visitor.visitDefinicionVariable(self)
            else:
                return visitor.visitChildren(self)




    def definicionVariable(self):

        localctx = traductorParser.DefinicionVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_definicionVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.tipoVariable()
            self.state = 66
            self.match(traductorParser.ID)
            self.state = 67
            self.match(traductorParser.T__0)
            self.state = 68
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoVariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTERO(self):
            return self.getToken(traductorParser.ENTERO, 0)

        def TEXTO(self):
            return self.getToken(traductorParser.TEXTO, 0)

        def BOOLEANO(self):
            return self.getToken(traductorParser.BOOLEANO, 0)

        def FLOTANTE(self):
            return self.getToken(traductorParser.FLOTANTE, 0)

        def getRuleIndex(self):
            return traductorParser.RULE_tipoVariable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoVariable" ):
                listener.enterTipoVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoVariable" ):
                listener.exitTipoVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoVariable" ):
                return visitor.visitTipoVariable(self)
            else:
                return visitor.visitChildren(self)




    def tipoVariable(self):

        localctx = traductorParser.TipoVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_tipoVariable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30720) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self, i:int=None):
            if i is None:
                return self.getTokens(traductorParser.SI)
            else:
                return self.getToken(traductorParser.SI, i)

        def expresion(self):
            return self.getTypedRuleContext(traductorParser.ExpresionContext,0)


        def ENTONCES(self):
            return self.getToken(traductorParser.ENTONCES, 0)

        def cuerpo(self):
            return self.getTypedRuleContext(traductorParser.CuerpoContext,0)


        def FIN(self):
            return self.getToken(traductorParser.FIN, 0)

        def getRuleIndex(self):
            return traductorParser.RULE_condicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicion" ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicion" ):
                listener.exitCondicion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicion" ):
                return visitor.visitCondicion(self)
            else:
                return visitor.visitChildren(self)




    def condicion(self):

        localctx = traductorParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(traductorParser.SI)
            self.state = 73
            self.expresion(0)
            self.state = 74
            self.match(traductorParser.ENTONCES)
            self.state = 75
            self.cuerpo()
            self.state = 76
            self.match(traductorParser.FIN)
            self.state = 77
            self.match(traductorParser.SI)
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

        def valor(self):
            return self.getTypedRuleContext(traductorParser.ValorContext,0)


        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(traductorParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(traductorParser.ExpresionContext,i)


        def MAS(self):
            return self.getToken(traductorParser.MAS, 0)

        def MENOS(self):
            return self.getToken(traductorParser.MENOS, 0)

        def MULTIPLICACION(self):
            return self.getToken(traductorParser.MULTIPLICACION, 0)

        def DIVISION(self):
            return self.getToken(traductorParser.DIVISION, 0)

        def MAYOR(self):
            return self.getToken(traductorParser.MAYOR, 0)

        def MENOR(self):
            return self.getToken(traductorParser.MENOR, 0)

        def MAYORIGUAL(self):
            return self.getToken(traductorParser.MAYORIGUAL, 0)

        def MENORIGUAL(self):
            return self.getToken(traductorParser.MENORIGUAL, 0)

        def IGUALIGUAL(self):
            return self.getToken(traductorParser.IGUALIGUAL, 0)

        def DIFERENTE(self):
            return self.getToken(traductorParser.DIFERENTE, 0)

        def getRuleIndex(self):
            return traductorParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = traductorParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 18, 29, 30, 31]:
                self.state = 80
                self.valor()
                pass
            elif token in [2]:
                self.state = 81
                self.match(traductorParser.T__1)
                self.state = 82
                self.expresion(0)
                self.state = 83
                self.match(traductorParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 95
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 93
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = traductorParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 87
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 88
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7864320) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 89
                        self.expresion(4)
                        pass

                    elif la_ == 2:
                        localctx = traductorParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 90
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 91
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 528482304) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 92
                        self.expresion(3)
                        pass

             
                self.state = 97
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ValorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(traductorParser.NUMERO, 0)

        def CADENA(self):
            return self.getToken(traductorParser.CADENA, 0)

        def VERDADERO(self):
            return self.getToken(traductorParser.VERDADERO, 0)

        def FALSO(self):
            return self.getToken(traductorParser.FALSO, 0)

        def ID(self):
            return self.getToken(traductorParser.ID, 0)

        def getRuleIndex(self):
            return traductorParser.RULE_valor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValor" ):
                listener.enterValor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValor" ):
                listener.exitValor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValor" ):
                return visitor.visitValor(self)
            else:
                return visitor.visitChildren(self)




    def valor(self):

        localctx = traductorParser.ValorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_valor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3758489600) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




