"""Module for checking the readiness of the game board for playing a puzzle

Github: https://github.com/mykytaishchenko/ucu_lab_1_2
"""


def check_horizontal(board):
    """Checks numbers for uniqueness in each row.

    Return True if number in a row are unique, False otherwise.

    >>> check_horizontal(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", \
    " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    """
    for line in board:
        for char in line:
            if char != " " and char != "*" and line.count(char) > 1:
                return False
    return True


def check_vertical(board):
    """Checks numbers for uniqueness in each column.

    Return True if number in a column are unique, False otherwise.

    >>> check_vertical(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", \
    " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    """
    inverted_board = [''.join([line[char] for line in board]) for char in range(len(board[0]))]
    return check_horizontal(inverted_board)


def generate_color_line(board, line):
    """Collect all numbers in one color into a string.

    >>> generate_color_line(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", \
    " 6  83  *", "3   1  **", "  8  2***", "  2  ****"], 4)
    ' 9 5   31'
    """
    color_line = board[len(board[0]) - 1 - line][line:]
    for line_index in range(len(board[0])-line-1):
        color_line += board[line_index][line]
    return color_line


def check_color(line):
    """Checks numbers for uniqueness in color.

    Return True if number in a color are unique, False otherwise.

    >>> check_color('0123')
    True
    """
    for char in line:
        if char != " " and char != "*" and line.count(char) > 1:
            return False
    return True


def check_colors(board):
    """Checks numbers for uniqueness in each color.

    Return True if number in a color are unique, False otherwise.

    >>> check_colors(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", \
    " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    """
    for color in range(5):
        color_line = generate_color_line(board, color)
        if not check_color(color_line):
            return False
    return True


def validate_board(board):
    """Checks the board for readiness.

    Return True if the board is ready, False otherwise.

    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", \
    " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    """
    if not check_horizontal(board) or not check_vertical(board) or not check_colors(board):
        return False
    return True
