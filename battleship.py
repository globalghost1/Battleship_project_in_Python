import Output
import input_bt
import os
import winsound
from colorama import *
from enums import Players, Modes


def make_edges(board):
    """Add safe area around ships, to protect against placing ships too close."""
    temp_board = board
    x = 0
    for row in temp_board:
        y = 0
        for element in row:
            if element == 'X':
                try:
                    if x - 1 == -1:
                        raise IndexError
                    if temp_board[x - 1][y] == "0":
                        temp_board[x - 1][y] = "E"
                except IndexError:
                    pass
                try:
                    if temp_board[x + 1][y] == "0":
                        temp_board[x + 1][y] = "E"
                except IndexError:
                    pass
                try:
                    if y - 1 == -1:
                        raise IndexError
                    if temp_board[x][y - 1] == "0":
                        temp_board[x][y - 1] = "E"
                except IndexError:
                    pass
                try:
                    if temp_board[x][y + 1] == "0":
                        temp_board[x][y + 1] = "E"
                except IndexError:
                    pass
                try:
                    if x - 1 == -1 or y - 1 == -1:
                        raise IndexError
                    if temp_board[x - 1][y - 1] == "0":
                        temp_board[x - 1][y - 1] = "E"
                except IndexError:
                    pass
                try:
                    if x - 1 == -1:
                        raise IndexError
                    if temp_board[x - 1][y + 1] == "0":
                        temp_board[x - 1][y + 1] = "E"
                except IndexError:
                    pass
                try:
                    if temp_board[x + 1][y + 1] == "0":
                        temp_board[x + 1][y + 1] = "E"
                except IndexError:
                    pass
                try:
                    if y - 1 == -1:
                        raise IndexError
                    if temp_board[x + 1][y - 1] == "0":
                        temp_board[x + 1][y - 1] = "E"
                except IndexError:
                    pass
            y += 1
        x += 1
    return temp_board


def get_board_size():
    """Function in which player defines the size of the grid. It also checks input to be digit."""
    os.system("cls || clear1")
    size = input("Please enter number of columns in the board: \n")
    while not size.isdigit() or int(size) < 5 or int(size) > 9:
        size = input("Wrong value, please try again! Provide 5 - 9: ")
    return int(size)


def place_ship(board, current_player, ship_len=1):
    """Place the ship, with ship size."""
    part_of_ship = 0
    while ship_len > part_of_ship:
        Output.display_set_ships_playground(board, current_player)
        row, col = input_bt.get_move(board, additional_message=f" (Ship size: {ship_len})")
        part_of_ship += 1
        while not is_next(board, row, col, part_of_ship):
            row, col = input_bt.get_move(board, additional_message=f" (Ship size: {ship_len})")
        board[row][col] = 'X'
    return board


