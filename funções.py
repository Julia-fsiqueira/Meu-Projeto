def livro():
    l = str(input('Qual livro tu terminou de ler? '))
    return l


def genero():
    g = str(input('Gênero: '))
    return g


def titulo(arquivo):
    try:
        abrir_arquivo = open(arquivo,'at+')
    except FileNotFoundError:
        print(f'Falha ao executar arquivo {arquivo}.')
    else:
        try:
            abrir_arquivo.write(f'\n{livro()};{genero()}')
        except ValueError:
            print('Houve um erro no registro do título.')
        else:
            print('Novo título registrado!')
            pergunta = str(input('Quer uma indicação de um similar?[S/N] ')).strip().upper()[0]
            if pergunta in 'S':
                print('Vou pesquisar...')
            else:
                print('')
        finally:
            abrir_arquivo.close()
    return


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


def mini_menu():
    print('-' * 20)
    print('PROJETO')
    print('-' * 20)
    print('V - VER LIVROS JÁ LIDOS')
    print('C - CADASTRAR UM NOVO LIVRO')
    print('S - SAIR')
