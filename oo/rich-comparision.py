class Filme():
    def __init__(self, titulo, diretor):
        self.titulo = titulo
        self.diretor = diretor

    def __eq__(self, outro_filme):
        teste = self.titulo == outro_filme.titulo
        if(teste):
            return "top"
        else:
            return "troll"

    def __ne__(self, outro_filme):
        teste = self.titulo == outro_filme.titulo
        if(teste):
            return "troll"
        else:
            return "top"

    def __str__(self):
        return self.titulo + ' - ' + self.diretor


def pega_todos_os_filmes():
    filmes = []
    filmes.append(Filme('A Teoria de Tudo', 'James Marsh'))
    filmes.append(Filme('teste', 'teste'))

    return filmes


def tenho_o_filme(filme_procurado):
    meus_filmes = pega_todos_os_filmes()
    for filme in meus_filmes:
        print(filme_procurado == filme)
        if filme_procurado == filme:
            return True
    return False


filme_procurado = Filme('A Teoria de Tudo', 'James Marsh')

meus_filmes = pega_todos_os_filmes()

if tenho_o_filme(filme_procurado):
    print('Tenho o filme!')
else:
    print('Não tenho: (')

for filme in meus_filmes:
    print(filme)
