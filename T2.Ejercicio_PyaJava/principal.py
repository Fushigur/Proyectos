from antlr4 import *
from traductorPyaJavaLexer import traductorPyaJavaLexer
from traductorPyaJavaParser import traductorPyaJavaParser
from PythonaJava import PythonaJava 

def main():
    file_path = input("Ingresa el nombre o la ruta del archivo Python: ")

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            python_code = file.read()
    except FileNotFoundError:
        print(f"El archivo {file_path} no se encuentra. Asegúrate de que la ruta sea correcta.")
        return

    lexer = traductorPyaJavaLexer(InputStream(python_code))
    token_stream = CommonTokenStream(lexer)

    parser = traductorPyaJavaParser(token_stream)

    tree = parser.program()

    converter = PythonaJava()
    walker = ParseTreeWalker()
    walker.walk(converter, tree)

    java_code = converter.get_java_code()
    with open("PyaJava.java", "w") as java_file:
        java_file.write("public class PyaJava {\n")
        java_file.write(java_code)
        java_file.write("\n}")

    print("Función convertida y guardada en PyaJava.java")

if __name__ == '__main__':
    main()
