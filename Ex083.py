# Crie um programa onde o usuario digite uma expressão qualquer que use parenteses.
# Seu aplicativo deverá analisar se a expressao passada esta com os parenteses abertos e fechados em ordem correta.

expr = str(input('Digite a expressão '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print("Sua expressão está válida.")
else:
    print("Sua expressão está errada.")
