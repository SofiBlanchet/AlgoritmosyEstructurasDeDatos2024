
class Queue:
    def __init__(self):
        self.__elements = []

    def arrive(self, element):
        self.__elements.append(element)

    def attention(self):
        if len(self.__elements) > 0:
            return self.__elements.pop(0)
        else:
            return None
    
    def size(self):
        return len(self.__elements)

    def on_front(self):
        if len(self.__elements) > 0:
            return self.__elements[0]
        else:
            return None
    
    def move_to_end(self):
        element = self.attention()
        if element is not None:
            self.arrive(element)

# 11. Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta
# de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:
# a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
# b. indicar el plantea natal de Luke Skywalker y Han Solo
# c. insertar un nuevo personaje antes del maestro Yoda
# d. eliminar el personaje ubicado después de Jar Jar Binks

pj = [{"name": "Luke Skywalker", "planet": "Tatooine",
      "name": "Anakin Skywalker" , "planet": "Tatooine",
      "name": "Leia Organa", "planet":"Alderaan",
      "name": "Yoda","planet":"Dagobah",
      "name": "Han Solo", "planet": "Corellia",
      "name": "Jar Jar Binks", "planet":"Naboo",
      "name": "Padme Amidala", "planet": "Naboo"}]

pj = [{"name": "Luke Skywalker", "planet": "Tatooine"},
      {"name": "Anakin Skywalker" , "planet": "Tatooine"},
      {"name": "Leia Organa", "planet":"Alderaan"},
      {"name": "Yoda","planet":"Dagobah"},
      {"name": "Han solo", "planet": "Corellia"},
      {"name": "Jar Jar Binks", "planet":"Naboo"},
      {"name": "Padme Amidala", "planet": "Naboo"}]
personajes = Queue()
queue_aux = Queue()
lista_planetas = []
for personaje in pj:
    personajes.arrive(personaje)
#PUNTO A y B
for i in range(personajes.size()):
    aux = personajes.attention()
    if aux["name"] in ["Luke Skywalker"]:
        print("Planteas de luke : ",aux["planet"])
    if aux["name"] in ["Han solo"]:
        print("Planeta de Han Solo: ",aux["planet"])
    if aux["planet"] in ["Alderaan", "Endor","Tatooine"]:
        print(aux)
    queue_aux.arrive(aux)
for i in range(queue_aux.size()):
    a = queue_aux.attention()
    personajes.arrive(a)
#punto C
nuevo_personaje = {"name": "Ahsoka Tano", "planet": "Shili"}
cola_aux = Queue()
insertado = False
for i in range(personajes.size()):
    personaje_actual = personajes.attention() 
    if personaje_actual["name"] == "Yoda" and not insertado:
        cola_aux.arrive(nuevo_personaje)  
        insertado = True
    cola_aux.arrive(personaje_actual)
for i in range(cola_aux.size()):
    personajes.arrive(cola_aux.attention())
#Punto D
cola_aux = Queue()
saltar_siguiente = False
for i in range(personajes.size()):
    personaje_actual = personajes.attention()  
    if saltar_siguiente:
        saltar_siguiente = False  
        continue
    if personaje_actual["name"] == "Jar Jar Binks":
        saltar_siguiente = True

    cola_aux.arrive(personaje_actual)  
for i in range(cola_aux.size()):
    personajes.arrive(cola_aux.attention())
print("Lista final de personajes en la cola:")
for i in range(personajes.size()):
    print(personajes.attention())

# 22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se cono-
# ce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, 
# {Natasha Ro-manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.

personajes_mcu = [
    {"nombre_personaje": "Tony Stark", "nombre_superheroe": "Iron Man", "genero": "M"},
    {"nombre_personaje": "Steve Rogers", "nombre_superheroe": "Capitán América", "genero": "M"},
    {"nombre_personaje": "Natasha Romanoff", "nombre_superheroe": "Black Widow", "genero": "F"},
    {"nombre_personaje": "Thor Odinson", "nombre_superheroe": "Thor", "genero": "M"},
    {"nombre_personaje": "Bruce Banner", "nombre_superheroe": "Hulk", "genero": "M"},
    {"nombre_personaje": "Wanda Maximoff", "nombre_superheroe": "Scarlet Witch", "genero": "F"},
    {"nombre_personaje": "Peter Parker", "nombre_superheroe": "Spider-Man", "genero": "M"},
    {"nombre_personaje": "Carol Danvers", "nombre_superheroe": "Captain Marvel", "genero": "F"},
    {"nombre_personaje": "T'Challa", "nombre_superheroe": "Black Panther", "genero": "M"},
    {"nombre_personaje": "Gamora", "nombre_superheroe": "Gamora", "genero": "F"},
    {"nombre_personaje":"Scott Lang","nombre_superheroe":"Ant-Man","genero":"M"}
]
cola = Queue()
cola_aux = Queue()
list_femenino = []
lista_masculino = []
lista_letras = []
for char in personajes_mcu:
    cola.arrive(char)
for i in range(cola.size()):
    aux = cola.attention()
    #punto a
    if aux["nombre_superheroe"] == "Captain Marvel":
        print("el nombre de la capitana marvel es: ",aux["nombre_personaje"])
    #punto b
    if aux["genero"] == "F" :
        list_femenino.append(aux)
    #punto c
    if aux["genero"] == "M":
        lista_masculino.append(aux)
    #punto d
    if aux["nombre_personaje"]== "Scott Lang":
        print("el nombre de superheroe de Scott Lang: ", aux["nombre_superheroe"])
    #punto e
    if aux["nombre_personaje"].startswith("S") == True:
        lista_letras.append(aux)
    #punto f
    if aux["nombre_personaje"]== "Carol Danvers":
        print("el nombre de superheroe de Carol Danvers es: ",aux["nombre_superheroe"])
    cola_aux.arrive(aux)
