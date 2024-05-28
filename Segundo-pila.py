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
    
class Personaje:
    def __init__(self,nombre,cant_peli=None):
        self.nombre=nombre
        self.cant_peli=cant_peli
    
    def __str__(self):
        return f"{str(self.nombre)} {int(self.cant_peli)}"

"""Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire
strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que
permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en ambos episodios."""
print ("EJERCICIO 1")
print ("----------------------------")

PilaV=Stack()
PilaVII=Stack()

#Lista de personajes del episodio V de “The empire strikes back”
Lista=[
    Personaje("Luke Skywalker",),
    Personaje("Han Solo"),
    Personaje("Leia Organa"),
    Personaje("Darth Vader"),
    Personaje("Yoda")]

#Lista de personajes del episodio VII “The force awakens”
Lista2 = [
    Personaje("Rey"),
    Personaje("Finn (FN-2187)"),
    Personaje("Kylo Ren (Ben Solo)"),
    Personaje("Han Solo"),
    Personaje("Leia Organa"),
    Personaje("Luke Skywalker")]

#Carga los personajes del episodio V de “The empire strikes back” en la pila
for personaje in Lista:
    PilaV.push(personaje)

#Carga los personajes del episodio VII “The force awakens” en la pila
for personaje in Lista2:
    PilaVII.push(personaje)

#Interseccion de personajes en ambas películas
def interseccion(PilaV,PilaVII):
    pilaux=Stack()
    for i in range(PilaV.size()):
        for j in range (PilaVII.size()):
            if PilaV.on_top().nombre==PilaVII.on_top().nombre:
                print (PilaVII.on_top().nombre)
            pilaux.push(PilaVII.pop())
        PilaV.pop()
        while pilaux.size()>0:
            PilaVII.push(pilaux.pop())

print("La intersección de personajes es:")
(interseccion(PilaV,PilaVII))
print ("----------------------------")
"""Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
necesarias para resolver las siguientes actividades:
a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar 
la cantidad de películas en la que aparece;
c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
d. mostrar todos los personajes cuyos nombre empiezan con C, D y G."""
print ("EJERCICIO 2")
print ("----------------------------")

PilaPersonajes=Stack()
Pilaux=Stack()

#Lista de personajes de MCU
Lista=[ 
    Personaje("Iron Man", 10),
    Personaje("Thor", 9),
    Personaje("Captain America", 11),
    Personaje("Black Widow", 8),
    Personaje("Hulk", 7),
    Personaje("Hawkeye", 6),
    Personaje("Doctor Strange", 5),
    Personaje("Spider-Man", 6),
    Personaje("Rocket Raccoon", 4),
    Personaje("Ant-Man", 4),
    Personaje("Star-Lord", 4),
    Personaje("Gamora", 4),
    Personaje("Groot", 4),
    Personaje("Drax", 4),
    Personaje("Scarlet Witch", 5),
    Personaje("Vision", 4),
    Personaje("Falcon", 6),
    Personaje("Winter Soldier", 6),
    Personaje("Black Panther", 4),
    Personaje("War Machine", 7),
    Personaje("Loki", 6),
    Personaje("Nick Fury", 11),
    Personaje("Wasp", 3),
    Personaje("Nebula", 5),
    Personaje("Mantis", 3),
    Personaje("Okoye", 3),
    Personaje("Shuri", 3),
    Personaje("Valkyrie", 3),
    Personaje("Captain Marvel", 3),
    Personaje("Happy Hogan", 5)]
#Carga de pila
for personaje in Lista:
    PilaPersonajes.push(personaje)

#Define en que posición están Rocket Raccoon y Groot
def posicion(Pila1,Pila2):
    c=0
    while Pila1.size()>0:
        c+=1 
        per=Pila1.on_top().nombre
        if per==("Rocket Raccoon"):
            print ("Raccoon esta en la posicion",c)
        if per==("Groot"):
            print ("Groot esta en la posicion",c)
        Pila2.push(Pila1.pop())
 
#Recarga la pila original  
def recargar(Pila1,Pila2):
    while Pila2.size()>0:
            Pila1.push(Pila2.pop())
    return Pila1
print ("A:")
posicion(PilaPersonajes,Pilaux)
recargar(PilaPersonajes,Pilaux)
print ("----------------------------")

#Muestra los personajes que participaron en 5 o más peliculas y cuantas fueron
def cantidad(Pila1,Pila2):
    MasPersonajes=[]
    while Pila1.size()>0:
        if Pila1.on_top().cant_peli>=5:
            MasPersonajes.append(Pila1.on_top())
        Pila2.push(Pila1.pop())
    print ("Esta es la lista de personajes que participaron en 5 o más películas")
    for personaje in MasPersonajes:
        print ((personaje.nombre),"participó en",(personaje.cant_peli),"películas")
print ("B:")
cantidad(PilaPersonajes,Pilaux)
recargar(PilaPersonajes,Pilaux)
print ("----------------------------")

#Busca a Black Widow y muestra en cuantas películas participó
def buscado(Pila1,Pila2):
    while Pila1.size()>0:
        if Pila1.on_top().nombre==("Black Widow"):
            print ("Black Widow está en la lista y participó en",Pila1.on_top().cant_peli,"peliculas")
        Pila2.push(Pila1.pop())
print ("C:")
buscado(PilaPersonajes,Pilaux)
recargar(PilaPersonajes,Pilaux)
print ("----------------------------")

#Muestra los personajes que su nombre comienza con las letras C, D o G
def letras(Pila1,Pila2):
    Personajes=[]
    while Pila1.size()>0:
        if Pila1.on_top().nombre[0] in {"C","D","G"}:
            Personajes.append(Pila1.on_top())
        Pila2.push(Pila1.pop())
    print ("Los personajes que empiezan con C,D, o G son: ")
    for personaje in Personajes:
        print (personaje.nombre)
print ("D:")
letras(PilaPersonajes,Pilaux)
recargar(PilaPersonajes,Pilaux)
