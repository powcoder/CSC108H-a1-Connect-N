https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
"""Main program for the Connect-N game.
"""

import random
import connect_n_functions as cnf


SYMBOLS = 'RB'  # The player symbols.
COMPUTER = 0  # The index in SYMBOLS of a player's character (for computer).
HUMAN = 1  # The index in SYMBOLS of a player's character (for human).

# The text to display when asking for a game board size.
GAME_BOARD_SIZE = 'game board size'

# The text to display when asking for a winning connect size.
CONNECT_SIZE = 'connect size'


def is_valid_response(response: str, min_value: int, max_value: int) -> bool:
    """Return True if and only if response contains the representation of
    an integer without a +/- sign that is between min_value and max_value,
    inclusive.

    >>> is_valid_response('4', 1, 9)
    True
    >>> is_valid_response('abc', 1, 3)
    False
    """

    return (response.isdigit() and
            cnf.between(int(response), min_value, max_value))


def get_valid_response(prompt_message: str, error_message: str,
                       min_value: int, max_value: int) -> int:
    """Return the user's response to prompt_message. Repeatedly prompt the
    user for input with prompt_message until the user enters a valid
    response. Display error_message for each invalid response entered
    by the user.

    A response is valid if it is a str representation of an integer,
    without a +/- sign, between min_value and max_value, inclusive.

    (No docstring example given since function depends on user input.)
    """

    response = input(prompt_message)
    while not is_valid_response(response, min_value, max_value):
        print(error_message)
        response = input(prompt_message)

    return int(response)


def get_size(which_size: str, max_size: int) -> int:
    """Return the valid game-board-size/connect-size entered by the
    user. Repeatedly prompt the user for which_size until the user
    enters a valid response. Display an error message for each invalid
    response entered by the user. The user's input is valid if it is a
    str representation of an integer, without a +/- sign, between 1
    and max_size, inclusive.

    Precondition: which_size is either GAME_BOARD_SIZE or CONNECT_SIZE.

    (No docstring example given since the function depends on user input.)
    """

    prompt_message = ('Enter desired ' + which_size + ' (an int between 1 and '
                      + str(max_size) + '): ')
    error_message = ('Your requested ' + which_size + ' is not valid. Try '
                     + 'again!')

    return get_valid_response(prompt_message, error_message, 1, max_size)


def get_valid_row_col(board_size: int) -> (int, int):
    """Return the valid (row, column) pair entered by the user. Repeatedly
    prompt the user for row and column until the user enters valid
    responses. Display an error message for each invalid response
    entered by the user. The user's input is valid if it is a str
    representation of an integer, without a +/- sign, between 1 and
    board_size.

    (No docstring example given since the function depends on user input.)
    """

    print('Enter row and column numbers between 1 and ' + str(board_size)
          + '.')
    error_message = 'Your suggested row number is not valid. Try again!'
    row = get_valid_response('Enter row number: ', error_message,
                             1, board_size)
    error_message = 'Your suggested col number is not valid. Try again!'
    col = get_valid_response('Enter col number: ', error_message,
                             1, board_size)
    return (row, col)


def is_occupied(row_index: int, col_index: int, game_board: str) -> bool:
    """Return True if and only if the cell with indices row_index and
    col_index in game_board does not contain the EMPTY cell character.

    Precondition: row_index and col_index are valid indices for a cell
                  in the game_board.

    >>> is_occupied(1, 1, 'BRB-')
    True
    >>> is_occupied(2, 2, 'BRB-')
    False
    """

    board_size = cnf.get_board_size(game_board)
    position = cnf.get_str_index(row_index, col_index, board_size)
    return game_board[position] != cnf.EMPTY


def get_empty_row_col(game_board: str) -> (int, int):
    """Return a pair of row and column indices, entered by the user, that
    are valid indices of a non-occupied cell in game_board.
    Repeatedly prompt the user for input, until the user enters valid
    row/col indices of a non-occupied cell. Display an error message
    for each invalid input.

    (No docstring example given since the function either depends on user
    input or randomly generated numbers.)
    """

    board_size = cnf.get_board_size(game_board)

    (row, col) = get_valid_row_col(board_size)
    while is_occupied(row, col, game_board):
        print('That spot is already taken! Try again.')
        (row, col) = get_valid_row_col(board_size)

    return (row, col)


def get_move(is_human_move: bool, game_board: str) -> (int, int):
    """Return a pair of row and column indices that are valid indices of a
    non-occupied cell in game_board.  If is_human_move is True,
    repeatedly prompt the user for input, until the user enters valid
    row/col indices of a non-occupied cell.  Display an error message
    for each invalid input. Otherwise, randomly generate a valid pair
    of a non-occupied cell's indices.

    (No docstring example given since the function either depends on user
    input or randomly generated numbers.)
    """

    if is_human_move:
        return get_empty_row_col(game_board)

    board_size = cnf.get_board_size(game_board)
    row = random.randint(1, board_size)
    col = random.randint(1, board_size)
    while is_occupied(row, col, game_board):
        row = random.randint(1, board_size)
        col = random.randint(1, board_size)
    return (row, col)


