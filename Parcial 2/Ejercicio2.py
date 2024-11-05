"""2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las siguientes tareas: 
a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan; 
b) hallar el árbol de expansión minino y determinar si contiene a Yoda; 
c) determinar cuál es el número máximo de episodio que comparten dos personajes, y quienes son. 
d) cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8.
"""
from Clases import Graph
star_wars_characters = [
    "Luke Skywalker",
    "Darth Vader",
    "Yoda",
    "Boba Fett",
    "C-3PO",
    "Leia",
    "Rey",
    "Kylo Ren",
    "Chewbacca",
    "Han Solo",
    "R2-D2",
    "BB-8"]
star_wars_graph=Graph(False)
print("-------PUNTO A-------")
for character in star_wars_characters:
    star_wars_graph.insert_vertice(character)

relationships = [
    ("Luke Skywalker", "Leia", 3),
    ("Luke Skywalker", "Darth Vader", 5),
    ("Leia", "Han Solo", 4),
    ("Rey", "Kylo Ren", 2),
    ("C-3PO", "R2-D2", 4),
    ("Yoda", "Luke Skywalker", 2),
    ("Darth Vader", "Boba Fett", 1),
    ("Chewbacca", "Han Solo", 4),
    ("BB-8", "Rey", 2),
]

for origen, destino, peso in relationships:
    star_wars_graph.insert_arista(origen, destino, peso)

print("-------PUNTO B-------")
print("Árbol de Expansión Mínimo:")
tree_min = star_wars_graph.kruskal("Yoda")
StayYoda=False
print(tree_min)
for tree in tree_min:
    if "Yoda" in tree:
        EstaYoda=True
        break
if StayYoda==False:
    print("Yoda no está en el tree min")
else:
    print("Yoda está en el tree min")
print("-------PUNTO C-------")
tree_max = 0
characters= None

for nodo in star_wars_graph.elements:
    for arista in nodo["aristas"]:
        if arista["peso"] > tree_max:
            tree_max = arista["peso"]
            characters = (nodo["value"], arista["value"])  
print(f"Los personajes que más episodios comparten son {characters[0]} y {characters[1]} con {tree_max} episodios.")


