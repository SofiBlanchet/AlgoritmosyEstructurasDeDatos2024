
def by_name(item):
    return item['nombre']

def by_house(item):
    return item['casa_comic']+item['nombre']

def search( list_values, criterio, value):
    for index, element in enumerate(list_values):
        if element[criterio] == value:
            return index

def remove( list_values, criterio, value):
    index = search( list_values, criterio, value)
    if index is not None:
        return list_values.pop(index)

def show_list(title, list_values):
    print()
    print(f"{title}")
    for index, elemento in enumerate(list_values):
        print(index, elemento)
    print()

def show_list_list(title, subtitle, list_values):
    print()
    print(f"{title}")
    for index, elemento in enumerate(list_values):
        print(index, elemento['nombre'])
        print(f"    {subtitle}")
        for second_index, second_element in enumerate(elemento['sublist']):
            print('    ', second_index, second_element)
    print()

"""Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesa-
rias para poder realizar las siguientes actividades:

a. eliminar el nodo que contiene la información de Linterna Verde;
b. mostrar el año de aparición de Wolverine;
c. cambiar la casa de Dr. Strange a Marvel;
d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
“traje” o “armadura”;
e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
sea anterior a 1963;
f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
g. mostrar toda la información de Flash y Star-Lord;
h. listar los superhéroes que comienzan con la letra B, M y S;
i. determinar cuántos superhéroes hay de cada casa de comic."""

super_heroes = [
  {
    "nombre": "Linterna Verde",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Miembro de la Tropa de Linternas Verdes, posee un anillo que le otorga poderes basados en la fuerza de voluntad."
  },
  {
    "nombre": "Wolverine",
    "año_aparicion": 1974,
    "casa_comic": "Marvel Comics",
    "biografia": "Mutante con garras retráctiles y habilidades regenerativas, miembro de los X-Men."
  },
  {
    "nombre": "Doctor Strange",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Hechicero supremo del universo Marvel, maestro de las artes místicas y protector de la realidad."
  },
  {
    "nombre": "Capitana Marvel",
    "año_aparicion": 1968,
    "casa_comic": "Marvel Comics",
    "biografia": "Heroína cósmica con poderes de vuelo, fuerza sobrehumana y energía cósmica."
  },
  {
    "nombre": "Mujer Maravilla",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Princesa amazona y una de las principales defensoras de la justicia y la igualdad en el Universo DC."
  },
  {
    "nombre": "Flash",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Velocista con la capacidad de correr a velocidades superiores a la luz, miembro de la Liga de la Justicia."
  },
  {
    "nombre": "Star-Lord",
    "año_aparicion": 1976,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los Guardianes de la Galaxia, experto en combate y estrategia intergaláctica."
  },
  {
    "nombre": "Superman",
    "año_aparicion": 1938,
    "casa_comic": "DC Comics",
    "biografia": "El Hombre de Acero, uno de los héroes más icónicos de DC con superpoderes sobrehumanos."
  },
  {
    "nombre": "Batman",
    "año_aparicion": 1939,
    "casa_comic": "DC Comics",
    "biografia": "El Caballero Oscuro, detective y luchador experto que protege Gotham City."
  },
  {
    "nombre": "Iron Man",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Tony Stark, genio multimillonario y superhéroe con una armadura tecnológica de alta tecnología."
  },
  {
    "nombre": "Wonder Woman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "La princesa amazona Diana, guerrera y defensora de la paz y la justicia en el mundo."
  },
  {
    "nombre": "Spider-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Peter Parker, joven héroe con habilidades arácnidas tras ser picado por una araña radiactiva."
  },
  {
    "nombre": "Thor",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Dios nórdico del trueno y miembro de los Vengadores, posee un martillo encantado llamado Mjolnir."
  },
  {
    "nombre": "Aquaman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Rey de Atlantis con la capacidad de comunicarse con la vida marina y controlar el agua."
  },
  {
    "nombre": "Green Arrow",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Oliver Queen, arquero habilidoso y defensor de la justicia con su arco y flechas."
  },
  {
    "nombre": "Hulk",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Bruce Banner, científico transformado en monstruo verde con fuerza increíble."
  },
  {
    "nombre": "Black Widow",
    "año_aparicion": 1964,
    "casa_comic": "Marvel Comics",
    "biografia": "Natasha Romanoff, espía rusa y experta en combate mano a mano y armas."
  },
  {
    "nombre": "Mr. Fantástico",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los 4 Fantásticos, científico brillante con la capacidad de estirar y deformar su cuerpo."
  },
  {
    "nombre": "La Mujer Invisible",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee el poder de hacerse invisible y crear campos de fuerza."
  },
  {
    "nombre": "La Antorcha Humana",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, puede envolverse en llamas y volar a altas velocidades."
  },
  {
    "nombre": "La Cosa",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee una fuerza y resistencia sobrehumanas, con piel rocosa."
  },
  {
    "nombre": "Capitán América",
    "año_aparicion": 1941,
    "casa_comic": "Marvel Comics",
    "biografia": "El supersoldado Steve Rogers, símbolo de libertad y justicia con escudo indestructible."
  },
  {
    "nombre": "Ant-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Hanbiografiak Pym o Scott Lang, héroes capaces de cambiar de tamaño y comunicarse con insectos. Usa un traje que lo hace pequeño."
  }]

