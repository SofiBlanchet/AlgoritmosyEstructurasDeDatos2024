# 22
mochila=["Objeto 1","Objeto 2","Objeto 3","Sable de luz","Objeto 5","Objeto 6","Objeto 7"]
objetosquitados=[]
print (f"Los objetos de la mochila son {mochila}")

def usarlafuerza(mochila,objetosquitados):
    if len(mochila)==0:  
        return "La lista de objetos sacados es" ,objetosquitados
    else:
        objetosquitados.append(mochila.pop())
        print("El objeto es sacado es: ", objetosquitados[-1])
        if objetosquitados[-1]=="Sable de luz":
            return f"Se sacaron {len(objetosquitados)} objetos hasta encontrar el sable de luz"
    return usarlafuerza(mochila,objetosquitados)
    
print(usarlafuerza(mochila,objetosquitados))
