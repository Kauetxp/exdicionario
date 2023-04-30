#Escreva uma função que receba um dicionário como entrada e retorna duas listas. 
#Uma com chave e outra com valor.

def separando():
    dic = {"Kaue":"Portal","Camila":"Guitar Hero","José":"Friv"}
    print(dic)
    
    #separando em listas
    nome = []
    jogo = []
    #jogo
    for i in dic:
        jogo.append((dic[i]))
    print("Lista de jogos: ",jogo)
    #nome
    for j in dic.keys():
        nome.append(j)
    print("Lista de nomes: ",nome)
    
separando()
