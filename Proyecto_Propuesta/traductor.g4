grammar traductor;

programa: inicioFuncion cuerpo finFuncion;

inicioFuncion: INICIO FUNCION PRINCIPAL;
finFuncion: FIN FUNCION;

cuerpo: instruccion+;

repetir: REPITE NUMERO VECES cuerpo FIN REPITE;

instruccion
    : escribir
    | repetir
    | definicionVariable
    | asignacion          
    | condicion;

asignacion: ID '=' expresion;  // Regla para manejar x = x + 1

escribir: ESCRIBIR (CADENA | expresion);

definicionVariable: tipoVariable ID '=' expresion; 

tipoVariable: ENTERO | TEXTO | BOOLEANO | FLOTANTE;

condicion: SI expresion ENTONCES cuerpo FIN SI;

expresion
    : valor
    | expresion (MAS | MENOS | MULTIPLICACION | DIVISION) expresion
    | expresion (MAYOR | MENOR | MAYORIGUAL | MENORIGUAL | IGUALIGUAL | DIFERENTE) expresion
    | '(' expresion ')';


valor: NUMERO | CADENA | VERDADERO | FALSO | ID;

//Palabras clave
INICIO: 'Inicio';
FUNCION: 'Funcion';
PRINCIPAL: 'principal';
FIN: 'Fin';
ESCRIBIR: 'Escribir';
REPITE: 'Repetir';
VECES: 'Veces';
ENTERO: 'entero';
TEXTO: 'texto';
BOOLEANO: 'booleano';
FLOTANTE: 'flotante';
SI: 'Si';
ENTONCES: 'Entonces';
VERDADERO: 'verdadero';
FALSO: 'falso';

//Operadores Racionales
MAS: '+';
MENOS: '-';
MULTIPLICACION: '*';
DIVISION: '/';
MAYOR: '>';
MENOR: '<';
MAYORIGUAL: '>=';
MENORIGUAL: '<=';
IGUALIGUAL: '==';
DIFERENTE: '!=';

//Identificadores y Literales
ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMERO: [0-9]+;
CADENA: '"' .*? '"';

//Los espacios en blanco o vacios
ESPACIOS: [ \t\r\n]+ -> skip;
