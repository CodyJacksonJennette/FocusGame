# Name: Cody Jennette
# Date: 11/25/2020
# Description: Program that simulates the board game "Focus"


class FocusGame:
    """Simulation of the board game "Focus." Lets two players make moves while keeping track of reserves, captures,
    status of the board, and determines winner"""

    def __init__(self, player_1_info, player_2_info):
        """Initializes current state of the game with board information and the information about both players (their
        names and piece colors, stored as tuples). Initializes the game board as one full board parameter, represented
        as a list of lists. Each list within the list has its own index which is what will be used to update it according
        to players' moves. Each player's list of reserved pieces and captured pieces are also initialized to blank lists"""

        self._player_1_name = self.get_player_one_name(player_1_info)
        self._player_1_piece = self.get_player_one_piece(player_1_info)
        self._player_2_name = self.get_player_two_name(player_2_info)
        self._player_2_piece = self.get_player_two_piece(player_2_info)
        self._full_board = [[self._player_1_piece], [self._player_1_piece], [self._player_2_piece],
                            [self._player_2_piece], [self._player_1_piece], [self._player_1_piece],
                            [self._player_2_piece], [self._player_2_piece], [self._player_1_piece],
                            [self._player_1_piece], [self._player_2_piece], [self._player_2_piece],
                            [self._player_1_piece], [self._player_1_piece], [self._player_2_piece],
                            [self._player_2_piece], [self._player_1_piece], [self._player_1_piece],
                            [self._player_2_piece], [self._player_2_piece], [self._player_1_piece],
                            [self._player_1_piece], [self._player_2_piece], [self._player_2_piece],
                            [self._player_1_piece], [self._player_1_piece], [self._player_2_piece],
                            [self._player_2_piece], [self._player_1_piece], [self._player_1_piece],
                            [self._player_2_piece], [self._player_2_piece], [self._player_1_piece],
                            [self._player_1_piece], [self._player_2_piece], [self._player_2_piece]]
        self._p1_reserves = []
        self._p1_captures = []
        self._p2_reserves = []
        self._p2_captures = []

    def get_player_one_name(self, player_1_info):
        """Uses nested function to break apart its parameter: Tuple containing player one's name and piece color.
        Extracts player one's name from it and returns it"""

        def extract_player_one_name(name_1, piece_1):
            """Nested function that breaks apart the player_1_info tuple and saves the 'name' part of the tuple"""
            name = name_1
            piece = piece_1
            return name

        return extract_player_one_name(*player_1_info)

    def get_player_one_piece(self, player_1_info):
        """Uses nested function to break apart its parameter: Tuple containing player one's name and piece color.
        Extracts player one's piece color from it and returns it"""

        def extract_player_one_piece(name_1, piece_1):
            """Nested function that breaks apart the player_1_info tuple and saves the 'piece' part of the tuple"""
            name = name_1
            piece = piece_1
            return piece

        return extract_player_one_piece(*player_1_info)

    def get_player_two_name(self, player_2_info):
        """Uses nested function to break apart its parameter: Tuple containing player two's name and piece color.
        Extracts player two's name from it and returns it"""

        def extract_player_two_name(name_2, piece_2):
            """Nested function that breaks apart the player_2_info tuple and saves the 'name' part of the tuple"""
            name = name_2
            piece = piece_2
            return name

        return extract_player_two_name(*player_2_info)

    def get_player_two_piece(self, player_2_info):
        """Uses nested function to break apart its parameter: Tuple containing player two's name and piece color.
        Extracts player two's piece color from it and returns it"""

        def extract_player_two_piece(name_2, piece_2):
            """Nested function that breaks apart the player_2_info tuple and saves the 'piece' part of the tuple"""
            name = name_2
            piece = piece_2
            return piece

        return extract_player_two_piece(*player_2_info)

    def move_piece(self, player_name, move_start, move_end, num_of_pieces, move_counter=0):
        """Executes when a player makes a move in the game. Checks for certain base cases when a move is not viable
        (such as if players move out of turn or the move start/end coordinates are invalid), and returns appropriate
        message. Takes player's name, the move's starting and end positions, along with the number of pieces being moved
        as parameters. Move counter parameter is a default argument to keep track of whose turn it is; if it is an even
        number then the next player making a move will be player 1. If it is an odd number, then the next player making
        a move will be player 2. Calls the 'player_moves' method of the Player class as its return, which further checks
        the validity of the move and then calls the Board class to update the game board and player reserves/captures"""

        if move_counter % 2 != 0 and player_name == self._player_1_name:
            return False
        elif move_counter % 2 == 0 and player_name == self._player_2_name:
            return False
        elif move_start < (0, 0) or move_start > (5, 5):
            return False
        elif move_end < (0, 0) or move_end > (5, 5):
            return False
        else:
            move_counter += 1

            # move_counter variable is placed here because it only increments if a move is valid. If the move is not
            # valid, then it is still that same player's turn.

            if player_name == self._player_1_name:
                next_p1_move = Player(self._player_1_name, self._player_1_piece, self._player_2_name, self._player_2_piece, move_start, move_end, num_of_pieces, self._full_board, self._p1_reserves, self._p1_captures, self._p2_reserves, self._p2_captures)
                move_start_x = next_p1_move.move_start_x_coordinate(move_start)
                move_start_y = next_p1_move.move_start_y_coordinate(move_start)
                move_end_x = next_p1_move.move_end_x_coordinate(move_end)
                move_end_y = next_p1_move.move_end_y_coordinate(move_end)
                start_index = next_p1_move.start_coord_to_int(move_start_x, move_start_y)
                end_index = next_p1_move.end_coord_to_int(move_end_x, move_end_y)
                return next_p1_move.player_moves(self._player_1_name, move_start_x, move_start_y, move_end_x, move_end_y, start_index, end_index)
            elif player_name == self._player_2_name:
                next_p2_move = Player(self._player_1_name, self._player_1_piece, self._player_2_name, self._player_2_piece, move_start, move_end, num_of_pieces, self._full_board, self._p1_reserves, self._p1_captures, self._p2_reserves, self._p2_captures)
                move_start_x = next_p2_move.move_start_x_coordinate(move_start)
                move_start_y = next_p2_move.move_start_y_coordinate(move_start)
                move_end_x = next_p2_move.move_end_x_coordinate(move_end)
                move_end_y = next_p2_move.move_end_y_coordinate(move_end)
                start_index = next_p2_move.start_coord_to_int(move_start_x, move_start_y)
                end_index = next_p2_move.end_coord_to_int(move_end_x, move_end_y)
                return next_p2_move.player_moves(self._player_2_name, move_start_x, move_start_y, move_end_x, move_end_y, start_index, end_index)

    def show_pieces(self, board_space):
        """Returns a list containing the pieces that occupy a particular spot on the board (its parameter) during the
        game. Uses a nested function to break apart the board_space tuple and save its individual x and y coordinates,
        later used in a mathematical formula to calculate the board space's index in the full board"""

        # Multiple pieces at a given space on the board will be represented in list format. The piece at the very
        # bottom of a space's stack of pieces will be the left-most (0th) item in the list, and going to the right
        # in the list will represent each piece that follows after it. If a space does not have any pieces on it, the
        # function returns a blank list.

        def find_coordinates(x_coord, y_coord):
            """Extracts the given coordinates from the 'board_space' parameter in the show_pieces method to locate
            exactly where on the board that the method is searching, and returns the appropriate list of pieces
            located at that space"""

            board_space_x = x_coord
            board_space_y = y_coord

            space_index = board_space_x * 6 + board_space_y

            # This mathematical formula accurately represents the exact index of the full_board list that is being
            # referred to by the function. Since there are 6 spaces per row, the x-coordinate (the particular "row" of
            # the board) gets multiplied by 6, and then the y-coordinate (how many more spaces you have to go
            # horizontally) gets added onto the product. The result is the exact index of that particular space on the
            # board.

            return self._full_board[space_index]

        return find_coordinates(*board_space)

    def show_reserve(self, player_name):
        """Returns a list containing the current number of pieces in reserve for a particular player. If there are
        no pieces in the list, it will return 0. Function returns the get_p1_reserve or get_p2_reserve method of the
        Board class, depending on the given player_name parameter. The Board class is where the player reserve and
        capture information is stored"""

        if player_name == self._player_1_name:
            return Board.get_p1_reserve(self)
        elif player_name == self._player_2_name:
            return Board.get_p2_reserve(self)

    def show_captured(self, player_name):
        """Returns a list containing the current number of pieces captured by a particular player. If there are
        no pieces in the list, it will return 0. Function returns the get_p1_captures or get_p2_captures method of the
        Board class, depending on the given player_name parameter. The Board class is where the player reserve and
        capture information is stored"""

        if player_name == self._player_1_name:
            return Board.get_p1_captures(self)
        elif player_name == self._player_2_name:
            return Board.get_p2_captures(self)

    def reserved_move(self, player_name, move_location):
        """Responsible for making a move using a piece from a given player's current reserve when called. Places the
        piece from the player's reserve on the given 'move_location' parameter, and then removes the single piece
        from the player's current list of available reserve pieces"""

        if self._player_1_name == player_name and len(self._p1_reserves) == 0:
            return "No pieces in reserve."
        elif self._player_2_name == player_name and len(self._p2_reserves) == 0:
            return "No pieces in reserve."
        elif self._player_1_name == player_name and len(self._p1_reserves) > 0:
            return Board.reserve_update(self, self._p1_reserves, move_location)
        elif self._player_2_name == player_name and len(self._p2_reserves) > 0:
            return Board.reserve_update(self, self._p2_reserves, move_location)


