
from Clases import Graph
"""14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las si-
guientes tareas:

a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;

b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
ta es la distancia entre los ambientes, se debe cargar en metros;

c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
para conectar todos los ambientes;

d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
determinar cuántos metros de cable de red se necesitan para conectar el router con el
Smart Tv."""

grafo=Graph(False)
ambientes = ["Cocina", "Comedor", "Cochera", "Quincho", "Baño 1", "Baño 2", "Habitación 1", "Habitación 2", "Sala de estar", "Terraza", "Patio"]

aristas = [
    ("Cocina", "Comedor", 5), ("Cocina", "Baño 1", 3), ("Cocina", "Habitación 1", 7),
    ("Comedor", "Sala de estar", 8), ("Comedor", "Terraza", 5), ("Comedor", "Cochera", 8),
    ("Cochera", "Patio", 1), ("Cochera", "Quincho", 12), ("Cochera", "Habitación 1", 9),
    ("Quincho", "Patio", 7), ("Quincho", "Terraza", 11),
    ("Baño 1", "Baño 2", 2), ("Baño 1", "Habitación 2", 5),
    ("Baño 2", "Habitación 1", 6), ("Baño 2", "Habitación 2", 3),
    ("Habitación 1", "Habitación 2", 4), ("Habitación 1", "Sala de estar", 8),
    ("Sala de estar", "Terraza", 9), ("Terraza", "Patio", 4),
]

for ambiente in ambientes:
    grafo.insert_vertice(ambiente)

for origen , destino , peso in aristas:
    grafo.insert_arista(origen , destino , peso)

bosque_minimo = grafo.kruskal("Cocina")
total_cable =(sum([int(arista.split('-')[-1]) for arbol in bosque_minimo for arista in arbol.split(';') if '-' in arista]))
print("Árbol de expansión mínima (Kruskal):", bosque_minimo)
print(f"Longitud total de cables necesaria para conectar todos los ambientes: {total_cable} metros")


camino_minimo = grafo.dijkstra("Habitación 1")
camino = []
distancia_total = None
while camino_minimo.size() > 0:
    paso = camino_minimo.pop()
    camino.append(paso)
camino_final = []
for paso in camino:
    if paso[1][0] == "Sala de estar":
        distancia_total = paso[0]
        while paso:
            camino_final.insert(0, paso[1][0])  
            paso = next((p for p in camino if p[1][0] == paso[1][2]), None)
        break
camino_final_nombres = [paso[1][0] for paso in camino_final]
print("Camino más corto de 'Habitación 1' a 'Sala de estar':", " -> ".join(camino_final_nombres))
print(f"Longitud del cable de red necesario para conectar el router con el Smart TV: {distancia_total} metros")


"""15.Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas moder-
nas y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:

a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
uno en las naturales) y tipo (natural o arquitectónica);
b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
la distancia que las separa;
c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
e. determinar si algún país tiene más de una maravilla del mismo tipo;
f. deberá utilizar un grafo no dirigido."""

