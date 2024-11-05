"""1. Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada
de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir
tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:

a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos
caracteres–;
c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
además un listado por nivel por nombre;
e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
f) Determina cuantos Pokémons hay de tipo eléctrico y acero."""

from arbol_avl import BinaryTree

pokemons = [
    {"name": "Bulbasaur", "number": 1, "type": ["Planta","Veneno"]},
    {"name": "Charmander", "number": 4, "type": ["Fuego"]},
    {"name": "Squirtle", "number": 7, "type": ["Agua"]},
    {"name": "Pikachu", "number": 25, "type": ["Eléctrico"]},
    {"name": "Jigglypuff", "number": 39, "type": ["Normal","Hada"]},
    {"name": "Jolteon", "number": 135, "type": ["Eléctrico"]},
    {"name": "Lycanroc", "number": 745, "type": ["Roca"]},
    {"name": "Tyrantrum", "number": 697, "type": ["Roca", "dragón"]},
    {"name": "Cyndaquil", "number": 155, "type": ["Fuego"]},
    {"name": "Totodile", "number": 158, "type": ["Agua"]},
    {"name": "Treecko", "number": 252, "type": ["Planta"]},
    {"name": "Torchic", "number": 255, "type": ["Fuego"]},
    {"name": "Mudkip", "number": 258, "type": ["Agua"]},
    {"name": "Lucario", "number": 448, "type": ["Acero","Lucha"]},
    {"name": "Greninja", "number": 658, "type": ["Agua","Siniestro"]},
    {"name": "Scizor", "number": 212, "type": ["Acero","Bicho"]},
]

print("-------PUNTO A-------")
tree_name=BinaryTree()
tree_number=BinaryTree()
tree_type=BinaryTree()

for pokemon in pokemons:
    tree_name.insert_node(pokemon["name"],pokemon)
    tree_number.insert_node(pokemon["number"],pokemon)
    for pokemontipo in pokemon['type']:
        node = tree_type.search(pokemontipo)
        if node:
            node.other_value.append(pokemon)
        else:
            tree_type.insert_node(pokemontipo, [pokemon])

print("-------PUNTO B-------")
wanted=input("Ingrese el pokemon que busca: ")
result=tree_name.proximity_search(wanted)
if result:
    print(result.other_value)


wanted_number = int(input("Ingrese el numero del pokemon que busca: "))
result_number=tree_number.search(wanted_number)
if result_number:
    print (result_number.other_value)
else:
    print ("No se encontro pokemon con ese número")

print("-------PUNTO C-------")
wanted_type=input("¿Qué tipo de pokemon busca? ")
result_type=tree_type.search(wanted_type)
if result_type:
    print (result_type.other_value)


print("-------PUNTO D-------")
tree_name.inorden()
tree_number.inorden()
tree_name.by_level()


print("-------PUNTO E-------")
wanted_poke=["Jolteon","Lycanroc","Tyrantrum"]
for poke in wanted_poke:
    resultname = tree_name.search(poke)
    if resultname:
        print(resultname.other_value)

print("-------PUNTO F-------")

typewanted = input("ingrese el tipo de pokemon que desea buscar: ")
nodo = tree_type.search(typewanted)
if nodo and nodo.other_value:
    count = len(nodo.other_value)
else:
    count = 0
print(f"Total de Pokémon de tipo {typewanted}: {count}")