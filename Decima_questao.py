def traduzir_sentenca(sentenca):
    # Substitua "e" pelo conectivo lógico "and"
    sentenca = sentenca.replace(' e ', ' and ')
    # Substitua "ou" pelo conectivo lógico "or"
    sentenca = sentenca.replace(' ou ', ' or ')
    # Substitua "então" pelo conectivo lógico "->"
    sentenca = sentenca.replace('então', '->')
    # Substitua "não" pelo conectivo lógico "~"
    sentenca = sentenca.replace(' não ', '~')
    # Remova o "se"
    sentenca = sentenca.replace('se', '')
    # Remova as vírgulas
    sentenca = sentenca.replace(',', '')
    
    # Separe a sentença em duas partes, uma à esquerda e outra à direita de qualquer um dos conectivos
    partes = None
    for conectivo in [" and ", " or ", "->"]:
        if conectivo in sentenca:
            partes = sentenca.split(conectivo)
            break
    
    # Atribua "P" à sentença à esquerda e "Q" à sentença à direita
    if partes:
        P = partes[0].strip()
        Q = partes[1].strip()
        
        # Junta P e Q com o conectivo
        conectivo = conectivo.strip()
        sentenca_traduzida = f"P {conectivo} Q"
        
        # Exibir P e Q
        print("P:", P)
        print("Q:", Q)
    else:
        sentenca_traduzida = sentenca.strip()
    
    return sentenca_traduzida

# Solicitar a sentença do usuário
sentenca_usuario = input("Digite a sentença em linguagem natural: ")

# Traduzir a sentença
sentenca_traduzida = traduzir_sentenca(sentenca_usuario)

# Exibir a sentença original e a traduzida
print("Sentença em linguagem natural:", sentenca_usuario)
print("Sentença em lógica proposicional:", sentenca_traduzida)
