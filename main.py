dim = 9, 9


def input_board():
    board = {}
    for l in range(dim[0]):
        linha = input("Linha %i: " % (l + 1))

        for c in range(dim[1]):
            board[l, c] = linha[c]
    return board


def string_to_board(strboard):
    linhas = strboard.split('|')
    board = {}
    for l in range(dim[0]):
        for c in range(dim[1]):
            board[l, c] = int(linhas[l][c])

    return board


def sample_board():
    board = {}
    solut = {}
    strboard = "723000159|600302008|800010002|070654020|004207300|050931040|500070003|400103006|932000714"
    strsolut = "723846159|615392478|849715632|378654921|194287365|256931847|561479283|487123596|932568714"
    return string_to_board(strboard), string_to_board(strsolut)


def print_board(board):
    for l in range(dim[0]):
        linha = " ".join(str(board[l, i]) for i in range(9))
        print(linha)
    print("- " * 9)


def print_quadrado(quadrado):
    for l in range(3):
        linha = " ".join(str(quadrado[l, i]) for i in range(3))
        print(linha)


def retorna_linha(board, ilinha):
    return [board[ilinha, i] for i in range(dim[1])]


def retorna_coluna(board, icoluna):
    return [board[i, icoluna] for i in range(dim[0])]


def retorna_box(board, ilinha, icoluna):
    quadrado_linha = ilinha // 3
    quadrado_coluna = icoluna // 3
    quadrado = {}
    for l in range(quadrado_linha * 3, quadrado_linha * 3 + 3):
        for c in range(quadrado_coluna * 3, quadrado_coluna * 3 + 3):
            quadrado[(l - quadrado_linha * 3), (c - quadrado_coluna * 3)] = board[l, c]
    return [i for i in quadrado.values()]


def retorna_possibilidades(board, ilinha, icoluna):
    if board[ilinha, icoluna] != 0:
        return board[ilinha, icoluna]
    todosnumeros = set(i for i in range(10))
    linha = retorna_linha(board, ilinha)
    coluna = retorna_coluna(board, icoluna)
    box = retorna_box(board, ilinha, icoluna)
    full_list = set(linha + coluna + box)
    possibilidades = todosnumeros.difference(full_list)
    return [i for i in possibilidades]


def solve(board):
    for l in range(dim[0]):
        for c in range(dim[1]):
            if board[l, c] != 0:
                continue
            possibilidades = retorna_possibilidades(board, l, c)
            if len(possibilidades) == 1:
                board[l, c] = possibilidades[0]
                return solve(board)

# def solve2(board):  # isso nao esta funcionando


#     for l in range(dim[0]):
#         for c in range(dim[1]):
#             if board[l, c] != 0:
#                 continue
#             possibilidades = retorna_possibilidades(board, l, c)
#             if (len(possibilidades) > 1):
#                 protoboard = board.copy()
#                 for p in possibilidades:
#                     protoboard[l, c] = p
#                     if is_valid(protoboard):
#                         result = solve(protoboard)
#                         if 0 in result:
#                             continue
#                         return result


def is_valid(board):
    for l in range(dim[0]):
        for c in range(dim[1]):
            if board[l, c] != 0:
                continue
            possibilidades = retorna_possibilidades(board, l, c)
            if len(possibilidades) == 0:
                return False

        return True


def main():
    boards = sample_board()
    board = boards[0]
    solved = boards[1]
    print_board(board)
    solve(board)
    print_board(board)
    print_board(solved)
    print(board == solved)


if __name__ == "__main__":
    main()
