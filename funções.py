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
    print(f'{"PROJETO":^40}')
    linhas()
    print('V - VER TÍTULOS JÁ LIDOS')
    print('C - CADASTRAR UM NOVO TÍTULO')
    print('P - PESQUISAR TÍTULO PELO ÍNDICE')
    print('A - ATUALIZAR UM TÍTULO JÁ CADASTRADO')
    print('D - DELETAR UM TÍTULO JÁ CADASTRADO')
    print('S - SAIR')


def linhas():
    print('-' * 40)


def titulo(var):
    try:
        linhas()
        data = le_arquivo()
        data.append(var)
        escreve_arquivo(data)
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
        book = var['Livro']
        genre = var['Gênero']
    except ModuleNotFoundError:
        print('ERRO AO PESQUISAR TÍTULO')
    else:
        pergunta = str(input('Quer uma indicação de um similar?[S/N] ')).strip().upper()[0]
        if pergunta in 'S':
            print('Vou pesquisar...')
            sleep(1.5)
            webbrowser.open(f'https://www.google.com/search?q=similares+do+livro+{book}+{genre}', new=2)
        else:
            print('')


def pesquisa_indice():
    try:
        linhas()
        data = le_arquivo()
        indice = int(input('Qual o índice do livro para pesquisar? '))
        count = 0
        for linha in data:
            if indice == count:
                book = linha["Livro"]
                genre = linha["Gênero"]
            count += 1
    except FileNotFoundError:
        print('ERRO AO VISUALIZAR ARQUIVO')
    else:
        print('Vou pesquisar...')
        sleep(1.5)
        webbrowser.open(f'https://www.google.com/search?q=similares+do+livro+{book}+{genre}', new=2)


def deleta_titulo():
    try:
        linhas()
        data = le_arquivo()
        indice = int(input('Qual o índice do título para deletar? '))
        data.pop(indice)
        escreve_arquivo(data)
    except FileNotFoundError:
        print('ERRO AO DELETAR TÍTULO DO ARQUIVO')
    else:
        print('TÍTULO DELETADO COM SUCESSO')


def atualiza_titulo():
    try:
        linhas()
        data = le_arquivo()
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
        escreve_arquivo(data)
        print('TÍTULO ATUALIZADO COM SUCESSO')


def escreve_arquivo(var):
    try:
        with open('banco_de_dados.json', 'wt+') as file:
            json.dump(var, file, indent=2)
    except FileNotFoundError:
        print('Arquivo não encontrado')


def le_arquivo():
    try:
        with open('banco_de_dados.json') as outfile:
            data = json.load(outfile)
    except FileNotFoundError:
        print('Arquivo não encontrado')
    else:
        return data
