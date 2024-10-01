
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

class BinaryTree:

    class __Node:
        def __init__(self, value, left=None, right=None, other_value=None):
            self.value = value
            self.left = left
            self.right = right
            self.other_value = other_value
            self.height = 0

    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height

    def update_height(self, root):
        if root is not None:
            # print(f'actualizar altura de {root.value}')
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = max(left_height, right_height) + 1
            # print(f'altura izq {left_height} altura der {right_height}')
            # print(f'altura de {root.value} es {root.height}')

    def simple_rotation(self, root, control):
        if control:
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:
            aux = root.right
            root.right = aux.left
            aux.left = root
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root

    def double_rotation(self, root, control):
        if control:
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def balancing(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                # print('desbalanceado a la izquierda')
                if self.height(root.left.left) >= self.height(root.left.right):
                    # print('rotar simple derecha')
                    root = self.simple_rotation(root, True)
                else:
                    # print('rotar doble derecha')
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                # print('desbalanceado a la derecha')
                if self.height(root.right.right) >= self.height(root.right.left):
                    # print('rotar simple izquierda')
                    root = self.simple_rotation(root, False)
                else:
                    # print('rotar doble izquierda')
                    root = self.double_rotation(root, False)
        return root

    def insert_node(self, value, other_value=None):
        def __insert(root, value, other_value=None):
            if root is None:
                return BinaryTree.__Node(value, other_value=other_value)
            elif value < root.value:
                root.left = __insert(root.left, value, other_value)
            else:
                root.right = __insert(root.right, value, other_value)
            root = self.balancing(root)
            self.update_height(root)
            return root

        self.root = __insert(self.root, value, other_value)

    def search(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    # print('lo encontre')
                    return root
                elif key < root.value:
                    # print(f'buscalo a la izquierda de {root.value}')
                    return __search(root.left, key)
                else:
                    # print(f'buscalo a la derecha de {root.value}')
                    return __search(root.right, key)
            # else:
            #     print('no hay nada')
        aux = None
        if self.root is not None:
            aux = __search(self.root, key)
        return aux

    def preorden(self):
        def __preorden(root):
            if root is not None:
                print(root.value)
                # print(f'izquierda de {root.value}')
                __preorden(root.left)
                # print(f'derecha de {root.value}')
                __preorden(root.right)

        if self.root is not None:
            __preorden(self.root)

    def contar_super_heroes(self):
        def __contar_super_heroes(root):
            counter = 0
            if root is not None:
                if root.other_value.get('is_hero') is True:
                    counter = 1
                counter += __contar_super_heroes(root.left)
                counter += __contar_super_heroes(root.right)
            return counter

        return __contar_super_heroes(self.root)
    def contar_villanos(self):
        def __contar_villanos(root):
            counter = 0
            if root is not None:
                
                if root.other_value.get('is_hero') is False:
                    counter = 1
               
                counter += __contar_villanos(root.left)
                counter += __contar_villanos(root.right)
            return counter

        
        return __contar_villanos(self.root)

    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                __inorden(root.right)

        if self.root is not None:
            __inorden(self.root)

    def postorden(self):
        def __postorden(root):
            if root is not None:
                __postorden(root.right)
                print(root.value)
                __postorden(root.left)

        if self.root is not None:
            __postorden(self.root)

    def inorden_villanos(self):
        def __inorden_villanos(root):
            if root is not None:
                __inorden_villanos(root.left)
                if root.other_value.get('is_hero') is not True:
                    print(root.value)
                __inorden_villanos(root.right)

        if self.root is not None:
            __inorden_villanos(self.root)

    def inorden_superheros_start_with(self, start):
        def __inorden_superheros_start_with(root, start):
            if root is not None:
                __inorden_superheros_start_with(root.left, start)
                if root.other_value.get('is_hero') is True and root.value.startswith(start):
                    print(root.value)
                __inorden_superheros_start_with(root.right, start)

        if self.root is not None:
            __inorden_superheros_start_with(self.root, start)

    def proximity_search(self, search_value):
        def __proximity_search(root, search_value):
            if root is not None:
                __proximity_search(root.left, search_value)
                if root.value.startswith(search_value):
                    print(root.value)
                __proximity_search(root.right, search_value)

        if self.root is not None:
            __proximity_search(self.root, search_value)

    def by_level(self):
        pendientes = Queue()
        if self.root is not None:
            pendientes.arrive(self.root)

        while pendientes.size() > 0:
            node = pendientes.attention()
            print(f"nivel {node.height}", node.value)
            if node.left is not None:
                pendientes.arrive(node.left)
            if node.right is not None:
                pendientes.arrive(node.right)

    def delete_node(self, value):
        def __replace(root):
            if root.right is None:
                # print(f'no tiene derecha es el mayor {root.value}')
                return root.left, root
            else:
                # print('seguir buscando nodo par remplaz+ar a la dercha')
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete(root, value):
            value_delete = None
            extra_data_delete = None
            if root is not None:
                if root.value > value:
                    # print(f'buscar  a la izquierda de {root.value}')
                    root.left, value_delete, extra_data_delete = __delete(root.left, value)
                elif root.value < value:
                    # print(f'buscar  a la derecha de {root.value}')
                    root.right, value_delete, extra_data_delete = __delete(root.right, value)
                else:
                    # print('valor encontrado')
                    value_delete = root.value
                    extra_data_delete = root.other_value
                    if root.left is None:
                        # print('a la izquierda no hay nada')
                        return root.right, value_delete, extra_data_delete 
                    elif root.right is None:
                        # print('a la derecha  no hay nada')
                        return root.left, value_delete, extra_data_delete
                    else:
                        # print('tiene ambos hijos')
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                        root.other_value = replace_node.other_value
                        # return root, value_delete
                    root = self.balancing(root)
                    self.update_height(root)
            return root, value_delete, extra_data_delete

        delete_value = None
        delete_extra_value = None
        if self.root is not None:
            self.root, delete_value, delete_extra_value = __delete(self.root, value)
        return delete_value, delete_extra_value



#5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
# se (MCU), desarrollar un algoritmo que contemple lo siguiente:

# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
# leano que indica si es un héroe o un villano, True y False respectivamente;

# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.


arbol = BinaryTree()
arbol.insert_node('Iron Man', {'is_hero': True})
arbol.insert_node('Thanos', {'is_hero': False})
arbol.insert_node('Captain America', {'is_hero': True})
arbol.insert_node('Ultron', {'is_hero': False})
arbol.insert_node('Doctor Strang', {'is_hero': True})  # Mal escrito a propÃ³sito
arbol.insert_node('Loki', {'is_hero': False})
arbol.insert_node('Scarlet Witch', {'is_hero': True})

print("Villanos Ordenados Alfabeticamente: ")
arbol.inorden_villanos()
print("SuperHeroes que inician con C: ")
arbol.inorden_superheros_start_with("C")
print("En el arbol hay : ", arbol.contar_super_heroes(),"SuperHeroes")
print("SuperHeroes ordenados de manera descendente: ")
arbol.postorden()
arbol.proximity_search("Doctor")
arbol.delete_node("Doctor Strang")
arbol.insert_node("Doctor Strange",{"is_hero":True})
arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()
arbol_heroes.insert_node('Iron Man', {'is_hero': True})
arbol_heroes.insert_node('Captain America', {'is_hero': True})
arbol_heroes.insert_node('Doctor Strange', {'is_hero': True})
arbol_heroes.insert_node('Scarlet Witch', {'is_hero': True})
arbol_villanos.insert_node('Loki', {'is_hero': False})
arbol_villanos.insert_node('Ultron', {'is_hero': False})
arbol_villanos.insert_node('Thanos', {'is_hero': False})
print(arbol_heroes.contar_super_heroes())
print(arbol_villanos.contar_villanos())
arbol_heroes.inorden()
arbol_villanos.inorden()




tree = BinaryTree()

# Insertar las criaturas
criaturas = [
    ('Cerbero', {'derrotado_por': 'Heracles', 'descripcion': 'Perro de tres cabezas', 'capturada': None}),
    ('Toro de Creta', {'derrotado_por': 'Heracles', 'descripcion': 'Toro gigante', 'capturada': None}),
    ('Cierva Cerinea', {'derrotado_por': 'Heracles', 'descripcion': 'Cierva dorada', 'capturada': None}),
    ('Jabalí de Erimanto', {'derrotado_por': 'Heracles', 'descripcion': 'Jabalí feroz', 'capturada': None}),
    ('Aves del Estínfalo', {'derrotado_por': 'Heracles', 'descripcion': 'Aves de metal', 'capturada': None}),
    ('Sirenas', {'derrotado_por': None, 'descripcion': 'Criaturas del mar', 'capturada': None}),
    ('Talos', {'derrotado_por': 'Medea', 'descripcion': 'Gigante de bronce', 'capturada': None}),
    ('Basilisco', {'derrotado_por': None, 'descripcion': 'Reptil mortal', 'capturada': None}),
    ('Ladón', {'derrotado_por': 'Heracles', 'descripcion': 'Dragón de cien cabezas', 'capturada': None})
]

# Insertar cada criatura en el árbol
for criatura, info in criaturas:
    tree.insert_node(criatura, info)
def listar_inorden_con_derrotador(tree):
    def __inorden_con_info(root):
        if root is not None:
            __inorden_con_info(root.left)
            derrotador = root.other_value['derrotado_por'] or 'Nadie'
            print(f"Criatura: {root.value}, Derrotado por: {derrotador}")
            __inorden_con_info(root.right)

    if tree.root is not None:
        __inorden_con_info(tree.root)

listar_inorden_con_derrotador(tree)
talos = tree.search('Talos')
if talos:
    print(f"Criatura: {talos.value}, Derrotado por: {talos.other_value['derrotado_por']}, Descripción: {talos.other_value['descripcion']}")
from collections import defaultdict

def contar_derrotas(tree):
    derrotas = defaultdict(int)

    def __contar_derrotas(root):
        if root is not None:
            if root.other_value['derrotado_por']:
                derrotas[root.other_value['derrotado_por']] += 1
            __contar_derrotas(root.left)
            __contar_derrotas(root.right)

    if tree.root is not None:
        __contar_derrotas(tree.root)
    return derrotas

derrotas = contar_derrotas(tree)
top_3_heroes = sorted(derrotas.items(), key=lambda x: x[1], reverse=True)[:3]
print(f"Top 3 héroes que derrotaron más criaturas: {top_3_heroes}")
def listar_derrotados_por(tree, heroe):
    def __listar_derrotados(root, heroe):
        if root is not None:
            if root.other_value['derrotado_por'] == heroe:
                print(f"Criatura: {root.value}")
            __listar_derrotados(root.left, heroe)
            __listar_derrotados(root.right, heroe)

    if tree.root is not None:
        __listar_derrotados(tree.root, heroe)

listar_derrotados_por(tree, 'Heracles')
def listar_no_derrotadas(tree):
    def __listar_no_derrotadas(root):
        if root is not None:
            if root.other_value['derrotado_por'] is None:
                print(f"Criatura: {root.value}")
            __listar_no_derrotadas(root.left)
            __listar_no_derrotadas(root.right)

    if tree.root is not None:
        __listar_no_derrotadas(tree.root)

listar_no_derrotadas(tree)
capturar_criaturas = ['Cerbero', 'Toro de Creta', 'Cierva Cerinea', 'Jabalí de Erimanto']
for criatura in capturar_criaturas:
    nodo = tree.search(criatura)
    if nodo:
        nodo.other_value['capturada'] = 'Heracles'
tree.delete_node('Basilisco')
tree.delete_node('Sirenas')
aves = tree.search('Aves del Estínfalo')
if aves:
    aves.other_value['derrotado_por'] = 'Heracles (varias veces)'
ladon = tree.search('Ladón')
if ladon:
    ladon.value = 'Dragón Ladón'
tree.by_level()
def listar_capturadas_por(tree, heroe):
    def __listar_capturadas(root, heroe):
        if root is not None:
            if root.other_value['capturada'] == heroe:
                print(f"Criatura: {root.value}")
            __listar_capturadas(root.left, heroe)
            __listar_capturadas(root.right, heroe)

    if tree.root is not None:
        __listar_capturadas(tree.root, heroe)

listar_capturadas_por(tree, 'Heracles')