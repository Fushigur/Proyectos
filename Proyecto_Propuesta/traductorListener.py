# Generated from traductor.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .traductorParser import traductorParser
else:
    from traductorParser import traductorParser

# This class defines a complete listener for a parse tree produced by traductorParser.
class traductorListener(ParseTreeListener):

    # Enter a parse tree produced by traductorParser#programa.
    def enterPrograma(self, ctx:traductorParser.ProgramaContext):
        pass

    # Exit a parse tree produced by traductorParser#programa.
    def exitPrograma(self, ctx:traductorParser.ProgramaContext):
        pass


    # Enter a parse tree produced by traductorParser#inicioFuncion.
    def enterInicioFuncion(self, ctx:traductorParser.InicioFuncionContext):
        pass

    # Exit a parse tree produced by traductorParser#inicioFuncion.
    def exitInicioFuncion(self, ctx:traductorParser.InicioFuncionContext):
        pass


    # Enter a parse tree produced by traductorParser#finFuncion.
    def enterFinFuncion(self, ctx:traductorParser.FinFuncionContext):
        pass

    # Exit a parse tree produced by traductorParser#finFuncion.
    def exitFinFuncion(self, ctx:traductorParser.FinFuncionContext):
        pass


    # Enter a parse tree produced by traductorParser#cuerpo.
    def enterCuerpo(self, ctx:traductorParser.CuerpoContext):
        pass

    # Exit a parse tree produced by traductorParser#cuerpo.
    def exitCuerpo(self, ctx:traductorParser.CuerpoContext):
        pass


    # Enter a parse tree produced by traductorParser#repetir.
    def enterRepetir(self, ctx:traductorParser.RepetirContext):
        pass

    # Exit a parse tree produced by traductorParser#repetir.
    def exitRepetir(self, ctx:traductorParser.RepetirContext):
        pass


    # Enter a parse tree produced by traductorParser#instruccion.
    def enterInstruccion(self, ctx:traductorParser.InstruccionContext):
        pass

    # Exit a parse tree produced by traductorParser#instruccion.
    def exitInstruccion(self, ctx:traductorParser.InstruccionContext):
        pass


    # Enter a parse tree produced by traductorParser#asignacion.
    def enterAsignacion(self, ctx:traductorParser.AsignacionContext):
        pass

    # Exit a parse tree produced by traductorParser#asignacion.
    def exitAsignacion(self, ctx:traductorParser.AsignacionContext):
        pass


    # Enter a parse tree produced by traductorParser#escribir.
    def enterEscribir(self, ctx:traductorParser.EscribirContext):
        pass

    # Exit a parse tree produced by traductorParser#escribir.
    def exitEscribir(self, ctx:traductorParser.EscribirContext):
        pass


    # Enter a parse tree produced by traductorParser#definicionVariable.
    def enterDefinicionVariable(self, ctx:traductorParser.DefinicionVariableContext):
        pass

    # Exit a parse tree produced by traductorParser#definicionVariable.
    def exitDefinicionVariable(self, ctx:traductorParser.DefinicionVariableContext):
        pass


    # Enter a parse tree produced by traductorParser#tipoVariable.
    def enterTipoVariable(self, ctx:traductorParser.TipoVariableContext):
        pass

    # Exit a parse tree produced by traductorParser#tipoVariable.
    def exitTipoVariable(self, ctx:traductorParser.TipoVariableContext):
        pass


    # Enter a parse tree produced by traductorParser#condicion.
    def enterCondicion(self, ctx:traductorParser.CondicionContext):
        pass

    # Exit a parse tree produced by traductorParser#condicion.
    def exitCondicion(self, ctx:traductorParser.CondicionContext):
        pass


    # Enter a parse tree produced by traductorParser#expresion.
    def enterExpresion(self, ctx:traductorParser.ExpresionContext):
        pass

    # Exit a parse tree produced by traductorParser#expresion.
    def exitExpresion(self, ctx:traductorParser.ExpresionContext):
        pass


    # Enter a parse tree produced by traductorParser#valor.
    def enterValor(self, ctx:traductorParser.ValorContext):
        pass

    # Exit a parse tree produced by traductorParser#valor.
    def exitValor(self, ctx:traductorParser.ValorContext):
        pass



del traductorParser