class Player:
    """Class that is called upon whenever a player makes a move. Parameters are 'carried over' from the FocusGame
    class to use in recording each move; the player's name making the move, where the move starts and ends, along
    with the current status of the game board, as stored by the FocusGame class"""

    def __init__(self, p1_name, p1_piece, p2_name, p2_piece, move_start, move_end, num_of_pieces, current_board,
                 p1_reserves, p1_captures, p2_reserves, p2_captures):
        """Initializes the instance of the class with each player's name and piece, a given move's start and ending
        positions, the number of pieces being moved, the status of the current board, and each player's list of reserves
        and captures. Many of these parameters are 'carried over' from he FocusGame class, in order to keep each instance
        of each class consistent and updated correctly"""

        self._p1_name = p1_name
        self._p1_piece = p1_piece
        self._p2_name = p2_name
        self._p2_piece = p2_piece
        self._move_start = move_start
        self._move_end = move_end
        self._num_of_pieces = num_of_pieces
        self._current_board = current_board
        self._p1_reserves = p1_reserves
        self._p1_captures = p1_captures
        self._p2_reserves = p2_reserves
        self._p2_captures = p2_captures

    def move_start_x_coordinate(self, move_start):
        """Uses nested function to break apart its parameter: Tuple containing the coordinates of the move's starting
        position. Extracts the x coordinate from the tuple and returns it"""

        def extract_start_x_coordinate(x, y):
            """Nested function that breaks apart the move_start tuple, saving the x-coordinate of the move's starting
            position"""
            x_start = x
            y_start = y
            return x_start

        return extract_start_x_coordinate(*move_start)

    def move_start_y_coordinate(self, move_start):
        """Uses nested function to break apart its parameter: Tuple containing the coordinates of the move's starting
        position. Extracts the y coordinate from the tuple and returns it"""

        def extract_start_x_coordinate(x, y):
            """Nested function that breaks apart the move_start tuple, saving the y-coordinate of the move's starting
            position"""
            x_start = x
            y_start = y
            return y_start

        return extract_start_x_coordinate(*move_start)

    def move_end_x_coordinate(self, move_end):
        """Uses nested function to break apart its parameter: Tuple containing the coordinates of the move's ending
        position. Extracts the x coordinate from the tuple and returns it"""

        def extract_end_x_coordinate(x, y):
            """Nested function that breaks apart the move_end tuple, saving the x-coordinate of the move's ending
            position"""
            x_end = x
            y_end = y
            return x_end

        return extract_end_x_coordinate(*move_end)

    def move_end_y_coordinate(self, move_end):
        """Uses nested function to break apart its parameter: Tuple containing the coordinates of the move's ending
        position. Extracts the x coordinate from the tuple and returns it"""

        def extract_end_y_coordinate(x, y):
            """Nested function that breaks apart the move_end tuple, saving the y-coordinate of the move's ending
            position"""
            x_end = x
            y_end = y
            return y_end

        return extract_end_y_coordinate(*move_end)

    def start_coord_to_int(self, x_start, y_start):
        """Method responsible for converting a given pair of coordinates corresponding to the move's starting position
        to an integer. This integer represents the index of the 'full_board' list that will get updated later"""

        # This function is a duplicate of the 'find_coordinates' method in the FocusGame class. But instead of returning
        # the list of pieces at a current spot on the board, it returns a value representing the index of a given
        # move's starting position. The same mathematical formula in 'find_coordinates' is ued to calculate the index.

        board_start_index = x_start * 6 + y_start
        return board_start_index

    def end_coord_to_int(self, x_end, y_end):
        """Method responsible for converting a given pair of coordinates corresponding to the move's end position to an
        integer. This integer represents the index of the 'full_board' list that will get updated later"""

        # This funciton is a duplicate of the 'find_coordinates' method in the FocusGame class. But instead of returning
        # the list of pieces at a current spot on the board, it returns a value representing the index of a given
        # move's ending position. The same mathematical formula in 'find_coordinates' is used to calculate the index.

        board_end_index = x_end * 6 + y_end
        return board_end_index

    def player_moves(self, player_moving, move_start_x_coordinate, move_start_y_coordinate, move_end_x_coordinate,
                     move_end_y_coordinate, move_start_index, move_end_index):
        """Method that is called by the FocusGame class when a move is ready to be made. Checks to see if a move is
        further valid by verifying that pieces are not moving diagonally, then calls an instance of the Board class to
        update the current status of the board, along with each player's list of reserves and captures. The player that
        is moving, the move's starting and ending coordinates, and the start/end indices are all used as parameters. The
        coordinates are used to check the validity of the move, and the indices are used to update the current status
        of the board"""

        if move_start_x_coordinate != move_end_x_coordinate and move_start_y_coordinate != move_end_y_coordinate:
            return False
        else:
            if move_start_x_coordinate > move_end_x_coordinate or move_start_x_coordinate < move_end_x_coordinate:
                h_board_update = Board(self._p1_name, self._p1_piece, self._p2_name, self._p2_piece, self._current_board, move_start_index, move_end_index, self._num_of_pieces, self._p1_reserves, self._p1_captures, self._p2_reserves, self._p2_captures)
                if player_moving == self._p1_name:
                    return h_board_update.board_update(self._p1_name, self._current_board, self._num_of_pieces, move_start_index, move_end_index)
                elif player_moving == self._p2_name:
                    return h_board_update.board_update(self._p2_name, self._current_board, self._num_of_pieces, move_start_index, move_end_index)
            elif move_start_y_coordinate > move_end_y_coordinate or move_start_y_coordinate < move_end_y_coordinate:
                v_board_update = Board(self._p1_name, self._p1_piece, self._p2_name, self._p2_piece, self._current_board, move_start_index, move_end_index, self._num_of_pieces, self._p1_reserves, self._p1_captures, self._p2_reserves, self._p2_captures)
                if player_moving == self._p1_name:
                    return v_board_update.board_update(self._p1_name, self._current_board, self._num_of_pieces, move_start_index, move_end_index)
                elif player_moving == self._p2_name:
                    return v_board_update.board_update(self._p2_name, self._current_board, self._num_of_pieces, move_start_index, move_end_index)