print ("---------- PUNTO A ----------")
print ("Heroe quitado: ", remove(super_heroes,"nombre","Linterna Verde"))

print ("---------- PUNTO B ----------") 
pos=(search (super_heroes, 'nombre', "Wolverine"))
if pos is not None:
    print (super_heroes[pos]['nombre'],"apareció en el año",super_heroes[pos]['año_aparicion'])

print ("---------- PUNTO C ----------")
pos=(search (super_heroes, 'nombre', "Doctor Strange"))
if pos is not None:
    super_heroes[pos]['casa_comic']= "DC Comics"
print ("Ahora",super_heroes[pos] ['nombre'], "pertenece a la casa ",super_heroes[pos] ['casa_comic'])

print("---------- PUNTO D ----------")
print ("Los heroes que usan traje o armadura son: ")
for index, heroe in enumerate(super_heroes):
    if "traje" in heroe["biografia"] or "armadura" in heroe["biografia"]:
        print ("En la posicion" ,index, heroe['biografia'])

print ("---------- PUNTO E ----------") 
print ("Los personajes que aparecieron en 1963 o antes son: ")
for index, heroe in enumerate(super_heroes):
    if heroe['año_aparicion']<= 1963:
        print (heroe['nombre'],heroe['casa_comic'],heroe['año_aparicion'])

print ("---------- PUNTO F ----------")
pos1=search(super_heroes,'nombre',"Capitana Marvel")
pos2=search(super_heroes,'nombre',"Mujer Maravilla")
if pos1 is not None:
    print (super_heroes[pos1]['nombre'], "pertenece a la casa ",super_heroes[pos1]['casa_comic'])
if pos2 is not None:
    print (super_heroes[pos2]['nombre'], "pertenece a la casa ",super_heroes[pos2]['casa_comic'])

print("---------- PUNTO G ----------")
print ("La información completa de Flash y Star-Lord es:")
pos3=search(super_heroes,'nombre',"Flash")
print (super_heroes[pos3])
pos4=search(super_heroes,'nombre',"Star-Lord")
print(super_heroes[pos4])

print("---------- PUNTO H ----------")
print ("Los superheroes cuyo nombre empiezan con B, S o M son:")
for index, heroe in enumerate(super_heroes):
    if heroe['nombre'].startswith(('B', 'S', 'M')):
        print(index, heroe['nombre'])

print("---------- PUNTO I ----------")
D=0
M=0
for index, heroe in enumerate(super_heroes):
    if heroe['casa_comic']=="DC Comics":
        D+=1
    elif heroe ["casa_comic"]=="Marvel Comics":
        M+=1