from Clases import Graph
maravillas = [
    {"nombre": "Gran Muralla China", "pais": ["China"], "tipo": "arquitectonica"},
    {"nombre": "Petra", "pais": ["Jordania"], "tipo": "arquitectonica"},
    {"nombre": "Cristo Redentor", "pais": ["Brasil"], "tipo": "arquitectonica"},
    {"nombre": "Machu Picchu", "pais": ["Perú"], "tipo": "arquitectonica"},
    {"nombre": "Chichen Itza", "pais": ["México"], "tipo": "arquitectonica"},
    {"nombre": "Coliseo Romano", "pais": ["Italia"], "tipo": "arquitectonica"},
    {"nombre": "Taj Mahal", "pais": ["India"], "tipo": "arquitectonica"},
    {"nombre": "Amazonas", "pais": ["Brasil", "Perú", "Colombia", "Venezuela"], "tipo": "natural"},
    {"nombre": "Bahía de Ha Long", "pais": ["Vietnam"], "tipo": "natural"},
    {"nombre": "Cataratas del Iguazú", "pais": ["Argentina", "Brasil"], "tipo": "natural"},
    {"nombre": "Isla Jeju", "pais": ["Corea del Sur"], "tipo": "natural"},
    {"nombre": "Komodo", "pais": ["Indonesia"], "tipo": "natural"},
    {"nombre": "Río subterráneo de Puerto Princesa", "pais": ["Filipinas"], "tipo": "natural"},
    {"nombre": "Montaña de la Mesa", "pais": ["Sudáfrica"], "tipo": "natural"}
]
distancias_arquitectonicas = {
    ("Gran Muralla China", "Petra"): 6000,
    ("Gran Muralla China", "Cristo Redentor"): 17500,
    ("Gran Muralla China", "Machu Picchu"): 17100,
    ("Gran Muralla China", "Chichen Itza"): 12500,
    ("Gran Muralla China", "Coliseo Romano"): 8100,
    ("Gran Muralla China", "Taj Mahal"): 4200,
    ("Petra", "Cristo Redentor"): 12000,
    ("Petra", "Machu Picchu"): 11700,
    ("Petra", "Chichen Itza"): 12000,
    ("Petra", "Coliseo Romano"): 2300,
    ("Petra", "Taj Mahal"): 4000,
    ("Cristo Redentor", "Machu Picchu"): 3300,
    ("Cristo Redentor", "Chichen Itza"): 6600,
    ("Cristo Redentor", "Coliseo Romano"): 9500,
    ("Cristo Redentor", "Taj Mahal"): 14500,
    ("Machu Picchu", "Chichen Itza"): 4100,
    ("Machu Picchu", "Coliseo Romano"): 10500,
    ("Machu Picchu", "Taj Mahal"): 17000,
    ("Chichen Itza", "Coliseo Romano"): 9600,
    ("Chichen Itza", "Taj Mahal"): 14800,
    ("Coliseo Romano", "Taj Mahal"): 5700
}
distancias_naturales = {
    ("Amazonas", "Bahía de Ha Long"): 19000,
    ("Amazonas", "Cataratas del Iguazú"): 3000,
    ("Amazonas", "Isla Jeju"): 15500,
    ("Amazonas", "Komodo"): 17700,
    ("Amazonas", "Río subterráneo de Puerto Princesa"): 18300,
    ("Amazonas", "Montaña de la Mesa"): 7800,
    ("Bahía de Ha Long", "Cataratas del Iguazú"): 17600,
    ("Bahía de Ha Long", "Isla Jeju"): 3000,
    ("Bahía de Ha Long", "Komodo"): 4600,
    ("Bahía de Ha Long", "Río subterráneo de Puerto Princesa"): 1600,
    ("Bahía de Ha Long", "Montaña de la Mesa"): 12000,
    ("Cataratas del Iguazú", "Isla Jeju"): 18200,
    ("Cataratas del Iguazú", "Komodo"): 17500,
    ("Cataratas del Iguazú", "Río subterráneo de Puerto Princesa"): 19300,
    ("Cataratas del Iguazú", "Montaña de la Mesa"): 7800,
    ("Isla Jeju", "Komodo"): 4100,
    ("Isla Jeju", "Río subterráneo de Puerto Princesa"): 1800,
    ("Isla Jeju", "Montaña de la Mesa"): 13300,
    ("Komodo", "Río subterráneo de Puerto Princesa"): 2300,
    ("Komodo", "Montaña de la Mesa"): 12000,
    ("Río subterráneo de Puerto Princesa", "Montaña de la Mesa"): 12900
}
grafo = Graph(dirigido=False)
for maravilla in maravillas:
    grafo.insert_vertice(maravilla["nombre"])
for (origen, destino), distancia in distancias_arquitectonicas.items():
    grafo.insert_arista(origen, destino, distancia)
for (origen, destino), distancia in distancias_naturales.items():
    grafo.insert_arista(origen, destino, distancia)  
bosque_minimo_arquitectonicas = grafo.kruskal("Gran Muralla China")
bosque_minimo_naturales = grafo.kruskal("Amazonas")
total_cable_arquitectonicas = sum(
    int(arista.split('-')[-1]) for arbol in bosque_minimo_arquitectonicas for arista in arbol.split(';') if '-' in arista
)  
total_cable_naturales = sum(
    int(arista.split('-')[-1]) for arbol in bosque_minimo_naturales for arista in arbol.split(';') if '-' in arista
)
print("Árbol de expansión mínima (Arquitectónicas):", bosque_minimo_arquitectonicas)
print(f"Longitud total de cables para maravillas arquitectónicas: {total_cable_arquitectonicas} km")
print("Árbol de expansión mínima (Naturales):", bosque_minimo_naturales)
print(f"Longitud total de cables para maravillas naturales: {total_cable_naturales} km")
paises_tipos = {}
for maravilla in maravillas:
    for pais in maravilla["pais"]:
        if pais not in paises_tipos:
            paises_tipos[pais] = set()
        paises_tipos[pais].add(maravilla["tipo"])
paises_con_ambos_tipos = [pais for pais, tipos in paises_tipos.items() if len(tipos) > 1]
print("Países con maravillas arquitectónicas y naturales:", paises_con_ambos_tipos)
paises_maravillas = {}
for maravilla in maravillas:
    for pais in maravilla["pais"]:
        if pais not in paises_maravillas:
            paises_maravillas[pais] = {"arquitectonica": 0, "natural": 0}
        paises_maravillas[pais][maravilla["tipo"]] += 1
paises_con_multiples_maravillas_mismo_tipo = {
    pais: tipo for pais, tipo_cantidad in paises_maravillas.items() for tipo, cantidad in tipo_cantidad.items() if cantidad > 1
}
print("Países con múltiples maravillas del mismo tipo:", paises_con_multiples_maravillas_mismo_tipo)