def format_game_board(game_board: str) -> str:
    """Return a string representation of game_board for printing.

    >>> expected = ("\\nThe Connect-N board:\\n\\n   1   2  \\n\\n" +
    ...             "1  B | R\\n  ---+---\\n2  B | -\\n")
    >>> format_game_board('BRB-') == expected
    True
    """

    formatted_board = "\nThe Connect-N board:\n\n"

    board_size = cnf.get_board_size(game_board)

    # Add in the column numbers.
    formatted_board += '  '
    for col in range(1, board_size + 1):
        formatted_board += ' ' + str(col) + '  '
    formatted_board += '\n\n'

    # Add in the row numbers, board contents, and grid markers.
    position = 0
    for row in range(1, board_size + 1):
        formatted_board += str(row) + ' '
        for col in range(1, board_size):
            formatted_board += ' ' + game_board[position] + ' |'
            position += 1
        formatted_board += ' ' + game_board[position] + '\n'
        position += 1
        if row < board_size:
            formatted_board += '  ' + '---+' * (board_size - 1) + '---\n'

    return formatted_board


def retrieve_line(game_board: str, row: int, col: int, direction: str) -> str:
    """Return a line of characters in game_board, starting at position
    (row, col), in the direction direction.

    Precondition: row and col specify a valid location of a cell in
                  game_board.
                  direction is one of DOWN, ACROSS, DOWN_LEFT, DOWN_RIGHT
                  when direction is DOWN_LEFT, location (row, col) is either
                   on the top row or the rightmost column of the game board
                  when direction is DOWN_RIGHT, location (row, col) is either
                   on the top row or the leftmost column of the game board

    >>> retrieve_line('-B--R--B-', 1, 2, 'down')
    'BRB'
    >>> retrieve_line('------BRB', 3, 1, 'across')
    'BRB'
    >>> retrieve_line('B---B---B', 1, 1, 'down_right')
    'BBB'
    >>> retrieve_line('-B---B---', 1, 2, 'down_right')
    'BB'
    >>> retrieve_line('--B------', 1, 3, 'down_right')
    'B'
    >>> retrieve_line('---B---R-', 2, 1, 'down_right')
    'BR'
    >>> retrieve_line('------B--', 3, 1, 'down_right')
    'B'
    >>> retrieve_line('B--------', 1, 1, 'down_left')
    'B'
    >>> retrieve_line('-B-R-----', 1, 2, 'down_left')
    'BR'
    >>> retrieve_line('--B-R-B--', 1, 3, 'down_left')
    'BRB'
    >>> retrieve_line('-----B-R-', 2, 3, 'down_left')
    'BR'
    >>> retrieve_line('--------B', 3, 3, 'down_left')
    'B'
    """

    board_size = cnf.get_board_size(game_board)
    first_index = cnf.get_str_index(row, col, board_size)
    increment = cnf.get_increment(direction, board_size)
    last_index = cnf.get_last_index(row, col, direction, board_size)
    return game_board[first_index:last_index + 1:increment]


def horizontal_win(game_board: str, winning_string: str) -> bool:
    """Return True if and only if winning_string appears in any row in
    game_board.

    >>> horizontal_win('BBB-R-R--', 'BBB')
    True
    >>> horizontal_win('BRB-BBRRR', 'RRR')
    True
    >>> horizontal_win('BRB-BBRRR', 'BBB')
    False
    """

    return check_win(game_board, winning_string,
                     range(cnf.get_board_size(game_board) + 1), range(1, 2),
                     cnf.ACROSS)


def vertical_win(game_board: str, winning_string: str) -> bool:
    """Return True if and only if winning_string appears in any column in
    game_board.

    >>> vertical_win('RBBR--R--', 'RRR')
    True
    >>> vertical_win('-R--R--R-', 'RRR')
    True
    >>> vertical_win('RBBR--R--', 'BRB')
    False
    """

    return check_win(game_board, winning_string,
                     range(1, 2), range(cnf.get_board_size(game_board) + 1),
                     cnf.DOWN)


