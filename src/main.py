from funcoes import *
from ordenacoes import *
import time
from aluno import Aluno

def menu():
    os.system('clear')
    print('ESCOLHA UMA OPCAO:\n')

    print('1. Gerar Alunos Aleatoriamente')
    print('2. Cadastrar Aluno Individual')
    print('3. Ordenar com Selection Sort')
    print('4. Ordenar com Insertion Sort')
    print('5. Ordenar com Bubble Sort')
    print('6. Ordenar com Shell Sort')
    print('7. Ver Ranking ordenado dos Alunos')
    print('8. Ver Ranking desordenado dos Alunos')
    print('9. Comparar Metodos de Ordenacao')
    print('10. Ver Media dos Alunos')
    print('0. Encerrar Programa')
    print('')

if __name__ == '__main__':
    alunos = []
    desordenado = []
    ordenado = False
    while True:
        menu()
        opcao = int(input('Opcao: '))
        if opcao == 1:
            print('Opcao escolhida: Gerar Alunos Aleatoriamente')
            tamanho = int(input('Digite quantos alunos voce quer criar: '))

            while tamanho < 1:
                tamanho = int(input('Tamanho nao pode ser menor que 1, tente novamente: '))
            
            inicio = time.time()
            gerar_alunos_aleatorios(alunos, tamanho)
            fim = time.time()
            tempo_total = fim - inicio
            print('{} Alunos gerados.'.format(len(alunos)))
            print('Tempo decorrido:',round(tempo_total, 6), 's\n')
            desordenado = alunos.copy()

            ordenado = False
            clear()
        elif opcao == 2:
            print('Opcao escolhida: Cadastrar Aluno Individual')
            cadastrar_aluno(alunos)
            ordenado = False
            clear()
        elif opcao == 3:
            if len(alunos) > 0:
                print('Opcao escolhida: Ordenar com Selection Sort')
                inicio = time.time()
                selection_sort(alunos)
                fim = time.time()
                tempo_total = fim - inicio
                print('\nTempo decorrido:',round(tempo_total, 6), 's')
                print('A Ordenacao terminou.\n')
                ordenado = True
                clear()
            else:
                print('Nao ha nenhum aluno cadastrado.')
                clear()
        elif opcao == 4:
            if len(alunos) > 0:
                print('Opcao escolhida: Ordenar com Insertion Sort')
                inicio = time.time()
                insertion_sort(alunos)
                fim = time.time()
                tempo_total = fim - inicio
                print('\nTempo decorrido:',round(tempo_total, 6) , 's')
                print('A Ordenacao terminou.\n')
                ordenado = True
                clear()
            else:
                print('Nao ha nenhum aluno cadastrado.')
                clear()
        elif opcao == 5:
            if len(alunos) > 0:
                print('Opcao escolhida: Ordenar com Bubble Sort')
                inicio = time.time()
                bubble_sort(alunos)
                fim = time.time()
                tempo_total = fim - inicio
                print('\nTempo decorrido:',round(tempo_total, 6), 's')
                print('A Ordenacao terminou.\n')
                ordenado = True
                clear()
            else:
                print('Nao ha nenhum aluno cadastrado.')
                clear()
        elif opcao == 6:
            if len(alunos) > 0:
                print('Opcao escolhida: Ordenar com Shell Sort')
                inicio = time.time()
                shell_sort(alunos)
                fim = time.time()
                tempo_total = fim - inicio
                print('\nTempo decorrido:',round(tempo_total, 6), 's')
                print('A Ordenacao terminou.\n')
                ordenado = True
                clear()
            else:
                print('Nao ha nenhum aluno cadastrado.')
                clear()
        elif opcao == 7:
            if ordenado == True:
                print('Opcao escolhida: Ver Ranking dos Alunos')
                print("O ranking possui {} alunos".format(len(alunos)))
                tamanho = int(input('Quantos alunos do ranking voce quer ver? '))

                while tamanho > len(alunos):
                    tamanho = int(input('Tamanho nao pode ser maior que o maximo de alunos, tente novamente: '))

                mostrar_ranking(alunos, tamanho)
                clear()
            else:
                print('Primeiro use algum mecanismo de ordenacao para ver o ranking.')
                clear()
        elif opcao == 8:
            if len(alunos) > 0:
                print('Opcao escolhida: Ver Ranking desordenado dos Alunos')
                print("O ranking possui {} alunos".format(len(alunos)))
                tamanho = int(input('Quantos alunos do ranking voce quer ver? '))

                while tamanho > len(alunos):
                    tamanho = int(input('Tamanho nao pode ser maior que o maximo de alunos, tente novamente: '))
                
                mostrar_ranking(desordenado, tamanho)
                clear()
            else:
                print('Não há alunos cadastrados!')
                clear()
        elif opcao == 9:
            
            if len(alunos) > 0:

                lista_tempos = {}
                os.system('clear')

                print('Comparação entre os Metodos de Ordenacao\n')

                # Selection Sort
                alunos = desordenado.copy()
                print('Selection Sort')
                inicio = time.time()
                selection_sort(alunos)
                fim = time.time()
                
                lista_tempos['Selection Sort'] = (fim - inicio)
                print('Tempo decorrido:',lista_tempos['Selection Sort'], 's')
                print('')

                #Insertion Sort
                alunos = desordenado.copy()
                print('Insertion Sort')
                inicio = time.time()
                insertion_sort(alunos)
                fim = time.time()
                lista_tempos['Insertion Sort'] = (fim - inicio)
                print('Tempo decorrido:', lista_tempos['Insertion Sort'], 's')
                print('')

                #Buble Sort
                alunos = desordenado.copy()
                print("Bubble Sort")
                inicio = time.time()
                bubble_sort(alunos)
                fim = time.time()
                lista_tempos['Bubble Sort'] = (fim - inicio)
                print('Tempo decorrido:', lista_tempos['Bubble Sort'], 's')
                print('')

                #Shell Sort
                alunos = desordenado.copy()
                print("Shell Sort")
                inicio = time.time()
                shell_sort(alunos)
                fim = time.time()
                lista_tempos['Shell Sort'] = (fim - inicio)
                print('Tempo decorrido:', lista_tempos['Shell Sort'], 's')
                print('')

                tipos = ['Selection Sort', 'Insertion Sort', 'Bubble Sort', 'Shell Sort']
                tempos = [lista_tempos['Selection Sort'], lista_tempos['Insertion Sort'], lista_tempos['Bubble Sort'], lista_tempos['Shell Sort']]

                _, ax = plt.subplots(figsize=(16, 9))
                ax.set(xlabel='Metodo de Ordenacao', ylabel='Tempo (s)')
                plt.figure(1)
                plt.bar(tipos, tempos)

                for i, v in enumerate(tempos):
                    plt.text(i-0.4, max(tempos)/100, " "+str(v), color='black', va='center', fontweight='bold', fontsize=12)
                
                plt.suptitle('Tempo em segundos para ordenar {} alunos'.format(len(alunos)))
                plt.show()
                
                clear()
            else:
                print('Não há nenhuma aluno cadastrado')

        elif opcao == 10:
            print('Opcao escolhida: Ver Media dos Alunos')
            grafico_medias(alunos)
        elif opcao == 0:
            print('Encerrando programa')
            break
        else:
            print('Opcao Invalida')
