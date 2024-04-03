def parse_input(expression):
    # Remove espaços em branco extras e converte para minúsculas
    expression = expression.strip().lower()
    # Separa a expressão em uma lista de tokens
    tokens = expression.split()
    return tokens

def evaluate(expression):
    stack = []
    for token in expression:
        if token == 'and':
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(operand1 and operand2)
        elif token == 'or':
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(operand1 or operand2)
        elif token == 'not':
            operand = stack.pop()
            stack.append(not operand)
        else:
            stack.append(token)
    # O resultado final é o único item restante na pilha
    return stack[0]

def equivalent(sent1, sent2):
    tokens1 = parse_input(sent1)
    tokens2 = parse_input(sent2)
    # Verifica se ambas as sentenças avaliam para o mesmo valor
    return evaluate(tokens1) == evaluate(tokens2)

def main():
    sent1 = input("Digite a primeira sentença lógica (use 'and', 'or' e 'not' como operadores): ")
    sent2 = input("Digite a segunda sentença lógica (use 'and', 'or' e 'not' como operadores): ")
    
    if equivalent(sent1, sent2):
        print("As sentenças são equivalentes.")
    else:
        print("As sentenças não são equivalentes.")

if __name__ == "__main__":
    main()
