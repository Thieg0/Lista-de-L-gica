def evaluate_expression(expression, truth_values):
    stack = []
    for token in expression:
        if token in (True, False):
            stack.append(token)
        elif token == 'not':
            stack[-1] = not stack[-1]
        elif token == 'and':
            if len(stack) < 2:
                return False  # Não há operandos suficientes para a operação 'and'
            stack[-2:] = [stack[-2] and stack[-1]]
        elif token == 'or':
            if len(stack) < 2:
                return False  # Não há operandos suficientes para a operação 'or'
            stack[-2:] = [stack[-2] or stack[-1]]
    return stack[0]

def classify_sentence(sentence, truth_values):
    result = evaluate_expression(sentence, truth_values)
    if result is True:
        return "Tautologia"
    elif result is False:
        return "Contradição"
    else:
        return "Satisfatível"

def main():
    expression = input("Digite a sentença na linguagem da lógica proposicional: ")
    variables = set(token for token in expression if token.isalpha())
    truth_values = {}
    for i in range(2 ** len(variables)):
        truth_values.update({var: bool((i >> j) & 1) for j, var in enumerate(sorted(variables, reverse=True))})
        classification = classify_sentence(expression, truth_values)
        print(''.join(str(int(truth_values[var])) for var in sorted(variables, reverse=True)))
        print(int(classification == 'Tautologia'), int(classification == 'Contradição'), int(classification == 'Satisfatível'))

if __name__ == "__main__":
    main()
