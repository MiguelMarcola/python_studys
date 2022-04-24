from typing import Counter


texto1 = """
Você já fez uma pesquisa na internet e encontrou exatamente o que procurava? É incrível, né? Páginas otimizadas para mecanismos de buscas apresentam esse desempenho na web. E sabe quem te ajuda a criar aplicações web com esse tipo de otimização? O Next.js. Ele é uma estrutura para aplicativos React, gerados estaticamente ou renderizados pelo servidor.

Neste artigo mostrarei como usar o Next.js para criar aplicações otimizadas para SEO, utilizando meta-tags. Aqui, iremos aprender também:

O que é SEO;
O que são meta-tags e porque elas são importantes;
Como adicionar meta-tags no Next js.
Vamos lá?

SEO (Search Engine Optimization)
O SEO envolve muitas estratégias para aumentar a posição de classificação de uma página da web nos resultados de mecanismos de busca. Quanto melhor for o SEO de sua página, mais fácil será para as pessoas encontrarem seu site e acessarem o seu conteúdo.

Imagine que você tenha uma página que vende produtos Geeks. Quando qualquer pessoa interessada em comprar algo relacionado a seus produtos pesquisar na internet sobre um produto deste nicho é importante que sua página apareça entre os primeiros resultados da busca, e isso é possível com uma boa estratégia de SEO. Assim, é fundamental ter uma boa pontuação de SEO se o seu objetivo é obter um maior número de pessoas visualizando seu site, já que mais visitantes podem significar um aumento no número de vendas do seu negócio, por exemplo.

Os mecanismos de buscas estão cada vez mais inteligentes, pois, ajustam constantemente seus algoritmos. Contudo, eles acabam ficando limitados por quais informações você fornece e como fornece em seus sites. Uma forma de solucionar essa limitação é melhorar a indexação do seu conteúdo nos mecanismos de pesquisa. Para isso, o método mais comum é o uso de meta-tags que ajudam os algoritmos a caracterizarem o conteúdo de suas páginas da web.

O que são e porque utilizar meta-tags?
As meta-tags fornecem dados sobre a sua página aos mecanismos de pesquisa. Elas são elementos HTML que você cria para descrever o conteúdo de uma página. São colocadas na tag <head> e geralmente não são visíveis aos usuários, mas são pequenas instruções para os algoritmos dos sites de busca.

Meta-tags são muito importantes pois ajudam os mecanismos de pesquisa a categorizar o conteúdo da página corretamente. Elas constituem os elementos “otimizáveis” que destacam as características mais importantes de um conteúdo e ajudam no melhor ranqueamento de um site, certificando que as informações do site escolhido pelo algoritmo dos mecanismos de busca sejam condizentes com a procura do usuário.
"""

texto2 = """
Os bancos de dados são as ferramentas mais utilizadas para o armazenamento das informações e dos dados, seja em um servidor físico ou na nuvem.

É possível armazenar diversas informações em um banco de dados, surgindo assim a necessidade de termos ferramentas específicas que facilitem o nosso trabalho na hora de estruturá-los para receber essas informações. Neste momento, entram os SGBDs(Sistemas de Gestão de Bancos de Dados).

Podemos encontrar uma diversidade de SGBDs disponíveis no mercado que pode variar entre os não-relacionais como o MongoDB e os relacionais como o MySQL, Oracle, PostgreSQL, SQL Server, entre outros.

Neste artigo, vamos focar em conhecer mais sobre alguns SGBDs relacionais e suas diferenças.

Podemos fazer todas essas alterações em um banco de dados sem um SGBD?
Ao utilizar um SGBD, podemos realizar vários processos nos bancos de dados: consultar, alterar e excluir dados das tabelas; criar e gerenciar usuários; importar e exportar dados; e gerenciar backups, garantindo assim a segurança, a integridade, controle de redundância e até o compartilhamento dos dados.

Ilustração em tons de laranja e azul. Ela contém três personagens e plano de fundo composto por uma caixa com arquivos, um notebook e uma estante com arquivos, localizados da esquerda para a direita. O(a) primeiro(a) personagem à esquerda está segurando uma lupa em frente ao notebook, o(a) segundo(a) personagem ao centro está com uma pasta na mão e o terceiro à direita está guardando um livro na estante.

Devido a grande variedade de opções disponíveis no mercado, uma dúvida que pode surgir no momento da escolha é:

Qual SGBD irei utilizar?
Normalmente, chamamos o MySQL, Oracle, PostgreSQL de banco de dados, mas na realidade eles são os SGBDs que gerenciam os bancos de dados. Todos esses SGBDs, por padrão, utilizam a linguagem SQL para realizar as consultas.

Devido a esse padrão entre os SGBDs, algumas vantagens são levantadas ao se trabalhar com os SGBDs relacionais, como: aprendizado, portabilidade, longevidade, comunicação e liberdade de escolha.

Entretanto, é preciso dizer que existem diferenças que podem ser muito significativas no momento de realizar a escolha de qual software iremos utilizar para implementar o nosso projeto.

Vamos estudar algumas delas?

MySQL
Logomarca do SGBD MySQL. Ela é composta pelas palavras “My” em azul e “SQL” em laranja. Acima da letra L é apresentado traços de um golfinho na cor azul.

O MySQL é um dos bancos de dados mais populares da Oracle Corporation, possui uma versão gratuita, open source, multiplataforma, sendo compatível com diversas linguagens de programação. Além disso, tem uma comunidade ativa e pode ser utilizado em qualquer tipo de aplicação, desde as mais simples até as mais robustas.

Outro ponto favorável é a facilidade de programação e aprendizado deste SGBD. É importante lembrar que a ferramenta e a documentação estão disponíveis apenas em inglês.

O MySQL Workbench é um exemplo de software disponibilizado para simplificar a execução de tarefas complexas, configurar, gerenciar, administrar o banco de dados.

Oracle
alt text:Logomarca do SGBD Oracle. Ela é composta pela palavra “Oracle” na cor vermelha.

O Oracle é um SGBD que surgiu no fim dos anos 70, também faz parte da Oracle Corporation e possui várias edições, cada uma com características diferentes focadas para as necessidades de empresas de médio e grande porte.

Possui uma versão gratuita, suporta múltiplos bancos de dados e é compatível com diversas linguagens de programação. E assim como o MySQL, não possui uma versão em português da sua documentação.

O SQL Developer é um software gratuito disponibilizado para facilitar a utilização dos(as) usuários(as) e administradores(as) de banco de dados para execução de suas tarefas.
"""


def analisa_frequencia_texto(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia / total_de_caracteres * 100)
                  for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))

    for caractere, proporcao in proporcoes.most_common(10):
        print(f"{caractere} -> {proporcao:.2f}%")


analisa_frequencia_texto(texto1)
print()
analisa_frequencia_texto(texto2)