print ("La cantidad en DC Comics es de ",D, ", mientras que en Marvel Comics",M)

print ("------------------------------------------------------------------------------------")
print("------------------PUNTO 15-------------------------")
entrenadores = [
    {
        "nombre": "Ash Ketchum",
        "torneos_ganados": 7,
        "batallas_perdidas": 50,
        "batallas_ganadas": 120
    },
    {
        "nombre": "Goh",
        "torneos_ganados": 2,
        "batallas_perdidas": 10,
        "batallas_ganadas": 40
    },
    {
        "nombre": "Leon",
        "torneos_ganados": 10,
        "batallas_perdidas": 5,
        "batallas_ganadas": 100
    },
    {
        "nombre": "Chloe",
        "torneos_ganados": 1,
        "batallas_perdidas": 8,
        "batallas_ganadas": 30
    },
    {
        "nombre": "Raihan",
        "torneos_ganados": 4,
        "batallas_perdidas": 15,
        "batallas_ganadas": 60
    }
]

pokemons = [
    {
        "nombre": "Pikachu",
        "nivel": 35,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "nombre": "Pikachu",
        "nivel": 20,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "nombre": "Charizard",
        "nivel": 40,
        "tipo": "Fuego",
        "subtipo": "Volador"
    },
    {
        "nombre": "Bulbasaur",
        "nivel": 30,
        "tipo": "Planta",
        "subtipo": "Veneno"
    },
    {
        "nombre": "Starmie",
        "nivel": 30,
        "tipo": "Agua",
        "subtipo": "Psíquico"
    },
    {
        "nombre": "Psyduck",
        "nivel": 25,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Gyarados",
        "nivel": 35,
        "tipo": "Agua",
        "subtipo": "Volador"
    },
    {
        "nombre": "Onix",
        "nivel": 38,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Geodude",
        "nivel": 28,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Vulpix",
        "nivel": 20,
        "tipo": "Fuego",
        "subtipo": None
    },
    {
        "nombre": "Blastoise",
        "nivel": 50,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Umbreon",
        "nivel": 45,
        "tipo": "Siniestro",
        "subtipo": None
    },
    {
        "nombre": "Nidoking",
        "nivel": 40,
        "tipo": "Veneno",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Dragonite",
        "nivel": 55,
        "tipo": "Dragón",
        "subtipo": "Volador"
    },
    {
        "nombre": "Aerodactyl",
        "nivel": 52,
        "tipo": "Roca",
        "subtipo": "Volador"
    },
    {
        "nombre": "Terrakion",
        "nivel": 52,
        "tipo": "Tierra",
        "subtipo": None
    }
]

nombres = ["Ash Ketchum", "Goh", "Leon", "Chloe", "Raihan"]

lista_entrenadores = []

for entrenador in entrenadores:
    entrenador.update({'sublist': []})
    lista_entrenadores.append(entrenador)

for pokemon in pokemons:
    pos = search(lista_entrenadores, 'nombre', choice(nombres))
    if pos is not None:
        lista_entrenadores[pos]['sublist'].append(pokemon)
    else:
        print('no existe el entrenador')



print("-------------PUNTO A-------------")
buscado=(input("Ingrese el entrenador que busca para saber la cantidad de pokemones que tiene: "))
pos=search(lista_entrenadores,'nombre',buscado)
c=0
if pos is not None:
      for pokemon in lista_entrenadores[pos]['sublist']:
          c+=1
      print("La cantidad de pokemones de",buscado, "es de",c)

print("-------------PUNTO B-------------")
print ("Los entrenadores con mas de 3 torneos ganados son: ")
for index,entrenador in enumerate(lista_entrenadores):
    if entrenador['torneos_ganados']>3:
        print (entrenador['nombre'])

print("-------------PUNTO C-------------") #el que mas batallas gano, y sus poke mas poderoso
 
