#Escreva uma função que receba itens (números) em um dicionário como entrada e retorne a chave com o maior valor.

dicionario = {}

def recebe():
    
    while True:

        chave = input("Digite uma palavra: ")
        item = int(input("Atribua um número a ele: "))
        dicionario[chave]=item
        c = input("Deseja adicionar mais itens? (sim/nao)")
        if c == 'nao':
            break
    n = sorted(dicionario.values())
    n = n[-1]
    print(n)

recebe()
