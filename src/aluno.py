class Aluno:

    _totalAlunos = 0

    __slots__ = ['nome', 'curso', 'notaMat', 'notaLing', 'notaHum', 'notaCien', 'notaRed', 'media']

    def __init__(self, nome, curso, notaMat, notaLing, notaHum, notaCien, notaRed):
        self.nome = nome
        self.curso = curso
        self.notaMat = notaMat
        self.notaLing = notaLing
        self.notaHum = notaHum
        self.notaCien = notaCien
        self.notaRed = notaRed
        self.media = (notaMat + notaLing + notaHum + notaCien + notaRed) / 5
        type(self)._totalAlunos += 1

    @property
    def get_media(self):
        return self.media

    @classmethod
    def get_totalAlunos(cls):
        return cls._totalAlunos

    def __gt__(self, concorrente):
        if(self.media == concorrente.media):
            return self.nome < concorrente.nome # Ordenar em ordem alfabetica

        return self.media > concorrente.media # Maior media vem primeiro
