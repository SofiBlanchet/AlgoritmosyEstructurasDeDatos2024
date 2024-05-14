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

#5
num="CCLXV"
numd=0
def numeros(num, numd):
    dic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    if len(num)==0:
        return "El número decimal es", numd
    else:
        if len(num)!=1:
            if dic[num[1]]>dic[num[0]]:
                a=dic[num[1]]-dic[num[0]]
                numd+=int(a)
                return numeros(num[2:],numd)
            else:
                numd+=int(dic[num[0]])
                return numeros(num[1:],numd)
        else: 
            numd+=int(dic[num[0]])
            return numeros (num[1:],numd)
    
print(numeros(num,numd))
