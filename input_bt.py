import string
import time
import random
import winsound
import battleship


def convert_input_to_coordinates(user_input):
    """Convert input e.g. A1 to indexes of 2 dimension board."""
    row = user_input[0]
    col = int(user_input[1])
    row = string.ascii_uppercase.index(row)
    col -= 1
    return row, col


def get_move(board, is_setting_ships=True, additional_message=""):
    """Get move from user e.g. A1, if input is not correct ask again."""
    board_size = len(board)
    row_headers = list(map(lambda x: x + 1, list(range(board_size))))
    row_headers = [str(element) for element in row_headers]
    col_headers = string.ascii_uppercase[:board_size]

    user_input = input(f"Provide coordinates (e.g. A1){additional_message}: ").upper()
    winsound.Beep(500, 200)
    if is_setting_ships:
        while len(user_input) < 2 or\
                user_input[0] not in col_headers or \
                user_input[1] not in row_headers or \
                not is_empty_field(board, user_input):
            user_input = input(f"Incorrect coordinates. Provide coordinates (e.g. A1){additional_message}: ").upper()
            winsound.Beep(500, 200)
    else:
        while len(user_input) < 2 or\
                user_input[0] not in col_headers or \
                user_input[1] not in row_headers:
            user_input = input(f"Incorrect coordinates. Provide coordinates (e.g. A1){additional_message}: ").upper()
            winsound.Beep(500, 200)
    return convert_input_to_coordinates(user_input)


def ai_shoot(visible_board):
    """Gets move from AI."""
    board_size = len(visible_board)
    row_headers = list(map(lambda x: str(x + 1), list(range(board_size))))
    col_headers = string.ascii_uppercase[:board_size]
    board_fields = {"columns": col_headers, "rows": row_headers}

    is_part_of_ship = False
    h_x = -1
    h_y = -1
    i = 0
    while i < board_size:
        j = 0
        while j < board_size:
            if visible_board[i][j] == 'H':
                is_part_of_ship = True
                h_x = i
                h_y = j
                break
            j += 1
        if is_part_of_ship:
            break
        i += 1

    if not is_part_of_ship:
        col_guess = random.choice(board_fields["columns"])
        row_guess = random.choice(board_fields["rows"])
        field_guess = col_guess + str(row_guess)
        result = convert_input_to_coordinates(field_guess)
        while visible_board[result[0]][result[1]] != '0':
            print("Already in! Let's try again!")
            col_guess = random.choice(board_fields["columns"])
            row_guess = random.choice(board_fields["rows"])
            field_guess = col_guess + str(row_guess)
            result = convert_input_to_coordinates(field_guess)
    else:
        try:
            if h_x - 1 == -1:
                raise IndexError
            if visible_board[h_x - 1][h_y] == '0':
                result = (h_x - 1, h_y)
        except IndexError:
            pass
        try:
            if visible_board[h_x + 1][h_y] == '0':
                result = (h_x + 1, h_y)
        except IndexError:
            pass
        try:
            if h_y == -1:
                raise IndexError
            if visible_board[h_x][h_y - 1] == '0':
                result = (h_x, h_y - 1)
        except IndexError:
            pass
        try:
            if visible_board[h_x][h_y + 1] == '0':
                result = (h_x, h_y + 1)
        except IndexError:
            pass

    time.sleep(1.0)
    winsound.Beep(500, 200)
    return result


def get_ai_board(size):
    board = battleship.init_board(size)
    ai_place_ship(board, 1)
    battleship.make_edges(board)
    ai_place_ship(board, 2)
    battleship.make_edges(board)
    return board


def display_select_ship_menu(current_player):
    print(current_player)


def is_empty_field(board, user_input):
    row, col = convert_input_to_coordinates(user_input)
    if board[row][col] == '0':
        return True
    return False


def ai_get_first_coordinate(size=5):
    list_of_number_row = list(map(str, list(range(size))))
    list_of_number_col = list(map(str, list(range(size))))

    row = random.choice(list_of_number_row)
    col = random.choice(list_of_number_col)

    return int(row), int(col)


def ai_place_ship(board, ship_len=1):
    assignment_bool = True
    loop_counter = 1
    len_board = len(board)

    if ship_len == 1:
        while assignment_bool:
            row, col = ai_get_first_coordinate(size=len_board)
            if board[row][col] == "0":
                board[row][col] = "X"
                assignment_bool = False
    elif ship_len == 2:
        while assignment_bool:
            row, col = ai_get_first_coordinate(size=len_board)
            if board[row][col] == "0":
                board[row][col] = "X"
                assignment_bool = False
        while 1 >= loop_counter:

            try:
                loop_counter += 1
                list_of_case = [1, 2, 3, 4]
                case = random.choice(list_of_case)
                if case == 1:
                    if board[row + 1][col] == "0":
                        board[row + 1][col] = "X"
                    else:
                        loop_counter -= 1
                elif case == 2:
                    if row - 1 == -1:
                        raise IndexError
                    if board[row - 1][col] == "0":
                        board[row - 1][col] = "X"
                    else:
                        loop_counter -= 1
                elif case == 3:
                    if board[row][col + 1] == "0":
                        board[row][col + 1] = "X"
                    else:
                        loop_counter -= 1
                elif case == 4:
                    if col - 1 == -1:
                        raise IndexError
                    if board[row][col - 1] == "0":
                        board[row][col - 1] = "X"
                    else:
                        loop_counter -= 1
            except IndexError:
                loop_counter -= 1
        # elif ship_len>2:

    return board

