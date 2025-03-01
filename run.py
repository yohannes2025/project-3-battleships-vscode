from random import randint
import re

# Global variable to keep track of scores
scores = {"computer": 0, "player": 0}


class Board:
    """Handles game logic, including ships, guesses, and board display."""

    def __init__(self, board_size, num_ships, name, board_type):
        self.board_size = board_size
        self.board = [
            ["." for _ in range(board_size)]
            for _ in range(board_size)
        ]

        self.num_ships = num_ships
        self.name = name
        self.type = board_type  # "player" or "computer"
        self.guesses = []  # List to track guesses
        self.ships = []  # List to track ships

    def display(self, hide_ships=False):
        """Print the board. Optionally hide ships for the computer's board."""
        for row in self.board:
            row_display = [
                "." if hide_ships and cell == "@" else cell for cell in row
            ]
            print(" ".join(row_display))
        print()

    def process_guess(self, x, y):
        """Process a guess and return whether it's a hit, miss, or repeat."""
        if (x, y) in self.guesses:
            print("You cannot guess the same coordinates more than once")
            return "Repeat"

        self.guesses.append((x, y))

        if (x, y) in self.ships:
            self.board[x][y] = "X"  # Mark as hit
            return "Hit"

        self.board[x][y] = "O"  # Mark as miss
        return "Miss"

    def add_ship(self, x, y):
        """Add a ship to the board at the specified coordinates."""
        if len(self.ships) >= self.num_ships:
            raise ValueError("Cannot add more ships!")
        if (x, y) in self.ships:
            raise ValueError("Ship already placed at this location!")

        self.ships.append((x, y))
        if self.type == "player":  # Display ships on player's board
            self.board[x][y] = "@"


# Helper functions
def random_point(board_size):
    """Return a random integer between 0 and board_size-1."""
    return randint(0, board_size - 1)


def valid_coordinates(x, y, board):
    """Check if coordinates are valid and not already occupied."""
    return (
        0 <= x < board.board_size and
        0 <= y < board.board_size and
        (x, y) not in board.ships
    )


def populate_board(board):
    """Place ships randomly on the board."""
    while len(board.ships) < board.num_ships:
        x, y = random_point(board.board_size), random_point(board.board_size)
        if valid_coordinates(x, y, board):
            board.add_ship(x, y)


def populate_board_player(board):
    """Allow the player to manually place ships on the board."""
    print(f"{board.name}, it's time to place your ships!")
    while len(board.ships) < board.num_ships:
        while True:
            try:
                x, y = map(int, input(
                    f"Enter coordinates for ship {len(board.ships) + 1} "
                    "as 'row column' (e.g., 1 2): "
                ).split())

                if valid_coordinates(x, y, board):
                    board.add_ship(x, y)
                    print(f"Ship placed at ({x}, {y}).")
                    board.display()
                    break
                else:
                    print(
                        "Invalid coordinates or location already occupied. Try again.")

            except ValueError:
                print("Invalid input. Please enter two numbers separated by a space.")


def get_player_guess(board):
    """Get player's guess input."""
    while True:
        try:
            x, y = map(int, input(
                "Enter your guess as 'row column' (e.g., 1 2): ").split())
            if 0 <= x < board.board_size and 0 <= y < board.board_size:
                return x, y
            print(
                f"Invalid input. Please enter a number between 0 and {board.board_size - 1} for both row and column.")
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")


def get_computer_guess(board):
    """Generate a random guess for the computer."""
    while True:
        x, y = random_point(board.board_size), random_point(board.board_size)
        if (x, y) not in board.guesses:
            return x, y


def take_turn(board, guess_func):
    """Handle a single turn for either player or computer."""
    x, y = guess_func(board)
    return board.process_guess(x, y)