lista_entrenadores.sort(key=by_ganado,reverse=True)
show_list_list('Entrenadores', 'Pokemons', lista_entrenadores)
mayor=0
for pokemon in lista_entrenadores[0]['sublist']:
    if pokemon['nivel']>mayor:
        mayor=pokemon['nivel']
        pokemonn=pokemon['nombre']
print ("El pokemon de mayor nivel es", pokemonn, "con nivel" ,mayor)

print("-------------PUNTO D-------------")
buscado = input("Ingrese el entrenador que busca para ver sus pokemons: ")
pos = search(lista_entrenadores, 'nombre', buscado)

if pos is not None:
    entrenador = lista_entrenadores[pos]
    print(f"Datos del entrenador: torneos ganados: {entrenador['torneos_ganados']}, batallas perdidas: {entrenador['batallas_perdidas']}, batallas ganadas: {entrenador['batallas_ganadas']}")
    print("Pokémones:")
    for pokemon in lista_entrenadores[pos]['sublist']:
        print (pokemon)

print("-------------PUNTO E-------------")
for entrenador in lista_entrenadores:
    porcentaje = (entrenador['batallas_ganadas'] / (entrenador['batallas_ganadas'] + entrenador['batallas_perdidas'])) * 100
    if porcentaje > 79:
        print(f"Nombre: {entrenador['nombre']}, porcentaje de batallas ganadas: {porcentaje:.2f}%")

print("-------------PUNTO F-------------")

for entrenador in lista_entrenadores:
    for pokemon in entrenador['sublist']:
        if pokemon['tipo'] == "Fuego" or pokemon['subtipo'] == "Fuego":
            if pokemon['tipo'] == "Planta" or pokemon['subtipo'] == "Planta":
                print(f"Entrenador :{entrenador['nombre']}, Pokemon :{pokemon['nombre']}, tipo/subtipo : Fuego/Planta")
        if pokemon['tipo'] == "Agua" or pokemon['subtipo'] == "Agua":
            if pokemon['tipo'] == "Volador" or pokemon['subtipo'] == "Volador":
                print(f"Entrenador :{entrenador['nombre']}, Pokemon :{pokemon['nombre']}, tipo/subtipo : Agua/Volador")

print("-------------PUNTO G-------------")

nombre_entrenador = input("Ingrese nombre de entrenador para promediar el nivel de sus pokemons")

def sumatorianiveles(pokemons):
    if len(pokemons) == 1:
      return pokemons[0]['nivel']
    else:
        nivel = pokemons[-1]['nivel']
        pokemons.pop()
        return nivel + sumatorianiveles(pokemons)
    
for entrenador in lista_entrenadores:
    if entrenador['nombre'] == nombre_entrenador:
        if len(entrenador['sublist']) != 0:
          cantidad = len(entrenador['sublist'])
          promedio = sumatorianiveles(entrenador['sublist']) / cantidad
          print(f"Entrenador :{entrenador['nombre']}, Nivel promedio :{promedio}")


print("-------------PUNTO H-------------")
nombre_pokemon = input("Ingrese nombre de pokemon a buscar entre los entrenadores")
cant = 0
for entrenador in lista_entrenadores:
    for pokemon in entrenador['sublist']:
        if pokemon['nombre'] == nombre_pokemon:
            cant += 1
print(f"La cantidad de pokemones que tiene a {nombre_pokemon} es : {cant}")


print("-------------PUNTO I-------------")
for entrenador in lista_entrenadores:
    # Convertir cada diccionario a una tupla de pares clave-valor ordenados
    tuplas = [tuple(sorted(d.items())) for d in entrenador['sublist']]
    if len(tuplas) != len(set(tuplas)):
        print(entrenador)

print("-------------PUNTO J-------------")

pokemones_buscados = ["Tyrantrum", "Terrakion", "Wingull"]
for entrenador in lista_entrenadores:
    for pokemon in entrenador['sublist']:
      if pokemon['nombre'] in pokemones_buscados:
          print(f"El entrenador {entrenador['nombre']} tiene a {pokemon['nombre']}")


