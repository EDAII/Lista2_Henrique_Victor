import random
import string
from aluno import Aluno

cursos = ['ADMINISTRACAO',
          'AGRONOMIA',
          'BIBLIOTECONOMIA',
          'CIENCIA DA COMPUT.',
          'DIREITO',
          'ENFERMAGEM',
          'ENGENHARIA CIVIL',
          'ENGENHARIA MECANICA',
          'ESTATISTICA',
          'FARMACIA',
          'FILOSOFIA',
          'FISICA',
          'HISTORIA',
          'JORNALISMO',
          'MATEMATICA',
          'MEDICINA',
          'MUSEOLOGIA',
          'MUSICA',
          'NUTRICAO',
          'ODONTOLOGIA',
          'PEDAGOGIA',
          'QUIMICA',
          'TURISMO'
          ]

def gerar_alunos_aleatorios(alunos, tamanho):
    maiuscula = string.ascii_uppercase
    minuscula = string.ascii_lowercase
    alunos.clear()
    
    for _ in range (tamanho):
        nome = ''.join([random.choice(maiuscula)])
        nome += ''.join(random.choice(minuscula) for _ in range(9))

        curso = cursos[random.randrange(0, len(cursos))]
        
        notaMat = random.randrange(0, 1001)
        notaLing = random.randrange(0, 1001)
        notaHum = random.randrange(0, 1001)
        notaCien = random.randrange(0, 1001)
        notaRed = random.randrange(0, 1001)

        aluno = Aluno(nome, curso, notaMat, notaLing, notaHum, notaCien, notaRed)

        alunos.append(aluno)

def mostrar_ranking(alunos, tamanho):
    print('------------------------------------------------------------------------------------------')
    print("|                             RANKING DOS {} MELHORES ALUNOS                             |".format(Aluno.get_totalAlunos()))
    print('------------------------------------------------------------------------------------------')
    print('|  POS   |    NOME    | MAT  | LING | HUM  | CIEN | RED  | MEDIA  |    CURSO DESEJADO    |')
    print('------------------------------------------------------------------------------------------')

    for i in range(tamanho):
        print("| {:06} | {} | {:04} | {:04} | {:04} | {:04} | {:04} | {:06.1f} | {:^20} |".format(
            i+1, alunos[i].nome, alunos[i].notaMat, alunos[i].notaLing, alunos[i].notaHum,
            alunos[i].notaCien, alunos[i].notaRed, alunos[i].media, alunos[i].curso))
        print('------------------------------------------------------------------------------------------')
    
    print()