def is_next(board, x, y, part_of_ship, another_mart_to_check=''):
    """Check if next part of ship is close of previous part."""
    len_board = len(board) - 1
    len_ship_to_place = part_of_ship - 1
    communicate = "Place the ship in a straight line!"
    if another_mart_to_check != '':
        ship_mark = another_mart_to_check
    else:
        ship_mark = "X"
    if part_of_ship == 1:
        return True
    elif x == 0 and y == 0:
        if board[x + len_ship_to_place][y] == ship_mark and board[x + 1][y] == ship_mark:
            return True
        elif board[x][y + len_ship_to_place] == ship_mark and board[x][y + 1] == ship_mark:
            return True
        else:
            print(communicate)
            return False
    elif x == len_board and y == 0:
        if board[x - len_ship_to_place][y] == ship_mark and board[x - 1][y] == ship_mark:
            return True
        elif board[x][y + len_ship_to_place] == ship_mark and board[x][y + 1] == ship_mark:
            return True
        else:
            print(communicate)
            return False
    elif x == 0 and y == len_board:
        if board[x + len_ship_to_place][y] == ship_mark and board[x + 1][y] == ship_mark:
            return True
        elif board[x][y - len_ship_to_place] == ship_mark and board[x][y - 1] == ship_mark:
            return True
        else:
            print(communicate)
            return False
    elif x == len_board and y == len_board:
        if board[x - len_ship_to_place][y] == ship_mark and board[x - 1][y] == ship_mark:
            return True
        elif board[x][y - len_ship_to_place] == ship_mark and board[x][y - 1] == ship_mark:
            return True
        else:
            print(communicate)
            return False
    elif x == 0:
        if board[x + len_ship_to_place][y] == ship_mark and board[x + 1][y] == ship_mark:
            return True
        elif board[x][y - len_ship_to_place] == ship_mark and board[x][y - 1] == ship_mark:
            return True
        elif board[x][y + len_ship_to_place] == ship_mark and board[x][y + 1] == ship_mark:
            return True
        else:
            print(communicate)
            return False
    elif y == 0:
        if board[x - len_ship_to_place][y] == ship_mark and board[x - 1][y] == ship_mark:
            return True
        elif board[x + len_ship_to_place][y] == ship_mark and board[x + 1][y] == ship_mark:
            return True
        elif board[x][y + len_ship_to_place] == ship_mark and board[x][y + 1] == ship_mark:
            return True
        else:
            print(communicate)
            return False
    elif x == len_board:
        if board[x - len_ship_to_place][y] == ship_mark and board[x - 1][y] == ship_mark:
            return True
        elif board[x][y - len_ship_to_place] == ship_mark and board[x][y - 1] == ship_mark:
            return True
        elif board[x][y + len_ship_to_place] == ship_mark and board[x][y + 1] == ship_mark:
            return True
        else:
            print(communicate)
            return False
    elif y == len_board:
        if board[x - len_ship_to_place][y] == ship_mark and board[x - 1][y] == ship_mark:
            return True
        elif board[x + len_ship_to_place][y] == ship_mark and board[x + 1][y] == ship_mark:
            return True
        elif board[x][y - len_ship_to_place] == ship_mark and board[x][y - 1] == ship_mark:
            return True
        else:
            print(communicate)
            return False
    else:
        if part_of_ship == 1:
            return True
        elif board[x - len_ship_to_place][y] == ship_mark and board[x - 1][y] == ship_mark:
            return True
        elif board[x + len_ship_to_place][y] == ship_mark and board[x + 1][y] == ship_mark:
            return True
        elif board[x][y - len_ship_to_place] == ship_mark and board[x][y - 1] == ship_mark:
            return True
        elif board[x][y + len_ship_to_place] == ship_mark and board[x][y + 1] == ship_mark:
            return True
        else:
            print(communicate)
            return False


def main_menu(mode, board_size):
    """Handle the menu."""
    Output.display_menu(mode, board_size)
    user_input = input("Your pick: ")
    winsound.Beep(500, 200)
    choices = ['1', '2', '3', '4']
    while user_input not in choices:
        user_input = input('Incorrect value. Your pick: ')
        winsound.Beep(500, 200)

    if user_input == '1':
        game(mode, board_size)
    elif user_input == '2':
        Output.display_mode_menu(mode)
        mode_menu(mode, board_size)
    elif user_input == '3':
        board_size = get_board_size()
        main_menu(mode, board_size)
    elif user_input == '4':
        print()
        print("Good bye! See you next time.")
        input("Press enter to continue...")


def mode_menu(mode, board_size):
    """Handle the mode menu."""
    Output.display_mode_menu(mode)
    user_input = input("Your pick: ").lower()
    winsound.Beep(500, 200)
    choices = ['1', '2', 'back']
    while user_input not in choices:
        user_input = input('Incorrect value. Your pick: ').lower()
        winsound.Beep(500, 200)
    if user_input == '1':
        mode = Modes.HUMAN_HUMAN
        main_menu(mode, board_size)
    elif user_input == '2':
        mode = Modes.HUMAN_AI
        main_menu(mode, board_size)
    elif user_input == 'back':
        Output.display_menu(mode, board_size)
        main_menu(mode, board_size)


def init_board(size=5):
    """Create board for playground."""
    board = []
    row = []
    while len(row) < size:
        row.append("0")
    while len(board) < size:
        copy_row = row.copy()
        board.append(copy_row)
    return board


