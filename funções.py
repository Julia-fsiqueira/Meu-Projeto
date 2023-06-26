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
    print('-' * 20)
    print('PROJETO')
    print('-' * 20)
    print('V - VER LIVROS JÁ LIDOS')
    print('C - CADASTRAR UM NOVO LIVRO')
    print('P - PESQUISAR LIVRO PELO ÍNDICE')
    print('S - SAIR')


def titulo(var):
    try:
        with open('banco_de_dados.json', 'rt') as outfile:
            j = json.load(outfile)
        j.append(var)
        with open('banco_de_dados.json', 'wt+') as file:
            json.dump(j, file, indent=2)
    except FileNotFoundError:
        print('Houve um erro no registro do título.')
    else:
        print('Novo título registrado!')
        pesquisa(var)
    return


'''def visualizar_arquivo(nome):
    try:
        with open(nome, 'rt') as outfile:
            j = json.load(outfile)
    except FileNotFoundError:
        print(f'Arquivo {nome} não encotrado.')
    else:
        indice = 0
        print(f'{" ÍNDICE":<3}', end='')
        print(f'{"LIVRO":^30}', end='')
        print(f'{"GÊNERO":>20}')
        for linha in j:
            indice += 1
            print(f'   {indice:<2} {linha["Livro"]:^35} {linha["Gênero"]:>15}')'''


def visualizacao_arquivo():
    try:
        print(pd.read_json('banco_de_dados.json', orient='records'))
    except FileNotFoundError:
        print('ARQUIVO NÃO ENCONTRADO')


def pesquisa(var):
    try:
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
        with open(arquivo, 'rt') as outfile:
            j = json.load(outfile)
        indice = int(input('Qual o índice do livro para pesquisar? '))
        count = 0
        for linha in j:
            count += 1
            if indice == count:
                dados_1 = linha["Livro"]
                dados_2 = linha["Gênero"]
    except FileNotFoundError:
        print('ERRO AO VISUALIZAR ARQUIVO')
    else:
        print('Vou pesquisar...')
        sleep(1.5)
        webbrowser.open(f'https://www.google.com/search?q=similares+do+livro+{dados_1}+{dados_2}', new=2)
