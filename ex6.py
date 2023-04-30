#Escreva uma função que receba um dicionário como entrada e retorna uma nova lista com as chaves ordenadas em ordem alfabética.

def ordenaChave():
    
    dic = {"Kaue":"Portal","Camila":"Guitar Hero","José":"Friv"}
    
    #Separando
    chaves = []
    for i in dic.keys():
        chaves.append(i)
    chaves.sort()
    print(chaves)
    
ordenaChave()
        