import webbrowser

def livro():
    l = str(input('Qual livro tu terminou de ler? '))
    return l


def genero():
    g = str(input('Gênero: '))
    return g


def titulo(arquivo):
    try:
        abrir_arquivo = open(arquivo, 'at+')
    except FileNotFoundError:
        print(f'Falha ao executar arquivo {arquivo}.')
    else:
        try:
            abrir_arquivo.write(f'\n{livro()};{genero()}')
        except ValueError:
            print('Houve um erro no registro do título.')
        else:
            print('Novo título registrado!')
            pesquisa(arquivo)
        finally:
            abrir_arquivo.close()
    return


'''def titulo(arquivo):
    try:
        dic = {'Livro': livro(), 'Gênero': genero()}
        with open(arquivo, 'w') as file:
            json.dump(dic, file)
    except:
        print('Houve um erro no registro do título.')
    else:
        print('Novo título adicionado com sucesso.')
        pergunta = str(input('Quer uma indicação de um similar?[S/N] ')).strip().upper()[0]
        if pergunta in 'S':
            print('Vou pesquisar...')
        else:
            print('')'''


def visualizar_arquivo(nome):
    try:
        abrir = open(nome, 'rt')
    except FileNotFoundError:
        print(f'Arquivo {nome} não encotrado.')
    else:
        for linha in abrir:
            dados = linha.replace('\n', '').split(';')
            print('-' * 20)
            print(f'Livro: {dados[0]}')
            print(f'Gênero: {dados[1]}')
    finally:
        abrir.close()


'''def visualizar_arquivo(arquivo):
    try:
        with open(arquivo, 'r') as read:
            print(json.load(read))
    except FileNotFoundError:
        print(f'Arquivo {arquivo} não encotrado.')'''


def pesquisa(arquivo):
    try:
        f = open(arquivo, 'rt')
        for linha in f:
            dado = linha.split(';')
            t = dado[-2]
            g = dado[-1]
    except FileNotFoundError:
        print('ERRO AO VISUALIZAR ARQUIVO')
    else:
        pergunta = str(input('Quer uma indicação de um similar?[S/N] ')).strip().upper()[0]
        if pergunta in 'S':
            print('Vou pesquisar...')
            webbrowser.open(f'https://www.google.com/search?q=similar+{t}+{g}', new=2)
        else:
            print('')



def mini_menu():
    print('-' * 20)
    print('PROJETO')
    print('-' * 20)
    print('V - VER LIVROS JÁ LIDOS')
    print('C - CADASTRAR UM NOVO LIVRO')
    print('S - SAIR')
