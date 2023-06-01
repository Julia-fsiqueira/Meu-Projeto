def arquivo_existe(nome):
    try:
        arquivo = open(nome, 'rt')
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        criar = open(nome, 'wt+')
        criar.close()
    except:
        print(f'Houve um erro ao criar o arquivo {nome}')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


