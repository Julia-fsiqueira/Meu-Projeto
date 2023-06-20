import arquivo
import funções

file = 'banco_de_dados.txt'
if arquivo.arquivo_existe(file):
    print('AGUARDE...')
else:
    arquivo.criar_arquivo(file)
while True:
    try:
        funções.mini_menu()
        opcao = str(input('Opção desejada: ')).strip().upper()[0]
        if opcao in 'V':
            funções.visualizar_arquivo(file)
        elif opcao in 'C':
            novo_livro = funções.titulo(file)
        elif opcao in 'P':
            funções.pesquisa_indice(file)
        elif opcao in 'S':
            break
        else:
            print('Tente novamente.')
    except ValueError:
        print('Erro ao adicionar opção.')
        continue
    except KeyboardInterrupt:
        print('\nO usuário não quis continuar o programa')
        break

