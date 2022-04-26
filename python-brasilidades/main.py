import re

padrao = "\w@\w.\w"
texto = "grewgf ateste@email.com dasdasasd@dasd.1dasd dasdw dadwf"
resposta = re.search(padrao, texto)
print(resposta.group)
