import random
import string
import os
import matplotlib
import matplotlib.pyplot as plt
from aluno import Aluno

cursos = ['ADMINISTRACAO',
          'AGRONOMIA',
          'BIBLIOTECONOMIA',
          'BIOTECNOLOGIA',
          'CIENCIA DA COMPUTACAO',
          'DIREITO',
          'ENFERMAGEM',
          'ENGENHARIA AERONAUTICA',
          'ENGENHARIA AGRONOMICA',
          'ENGENHARIA AMBIENTAL',
          'ENGENHARIA CIVIL',
          'ENGENHARIA DE MINAS',
          'ENGENHARIA ELETRICA',
          'ENGENHARIA FLORESTAL',
          'ENGENHARIA MECANICA',
          'ENGENHARIA MECATRONICA',
          'ENGENHARIA QUIMICA',
          'ESTATISTICA',
          'FARMACIA',
          'FILOSOFIA',
          'FISICA',
          'GEOFÍSICA',
          'GEOGRAFIA',
          'GEOLOGIA',
          'HISTORIA',
          'JORNALISMO',
          'MATEMATICA',
          'MEDICINA',
          'MUSEOLOGIA',
          'MUSICA',
          'NUTRICAO',
          'ODONTOLOGIA',
          'PEDAGOGIA',
          'PUBLICIDADE E PROPAGANDA',
          'QUIMICA',
          'RELACOES INTERNACIONAIS',
          'TURISMO',
          'ZOOTECNIA'
          ]

def gerar_alunos_aleatorios(alunos, tamanho):
    maiuscula = string.ascii_uppercase
    minuscula = string.ascii_lowercase
    alunos.clear()
    
    for _ in range (tamanho):
        nome = ''.join([random.choice(maiuscula)])
        nome += ''.join(random.choice(minuscula) for _ in range(random.randrange(3, 10)))

        curso = cursos[random.randrange(0, len(cursos))]
        
        notaMat = random.randrange(0, 1001)
        notaLing = random.randrange(0, 1001)
        notaHum = random.randrange(0, 1001)
        notaCien = random.randrange(0, 1001)
        notaRed = random.randrange(0, 1001)

        aluno = Aluno(nome, curso, notaMat, notaLing, notaHum, notaCien, notaRed)

        alunos.append(aluno)

def mostrar_ranking(alunos, tamanho):
    print('----------------------------------------------------------------------------------------------')
    print("|{:^92}|".format("RANKING DOS {} MELHORES ALUNOS".format(tamanho)))
    print('----------------------------------------------------------------------------------------------')
    print('|  RANK  |    NOME    | MAT  | LING | HUM  | CIEN | RED  | MEDIA  |      CURSO DESEJADO      |')
    print('----------------------------------------------------------------------------------------------')

    for i in range(tamanho):
        print("| {:^6} | {:^10} | {:^4} | {:^4} | {:^4} | {:^4} | {:^4} | {:^6} | {:^24} |".format(
            i+1, alunos[i].nome, alunos[i].notaMat, alunos[i].notaLing, alunos[i].notaHum,
            alunos[i].notaCien, alunos[i].notaRed, alunos[i].media, alunos[i].curso))
        print('----------------------------------------------------------------------------------------------')
    
    print()

def cadastrar_aluno(alunos):
    nome = input("Digite o nome do aluno: ")
    while len(nome) > 10:
        nome = input("Nome do aluno muito grande, escreva uma versao reduzida: ")

    curso = input("Digite o nome do curso: ")
    while len(curso) > 24:
        curso = input("Nome do curso muito grande, escreva uma versao reduzida: ")

    notaMat = int(input("Digita a nota de Matematica: "))
    while notaMat < 0 or notaMat > 1000:
        notaMat = int(input("A nota de Matematica deve ser entre 0 e 1000: "))

    notaLing = int(input("Digite a nota de Linguagens: "))
    while notaLing < 0 or notaLing > 1000:
        notaLing = int(input("A nota de Linguagens deve ser entre 0 e 1000: "))

    notaHum = int(input("Digite a nota de Ciencias Humanas: "))
    while notaHum < 0 or notaHum > 1000:
        notaHum = int(input("A nota de Ciencias Humanas deve ser entre 0 e 1000: "))

    notaCien = int(input("Digite a nota de Ciencias Naturais: "))
    while notaCien < 0 or notaCien > 1000:
        notaCien = int(input("A nota de Ciencias Naturais deve ser entre 0 e 1000: "))

    notaRed = int(input("Digite a nota da Redacao: "))
    while notaRed < 0 or notaRed > 1000:
        notaRed = int(input("A nota da Redacao deve ser entre 0 e 1000: "))
    
    aluno = Aluno(nome, curso, notaMat, notaLing, notaHum, notaCien, notaRed)
    alunos.append(aluno)
    print('\nAluno cadastrado com sucesso\n')

def grafico_medias(alunos):
    print('Calculando media dos alunos e dividindo eles em grupos...')
    n = len(alunos)
    notas = ['0-100',
             '101-200',
             '201-300',
             '301-400',
             '401-500',
             '501-600',
             '601-700',
             '701-800',
             '801-900',
             '901-1000'
             ]

    lista_notas = {'0-100' : 0,
                       '101-200' : 0,
                       '201-300' : 0,
                       '301-400' : 0,
                       '401-500' : 0,
                       '501-600' : 0,
                       '601-700' : 0,
                       '701-800' : 0,
                       '801-900' : 0,
                       '901-1000' : 0}
    
    for i in range(n):
        if 0 <= alunos[i].media <= 100:
            lista_notas['0-100'] += 1
        elif 101 <= alunos[i].media <= 200:
            lista_notas['101-200'] += 1
        elif 201 <= alunos[i].media <= 300:
            lista_notas['201-300'] += 1
        elif 301 <= alunos[i].media <= 400:
            lista_notas['301-400'] += 1
        elif 401 <= alunos[i].media <= 500:
            lista_notas['401-500'] += 1
        elif 501 <= alunos[i].media <= 600:
            lista_notas['501-600'] += 1
        elif 601 <= alunos[i].media <= 700:
            lista_notas['601-700'] += 1
        elif 701 <= alunos[i].media <= 800:
            lista_notas['701-800'] += 1
        elif 801 <= alunos[i].media <= 900:
            lista_notas['801-900'] += 1
        elif 901 <= alunos[i].media <= 1000:
            lista_notas['901-1000'] += 1
    
    quantidade = [lista_notas['0-100'],
                  lista_notas['101-200'],
                  lista_notas['201-300'],
                  lista_notas['301-400'],
                  lista_notas['401-500'],
                  lista_notas['501-600'],
                  lista_notas['601-700'],
                  lista_notas['701-800'],
                  lista_notas['801-900'],
                  lista_notas['901-1000'],
                  ]

    print('Pronto.')
    
    _, ax = plt.subplots(figsize=(16, 9))
    ax.set(xlabel='Varicao das Notas', ylabel='Quantidade de Alunos')
    plt.figure(1)
    plt.bar(notas, quantidade)

    for i, v in enumerate(quantidade):
        plt.text(i-(len(str(v))/15), max(quantidade)/100, " "+str(v), color='black', va='center', fontweight='bold', fontsize=12)
    
    plt.suptitle('Notas dos {} alunos'.format(len(alunos)))
    plt.show()


def clear():
    input("Pressione uma tecla para continuar...")
    os.system('clear')

    