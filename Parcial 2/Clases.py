
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
    
    def search(self, value):
        for index, element in enumerate(self.elements):
            if element[1][0] == value:
                return index
    
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


class HeapMin():

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
        while index > 0 and self.elements[index] < self.elements[father]:
            self.interchange(index, father)
            index = father
            father = (index-1) // 2

    def sink(self, index):
        left_child = (index * 2) + 1
        control = True
        while control and left_child < len(self.elements):
            right_child = (index * 2) + 2
            min = left_child
            if right_child < len(self.elements):
                if self.elements[right_child] < self.elements[left_child]:
                    min = right_child
            if self.elements[index] > self.elements[min]:
                self.interchange(index, min)
                index = min
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

    def search(self, value):
        for index, element in enumerate(self.elements):
            if element[1][0] == value:
                return index

    def arrive(self, value, priority):
        self.add([priority, value])

    def atention(self):
        return self.remove()

    def change_proirity(self, index, new_priority):
        if index < len(self.elements):
            previous_priority = self.elements[index][0]
            self.elements[index][0] = new_priority
            if new_priority < previous_priority:
                self.float(index)
            elif new_priority > previous_priority:
                self.sink(index)

class Stack:

    def __init__(self):
        self.__elements = []

    def push(self, element):
        self.__elements.append(element)

    def pop(self):
        if len(self.__elements) > 0:
            return self.__elements.pop()
        else:
            return None

    def on_top(self):
        if len(self.__elements) > 0:
            return self.__elements[-1]
        else:
            return None

    def size(self):
        return len(self.__elements)
    
