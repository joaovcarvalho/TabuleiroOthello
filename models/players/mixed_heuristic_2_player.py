# -*- coding: utf-8 -*-
from models.minimax_alfabeta import mini_max_alfa_beta

class MixedHeuristics2(object):
    def corner_squares(self,board,color):
        value_map = [ [ None ] * 8 ] * 8

        corners = {
            (1,1) : 999,
            (1,8) : 999,
            (8,1) : 999,
            (8,8) : 999,

            (1,2) : -999,
            (2,1) : -999,
            (2,2) : -999,

            (7,1) : -999,
            (8,2) : -999,
            (7,2) : -999,

            (1,7) : -999,
            (2,8) : -999,
            (2,7) : -999,

            (8,7) : -999,
            (7,8) : -999,
            (7,7) : -999
        }

        for i in range(1,8):
            for j in range(1,8):
                if (i,j) in corners:
                    value_map[i - 1][j - 1] = corners.get((i,j))
                else:
                    value_map[i - 1][j - 1] = 0.0

        current_player_score = 0

        for i in range(1, 8):
            for j in range(1, 8):
                if board.board[i][j] == color:
                    current_player_score += value_map[i - 1][j - 1]

        return current_player_score

    def porcentage_of_difference_of_pieces(self,board,color):
        my_pieces = 0
        for i in range(1, 8):
            for j in range(1, 8):
                if board.board[i][j] == color:
                    my_pieces += 1

        return my_pieces/100

    def mobility_factor(self,board,color):
        number_color = len(board.valid_moves(color))
        number_opponent = len(board.valid_moves(board._opponent(color)))

        return number_color - number_opponent

    def heuristic_value(self, board, color):
        return self.porcentage_of_difference_of_pieces(board, color) \
                + self.mobility_factor(board,color) \
                + self.corner_squares(board,color)

    def __init__(self, color):
        self.color = color

    def play(self, board):
        depth = 3
        _, best_move = mini_max_alfa_beta(
            board,
            depth,
            self.color,
            float('-inf'),
            float('inf'),
            True,
            self.heuristic_value
        )

        return best_move
