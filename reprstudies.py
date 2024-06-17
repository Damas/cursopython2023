class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

    def __repr__(self):
        return f'Programa(nome={self._nome}, ano={self._ano}, likes={self._likes})'

class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self._duracao = duracao

    def __repr__(self):
        return f'Filme(nome={self._nome}, ano={self._ano}, duracao={self._duracao}, likes={self._likes})'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas

    def __repr__(self):
        return f'Serie(nome={self._nome}, ano={self._ano}, temporadas={self._temporadas}, likes={self._likes})'

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
atlanta = Serie("atlanta", 2018, 2)
filmes_e_series = [vingadores, atlanta]

print(type(filmes_e_series))

for programa in filmes_e_series:
    print(repr(programa))

# for programa in filmes_e_series:
#     print(repr(programa))
#     print(programa.__repr__())
#     print(programa)