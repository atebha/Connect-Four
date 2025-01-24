class ConnectFour:
    def __init__(self):
        # Initialize a 6x7 board with all cells set to 0 (empty)
        self.board = [[0 for _ in range(7)] for _ in range(6)]

    def __str__(self):
        # Create a string representation of the board for easy viewing
        return "\n".join([" ".join(map(str, row)) for row in self.board])

    def drop_piece(self, column, player):
        """
        Drops a piece for a player into the specified column.
        :param column: Column index (0-based) to drop the piece into
        :param player: Player number (1 or 2)
        :return: True if the piece was successfully dropped, False otherwise
        """
        if column < 0 or column >= 7:
            print("Invalid column. Please choose a column between 0 and 6.")
            return False
        
        for row in reversed(self.board):
            if row[column] == 0:  # Find the first empty cell in the column
                row[column] = player
                return True
        
        print("Column is full. Choose a different column.")
        return False

# Example usage
game = ConnectFour()
print("Initial Board:")
print(game)

# Drop pieces into the board
game.drop_piece(3, 1)  # Player 1 drops a piece into column 3
game.drop_piece(3, 2)  # Player 2 drops a piece into column 3
game.drop_piece(3, 1)  # Player 1 drops another piece into column 3

print("\nBoard After Moves:")
print(game)
