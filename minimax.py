from board import Board
from utils import raiseNotDefined

def minimax(board, depth, maximizing_player, player_color, use_pruning=False, alpha=-float('inf'), beta=float('inf')):
    """
    Implements the Minimax algorithm to determine the best move for a player in an Othello game.

    Args:
        board (Board): The current game board, representing the current state of the game.
        depth (int): The remaining depth to search in the game tree, indicating how many moves ahead to simulate.
        maximizing_player (bool): A boolean indicating whether the current player is the maximizing player.
                                  If True, the player aims to maximize the score; otherwise, they aim to minimize it.
        player_color (str): The color of the current player ('B' for black, 'W' for white), used to determine moves.
        use_pruning (bool): Optional. Whether to use alpha-beta pruning to optimize the search by cutting off branches.
        alpha (float): The alpha value for pruning, representing the best score achievable by the maximizing player.
        beta (float): The beta value for pruning, representing the best score achievable by the minimizing player.

    Returns:
        tuple: A tuple containing the best move (row, col) and its evaluation score (int).
               If no valid moves are available, returns (None, evaluation score), where evaluation score is the board's
               evaluated score for the player.
    """
    
    if depth == 0 or board.is_full():
        return None, evaluate_board(board, player_color)

    
    valid_moves = board.get_valid_moves(player_color)
    
    if not valid_moves:
        return None, evaluate_board(board, player_color)

    best_move = None
    if maximizing_player:
        max_eval = -float('inf')
        for move in valid_moves:
            
            new_board = copy_board(board)
            new_board.place_disc(move[0], move[1], player_color)

            
            _, eval_score = minimax(new_board, depth - 1, False, player_color, use_pruning, alpha, beta)
            
            
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move
            
            
            if use_pruning:
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
        return best_move, max_eval
    else:
        min_eval = float('inf')
        opponent_color = 'W' if player_color == 'B' else 'B'
        for move in valid_moves:
            
            new_board = copy_board(board)
            new_board.place_disc(move[0], move[1], opponent_color)

            
            _, eval_score = minimax(new_board, depth - 1, True, player_color, use_pruning, alpha, beta)
            
            
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move
            
          
            if use_pruning:
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
        return best_move, min_eval

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
    
    
    if player_color == 'W':
        return W_score - B_score
    else:
        return B_score - W_score

def copy_board(board):
    """
    Creates a deep copy of the current board to simulate future moves without altering the original.

    Args:
        board (Board): The current game board to be copied.

    Returns:
        Board: A new Board object with the same state as the original, allowing the minimax algorithm to simulate
               moves on separate instances of the board without affecting the actual game state.
    """
    
    new_board = Board(board.size)
    
    
    new_board.board = [row[:] for row in board.board]
    
    return new_board