def player_input_ships(board, current_player, amount_of_ships=2):
    """Place a specific number of ship."""
    n = 1
    temp_board = board
    while n <= amount_of_ships:
        temp_board = place_ship(board, current_player, n)
        make_edges(temp_board)
        Output.display_set_ships_playground(temp_board, current_player)
        n += 1
    return temp_board


def enter_ships(player, board_size=5, ship_amount=2):
    """Function initialize board object for the provided player and asks for the location of the ships on the grid"""
    os.system("cls || clear")
    player_board = init_board(board_size)
    player_board = player_input_ships(player_board, player, ship_amount)
    input("Press enter to continue...")
    winsound.Beep(500, 200)
    return player_board


def mark_move(row, col, visible_board, hidden_board):
    """Provide move in opponent board."""
    if hidden_board[row][col] == "0" or hidden_board[row][col] == 'E':
        visible_board[row][col] = "M"
    elif hidden_board[row][col] == 'X' and \
            is_next(hidden_board, row, col, 2) and \
            not is_next(visible_board, row, col, 2, 'H'):
        visible_board[row][col] = 'H'
    elif hidden_board[row][col] == "X":
        visible_board[row][col] = "S"

    i = 0
    while i < len(visible_board):
        j = 0
        while j < len(visible_board):
            if visible_board[i][j] == 'H' and is_next(visible_board, i, j, 2, 'S'):
                visible_board[i][j] = 'S'
            j += 1
        i += 1

    return hidden_board


def all_ship_sunk(player, boards_hidden_ship, boards_visible):
    """Return True if ships are stunk."""
    i = 0
    while i < len(boards_hidden_ship[player]):
        j = 0
        while j < len(boards_hidden_ship[player]):
            if boards_hidden_ship[player][i][j] == "X":
                if boards_visible[player][i][j] != "S":
                    return False
            j += 1
        i += 1
    return True


def get_ships_amount(board):
    ship_amount = 0
    for row in board:
        for field in row:
            if field == 'X':
                ship_amount += 1
    return ship_amount


def game(mode, board_size):
    """Game logic. """
    board_p1 = enter_ships(Players.Player1, board_size=board_size)

    board_p1_hidden_ships = init_board(board_size)
    board_p2_hidden_ships = init_board(board_size)

    if mode == Modes.HUMAN_HUMAN:
        board_p2 = enter_ships(Players.Player2, board_size=board_size)

        hidden_boards = {Players.Player1: board_p1, Players.Player2: board_p2}
        visible_boards = {Players.Player1: board_p1_hidden_ships, Players.Player2: board_p2_hidden_ships}
    else:
        board_p2 = input_bt.get_ai_board(board_size)

        hidden_boards = {Players.Player1: board_p1, Players.AI: board_p2}
        visible_boards = {Players.Player1: board_p1_hidden_ships, Players.AI: board_p2_hidden_ships}

    players = list(hidden_boards.keys())

    current_player = list(hidden_boards.keys())[0]
    opponent = list(hidden_boards.keys())[1]

    while not all_ship_sunk(current_player, hidden_boards, visible_boards):
        Output.display_playground(board_p1_hidden_ships, board_p2_hidden_ships, players, current_player)
        if current_player == Players.AI:
            row, col = input_bt.ai_shoot(visible_boards[opponent])
        else:
            row, col = input_bt.get_move(hidden_boards[opponent], is_setting_ships=False)
        mark_move(row, col, visible_boards[opponent], hidden_boards[opponent])

        current_player, opponent = opponent, current_player

    Output.display_playground(board_p1_hidden_ships, board_p2_hidden_ships, players, current_player)

    if all_ship_sunk(Players.Player1, hidden_boards, visible_boards):
        winner = Players.Player2 if mode == Modes.HUMAN_HUMAN else Players.AI
    else:
        winner = Players.Player1
    winner = str(winner).split(".")[1]

    print(Fore.GREEN + f"\n{winner} won!" + Fore.RESET)
    winsound.Beep(1000, 500)
    input("Press enter to come back to main menu...")
    winsound.Beep(500, 200)
    main_menu(mode, board_size)


if __name__ == "__main__":
    board_size = 5
    current_mode = Modes.HUMAN_HUMAN
    main_menu(current_mode, board_size)
