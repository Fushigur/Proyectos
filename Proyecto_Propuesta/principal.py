import os #Verificamos si el archivo existe
from antlr4 import FileStream, CommonTokenStream
from traductorLexer import traductorLexer
from traductorParser import traductorParser
from traductorVisitor import traductorVisitor

class traductorToPython(traductorVisitor):
    # Programa completo Método General
    def visitPrograma(self, ctx):
        return "".join(self.visit(child) for child in ctx.getChildren())
    #Traduce el programa
    #Combina las partes (inicioFuncion | cuerpo | finFuncion)

    # Inicio y Fin de la función principal
    def visitInicioFuncion(self, ctx):
        return "def main():\n" #Inicio Funcion principal

    def visitFinFuncion(self, ctx):
        return "\nif __name__ == '__main__':\n    main()\n"# Fin funcion

    # Cuerpo general y las instrucciones
    def visitCuerpo(self, ctx):#Instrucciones del programa
        return "".join(self.visit(child) for child in ctx.instruccion())
    
    #Traduce asignaciones (nuevas asignaciones)
    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expresion())
        return f"    {nombre} = {valor}\n"
    # x = x + 1 

    # Instrucciones (selecciona el método adecuado)
    #Define que tipo de expresion es (repetir, escribir, etc) y hace llamado al metodo adecuado
    def visitInstruccion(self, ctx):
        if ctx.repetir():
            return self.visit(ctx.repetir())
        elif ctx.escribir():
            return self.visit(ctx.escribir())
        elif ctx.definicionVariable():
            return self.visit(ctx.definicionVariable())
        elif ctx.asignacion():   # NUEVA CONDICIÓN
            return self.visit(ctx.asignacion())
        elif ctx.condicion():
            return self.visit(ctx.condicion())

    # Escribir: imprime cadenas, expresiones o valores
    def visitEscribir(self, ctx):
        if ctx.CADENA():
            mensaje = ctx.CADENA().getText()
            return f"    print({mensaje})\n"
        elif ctx.expresion():
            mensaje = self.visit(ctx.expresion())
            return f"    print({mensaje})\n"

    # Repetir (bucle for), Repetir n Veces
    def visitRepetir(self, ctx):
        # Obtener el número de repeticiones
        veces = ctx.NUMERO().getText()
        # Procesar el cuerpo del bucle
        cuerpo = self.visit(ctx.cuerpo()) if ctx.cuerpo() else ""
        # Indentar cada línea del cuerpo
        cuerpo_indentado = "\n".join(f"        {line}" for line in cuerpo.splitlines() if line.strip())
        return f"    for _ in range({veces}):\n{cuerpo_indentado}\n"


    # Condicional (if) Si ... Entonces
    def visitCondicion(self, ctx):
        condicion = self.visit(ctx.expresion())
        cuerpo = self.visit(ctx.cuerpo())
        cuerpo_indentado = "\n".join(f"        {line}" for line in cuerpo.splitlines() if line.strip())
        return f"    if {condicion}:\n{cuerpo_indentado}\n"

    # Definición de variables
    def visitDefinicionVariable(self, ctx):
        nombre = ctx.ID().getText()  # Nombre de la variable
        #Traducimos la expresión
        valor = self.visit(ctx.expresion())  # Valor de la asignación
        #Retorna la declaración
        return f"    {nombre} = {valor}\n"

    # Expresiones (traduce operaciones matematicas)
    def visitExpresion(self, ctx):
        if ctx.getChildCount() == 1:  # Valor simple
            return self.visit(ctx.getChild(0))
        elif ctx.getChildCount() == 3:  # Operación binaria (ejemplo: x + 1)
            izquierda = self.visit(ctx.getChild(0))
            operador = ctx.getChild(1).getText()
            derecha = self.visit(ctx.getChild(2))
            #Mapera operadores a su representación en Python
            operadores = {
            '>': '>',
            '<': '<',
            '>=': '>=',
            '<=': '<=',
            '==': '==',
            '!=': '!='
        }
            return f"{izquierda} {operador} {derecha}"

    # Condición lógica (para if o while)
    def visitCondicionLogica(self, ctx):
        if ctx.MAYOR():
            izquierda = self.visit(ctx.getChild(0))
            derecha = self.visit(ctx.getChild(2))
            return f"{izquierda} > {derecha}"
        elif ctx.MENOR():
            izquierda = self.visit(ctx.getChild(0))
            derecha = self.visit(ctx.getChild(2))
            return f"{izquierda} < {derecha}"
        elif ctx.IGUAL():
            izquierda = self.visit(ctx.getChild(0))
            derecha = self.visit(ctx.getChild(2))
            return f"{izquierda} == {derecha}"
        else:
            raise ValueError("Operador lógico inesperado en 'visitCondicionLogica'")

    # Valores simples (Cadenas, números y variables)
    def visitValor(self, ctx):
        if ctx.NUMERO():
            return ctx.NUMERO().getText()
        elif ctx.CADENA():
            return ctx.CADENA().getText()
        elif ctx.VERDADERO():
            return "True"
        elif ctx.FALSO():
            return "False"
        elif ctx.ID():
            return ctx.ID().getText()
        else:
            raise ValueError("Nodo inesperado en 'visitValor'")

    # VisitChildren: método base
    def visitChildren(self, node):
        return "".join(self.visit(child) for child in node.getChildren())


#Menu principal del programa
def menu():
    while True:
        print("=== Menú Principal ===")
        print("1. Traducir archivo")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            archivo = input("Ingrese el nombre del archivo .txt que desea traducir a Python: ")
            if os.path.isfile(archivo):
                traducir_archivo(archivo)
            else:
                print("Archivo no encontrado. Por favor, intente de nuevo.")
        elif opcion == "2":
            print("¡Gracias por usar el Traductor!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

#Traduce todo el programa a Python
def traducir_archivo(ruta_archivo):
    try:
        # Leer el archivo con codificación UTF-8
        from antlr4 import InputStream
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            content = f.read()

        # Crear el lexer y parser de ANTLR4
        lexer = traductorLexer(InputStream(content))
        stream = CommonTokenStream(lexer)
        parser = traductorParser(stream)
        tree = parser.programa()

        #Visualizamos el arbol del Visitor
        #print(tree.toStringTree(recog=parser))

        # Traducir a Python
        translator = traductorToPython()
        codigo_python = translator.visit(tree) #Recorre el arbol
        
        if not codigo_python:
            raise ValueError("Error: El código generado es vacío. Revisa la gramática o los métodos visit.")

        # Mostrar el resultado
        print("\n=== Código Traducido ===")
        print(codigo_python)

        # Pedir al usuario la extensión deseada
        nueva_extension = input("Ingrese la nueva extensión para el archivo de salida (por ejemplo,'.abraham'): ").strip()
        if not nueva_extension.startswith("."):#Por si se le olvida poner el .
            nueva_extension = "." + nueva_extension

        # Guardar en un archivo con la extensión deseada
        nombre_salida = os.path.splitext(ruta_archivo)[0] + nueva_extension
        with open(nombre_salida, "w", encoding='utf-8') as f:
            f.write(codigo_python)
        print(f"Código traducido guardado en: {nombre_salida}")
    except Exception as e:
        print(f"Ocurrió un error al procesar el archivo: {e}")

if __name__ == "__main__":
    menu()