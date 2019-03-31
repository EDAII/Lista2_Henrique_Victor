# LISTA 2 - ESTRUTURA DE DADOS 2 - 2019/1

### Henrique Martins de Messias - 17/0050394
### Victor Rodrigues Silva - 16/0019516

<br>

### Instruções de uso

- No terminal, vá até o diretório do exercício, que contém, além de arquivos como o README, a pasta "src"
- Digite o seguinte comando:

  ```bash
    $ cd src
  ```

- Para executar o código, digite:

  ```bash
    $ python3 main.py
  ```

### Detalhes da Lista 2

O código deste repositório simula o resultado do ENEM, sendo que cada aluno possui:

- Nome
- Curso desejado
- Nota em Matemática e suas Tecnologias (MAT)
- Nota em Linguagens, Códigos e suas Tecnologias(LING)
- Nota em Ciências Humanas e suas Tecnologias (HUM)
- Nota em Ciências da Natureza e suas Tecnologias (CIEN)
- Nota em Redação (RED)
- Media aritmética das notas (MEDIA)

O usuário pode gerar uma quantidade de alunos, que possuirão nome, curso desejado e notas aleatórios, além de poder cadastrar um aluno com os dados que quiser.  
O código oferece 4 maneiras de ordenar os alunos. As 4 maneiras são:

- Selection Sort
- Insertion Sort
- Bubble Sort
- Shell Sort

Os alunos serão ordenados com base na média das notas, em que o aluno com a maior média vem primeiro. Em caso de empate nas médias, a ordem alfabética será aplicada para determinar quem virá primeiro.  
A média é calculada da seguinte maneira:

Media = (MAT + LING + HUM + CIEN + RED) / 5

O usuário também pode comparar a eficiência dos algoritmos de ordenação, usando-os individualmente ou selecionando a opção "Comparar Metodos de Ordenacao".