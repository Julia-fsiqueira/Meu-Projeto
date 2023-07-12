import arquivo
import funções

file = 'banco_de_dados.json'
if arquivo.arquivo_existe(file):
    print('AGUARDE...')
else:
    arquivo.criar_arquivo(file)
while True:
    try:
        funções.mini_menu()
        opcao = str(input('Opção desejada: ')).strip().upper()[0]
        if opcao in 'V':
            funções.visualizacao_arquivo()
        elif opcao in 'C':
            novo_livro = {
                "Livro": funções.livro(),
                "Gênero": [funções.genero(), funções.genero()]
            }
            pergunta = str(input('Quer adicionar outro gênero?[S/N] ')).strip().upper()[0]
            if pergunta in 'S':
                novo_livro["Gênero"].append(funções.genero())
            funções.titulo(novo_livro)
        elif opcao in 'P':
            funções.pesquisa_indice(file)
        elif opcao in 'A':
            funções.atualiza_titulo(file)
        elif opcao in 'D':
            funções.deleta_titulo(file)
        elif opcao in 'S':
            print(f'{"FIM. VOLTE SEMPRE":^40}')
            break
        else:
            print('Tente novamente.')
    except ValueError:
        print('Erro ao adicionar opção.')
        continue
    except KeyboardInterrupt:
        print('\nO usuário não quis continuar o programa')
        break