for i in range(cola_aux.size()):
    cola.arrive(cola_aux.attention())

print("personajes feminos: ",list_femenino)
print("personajes masculinos : ",lista_masculino)
print("personajes que empiezan con S: ", lista_letras)


# 3. El general Hux es la persona encargada de administrar todas las operaciones de la base Starki-
# ller, para lo cual nos solicita desarrollar un algoritmo que permita controlar las actividades que
# se realizan, contemplando lo siguiente:

# a. debe contemplar distintas prioridades para el control de operaciones de acuerdo al siguien-
# te criterio: pedidos de líder supremo Snoke y de Kylo Ren nivel tres, de capitán Phasma
# nivel dos y el resto de las operaciones nivel a cargo de los generales de la base de nivel uno;
# b. de cada actividad se conoce quien es el encargado, una descripción, la hora y opcional-
# mente la cantidad de Stormtroopers requeridos;
# c. utilizar una cola de prioridad para administrar las distintas operaciones, debe cargar al
# menos ocho: dos de nivel tres, cuatro de nivel dos y cuatro de nivel uno;
# d. opcionalmente se podrán agregar operaciones luego de atender una;
# e. realizar la atención de las operaciones de la cola;
# f. luego de atender la quinta operación, agregar una operación solicitada por capitán Phasma
# para revisión de intrusos en el hangar B7 que requiere 25 Stormstroopers;
# g. luego de atender la sexta operación, agregar una operación solicitada por el líder supremo
# Snoke para destruir el planeta Takodana.


class HeapMax():

    def __init__(self):
        self.elements = []
    
    def add(self, value):
        self.elements.append(value)
        self.float(len(self.elements)-1)

    def remove(self):
        if len(self.elements) > 0:
            self.interchange(0, len(self.elements)-1)
            value = self.elements.pop()
            self.sink(0)
            return value
        else:
            return None

    def interchange(self, index_1, index_2):
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    def float(self, index):
        father = (index-1) // 2
        while index > 0 and self.elements[index] > self.elements[father]:
            self.interchange(index, father)
            index = father
            father = (index-1) // 2

    def sink(self, index):
        left_child = (index * 2) + 1
        control = True
        while control and left_child < len(self.elements):
            right_child = (index * 2) + 2
            max = left_child
            if right_child < len(self.elements):
                if self.elements[right_child] > self.elements[left_child]:
                    max = right_child
            if self.elements[index] < self.elements[max]:
                self.interchange(index, max)
                index = max
                left_child = (index * 2) + 1
            else:
                control = False

    def heapify(self, elements):
        self.elements = elements
        for i in range(len(self.elements)):
            self.float(i)

    def sort(self):
        result = []
        amount_elements = len(self.elements)
        for i in range(amount_elements):
            value = self.remove()
            result.append(value)
        return result
    
    def arrive(self, value, priority):
        self.add([priority, value])

    def atention(self):
        return self.remove()

    def change_proirity(self, index, new_priority):
        if index < len(self.elements):
            previous_priority = self.elements[index][0]
            self.elements[index][0] = new_priority
            if new_priority > previous_priority:
                self.float(index)
            elif new_priority < previous_priority:
                self.sink(index)

heap = HeapMax()


actividades = [
    (3, ("Líder Supremo Snoke", "Destruir la resistencia en Jakku", "10:00", 50)),
    (3, ("Kylo Ren", "Buscar mapa de Skywalker", "11:00", None)),
    (2, ("Capitán Phasma", "Revisión de disciplina", "12:00", 10)),
    (2, ("Capitán Phasma", "Inspeccionar armas", "13:00", 5)),
    (2, ("Capitán Phasma", "Organizar patrullas", "14:00", 15)),
    (2, ("Capitán Phasma", "Entrenamiento de Stormtroopers", "15:00", 20)),
    (1, ("General Hux", "Revisión de sistemas", "16:00", None)),
    (1, ("General Hux", "Supervisión de prisioneros", "17:00", None))
]

#PUNTO A
for actividad in actividades:
    heap.add(actividad)

#PUNTO B
def mostrar_actividad(actividad):
    encargado, descripcion, hora, stormtroopers = actividad
    stormtroopers_str = f", Stormtroopers: {stormtroopers}" if stormtroopers else ", Stormtroopers: No requeridos"
    return f"Encargado: {encargado}, Descripción: {descripcion}, Hora: {hora}{stormtroopers_str}"

#PUNTO E y F
for i in range(5):
    actividad_atendida = heap.remove()[1]
    print(f"Atendiendo operación {i+1}: {mostrar_actividad(actividad_atendida)}")


heap.add((2, ("Capitán Phasma", "Revisión de intrusos en el hangar B7", "18:00", 25)))

#PUNTO G
actividad_atendida = heap.remove()[1]
print(f"Atendiendo operación 6: {mostrar_actividad(actividad_atendida)}")


heap.add((3, ("Líder Supremo Snoke", "Destruir el planeta Takodana", "19:00", None)))


contador = 7
while heap.elements:
    actividad_atendida = heap.remove()[1]
    print(f"Atendiendo operación {contador}: {mostrar_actividad(actividad_atendida)}")
    contador += 1