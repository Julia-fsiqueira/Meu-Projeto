import json
import pandas as pd
import webbrowser
from time import sleep


def livro():
    book = str(input('Qual livro tu terminou de ler? '))
    return f"{book}"


def genero():
    genres = str(input('Gênero: '))
    return f"{genres}"


def mini_menu():
    linhas()
    print('PROJETO')
    linhas()
    print('V - VER LIVROS JÁ LIDOS')
    print('C - CADASTRAR UM NOVO LIVRO')
    print('P - PESQUISAR LIVRO PELO ÍNDICE')
    print('A - ATUALIZAR UM TÍTULO JÁ CADASTRADO')
    print('D - DELETAR UM TÍTULO JÁ CADASTRADO')
    print('S - SAIR')


def linhas():
    print('-' * 40)


def titulo(var):
    try:
        linhas()
        with open('banco_de_dados.json', 'rt') as outfile:
            data = json.load(outfile)
        data.append(var)
    except FileNotFoundError:
        print('Houve um erro no registro do título.')
    else:
        print('Novo título registrado!')
        pesquisa(var)
    return


def visualizacao_arquivo():
    try:
        linhas()
        print(pd.read_json('banco_de_dados.json', orient='records'))
    except FileNotFoundError:
        print('ARQUIVO NÃO ENCONTRADO')


def pesquisa(var):
    try:
        linhas()
        dado_1 = var['Livro']
        dado_2 = var['Gênero']
    except ModuleNotFoundError:
        print('ERRO AO PESQUISAR TÍTULO')
    else:
        pergunta = str(input('Quer uma indicação de um similar?[S/N] ')).strip().upper()[0]
        if pergunta in 'S':
            print('Vou pesquisar...')
            sleep(1.5)
            webbrowser.open(f'https://www.google.com/search?q=similares+do+livro+{dado_1}+{dado_2}', new=2)
        else:
            print('')


def pesquisa_indice(arquivo):
    try:
        linhas()
        with open(arquivo, 'rt') as outfile:
            data = json.load(outfile)
        indice = int(input('Qual o índice do livro para pesquisar? '))
        count = 0
        for linha in data:
            if indice == count:
                dados_1 = linha["Livro"]
                dados_2 = linha["Gênero"]
            count += 1
    except FileNotFoundError:
        print('ERRO AO VISUALIZAR ARQUIVO')
    else:
        print('Vou pesquisar...')
        sleep(1.5)
        webbrowser.open(f'https://www.google.com/search?q=similares+do+livro+{dados_1}+{dados_2}', new=2)


def deleta_titulo(arquivo):
    try:
        linhas()
        with open(arquivo, 'rt') as outfile:
            data = json.load(outfile)
        indice = int(input('Qual o índice do título para deletar? '))
        data.pop(indice)
        with open(arquivo, 'wt') as file:
            json.dump(data, file, indent=2)
    except FileNotFoundError:
        print('ERRO AO DELETAR TÍTULO DO ARQUIVO')
    else:
        print('TÍTULO DELETADO COM SUCESSO')


def atualiza_titulo(arquivo):
    try:
        linhas()
        with open(arquivo, 'rt') as outfile:
            data = json.load(outfile)
        indice = int(input('Qual o índice do título para atualizar? '))
        print(data[indice])
        book = str(input('Livro: '))
        genre = str(input('Gênero:[USE VÍRGULA PARA SEPARAR] '))
        atualizado = {"Livro": book, "Gênero": [genre]}
    except FileNotFoundError:
        print('OCORREU UM ERRO')
    else:
        data.pop(indice)
        data.insert(indice, atualizado)
        with open(arquivo, 'wt') as file:
            json.dump(data, file, indent=2)
        print('TÍTULO ATUALIZADO COM SUCESSO')

