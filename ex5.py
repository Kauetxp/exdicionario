#Escreva uma função que receba um dicionário como entrada e retorna uma nova lista contendo apenas as chaves

def listaChave():
    dic = {"Kaue":"Portal","Camila":"Guitar Hero","José":"Friv"}
    
    chaves = []
    
    for i in dic.keys():
        chaves.append(i)
        
    print("Chaves do dicionario: ",chaves)
listaChave()
