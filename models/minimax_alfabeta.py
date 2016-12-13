from models.move import Move

def new_board_from_play(board,move,color):
    new_board = board.get_clone()
    new_board.play(move,color)
    return new_board

# Recurisve Implementation of MiniMaxAlfaBeta Algorithm
def mini_max_alfa_beta(board, depth, color, parent_alfa, parent_beta, isMaxLevel, heuristic_function):
    best_value = None
    best_move  = None

    # Base of the recursion
    if depth == 0 or not board.valid_moves(color):
        return heuristic_function(board, color), None

    alfa = float('-inf')
    beta = float('inf')

    # Recurvive calls
    # Each valid move is calculated using the recursive call
    for valid_move in board.valid_moves(color):
        child_value,_ = mini_max_alfa_beta(
            new_board_from_play(board,valid_move,color),
            depth - 1,
            board._opponent(color),
            alfa,
            beta,
            not isMaxLevel,
            heuristic_function
        )

        if isMaxLevel:
            if child_value > alfa:
                alfa = child_value
                best_move = valid_move
            best_value = alfa
            if best_value > parent_beta:
                break
        else:
            beta = min(child_value, beta)
            best_value = beta
            if best_value < parent_alfa:
                break

    return best_value, best_move
