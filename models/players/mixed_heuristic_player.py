# -*- coding: utf-8 -*-
from models.minimax_alfabeta import mini_max_alfa_beta

class MixedHeuristics(object):
    def normalize(self, positive, negative):
        numerator = positive - negative
        denominator = positive + negative
        if denominator != 0:
            return int(100 * numerator/denominator)
        else:
            return 0

    def position_factor(self,board,color):
        value_map = [
            [ 20, 11,  11,   8,   8,  11, 11, 20],
            [ 11, 15,  -4,   1,   1,  -4, 15, 11],
            [ 11, -4,   2,   2,   2,   2, -4, 11],
            [  8,  1,   2,  -3,  -3,   2,  1,  8],
            [  8,  1,   2,  -3,  -3,   2,  1,  8],
            [ 11, -4,   2,   2,   2,   2, -4, 11],
            [ 11, 15,  -4,   1,   1,  -4, 15, 11],
            [ 20, 11,  11,   8,   8,  11, 11, 20],
        ]

        current_player_score = 0
        opponent_score = 0

        for i in range(1, 8):
            for j in range(1, 8):
                if board.board[i][j] == color:
                    current_player_score += value_map[i - 1][j] + 7
                elif board.board[i][j] == board._opponent(color):
                    opponent_score += value_map[i - 1][j] + 7

        return self.normalize(current_player_score, opponent_score)

    def porcentage_of_difference_of_pieces(self,board,color):
        my_color = color
        enemy_color = board._opponent(my_color)
        my_pieces = 0
        opponent_pieces = 0
        for i in range(1, 8):
            for j in range(1, 8):
                if board.board[i][j] == my_color:
                    my_pieces += 1
                if board.board[i][j] == enemy_color:
                    opponent_pieces += 1

        return self.normalize(my_pieces,opponent_pieces)

    def game_is_finishing(self, board, color):
        flattened   = [val for sublist in board.board for val in sublist]
        spaces_left = filter(lambda x: x != color and x != board._opponent(color), flattened)
        return spaces_left < 20

    def mobility_factor(self,board,color):
        number_color = len(board.valid_moves(color))
        number_opponent = len(board.valid_moves(board._opponent(color)))
        return self.normalize(number_color, number_opponent)

    def heuristic_value(self, board, color):
        return self.porcentage_of_difference_of_pieces(board, color) \
                + self.mobility_factor(board,color) \
                + self.position_factor(board,color)

    def __init__(self, color):
        self.color = color

    def play(self, board):
        if self.game_is_finishing(board,self.color):
            depth = 4
        else:
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
