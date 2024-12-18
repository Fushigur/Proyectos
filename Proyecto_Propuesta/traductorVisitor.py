# Generated from traductor.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .traductorParser import traductorParser
else:
    from traductorParser import traductorParser

# This class defines a complete generic visitor for a parse tree produced by traductorParser.

class traductorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by traductorParser#programa.
    def visitPrograma(self, ctx:traductorParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by traductorParser#inicioFuncion.
    def visitInicioFuncion(self, ctx:traductorParser.InicioFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by traductorParser#finFuncion.
    def visitFinFuncion(self, ctx:traductorParser.FinFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by traductorParser#cuerpo.
    def visitCuerpo(self, ctx:traductorParser.CuerpoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by traductorParser#repetir.
    def visitRepetir(self, ctx:traductorParser.RepetirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by traductorParser#instruccion.
    def visitInstruccion(self, ctx:traductorParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by traductorParser#asignacion.
    def visitAsignacion(self, ctx:traductorParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by traductorParser#escribir.
    def visitEscribir(self, ctx:traductorParser.EscribirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by traductorParser#definicionVariable.
    def visitDefinicionVariable(self, ctx:traductorParser.DefinicionVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by traductorParser#tipoVariable.
    def visitTipoVariable(self, ctx:traductorParser.TipoVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by traductorParser#condicion.
    def visitCondicion(self, ctx:traductorParser.CondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by traductorParser#expresion.
    def visitExpresion(self, ctx:traductorParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by traductorParser#valor.
    def visitValor(self, ctx:traductorParser.ValorContext):
        return self.visitChildren(ctx)



del traductorParser