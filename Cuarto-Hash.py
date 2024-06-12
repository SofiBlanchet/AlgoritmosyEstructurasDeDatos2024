"""Escribir un algoritmo que permita utilizar tres tablas hash para guardar los datos de Pokémons,
que contemple las siguientes actividades: 

a. en la primera tabla hash la función hash debe ser sobre el tipo de Pokémon, en la segunda
tabla la función hash deberá utilizar el ultimo dígito del número del Pokémon como clave y 
la tercera sera en base  a su nivel repartiéndolos en 10 posiciones dentro de la tabla; 

b. debe utilizar tablas hash abiertas con listas como estructura secundaria;

c. si el Pokémon es de más de un tipo deberá cargarlo en cada uno de las tabla que indiquen estos tipos;

d. deberá permitir cargar Pokémons de los cuales se dispone de su número, nombre, tipo/s, nivel.

e. mostrar todos los Pokémons cuyos numeros terminan en 3, 7 y 9;

f. mostrar todos los Pokémons cuyos niveles son multiplos de 2, 5 y 10;

g. mostrar todos los Pokémons de los siguientes tipo: Acero, Fuego, Electrifico, Hielo"""

class Pokemon:
    def __init__(self,numero, nombre, tipo, nivel):
        self.nombre = nombre
        self.tipo = tipo
        self.numero = numero
        self.nivel = nivel

    def __str__(self):
        return f"#{self.numero} - {self.nombre}, Tipo: {self.tipo}, Nivel: {self.nivel}"

def hash_tipo(pokemon):
    return pokemon.tipo

def hash_ultimo(pokemon):
    return pokemon.numero % 10

def hash_nivel(pokemon):
    return pokemon.nivel // 10

tabla_tipo = {}
tabla_ultimo = {}
tabla_nivel = {}

pokemones = [
    Pokemon(25, "Pikachu", "Electrico", 15),
    Pokemon(6, "Charizard", "Fuego/Volador", 36),
    Pokemon(1, "Bulbasaur", "Planta/Veneno", 5),
    Pokemon(7, "Squirtle", "Agua", 8),
    Pokemon(39, "Jigglypuff", "Normal/Hada", 18),
    Pokemon(52, "Meowth", "Normal", 10),
    Pokemon(54, "Psyduck", "Agua", 22),
    Pokemon(66, "Machop", "Lucha", 16),
    Pokemon(74, "Geodude", "Roca/Tierra", 12),
    Pokemon(133, "Eevee", "Normal", 5),
    Pokemon(143, "Snorlax", "Normal", 30),
    Pokemon(131, "Lapras", "Agua/Hielo", 45),
    Pokemon(132, "Ditto", "Normal", 25),
    Pokemon(147, "Dratini", "Dragón", 10),
    Pokemon(150, "Mewtwo", "Psíquico", 70)
]

for pokemon in pokemones:
    tipos=pokemon.tipo.split("/")
    for tipo in tipos:
        if tipo not in tabla_tipo:
            tabla_tipo[tipo]=[]
        tabla_tipo[tipo].append(pokemon)

    numero=hash_ultimo(pokemon)
    if numero not in tabla_ultimo:
        tabla_ultimo[numero]=[]
    tabla_ultimo[numero].append(pokemon)

    nivel=hash_nivel(pokemon)
    if nivel not in tabla_nivel:
        tabla_nivel[nivel]=[]
    tabla_nivel[nivel].append(pokemon)

print ("------------------------------------------------------------")
print ("Los pokemons que su ultimo digito es 3, 7 o 9")
print ("------------------------------------------------------------")
for numero,pokemons in tabla_ultimo.items():
    if numero in [3,7,9]:
        for pokemon in pokemons:
            print (pokemon)

print ("------------------------------------------------------------")
print ("Los pokemons cuyos niveles son multiplos de 2, 5 y 10 son: ")
print ("------------------------------------------------------------")
for nivel,pokemons in tabla_nivel.items():
    for pokemon in pokemons:
        if pokemon.nivel % 2==0 or pokemon.nivel % 5==0:
            print (pokemon)

print ("------------------------------------------------------------")
print ("Los pokemons de los siguientes tipos: Acero, Fuego, Electrifico, Hielo son:")
print ("------------------------------------------------------------")
for tipo,pokemons in tabla_tipo.items():
    if tipo in ["Acero", "Fuego", "Electrico", "Hielo"]:
        for pokemon in pokemons:
            print (pokemon)