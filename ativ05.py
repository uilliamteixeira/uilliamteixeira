# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# ○ A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# ○ A mensagem "Reprovado", se a média for menor do que sete;
# ○ A mensagem "Aprovado com Distinção", se a média for igual a dez.

for i in range(3):
    nota1 = float(input('Digite uma nota: '))
    nota2 = float(input('Digite uma nota: '))
    media = (nota1 + nota2)/2
    if media == 10:
        print(f'Média {media} Aprovado com distinção! ') 
    elif media < 7:
        print(f'Média {media} Reprovado ')    
    elif media >= 7:
        print(f'Média {media} Aprovado! ')
       