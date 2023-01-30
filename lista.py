import os
lista = []
while True:
    print('Selecione uma opção:')
    opcao = input('[I]nserir [A]pagar [L]istar: ')
    if opcao =='i':
        os.system('clear')
        inserir = input('Inserir valor(nome/string): ')
        lista.append(inserir)
    elif opcao == 'a':
        apagar = input('Escolhe um índice/número p/ apagar:')       
        try:
            indice = int(apagar)
            del lista[indice]    
        except ValueError:
            print('Erro! Você deve digitar um número inteiro.')
        except IndexError:
            print('Erro! Este índice não existe.')
        except Exception:
            print('Erro desconhecido.')
    elif opcao == 'l':
        os.system('clear')
        if len(lista) == 0:
            print('Nada para listar.')
        for i, valor in enumerate(lista):
            print(i, valor)