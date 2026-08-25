# impar_1 = 3
# impar_2 = 5
# impar_3= 13
# impar_4 = 27

# impares = []
# print(type(impares))
# impares = [3,5,13,27]
# print(impares[3])

# lista_01 =[ 12,"pedro",12.53343,"[{_{^^{}}}", False, 0,[2,4,6,8]
#  ]                                                   


#print(lista_01[1],lista_01[2],lista_01[4],lista_01[6][2])

# condicionais  :

# lista_02 = ["Márcia"]
#if "Márcia" in lista_02 :
#else :
    # print("Márcia não está presente  na Lista.")

#Loopings :

# participantes = ["Isaque","Luana","Fernando","Bianca","Ana Paula"]

# #for participantes in participantes:
#    # print(participantes)

# partic_2 = "Hugo"
# participantes.append(partic_2)
# participantes.insert(2,partic_2)
# participantes.pop(1)
# participantes.remove("Hugo")
# participantes.reverse ()
# #participantes.count("Hugo")

# #participantes.count("Hugo")
# #
# participantes.clear()



# print(participantes)

# Tuplas:

# participantes = ["Isaque","Luana","Fernando","Bianca","Ana Paula"]
# print(participantes)
# print(participantes,type(participantes))
# participantes_02 = ("Fernando","111.111","******","Avenida Dr. Tibúrcio, 444", "DDD2199999999999")           
# print(participante02.index("Avenida Dr. Tibúrcio, 444"))
# Listinha_partic_02=List(participante_02)
#print(Listinha_particip_02)

#Sets
numeros_pares = {
    202,
    203,
    204,
    205,
    219,
    291,
    292,
    202
}

#print(numeros_pares,type(numeros_pares))
numeros_impares = {111,111,112,291,291,205}
print(numeros_pares.intersection(numeros_impares))
numeros_pares.remove(205)
print(numeros_pares)

#Dicionários

produtos = {"maçã": 5.99,"laranja":4.79}
#print(produtos,(type(produtos)))
print(produtos.items())
print(produtos.keys())
print(produtos.values())
print(produtos.get("laranja"))
produtos2 = produtos.copy()
print(produtos2)
#produtos2.pop("maçã")
produtos2["maçã"]=7.99
#produtos.update()
print(produtos2)
###
achadinhos = {}
print(type(achadinhos))
achadinhos["capinha celular"]=12.99
print(achadinhos)



