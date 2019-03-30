from ordenacoes import *
from aluno import Aluno

def menu():
    print('ESCOLHA UMA OPCAO:\n')

    print('1. Gerar Alunos Aleatoriamente')
    print('2. Ordenar com Selectioon Sort')
    print('3. Ordenar com Insertion Sort')
    print('4. Ordenar com Bubble Sort')
    print('5. Ordenar com Shell Sort')
    print('6. Ver Ranking dos Alunos')
    print('7. Comparar Metodos de Ordenacao')
    print('0. Encerrar Programa')
    print('')

if __name__ == '__main__':
    while True:
        menu()
        opcao = int(input('Opcao: '))
        if opcao == 1:
            print('Opcao escolhida: Gerar Alunos Aleatoriamente')
            # Funcao
        elif opcao == 2:
            print('Opcao escolhida: Ordenar com Selectioon Sort')
            # Funcao
        elif opcao == 3:
            print('Opcao escolhida: Ordenar com Insertion Sort')
            # Funcao
        elif opcao == 4:
            print('Opcao escolhida: Ordenar com Bubble Sort')
            # Funcao
        elif opcao == 5:
            print('Opcao escolhida: Ordenar com Shell Sort')
            # Funcao
        elif opcao == 6:
            print('Opcao escolhida: Ver Ranking dos Alunos')
            # Funcao
        elif opcao == 7:
            print('Opcao escolhida: Comparar Metodos de Ordenacao')
            # Funcao
        elif opcao == 0:
            print('Encerrando programa')
            break
        else:
            print('Opcao Invalida')