class Board:
    """Class that is responsible for keeping track of the current status of the game board, along with each player's
    list of pieces in reserve and pieces captured"""

    def __init__(self, p1_name, p1_piece, p2_name, p2_piece, current_board, move_start_index, move_end_index,
                 num_of_pieces, p1_reserves, p1_captures, p2_reserves, p2_captures):
        """Initializes the instance of the class with each player's name and piece, the current status of the board, the
        indices for a given move's start and ending positions, the number of pieces being moved, and the lists containing
        each player's reserves and captures. Many parameters are carried over from the FocusGame and Player classes to
        keep each instance of the classes consistent with one another and updated correctly"""

        self._p1_name = p1_name
        self._p1_piece = p1_piece
        self._p2_name = p2_name
        self._p2_piece = p2_piece
        self._current_board = current_board
        self._move_start_index = move_start_index
        self._move_end_index = move_end_index
        self._num_of_pieces = num_of_pieces
        self._p1_reserves = p1_reserves
        self._p1_captures = p1_captures
        self._p2_reserves = p2_reserves
        self._p2_captures = p2_captures

    def get_p1_reserve(self):
        """Returns player 1's list of pieces currently in reserve when called by the FocusGame class"""

        return len(self._p1_reserves)

    def get_p1_captures(self):
        """Returns player 1's list of pieces captured when called by the FocusGame class"""

        return len(self._p1_captures)

    def get_p2_reserve(self):
        """Returns player 2's list of pieces currently in reserve when called by the FocusGame class"""

        return len(self._p2_reserves)

    def get_p2_captures(self):
        """Returns player 2's list of opponent pieces captured when called by the FocusGame class"""

        return len(self._p2_captures)

    def pieces_moved_list(self, num_of_pieces, move_start_index):
        """Method that is responsible for tracking exactly which pieces are being moved, based on the num_of_pieces
        parameter. Extracts that particular slice of the list located at the move's starting index on the board and
        returns it"""

        if len(self._current_board[move_start_index]) < num_of_pieces:
            return False
            # The number of pieces at the move's starting index are less than the total number of pieces on that space,
            # rendering the move invalid

        the_pieces_moved = self._current_board[move_start_index][0:num_of_pieces]
        return the_pieces_moved

    def board_update(self, player_that_moved, current_board, num_of_pieces, move_start_index, move_end_index):
        """Method responsible for updating the current status of the board after a given player moves provided by
        information from the 'player_moves' method in the Player class. The name of the player that moved, the current
        status of the board, number of pieces being moved, as well as the indices for the move's start and ending
        positions are taken as parameters. Method also responsible for updating each player's list of reserves and
        captures accordingly, if the number of pieces on a particular space (or end index) become greater than 5.
        Method returns a call to the 'winner_check' method, which will see if a move allows a player to be declared
        a winner after it is completed"""

        self._current_board = current_board
        moved_pieces = self.pieces_moved_list(num_of_pieces, move_start_index)
        for item in moved_pieces:
            current_board[move_start_index].remove(item)
            current_board[move_end_index].append(item)
        while len(current_board[move_end_index]) > 5:
            if player_that_moved == self._p1_name:
                if current_board[move_end_index][0] == self._p1_piece:
                    self._p1_reserves.append(current_board[move_end_index][0])
                    del self._current_board[move_end_index][0]
                elif current_board[move_end_index][0] == self._p2_piece:
                    self._p1_captures.append(current_board[move_end_index][0])
                    del self._current_board[move_end_index][0]
            elif player_that_moved == self._p2_name:
                if current_board[move_end_index][0] == self._p2_piece:
                    self._p2_reserves.append(current_board[move_end_index][0])
                    del self._current_board[move_end_index][0]
                elif current_board[move_end_index][0] == self._p1_piece:
                    self._p2_captures.append(current_board[move_end_index][0])
                    del self._current_board[move_end_index][0]
        return self.winner_check(self._p1_captures, self._p2_captures)

    def reserve_update(self, reserves_list, move_end):
        """Method called whenever a player is making a move with a piece in their list of reserves. Called upon by the
        FocusGame class. The player's list of reserves and the move's end position are taken as parameters. In order to
        calculate the correct index, separate variables are created by calling the Player class's methods to break apart
        the move_end tuple, and then the 'end_coord_to_int' method to calculate the correct ending index of the move.
        Method also responsible for updating each player's list of reserves and captures accordingly, if the number of
        pieces on a particular space (or end index) become greater than 5. Method returns a call to the 'winner_check'
        method, which will see if a move allows a player to be declared a winner after it is completed"""

        move_end_x = Player.move_end_x_coordinate(self, move_end)
        move_end_y = Player.move_end_y_coordinate(self, move_end)
        move_end_index = Player.end_coord_to_int(self, move_end_x, move_end_y)

        if self._p1_reserves == reserves_list:
            used_p1_piece = self._p1_reserves[0]
            self._p1_reserves.remove(used_p1_piece)
            self._current_board[move_end_index].append(used_p1_piece)
            while len(self._current_board[move_end_index]) > 5:
                if self._current_board[move_end_index][0] == self._p1_piece:
                    self._p1_reserves.append(self._current_board[move_end_index][0])
                    del self._current_board[move_end_index][0]
                elif self._current_board[move_end_index][0] == self._p2_piece:
                    self._p1_captures.append(self._current_board[move_end_index][0])
                    del self._current_board[move_end_index][0]
        elif self._p2_reserves == reserves_list:
            used_p2_piece = self._p2_reserves[0]
            self._p2_reserves.remove(used_p2_piece)
            self._current_board[move_end_index].append(used_p2_piece)
            while len(self._current_board[move_end_index]) > 5:
                if self._current_board[move_end_index][0] == self._p2_piece:
                    self._p2_reserves.append(self._current_board[move_end_index][0])
                    del self._current_board[move_end_index][0]
                elif self._current_board[move_end_index][0] == self._p1_piece:
                    self._p2_captures.append(self._current_board[move_end_index][0])
                    del self._current_board[move_end_index][0]
        return self.winner_check(self._p1_captures, self._p2_captures)

    def winner_check(self, p1_captures, p2_captures):
        """Method called at the end of each successful move. Each player's list of captured pieces are taken as
        parameters, and both lists are checked at the end of each move. The goal of the game, according to the rules, is
        to have 6 of the opponent's pieces captured. Therefore, if the list length of a player's captures is greater
        than or equal to 6, that player is declared the winner. Method returns appropriate message if there is a winner.
        If not, returns a "successfully moved" message"""

        if len(p1_captures) >= 6:
            return self._p1_name + " wins"
        elif len(p2_captures) >= 6:
            return self._p2_name + " wins"
        else:
            return "successfully moved"


game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
print(game.move_piece('PlayerA', (0, 0), (0, 1), 1))  # Returns message "successfully moved"
print(game.show_pieces((0, 1)))  # Returns ['R','R']
print(game.show_captured('PlayerA'))  # Returns 0
print(game.reserved_move('PlayerA', (0, 0)))  # Returns message "No pieces in reserve"
print(game.show_reserve('PlayerA'))  # Returns 0