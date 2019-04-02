import random
import string
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

    