class Graph:
    def __init__(self, dirigido=True):
        self.elements = []
        self.dirigido = dirigido

    def show_graph(self):
        print()
        print("nodos")
        for index, nodo in enumerate(self.elements):
            print(nodo['value'])
            print(f"    aristas")
            for second_index, second_element in enumerate(nodo['aristas']):
                print(f"    destino {second_element['value']} peso: {second_element['peso']}")

        print()

    def search(self, value):
        for index, element in enumerate(self.elements):
            if element['value'] == value:
                return index

    def search_arista(self, vertice_value, value):
        pos_origen = self.search(vertice_value)
        if pos_origen is not None:
            for index, element in enumerate(self.elements[pos_origen]['aristas']):
                if element['value'] == value:
                    return pos_origen, index

    def insert_vertice(self, value, other_value=None):
        nodo = {
        'value': value,
        'aristas': [],
        'visitado': False,
        }
        self.elements.append(nodo)

    def insert_arista(self, origen, destino, peso):
        pos_origen = self.search(origen)
        pos_destino = self.search(destino)
        if pos_origen is not None and pos_destino is not None:
            # print(origen, destino)
            arista = {
                'value': destino,
                'peso': peso
            }
            self.elements[pos_origen]['aristas'].append(arista)
            if not self.dirigido:
                arista = {
                    'value': origen,
                    'peso': peso
                }
                self.elements[pos_destino]['aristas'].append(arista)

    
    def delete_arista(self, origen, destino):
        result = self.search_arista(origen, destino)
        if result:
            pos_vertice, pos_arista = result
            value = self.elements[pos_vertice]['aristas'].pop(pos_arista)
            if not self.dirigido:
                result = self.search_arista(destino, origen)
                if result:
                    pos_vertice, pos_arista = result
                    self.elements[pos_vertice]['aristas'].pop(pos_arista)
            return value
    
    def delete_vertice(self, value):
        pos_vertice = self.search(value)
        if pos_vertice is not None:
            delete_value = self.elements.pop(pos_vertice)
            for nodo in self.elements:
                self.delete_arista(nodo['value'], value)
            return delete_value
    
    def mark_as_not_visited(self):
        for nodo in self.elements:
            nodo['visitado'] = False

    def deep_show(self, origin):
        def __deep_show(graph, origin):
            pos_vertice = graph.search(origin)
            if pos_vertice is not None:
                if not graph.elements[pos_vertice]['visitado']:
                    graph.elements[pos_vertice]['visitado'] = True
                    print(graph.elements[pos_vertice]['value'])
                    adyacentes = graph.elements[pos_vertice]['aristas']
                    for adyacente in adyacentes:
                        __deep_show(graph, adyacente['value'])
        
        self.mark_as_not_visited()
        __deep_show(self, origin)

    def amplitude_show(self, origin):
        self.mark_as_not_visited()
        cola = Queue()
        pos_vertice = self.search(origin)
        if pos_vertice is not None:
            if not self.elements[pos_vertice]['visitado']:
                cola.arrive(self.elements[pos_vertice])
                while cola.size() > 0:
                    nodo = cola.attention()
                    nodo['visitado'] = True
                    print(nodo['value'])
                    adyacentes = nodo['aristas']
                    for adyacente in adyacentes:
                        pos_adyaecnte = self.search(adyacente['value'])
                        if not self.elements[pos_adyaecnte]['visitado']:
                            cola.arrive(self.elements[pos_adyaecnte])
    
    def exist_path(self, origen, destino):
        def __exist_path(graph, origin, destino):
            result = False
            pos_vertice = graph.search(origin)
            if pos_vertice is not None:
                if not graph.elements[pos_vertice]['visitado']:
                    graph.elements[pos_vertice]['visitado'] = True
                    if graph.elements[pos_vertice]['value'] == destino:
                        return True
                    else:
                        adyacentes = graph.elements[pos_vertice]['aristas']
                        for adyacente in adyacentes:
                            result = __exist_path(graph, adyacente['value'], destino)
                            if result:
                                break
            return result
        
        self.mark_as_not_visited()
        result = __exist_path(self, origen, destino)
        return result

    def dijkstra(self, origen):
        from math import inf
        no_visitados = HeapMin()
        camino = Stack()
        for nodo in self.elements:
            distancia = 0 if nodo['value'] == origen else inf
            no_visitados.arrive([nodo['value'], nodo, None], distancia)
        while len(no_visitados.elements) > 0:
            node = no_visitados.atention()
            costo_nodo_actual = node[0]
            camino.push(node)
            adjacentes = node[1][1]['aristas']
            # print(costo_nodo_actual, adjacentes)
            for adjacente in adjacentes:
                pos = no_visitados.search(adjacente['value'])
                if pos is not None:
                    if costo_nodo_actual + adjacente['peso'] < no_visitados.elements[pos][0]:
                        no_visitados.elements[pos][1][2] = node[1][0]
                        no_visitados.change_proirity(pos, costo_nodo_actual + adjacente['peso'])
        return camino

    def kruskal(self, origen):
        def buscar_en_bosque(bosque, buscado):
            for index, arbol in enumerate(bosque):
                # print(buscado, arbol)
                if buscado in arbol:
                    return index

        bosque = []
        aristas = HeapMin()
        for nodo in self.elements:
            bosque.append(nodo['value'])
            adjacentes = nodo['aristas']
            for adjacente in adjacentes:
                aristas.arrive([nodo['value'], adjacente['value']], adjacente['peso'])

        # print(aristas.elements)
        while len(bosque) > 1 and len(aristas.elements) > 0:
            arista = aristas.atention()
            # print(bosque)
            # print(arista[1][0], arista[1][1])
            # print(arista)
            origen = buscar_en_bosque(bosque, arista[1][0])
            destino = buscar_en_bosque(bosque, arista[1][1])
            # print(origen, destino)
            if origen is not None and destino is not None:
                if origen != destino:
                    if origen > destino:
                        vertice_ori = bosque.pop(origen)
                        vertice_des = bosque.pop(destino)
                    else:
                        vertice_des = bosque.pop(destino)
                        vertice_ori = bosque.pop(origen)

                    if '-' not in vertice_ori and '-' not in vertice_des:
                        bosque.append(f'{vertice_ori}-{vertice_des}-{arista[0]}')
                    elif '-' not in vertice_des:
                        bosque.append(vertice_ori+';'+f'{arista[1][0]}-{vertice_des}-{arista[0]}')
                    elif '-' not in vertice_ori:
                        bosque.append(vertice_des+';'+f'{vertice_ori}-{arista[1][1]}-{arista[0]}')
                    else:
                        bosque.append(vertice_ori+';'+vertice_des+';'+f'{arista[1][0]}-{arista[1][1]}-{arista[0]}')
        return bosque
    
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