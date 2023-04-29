#Escreva uma função que receba um dicionário como entrada e retorna duas listas. 
#Uma com chave e outra com valor.

def separandoDicionario():
    dicionario = {
        "Kaue":"RedDeadRedemption",
        "Camila":"GuitarHero",
        "Alexis":"FIFA23",
        "José":"Friv"
    }
    #Separando o dicionario
    print(dicionario)
    listaNome = []
    listaJogo = []

    for i in dicionario.keys():
        nome = dicionario[i]
        listaNome.append(nome)
    print(listaNome)