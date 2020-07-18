from random import randint


def checar_possibilidade(pos, jogador):
    try:
        pos = int(pos)
        if 0 <= pos <= 8:
            if 0 <= pos <= 2:
                linha = 0
                if tabuleiro[linha][pos] == ' ':
                    jogar(linha, pos, jogador)
                    jogador.append(pos)
                    return True
                else:
                    if jogador != computador:
                        print('Essa posição já foi preenchida')
                    return False
            elif 3 <= pos <= 5:
                pos -= 3
                linha = 1
                if tabuleiro[linha][pos] == ' ':
                    jogar(linha, pos, jogador)
                    jogador.append(pos+3)
                    return True
                else:
                    if jogador != computador:
                        print('Essa posição já foi preenchida')
                    return False
            else:
                linha = 2
                pos -= 6
                if tabuleiro[linha][pos] == ' ':
                    jogar(linha, pos, jogador)
                    jogador.append(pos+6)
                    return True
                else:
                    if jogador != computador:
                        print('Essa posição já foi preenchida')
                    return False
        else:
            print('Não há essa posição, jogue novamente')
            return False
    except ValueError:
        print('Valor Invalido')
        return False


def jogar(y, x, jogador):
    if jogador == jogador_um:
        tabuleiro[y][x] = 'X'
        base_para_jogar[y][x] = '-'
    else:
        tabuleiro[y][x] = 'O'
        base_para_jogar[y][x] = '-'


def imprimir():
    for i in range(3):
        print(f'{tabuleiro[i]}    Posições: {base_para_jogar[i]}')


def checar(jogador, jogando_dois=False):
    possibilidades = {
        '0': [0, 1, 2],
        '1': [3, 4, 5],
        '2': [6, 7, 8],
        '3': [0, 3, 6],
        '4': [1, 4, 7],
        '5': [2, 5, 8],
        '6': [0, 4, 8],
        '7': [6, 4, 2]
    }
    acabou = False
    for chave in possibilidades:
        valores = possibilidades.get(chave)
        foi = 0
        for numero in valores:
            for jogada in jogador:
                if numero == jogada:
                    foi += 1
        if foi == 3:
            acabou = True
            break
    if acabou:
        if jogador == jogador_um:
            if jogando_dois:
                print(f'O jogador um ganhou!')
            else:
                print('Parabens! Você ganhou!')
        elif jogador == jogador_dois:
            print('O jogador dois ganhou!')
        else:
            print('O computador ganhou!')
        return True
    else:
        if len(jogador_um) + len(computador) + len(jogador_dois) == 9:
            print('Deu velha')
            return True
        else:
            return False


jogador_um = []
jogador_dois = []
computador = []
base_para_jogar = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
tabuleiro = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
while True:
    print('1- Jogar contra o computador\n'
          '2- Jogar contra outra pessoa')
    escolha = input('Escolha: ')
    if escolha == '1':
        while True:
            imprimir()
            print('Sua vez, aonde deseja jogar?\n(Digite o número mostrado no tabuleiro acima)')
            posicao = input()
            retorno = checar_possibilidade(posicao, jogador_um)
            if retorno:
                fim = checar(jogador_um)
                if fim:
                    imprimir()
                    print('O jogo acabou.')
                    break
                print('Vez do computador')
                imprimir()
                while True:
                    posicao = randint(0,8)
                    retorno = checar_possibilidade(posicao, computador)
                    if retorno:
                        print(f'O computador jogou na posição {posicao}')
                        break
                fim = checar(computador)
                if fim:
                    imprimir()
                    print('O jogo acabou.')
                    break
        break

    elif escolha == '2':
        while True:
            imprimir()
            print('Jogador um, sua vez\n(Digite o número mostrado no tabuleiro acima)')
            posicao = input()
            retorno = checar_possibilidade(posicao, jogador_um)
            if retorno:
                fim = checar(jogador_um, True)
                if fim:
                    imprimir()
                    print('O jogo acabou.')
                    break
                while True:
                    imprimir()
                    print('Jogador dois, sua vez\n(Digite o número mostrado no tabuleiro acima)')
                    posicao = input()
                    retorno = checar_possibilidade(posicao, jogador_dois)
                    if retorno:
                        break
                fim = checar(jogador_dois)
                if fim:
                    imprimir()
                    print('O jogo acabou.')
                    break
        break
    else:
        print('Valor invalido')
