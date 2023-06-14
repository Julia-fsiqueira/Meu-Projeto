import webbrowser
from time import sleep


def livro():
    l = str(input('Qual livro tu terminou de ler? '))
    return l


def genero():
    g = str(input('Gênero: '))
    return g


def mini_menu():
    print('-' * 20)
    print('PROJETO')
    print('-' * 20)
    print('V - VER LIVROS JÁ LIDOS')
    print('C - CADASTRAR UM NOVO LIVRO')
    print('P - PESQUISAR LIVRO PELO ÍNDICE')
    print('S - SAIR')


def titulo(arquivo):
    try:
        abrir_arquivo = open(arquivo, 'at+')
    except FileNotFoundError:
        print(f'Falha ao executar arquivo {arquivo}.')
    else:
        try:
            abrir_arquivo.write(f'\n{livro()};{genero()}')
            abrir_arquivo.close()
        except ValueError:
            print('Houve um erro no registro do título.')
        else:
            print('Novo título registrado!')
            pesquisa(arquivo)
    return


def visualizar_arquivo(nome):
    try:
        abrir = open(nome, 'rt')
    except FileNotFoundError:
        print(f'Arquivo {nome} não encotrado.')
    else:
        indice = 0
        for linha in abrir:
            dados = linha.replace('\n', '').split(';')
            indice += 1
            print('-' * 20)
            print(f'{indice}  Livro: {dados[0]} Gênero: {dados[1]}')
    finally:
        abrir.close()


def pesquisa(arquivo):
    try:
        f = open(arquivo, 'rt')
        for linha in f:
            dado = linha.split(';')
    except FileNotFoundError:
        print('ERRO AO VISUALIZAR ARQUIVO')
    else:
        pergunta = str(input('Quer uma indicação de um similar?[S/N] ')).strip().upper()[0]
        if pergunta in 'S':
            print('Vou pesquisar...')
            sleep(1.5)
            webbrowser.open(f'https://www.google.com/search?q=similar+ao+título+{dado[-2]}+gênero+{dado[-1]}', new=2)
        else:
            print('')


def pesquisa_indice(arquivo):
    file = open(arquivo, 'rt')
    indice = int(input('Qual o índice do livro para pesquisar? '))
    count = 0
    try:
        for linha in file:
            count += 1
            if indice == count:
                dado = linha.replace('\n', '').split(';')
    except FileNotFoundError:
        print('ERRO AO VISUALIZAR ARQUIVO')
    else:
        print('Vou pesquisar...')
        sleep(1.5)
        webbrowser.open(f'https://www.google.com/search?q=similar+ao+título+{dado[0]}+gênero+{dado[1]}', new=2)

