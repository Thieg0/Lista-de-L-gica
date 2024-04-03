def tabela_verdade(expressao):
    """Gera a tabela-verdade para uma expressão lógica."""
    variaveis = set()
    for char in expressao:
        if char.isalpha():
            variaveis.add(char)
    variaveis = sorted(list(variaveis))
    
    tabela = []
    for i in range(2 ** len(variaveis)):
        linha = {}
        for j, var in enumerate(variaveis):
            linha[var] = (i // (2 ** j)) % 2
        tabela.append(linha)
    
    return tabela

def avaliar(expressao, valores):
    """Avalia uma expressão lógica com os valores de variáveis fornecidos."""
    expressao = expressao.replace("(", " ( ").replace(")", " ) ")
    partes = expressao.split()
    
    pilha = []
    for parte in partes:
        if parte.isalpha():
            pilha.append(valores[parte])
        elif parte in ['and', 'or', 'not']:
            continue
        elif parte == '→':
            b = pilha.pop()
            a = pilha.pop()
            pilha.append(not a or b)
        elif parte == '↔':
            b = pilha.pop()
            a = pilha.pop()
            pilha.append((not a or b) and (not b or a))
        elif parte == '¬':
            a = pilha.pop()
            pilha.append(not a)
        elif parte == '∧':
            b = pilha.pop()
            a = pilha.pop()
            pilha.append(a and b)
        elif parte == '∨':
            b = pilha.pop()
            a = pilha.pop()
            pilha.append(a or b)
    
    return pilha[0]

def sao_equivalentes(sentenca1, sentenca2):
    """Verifica se duas sentenças são logicamente equivalentes."""
    tabela1 = tabela_verdade(sentenca1)
    tabela2 = tabela_verdade(sentenca2)
    
    if len(tabela1) != len(tabela2):
        return False
    
    for valores1, valores2 in zip(tabela1, tabela2):
        resultado1 = avaliar(sentenca1, valores1)
        resultado2 = avaliar(sentenca2, valores2)
        if resultado1 != resultado2:
            return False
    
    return True

# Função para receber entrada do usuário
def obter_sentencas():
    sentenca1 = input("Digite a primeira sentença lógica: ")
    sentenca2 = input("Digite a segunda sentença lógica: ")
    return sentenca1, sentenca2

# Função principal
def main():
    sentenca1, sentenca2 = obter_sentencas()
    resultado = sao_equivalentes(sentenca1, sentenca2)
    print("As sentenças são logicamente equivalentes?" , resultado)

# Execução do programa
if __name__ == "__main__":
    main()
