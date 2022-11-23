https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
"""A simple checker for types of functions in connect_n_functions.py."""

from typing import Callable
import sys
sys.path.insert(0, 'pyta')
import python_ta
import connect_n_functions as cnf


def type_error_message(func_name: str, expected: str, got: str) -> str:
    """Return an error message for function func_name returning type got,
    where the correct return type is expected.
    """

    return ('{0} should return a {1}, but returned {2}' +
            '.').format(func_name, expected, got)


def check_function(func: Callable, args: list, ret_type: type) -> None:
    """Check that func called with arguments args returns a value of type
    ret_type. Display the progress and the result of the check.
    """

    print('Checking {0}...'.format(func.__name__))
    got = func(*args)
    assert isinstance(got, ret_type), \
        type_error_message(func.__name__, ret_type.__name__, type(got))
    print('  check complete')


print('==================== Start: checking coding style ===================')

python_ta.check_all('connect_n_functions.py', config='pyta/a1_pyta.txt')

print('=================== End: checking coding style ====================\n')


print('== Start: checking whether initial values of constants are modified ==')

# Get the initial values of the constants
CONSTS_BEFORE = [cnf.EMPTY, cnf.DOWN, cnf.ACROSS, cnf.DOWN_LEFT,
                 cnf.DOWN_RIGHT, cnf.MAX_BOARD_SIZE]

print('Check whether the constants are unchanged from the starter code.')

assert CONSTS_BEFORE == ['-', 'down', 'across', 'down_left', 'down_right', 9], \
    ('You have modified the value of some constant(s). Edit your code so that'
     + ' the values of constants are the same as in the starter code.')

print('  check complete')

print('== End: checking whether initial values of constants are modified ==\n')


print('============ Start: checking parameter and return types ============')

check_function(cnf.between, [1, 0, 2], bool)
check_function(cnf.game_board_full, ['BRRRBRRBB'], bool)
check_function(cnf.get_board_size, ['BRBRBRB--'], int)
check_function(cnf.create_empty_board, [3], str)
check_function(cnf.get_str_index, [2, 3, 3], int)
check_function(cnf.make_move, ['B', 2, 1, '----'], str)
check_function(cnf.get_increment, ['down_right', 5], int)
check_function(cnf.get_last_index, [2, 1, 'down_right', 5], int)

print('============= End: checking parameter and return types =============\n')

print('======= Start: checking whether functions modify constants =======')

# Get the final values of the constants
CONSTS_AFTER = [cnf.EMPTY, cnf.DOWN, cnf.ACROSS, cnf.DOWN_LEFT,
                cnf.DOWN_RIGHT, cnf.MAX_BOARD_SIZE]

# Check whether the constants are unchanged.
print('Checking whether functions modify constants...')
assert CONSTS_BEFORE == CONSTS_AFTER, \
    ('Your function(s) modified the value of some constant(s). Edit your' +
     '\ncode so that the values of constants are unchanged by your functions.')
print('  check complete')

print('=========== End: checking whether functions modify constants ====')
