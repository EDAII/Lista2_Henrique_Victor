from funcoes import *
from ordenacoes import *
import time
from aluno import Aluno

def menu():
    print('\n\nESCOLHA UMA OPCAO:\n')

    print('1. Gerar Alunos Aleatoriamente')
    print('2. Cadastrar Aluno Individual')
    print('3. Ordenar com Selectioon Sort')
    print('4. Ordenar com Insertion Sort')
    print('5. Ordenar com Bubble Sort')
    print('6. Ordenar com Shell Sort')
    print('7. Ver Ranking dos Alunos')
    print('8. Comparar Metodos de Ordenacao')
    print('0. Encerrar Programa')
    print('')

if __name__ == '__main__':
    alunos = []
    ordenado = False
    while True:
        menu()
        opcao = int(input('Opcao: '))
        if opcao == 1:
            print('Opcao escolhida: Gerar Alunos Aleatoriamente')
            tamanho = int(input('Digite quantos alunos voce quer criar: '))

            while tamanho < 1:
                tamanho = int(input('Tamanho nao pode ser menor que 1, tente novamente: '))
            
            gerar_alunos_aleatorios(alunos, tamanho)

            print('Alunos gerados.')
            ordenado = False
        elif opcao == 2:
            print('Opcao escolhida: Cadastrar Aluno Individual')
            # Funcao
        elif opcao == 3:
            if len(alunos) > 0:
                print('Opcao escolhida: Ordenar com Selection Sort')
                inicio = time.time()
                selection_sort(alunos)
                fim = time.time()
                tempo_total = fim - inicio
                print('\nTempo decorrido:',round(tempo_total, 6))
                print('A Ordenacao terminou.\n')
                ordenado = True
            else:
                print('Nao ha nenhum aluno cadastrado.')
        elif opcao == 4:
            if len(alunos) > 0:
                print('Opcao escolhida: Ordenar com Insertion Sort')
                inicio = time.time()
                insertion_sort(alunos)
                fim = time.time()
                tempo_total = fim - inicio
                print('\nTempo decorrido:',round(tempo_total, 6))
                print('A Ordenacao terminou.')
                ordenado = True
            else:
                print('Nao ha nenhum aluno cadastrado.')
        elif opcao == 5:
            if len(alunos) > 0:
                print('Opcao escolhida: Ordenar com Bubble Sort')
                inicio = time.time()
                bubble_sort(alunos)
                fim = time.time()
                print('\nTempo decorrido:',round(tempo_total, 6))
                print('A Ordenacao terminou.')
                ordenado = True
            else:
                print('Nao ha nenhum aluno cadastrado.')
        elif opcao == 6:
            if len(alunos) > 0:
                print('Opcao escolhida: Ordenar com Shell Sort')
                inicio = time.time()
                shell_sort(alunos)
                fim = time.time()
                print('\nTempo decorrido:',round(tempo_total, 6))
                print('A Ordenacao terminou.')
                ordenado = True
            else:
                print('Nao ha nenhum aluno cadastrado.')
        elif opcao == 7:
            if ordenado == True:
                print('Opcao escolhida: Ver Ranking dos Alunos')
                print("O ranking possui {} alunos".format(len(alunos)))
                tamanho = int(input('Quantos alunos do ranking voce quer ver? '))

                while tamanho > len(alunos):
                    tamanho = int(input('Tamanho nao pode ser maior que o maximo de alunos, tente novamente: '))

                mostrar_ranking(alunos, tamanho)
            else:
                print('Primeiro use algum mecanismo de ordenacao para ver o ranking.')
        elif opcao == 8:
            print('Opcao escolhida: Comparar Metodos de Ordenacao')
            # Funcao
        elif opcao == 0:
            print('Encerrando programa')
            break
        else:
            print('Opcao Invalida')
