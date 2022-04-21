class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    def __str__(self):
        return f"Nome: {self.nome}\nAno: {self.ano}\nLikes: {self.likes}\n\n"


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"Nome: {self.nome}\nAno: {self.ano}\nDuração: {self.duracao} minutos\nLikes: {self.likes}\n\n"


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)

        self.temporadas = temporadas

    def __str__(self):
        return f"Nome: {self.nome}\nAno: {self.ano}\nTemporadas: {self.temporadas}\nLikes: {self.likes}\n\n"


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome.title()
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


vingadores = Filme('vingadores - guerra infinita', 2008, 180)
thor = Filme('thor', 2013, 120)

twd = Serie('the walking dead', 2006, 10)
suits = Serie('suits', 2009, 8)

vingadores.dar_like()
thor.dar_like()
thor.dar_like()
twd.dar_like()
twd.dar_like()
twd.dar_like()
suits.dar_like()

filmes_e_series = [vingadores, thor, twd, suits]

playlist_fim_de_semana = Playlist("fim de semana", filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}\n')

for programas in playlist_fim_de_semana:
    print(programas)
