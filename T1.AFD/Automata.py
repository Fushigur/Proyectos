import csv

class MaquinaAFD:
    def __init__(self):
        #Inicialización del AFD.
        self.estados = []  # Conjunto de estados
        self.alfabeto = []  # Alfabeto
        self.transiciones = {}  # Funciones de transición
        self.estado_inicial = None #Estado inicial
        self.estados_aceptacion = []  # Conjunto de estados de aceptación
        self.estado_actual = None

    def definir_estados(self):
        #Define el conjunto de estados del autómata
        print("\nPor favor, ingresa el conjunto de estados. Los estados deben ser separados por espacios.")
        print("Ejemplo: q0 q1 q2")
        self.estados = input("Ingresa el conjunto de estados: ").split()
        print(f"Conjunto de estados: {self.estados}")

    def definir_alfabeto(self):
        #Define el alfabeto del autómata
        print("\nAhora, ingresa el alfabeto. Los símbolos deben ser separados por espacios.")
        print("Ejemplo: a b c o 0 1")
        self.alfabeto = input("Ingresa el alfabeto: ").split()
        print(f"Alfabeto: {self.alfabeto}")

    def definir_transiciones(self):
        #Define las funciones de transición
        print("\nDefiniendo las transiciones del autómata.")
        print("Cada transición sigue la forma: Estado, Simbolo, Estado siguiente.")
        print("Ejemplo: q0, a, q1 (significa que si el autómata está en q0 y lee el símbolo 'a', va al estado q1).")
        self.transiciones = {}
        for estado in self.estados:
            self.transiciones[estado] = {}
            for simbolo in self.alfabeto:
                self.transiciones[estado][simbolo] = input(f"Estado: {estado}, Simbolo: {simbolo}, Estado siguiente: ")

    def definir_estado_inicial(self):
        #Define el estado inicial
        print("\nIngresa el estado inicial.")
        print(f"Recuerda que debe ser uno de los siguientes: {self.estados}")
        self.estado_inicial = input("Ingresa el estado inicial: ")
        if self.estado_inicial not in self.estados:
            print("Estado inicial no válido.")
            return False
        print(f"Estado inicial: {self.estado_inicial}")

    def definir_estados_aceptacion(self):
        #Define los estados de aceptación/Final.
        print("\nAhora ingresa el estado de aceptación/Final.")
        print(f"Recuerda que deben ser parte de los estados definidos: {self.estados}")
        print("Ejemplo: q1 q2")
        self.estados_aceptacion = input("Ingresa el estado Final: ").split()
        print(f"Estado Final: {self.estados_aceptacion}")

    def verificar_cadena(self, cadena):
        #Verifica si la cadena es aceptada por el autómata.
        self.estado_actual = self.estado_inicial
        for simbolo in cadena:
            if simbolo in self.transiciones[self.estado_actual]:
                self.estado_actual = self.transiciones[self.estado_actual][simbolo]
            else:
                print(f"Cadena rechazada en el estado {self.estado_actual} con el símbolo {simbolo}.")
                return False
        if self.estado_actual in self.estados_aceptacion:
            print("Cadena aceptada.")
            return True
        else:
            print(f"Cadena rechazada. El estado final {self.estado_actual} no es de aceptación.")
            return False

    def cargar_desde_archivo(self, archivo):
        #Carga el autómata desde un archivo .csv o .txt
        with open(archivo, 'r') as f:
            reader = csv.reader(f)
            lineas = list(reader)

        # Procesar los estados, alfabeto y transiciones
        self.estados = []
        self.alfabeto = lineas[0][1:]  # Asumimos que el alfabeto está en la primera línea
        self.transiciones = {}

        for linea in lineas[1:]:
            estado = linea[0]
            transiciones_estado = linea[1:]
            if estado.startswith('->'):  # Identificar estado inicial
                self.estado_inicial = estado[2:]
                estado = self.estado_inicial
            if estado.startswith('*'):  # Identificar estado Final
                estado_aceptacion = estado[1:]
                self.estados_aceptacion.append(estado_aceptacion)
                estado = estado_aceptacion

            self.estados.append(estado)
            self.transiciones[estado] = {}
            for i, simbolo in enumerate(self.alfabeto):
                self.transiciones[estado][simbolo] = transiciones_estado[i]

        print(f"Estados: {self.estados}")
        print(f"Alfabeto: {self.alfabeto}")
        print(f"Estado inicial: {self.estado_inicial}")
        print(f"Estados de aceptación: {self.estados_aceptacion}")
        print(f"Transiciones: {self.transiciones}")

def mostrar_menu():
    #Muestra el menú principal.
    print("\n<-- MENÚ PRINCIPAL -->")
    print("1. Ingresar el autómata manualmente")
    print("2. Cargar la tabla del autómata desde un archivo")
    print("3. Salir")
    return input("Elige una de las opciones: ")

def main():
    #Función principal que gestiona el flujo del programa.
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            # Ingresamos el autómata manualmente desde el teclado
            afd = MaquinaAFD()
            afd.definir_estados()
            afd.definir_alfabeto()
            afd.definir_transiciones()
            afd.definir_estado_inicial()
            afd.definir_estados_aceptacion()

            # Ingreso de la cadena a validar
            cadena = input("\nIngresa la cadena a validar: ")
            afd.verificar_cadena(cadena)

        elif opcion == "2":
            # Cargar autómata desde un archivo
            nombre_archivo = input("Ingresa el nombre del archivo (puede ser .csv o .txt): ")
            afd = MaquinaAFD()
            afd.cargar_desde_archivo(nombre_archivo)

            # Ingreso de la cadena a validar
            cadena = input("\nIngresa la cadena a validar: ")
            afd.verificar_cadena(cadena)

        elif opcion == "3":
            print("Fin del programa.")
            break

        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()