def down_right_win(game_board: str, winning_string: int) -> bool:
    """Return True if and only if winning_string appears in any down_right
    diagonal in game_board.

    >>> down_right_win('RBBBR---R', 'RRR')
    True
    >>> down_right_win('-R---R---', 'RR')
    True
    >>> down_right_win('---R---R-', 'RR')
    True
    >>> down_right_win('-R--R--R-', 'RRR')
    False
    """

    board_size = cnf.get_board_size(game_board)

    return (check_win(game_board, winning_string,
                      range(1, 2), range(board_size + 1), cnf.DOWN_RIGHT) or
            check_win(game_board, winning_string,
                      range(board_size + 1), range(1, 2), cnf.DOWN_RIGHT))


def down_left_win(game_board: str, winning_string: int) -> bool:
    """Return True if and only if winning_string appears in any down_left
    diagonal in game_board.

    >>> down_left_win('--B-BRB-R', 'BBB')
    True
    >>> down_left_win('-----B-B-', 'BB')
    True
    >>> down_left_win('-B-B----B', 'BB')
    True
    >>> down_left_win('-R--R--R-', 'RRR')
    False
    """

    board_size = cnf.get_board_size(game_board)

    return (check_win(game_board, winning_string,
                      range(1, 2), range(board_size + 1), cnf.DOWN_LEFT) or
            check_win(game_board, winning_string,
                      range(board_size + 1), range(board_size, board_size + 1),
                      cnf.DOWN_LEFT))


def check_win(game_board: str, winning_string: str,
              row_range: range, col_range: range, direction: str) -> bool:
    """Return True if and only if winning_string appears in game_board
    starting at any of the locations specified by row_range and
    col_range, and going in direction direction.

    Precondition: row_range and col_range are valid ranges of values
                  for a cell location in game_board, and direction is
                  one of ACROSS, DOWN, DOWN_LEFT, or DOWN_RIGHT.

    >>> check_win('B-RBRRB-B', 'BBB', range(1, 2), range(3 + 1), 'down')
    True
    >>> check_win('--B-BRB-R', 'BBB', range(1, 2), range(3 + 1), 'down_left')
    True
    >>> check_win('--------B', 'BBB', range(3 + 1), range(1, 2), 'across')
    False
    """

    for row in row_range:
        for col in col_range:
            extract = retrieve_line(game_board, row, col, direction)
            if winning_string in extract:
                return True
    return False


def game_won(game_board: str, symbol: str, connect_size: int) -> bool:
    """Return True if and only if the player using symbol has won the game
    represented by game_board and connect_size.

    >>> game_won('BBB-R-R--', 'B', 3)
    True
    >>> game_won('BRBRBRRBR', 'B', 3)
    False
    """

    winning_string = symbol * connect_size

    return (horizontal_win(game_board, winning_string) or
            vertical_win(game_board, winning_string) or
            down_right_win(game_board, winning_string) or
            down_left_win(game_board, winning_string))


def play_connect_n() -> None:
    """Play a single game of Connect-N, with one player being the human user
    and the other player being this computer program.

    (No docstring example given since the function indirectly depends
    on either user input or randomly generated numbers.)

    """

    # Initialize the game setup.
    board_size = get_size(GAME_BOARD_SIZE, cnf.MAX_BOARD_SIZE)
    connect_size = get_size(CONNECT_SIZE, board_size)
    game_board = cnf.create_empty_board(board_size)

    print('You are using symbol ' + SYMBOLS[HUMAN] + ' and the computer '
          + 'program is using symbol ' + SYMBOLS[COMPUTER] + '.')
    print(format_game_board(game_board))

    # Play the game until a player wins or there is a draw.
    is_human_move = False
    have_a_winner = False
    while not have_a_winner and not cnf.game_board_full(game_board):

        is_human_move = not is_human_move
        (row, col) = get_move(is_human_move, game_board)

        if is_human_move:
            player_symbol = SYMBOLS[HUMAN]
            player = 'You'
        else:
            player_symbol = SYMBOLS[COMPUTER]
            player = 'The computer'

        print(player + ' chose row ' + str(row) + ' and column ' + str(col)
              + '.')

        game_board = cnf.make_move(player_symbol, row, col, game_board)

        if not is_human_move:
            print(format_game_board(game_board))

        have_a_winner = game_won(game_board, player_symbol, connect_size)

    finish_up(have_a_winner, is_human_move, game_board)


def finish_up(have_a_winner: bool, is_human_move: bool,
              game_board: str) -> None:
    """Display the results of the game of Connect-N with final state of
    the board game_board, announcing whether there is a winner (if and only if
    have_a_winner), and who won (based on whether is_human_move is True,
    indicating that the human won).
    """

    if have_a_winner:
        print('We have a winner!')
        if is_human_move:
            print(format_game_board(game_board))
            print('You beat the computer program! Congratulations!')
        else:
            print('The computer program won!')
            print('Re-think your strategy and try again.')
    else:
        print(format_game_board(game_board))
        print('The game has played to a draw.')
        print('Re-think your strategy and try again.')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    play_connect_n()
