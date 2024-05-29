from random import sample
aluno_1 = (input('digite o primeiro nome: '))
aluno_2 = (input('digite o segundo nome: '))
aluno_3 = (input('digite o terceiro nome: '))
aluno_4 = (input('digite o quarto nome: '))
lista = [aluno_1, aluno_2, aluno_3, aluno_4]
lista = sample(lista, k=len(lista))
print ('a ordem sorteada foi:\n {}'. format(lista))