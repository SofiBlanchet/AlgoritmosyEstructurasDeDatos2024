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
    
    def __str__(self):
        return (f"{self.__elements}")
    
# 2. Dada una pila con los datos de dinosaurios resolver lo siguiente actividades:
# a) Contar cuantas especies hay;
# b) Determinar cuantos descubridores distintos hay;
# c) Mostrar todos los dinosaurios que empiecen con T;
# d) Mostrar todos los dinosaurio que pesen menos de 275 Kg
# e) Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S;

dinosaurios = [
    {
      "nombre": "Tyrannosaurus Rex",
      "especie": "Theropoda",
      "peso": "7000 kg",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1902
    },
    {
      "nombre": "Triceratops",
      "especie": "Ceratopsidae",
      "peso": "6000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1889
    },
    {
      "nombre": "Velociraptor",
      "especie": "Dromaeosauridae",
      "peso": "15 kg",
      "descubridor": "Henry Fairfield Osborn",
      "ano_descubrimiento": 1924
    },
    {
      "nombre": "Brachiosaurus",
      "especie": "Sauropoda",
      "peso": "56000 kg",
      "descubridor": "Elmer S. Riggs",
      "ano_descubrimiento": 1903
    },
    {
      "nombre": "Stegosaurus",
      "especie": "Stegosauridae",
      "peso": "5000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Spinosaurus",
      "especie": "Spinosauridae",
      "peso": "10000 kg",
      "descubridor": "Ernst Stromer",
      "ano_descubrimiento": 1912
    },
    {
      "nombre": "Allosaurus",
      "especie": "Theropoda",
      "peso": "2000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Apatosaurus",
      "especie": "Sauropoda",
      "peso": "23000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Diplodocus",
      "especie": "Sauropoda",
      "peso": "15000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1878
    },
    {
      "nombre": "Ankylosaurus",
      "especie": "Ankylosauridae",
      "peso": "6000 kg",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1908
    },
    {
      "nombre": "Parasaurolophus",
      "especie": "Hadrosauridae",
      "peso": "2500 kg",
      "descubridor": "William Parks",
      "ano_descubrimiento": 1922
    },
    {
      "nombre": "Carnotaurus",
      "especie": "Theropoda",
      "peso": "1500 kg",
      "descubridor": "José Bonaparte",
      "ano_descubrimiento": 1985
    },
    {
      "nombre": "Styracosaurus",
      "especie": "Ceratopsidae",
      "peso": "2700 kg",
      "descubridor": "Lawrence Lambe",
      "ano_descubrimiento": 1913
    },
    {
      "nombre": "Therizinosaurus",
      "especie": "Therizinosauridae",
      "peso": "5000 kg",
      "descubridor": "Evgeny Maleev",
      "ano_descubrimiento": 1954
    },
    {
      "nombre": "Pteranodon",
      "especie": "Pterosauria",
      "peso": "25 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1876
    },
    {
      "nombre": "Quetzalcoatlus",
      "especie": "Pterosauria",
      "peso": "200 kg",
      "descubridor": "Douglas A. Lawson",
      "ano_descubrimiento": 1971
    },
    {
      "nombre": "Plesiosaurus",
      "especie": "Plesiosauria",
      "peso": "450 kg",
      "descubridor": "Mary Anning",
      "ano_descubrimiento": 1824
    },
    {
      "nombre": "Mosasaurus",
      "especie": "Mosasauridae",
      "peso": "15000 kg",
      "descubridor": "William Conybeare",
      "ano_descubrimiento": 1829
    },

  ]


piladinos= Stack()
pilaux=Stack()

for dinosaurio in dinosaurios:
    piladinos.push(dinosaurio)

#recargar pila
def recargar(Pila1,Pila2):
    while Pila2.size()>0:
      Pila1.push(Pila2.pop())
    return Pila1

print ("-----------PUNTO A-----------")

especies = set()
while piladinos.size() > 0:
    top_element = piladinos.pop()
    especies.add(top_element['especie'])
    pilaux.push(top_element)
print(f"Número de especies: {len(especies)}")

recargar(piladinos,pilaux)

print ("-----------PUNTO B-----------")
descubridor = set()
while piladinos.size()>0:
    descubridor.add(piladinos.on_top()['descubridor'])
    pilaux.push(piladinos.pop())
print(f"Número de especies: {len(descubridor)} y son: {descubridor}")

recargar(piladinos,pilaux)


print ("-----------PUNTO C-----------")
losdete=[]
while piladinos.size()>0:
    if piladinos.on_top()['nombre'][0] in {"T"}:
      losdete.append(piladinos.on_top()['nombre'])
    pilaux.push(piladinos.pop())
print ("Los que empiezan por T son: ")
for dinosaurio in losdete:
  print (dinosaurio)

recargar(piladinos,pilaux)

print ("-----------PUNTO D-----------")
losflacos=[]
while piladinos.size()>0:
    if int(piladinos.on_top()['peso'][:-3]) < 275:
        losflacos.append(piladinos.on_top())
    pilaux.push(piladinos.pop())
print ("Los que son flacos son: ")
for dinosaurio in losflacos:
  print (dinosaurio)

recargar(piladinos,pilaux)

print ("-----------PUNTO E-----------")
pilaletras= Stack()
while piladinos.size()>0:
    if piladinos.on_top()['nombre'][0] in {"A","Q","S"}:
      pilaletras.push(piladinos.pop())
    else:
        pilaux.push(piladinos.pop())

print("Los dinosaurios que empiezan por A,Q o S son:")
print(pilaletras)
print ("----------------------")
print ("----------------------")
print("Los que quedaron en la otra pila son: ")
print(pilaux)