def play_game(computer_board, player_board):
    """Alternate turns between player and computer until the game ends."""
    round_num = 0  # Track round number

    while player_board.ships and computer_board.ships:
        round_num += 1
        print(f"\nRound {round_num}")
        print("\nYour Board (with ships):")
        player_board.display()
        print("Computer's Board:")
        computer_board.display(hide_ships=True)

        # Player's turn
        print(f"\n{player_board.name}, it's your turn!")
        while True:
            player_x, player_y = get_player_guess(computer_board)
            player_result = take_turn(
                computer_board, lambda b: (player_x, player_y))

            # Allow the game to proceed if the guess is valid
            if player_result != "Repeat":
                break
            print("Please try again with new coordinates.")

        if player_result == "Hit":
            computer_board.ships.remove((player_x, player_y))
            scores["player"] += 1  # Increment player score for a hit

        # Computer's turn
        computer_x, computer_y = get_computer_guess(player_board)
        computer_result = take_turn(
            player_board, lambda b: (computer_x, computer_y))

        if computer_result == "Hit":
            player_board.ships.remove((computer_x, computer_y))
            scores["computer"] += 1  # Increment computer score for a hit

        # Round Summary
        print("\nSummary:")
        print(f"Player guessed: ({player_x}, {player_y}) - {player_result}")
        print(
            f"Computer guessed: ({computer_x}, {computer_y}) - {computer_result}")

        print("_" * 35)

        # Scores after each round
        print(f"After round {round_num}, the scores are:")
        print(f"{player_board.name}: {scores['player']} \t"
              f"Computer: {scores['computer']}")
        print("_" * 35)

        # Check for end of game
        if not computer_board.ships:
            print("You sank all the computer's ships! You win!")
            break

        if not player_board.ships:
            print("The computer sank all your ships! You lose!")
            break

        # Prompt to continue or quit
        choice = input(
            "Enter any key to continue or 'n' to quit: ").strip().lower()
        if choice == 'n':
            print("You chose to quit the game. Thank you for playing!")
            return  # Exit the function, ending the game

    # Final scores
    print("\nFinal Scores:")
    print(f"{player_board.name}: {scores['player']}, "
          f"Computer: {scores['computer']}")


def get_valid_input(prompt, min_value, max_value):
    """Get a valid integer input from the user within a specified range."""
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:  # Check for empty input
                print("Input cannot be empty. Please try again.")
                continue

            value = int(user_input)
            if min_value <= value <= max_value:
                return value
            else:
                print(
                    f"Input must be between {min_value} and {max_value}. Please try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
        except EOFError:  # Catch EOFError
            print("No input was provided. Exiting the game.")
            exit(0)  # Exit the program or handle it as needed


def is_valid_name(name):
    """Check if the player's name starts with an alphabet and contains only letters and numbers."""
    if not name or not re.match(r"^[A-Za-z][A-Za-z0-9]*$", name):
        return False
    # Changed from '>= 15' to '>' to ensure length is strictly less than or equal to 15
    if len(name) < 1 or len(name) > 15:
        return False
    return True



def new_game():
    """Initialize and start a new game."""
    board_size = get_valid_input("Enter board size (5-10): ", 5, 10)
    num_ships = get_valid_input(
        "Enter the number of ships (1 to board size - 1): ", 1, board_size - 1)

    # Reset scores for a new game
    scores["computer"] = 0
    scores["player"] = 0

    print("_" * 35)
    print()
    print("Welcome to ULTIMATE BATTLESHIPS!!")
    print(f"Board Size: {board_size}. Number of ships: {num_ships}")
    print("Top left corner is row: 0, col: 0")
    print("_" * 35)

    # Validate player name
    while True:
        player_name = input("Please enter your name: ").strip()
        if is_valid_name(player_name):
            break
        print("Invalid name! Name must start with an alphabet, have no special characters, "
              "and be between 1 and 14 characters long. Please try again.")

    computer_board = Board(board_size, num_ships, "Computer", "computer")
    player_board = Board(board_size, num_ships, player_name, "player")

    # Players manually places their ships
    populate_board_player(player_board)

    # Computer ships are placed randomly
    populate_board(computer_board)
    play_game(computer_board, player_board)


# Run the game
if __name__ == "__main__":
    new_game()
