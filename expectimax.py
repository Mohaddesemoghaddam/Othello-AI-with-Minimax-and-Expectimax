from board import Board
from utils import raiseNotDefined
import random

def expectimax(board, depth, maximizing_player, player_color):
    """
    Perform the Expectimax algorithm to evaluate and choose the optimal move in a two-player game.

    Expectimax is a variation of the minimax algorithm used in games of chance or imperfect information,
    where instead of choosing the best or worst move, it computes the expected value of a move based on
    possible outcomes.

    Parameters:
    -----------
    board : Board
        The current state of the game board. It should support methods such as `is_full`, `get_valid_moves`,
        and `place_disc`.
    depth : int
        The remaining depth to search. When the depth reaches 0, the algorithm stops searching further moves.
    maximizing_player : bool
        A flag to indicate whether the current node is for the maximizing player (True) or the opponent (False).
    player_color : str
        The color ('B' for black or 'W' for white) representing the player who is maximizing their score.

    Returns:
    --------
    best_move : tuple or None
        The best move for the maximizing player in the form (row, col). None is returned when calculating
        the expected value for the opponent's move.
    evaluation : float
        The evaluation score of the board from the perspective of the player using the `evaluate_board` function.

    Notes:
    ------
    - The function recursively explores possible moves down to the specified depth and evaluates the board using
      the `evaluate_board` function.
    - For the maximizing player, it selects the move that maximizes the evaluation score.
    - For the opponent, it calculates the expected value based on all valid moves.
    - The algorithm returns once the depth reaches 0 or if the board is full, in which case it evaluates the current
      board state.
    """
    
    if depth == 0 or board.is_full():
        return None, evaluate_board(board, player_color)

    valid_moves = board.get_valid_moves(player_color)
    
    
    if not valid_moves:
        return None, evaluate_board(board, player_color)

    if maximizing_player:
        max_eval = -float('inf')
        best_move = None
        for move in valid_moves:
            new_board = copy_board(board)
            new_board.place_disc(move[0], move[1], player_color)
            _, eval_score = expectimax(new_board, depth - 1, False, player_color)
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move
        return best_move, max_eval
    else:
        
        opponent_color = 'W' if player_color == 'B' else 'B'
        total_eval = 0
        for move in valid_moves:
            new_board = copy_board(board)
            new_board.place_disc(move[0], move[1], opponent_color)
            _, eval_score = expectimax(new_board, depth - 1, True, player_color)
            total_eval += eval_score
        expected_value = total_eval / len(valid_moves)
        return None, expected_value

def evaluate_board(board, player_color):
    """
    Evaluates the current board state for a given player by comparing the scores.

    Args:
        board (Board): The current game board, representing the current state of the game.
        player_color (str): The color of the player to evaluate the score for ('B' for black, 'W' for white).

    Returns:
        int: The difference between the player's score and the opponent's score.
             A positive value favors the player, indicating a board state advantageous to them, and a negative value
             favors the opponent, indicating a board state advantageous to the opponent.
    """
    B_score, W_score = board.get_score()
    return W_score - B_score if player_color == 'W' else B_score - W_score

def copy_board(board):
    """
    Creates a deep copy of the current board to simulate future moves without altering the original.

    Args:
        board (Board): The current game board to be copied.

    Returns:
        Board: A new Board object with the same state as the original, allowing the Expectimax algorithm to simulate
               moves on separate instances of the board without affecting the actual game state.
    """
    new_board = Board(board.size)
    new_board.board = [row[:] for row in board.board]
    return new_board
