from collections import deque

win = 'win'
lose = 'lose'
unknown = 'unknown'
temp_moves = deque();

###Position has representation: ("R--L", "R").
###Where R is for player right and L is for player left.
###position[0] is the current state of the board with "-" meaning an empty space.
###position[1] is whose turn it is.

##### Game Functions####
def rules(player, listArg):
    positions = []

    if player == "R":
        opponent = "L"
        for i in range(len(listArg) - 1):
            list = listArg[:]
            if i <= len(listArg) - 2 and list[i] == player and list[i + 1] == "-":
                list[i], list[i + 1] = "-", player
                positions.append((''.join(list), opponent))

            elif i <= len(listArg) - 3 and list[i] == player and list[i + 1] == opponent and list[i + 2] == "-":
                list[i], list[i + 1], list[i + 2] = "-", opponent, player
                positions.append((''.join(list), opponent))

    if player == "L":
        opponent = "R"
        for i in range(len(listArg) - 1, 0, -1):
            list = listArg[:]
            if i >= 1 and list[i] == player and list[i - 1] == "-":
                list[i], list[i - 1] = "-", player
                positions.append((''.join(list), opponent))
            elif i >= 2 and list[i] == player and list[i - 1] == opponent and list[i - 2] == "-":
                list[i], list[i - 1], list[i - 2] = "-", opponent, player
                positions.append((''.join(list), opponent))

    if positions:
        return positions
    else:
        return None


def do_move(position, move):
    if move:
        new_position = move
        return new_position

def generate_moves(position):
    return rules(position[1], list(position[0]))


def primitive_value(position):
    moves = generate_moves(position)
    if moves == None:
        return lose
    else:
        temp_moves.append(moves)
        return unknown


#### Solver#########
#Memoization
game_tree = {}


def solve(position):
    if position not in game_tree:
        primitiveVal = primitive_value(position)
        if primitiveVal != unknown:
            game_tree[position] = primitiveVal
            return primitiveVal
        else:
            moves = temp_moves.pop()
            children_pos = [do_move(position, move) for move in moves]
            children_val = [solve(child) for child in children_pos]
            if lose in children_val:
                game_tree[position] = win
                return win
            else:
                game_tree[position] = lose
                return lose
    else:
        return game_tree[position]
