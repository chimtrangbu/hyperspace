def print_board():
    global board
    print(end='  ')
    print(' '.join(cols))
    for x in range(8):
        print(end=str(x+1) + ' ')
        for y in range(7):
            print(end=board[x][y] + ' ')
        print(board[x][7])
    return True


def neighbor_move(i, j, direction):
    # find the neighbor in the appointed direction of index
    # if neighbor doesn't exist, return index itself.
    if direction == 'l':
        return (i, j) if j == 0 else (i, j-1)
    elif direction == 'r':
            return (i, j) if j == 7 else (i, j+1)
    elif direction == 't':
        return (i, j) if i == 0 else (i-1, j)
    elif direction == 'b':
        return (i, j) if i == 7 else (i+1, j)
    elif direction == 'tl':
        return (i, j) if i == 0 or j == 0 else (i-1, j-1)
    elif direction == 'tr':
        return (i, j) if i == 0 or j == 7 else (i-1, j+1)
    elif direction == 'bl':
        return (i, j) if i == 7 or j == 0 else (i+1, j-1)
    elif direction == 'br':
        return (i, j) if i == 7 or j == 7 else (i+1, j+1)


def valid_moves(i, j):
    # find valid moves base on a position
    global board
    flag = board[i][j]
    moves = {}
    directions = ['t', 'b', 'l', 'r', 'tl', 'tr', 'bl', 'br']
    for direction in directions:
        neighbor = neighbor_move(i, j, direction)
        i_next, j_next = neighbor[0], neighbor[1]
        next_move = board[i_next][j_next]
        if next_move in ('.', flag):
            continue
        else:
            enimies = []
            while board[i_next][j_next] not in ('.', flag):
                if (i_next, j_next) == \
                        neighbor_move(i_next, j_next, direction):
                    break
                else:
                    enimies.append((i_next, j_next))
                    i_next, j_next = \
                        neighbor_move(i_next, j_next, direction)
            if board[i_next][j_next] == '.':
                moves[(i_next, j_next)] = enimies
                continue
    return moves


def valid_choices(flag):
    # find all valid choices of a player
    global board
    res = {}
    dicts = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == player_name[flag]:
                dicts.append(valid_moves(i, j))

    for d in dicts:
        for key in d.keys():
            if key not in res:
                res[key] = d[key]
            else:
                res[key] = list(set(res[key] + d[key]))
    return res


def update_board(x, y, flag):
    # update the board when player makes a choice
    global board
    enemies = valid_choices(flag)[(x, y)]
    for enemy in enemies:
        board[enemy[0]][enemy[1]] = player_name[flag]
    board[x][y] = player_name[flag]
    return board


def count_result():
    # count 'W' and 'B' in the board,
    # return a tuple [example: (32,32)]
    global board
    result = ''
    for row in board:
        result += ''.join(row)
    return result.count('W'), result.count('B')


def ind_to_str(tup):
    # convert an index in the matrix to position string
    # [example: (0, 0) -> 'a1']
    return cols[tup[1]] + str(rows[tup[0]])


def str_to_ind(s):
    # convert a postion string to an index in the matrix
    # [example: 'a1' -> (0, 0)]
    return int(s[1])-1, cols.index(s[0])


if __name__ == '__main__':
    # init board
    board = [['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', 'W', 'B', '.', '.', '.'],
             ['.', '.', '.', 'B', 'W', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.']]
    # name of columns
    cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    # name of rows
    rows = range(1, 9)
    # name of players
    player_name = {1: 'B', 0: 'W'}
    # start from play B
    flag = 1
    while True:
        print_board()
        # get valid choices of current player
        choices = valid_choices(flag).keys()
        if not choices:
            # if there's no choice, print player cannot play
            print('Player %s cannot play.' % player_name[flag])
            if not valid_choices(not flag):
                # if other player cannot play either,
                # print result and end game.
                print_board()
                print('Player %s cannot play.' % player_name[not flag])
                result = count_result()
                print('End of the game. W: %d, B: %d' % (result[0], result[1]))
                print('B wins.') if result[1] > result[0] else print('W wins.')
                break
            else:
                # if other player can play, change side
                flag = not flag
        else:
            # convert all valid choices from index to position strings
            valids = []
            for e in choices:
                valids.append(ind_to_str(e))
            valids.sort()
            print('Valid choices: ' + ' '.join(valids))
            try:
                # get choice from player
                choice = input('Player %s: ' % player_name[flag])
            except EOFError:
                # if End Of File, end game.
                break

            if choice not in valids:
                # if choice is not valid, print it out and end game.
                print('%s: Invalid choice' % choice)
                print('Valid choices: ' + ' '.join(valids))
                break
            else:
                # if choice is valid, update board and change side
                choice = str_to_ind(choice)
                update_board(choice[0], choice[1], flag)
                flag = not flag
