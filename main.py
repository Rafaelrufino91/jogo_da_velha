tabuleiro = {1: '#', 2: '#', 3: '#',
             4: '#', 5: '#', 6: '#',
             7: '#', 8: '#', 9: '#'}


def limpar_tabuleiro(tabuleiro):
    for k, v in tabuleiro.items():
        tabuleiro[k] = '#'


def exibir_tabuleiro():
    print(f'{tabuleiro[1]}|{tabuleiro[2]}|{tabuleiro[3]}')
    print('-+-+-')
    print(f'{tabuleiro[4]}|{tabuleiro[5]}|{tabuleiro[6]}')
    print('-+-+-')
    print(f'{tabuleiro[7]}|{tabuleiro[8]}|{tabuleiro[9]}')


def vencedor(jogada):
    return (tabuleiro[1] == jogada and tabuleiro[2] == jogada and tabuleiro[3] == jogada or
            tabuleiro[4] == jogada and tabuleiro[5] == jogada and tabuleiro[6] == jogada or
            tabuleiro[7] == jogada and tabuleiro[8] == jogada and tabuleiro[9] == jogada or
            tabuleiro[1] == jogada and tabuleiro[4] == jogada and tabuleiro[7] == jogada or
            tabuleiro[2] == jogada and tabuleiro[5] == jogada and tabuleiro[8] == jogada or
            tabuleiro[3] == jogada and tabuleiro[6] == jogada and tabuleiro[9] == jogada or
            tabuleiro[1] == jogada and tabuleiro[5] == jogada and tabuleiro[9] == jogada or
            tabuleiro[3] == jogada and tabuleiro[5] == jogada and tabuleiro[7] == jogada)


def jogo_da_velha():
    while True:
        limpar_tabuleiro(tabuleiro)
        jogador1 = input('Quem vai ser o jogador 1? ')
        jogador2 = input('Quem vai ser o jogador 2? ')
        print()
        exibir_tabuleiro()
        for cont in range(5):
            # Jogada do primeiro jogador
            while True:
                try:
                    jogada = int(input(f'Informe sua jogada {jogador1}: '))
                    if tabuleiro[jogada] == '#':
                        tabuleiro[jogada] = 'X'
                        break
                    else:
                        print('Já está preenchido. Escolha outra opção.')
                except KeyError:
                    print('Informe uma opção valida')
                except ValueError:
                    print('Informe uma opção valida')

            exibir_tabuleiro()
            # Primeira validação de vitoria
            if vencedor(tabuleiro[jogada]):
                print(f'Parabéns {jogador1} você ganhou!')
                break

            # Validação empate
            if '#' not in tabuleiro.values():
                print('Empatou! Deu velha')
                break

            # Jogada do segundo jogador
            while True:
                try:
                    jogada = int(input(f'Informe sua jogada {jogador2}: '))
                    if tabuleiro[jogada] == '#':
                        tabuleiro[jogada] = 'O'
                        break
                    else:
                        print('Já está preenchido. Escolha outra opção.')
                except KeyError:
                    print('Informe uma opção valida')
                except ValueError:
                    print('Informe uma opção valida')

            exibir_tabuleiro()
            # Segunda validação de vitoria
            if vencedor(tabuleiro[jogada]):
                print(f'Parabéns {jogador2} você ganhou!')
                break
        while True:
            confirma = input('\nDeseja jogar novamente?[S/N] ')
            if confirma in 'SsNn':
                break
            else:
                print('Opção invalida, tente novamente.', end='')
        if confirma in 'Nn':
            break


if __name__ == '__main__':
    jogo_da_velha()
