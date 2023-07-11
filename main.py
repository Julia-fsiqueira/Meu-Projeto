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
                "Gênero": funções.genero(),
                "Gênero I": funções.genero()
            }
            funções.titulo(novo_livro)
        elif opcao in 'P':
            funções.pesquisa_indice()
        elif opcao in 'A':
            funções.atualiza_titulo()
        elif opcao in 'D':
            funções.deleta_titulo()
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
