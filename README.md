# ULTIMATE Battleships

![The deployed website](assets/images/responsive_site.png)
Battleships, also known simply as Battleship, is a classic two-player strategy game that blends deduction, tactics, and a touch of luck. Originating as a pencil-and-paper game during World War I, it has since evolved into a popular board game, digital adaptation, and mobile app enjoyed by players of all ages worldwide.

## Game Overview

In this Battleships, the player commands a fleet of ships strategically placed on a grid. The objective is to locate and "sink" the opponent’s fleet, in this case, the computer by guessing it's ships positions through a series of targeted strikes. The game involves strategic thinking as player must conceal his/her ships placement while trying to discover and destroy his/her opponent’s.

## Why should you play the battleship game?
Battleships is more than just a game-it's a test of strategy, anticipation, and patience. Its simplicity makes it accessible, while its depth keeps players coming back for more. Whether played on paper, a game board, or digitally, it remains an enduring favorite in family game nights and competitive play.

Are you ready to command your fleet and outmaneuver your opponent? Let the battle begin!

The deployed project live link is [HERE](https://portfolio-3-d66e66723f07.herokuapp.com/) - ***Use Ctrl (Cmd) and click to open in a new window.*** 

- [Introduction](#introduction)
- [Project](#project)
  - [Ultimate Battleships Game - User Goals](#Ultimate-Battleships-Game---User-Goals)
  - [Ultimate Battleships Game - Site Owner Goals](#Ultimate-Battleships-Game---Site-Owner-Goals)
- [Development](#development)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Resources](#resources)
- [Testing](#testing)
- [Future Updates](#future-updates)  
- [Validation](#validation)
- [Deployment](#deployment)
  - [Heroku](#heroku)
  - [Branching the GitHub Repository using GitHub Desktop and Visual Studio Code](#branching-the-github-repository-using-github-desktop-and-visual-studio-code)
- [Bugs](#bugs)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)
- [Updated Project in Response to the Assessment Result](#Updated-Project-in-Response-to-the-Assessment-Result)
- [How to run the project on Heroku](#How-to-run-the-project-on-Heroku)

## Introduction

Welcome to the Ultimate Battleships Game! This is a console-based implementation of the classic game of Battleship where a player competes against a computer opponent. The game involves placing ships on a grid and then taking turns to guess the location of each other's ships.

## Project 

## Ultimate Battleships Game - User Goals

### Entertainment and Engagement
- Enjoy a fun, strategic gameplay experience.
- Have an intuitive and seamless user interface.
- Experience a fair and balanced game.

### Competitive Play
- Challenge friends or random opponents the computr in this case.
- Improve skills through repeated play and strategizing.
- Track wins, losses, and rankings.

### Ease of Access
- Access the game easily on multiple platforms (desktop, mobile, or tablet).
- Play without needing extensive instructions or tutorials.

### Customization
- Personalize the game board, ships, and other visual elements.
- Select difficulty levels or specific rulesets.


## Ultimate Battleships Game - Site Owner Goals

### User Retention and Engagement
To ensure long-term user retention and engagement.

### Monetization
Monetizing the game effectively is essential for sustainability.

### Community Growth
Fostering a robust community will help drive traffic and promote user loyalty.

### Data Collection
Leveraging user data (with appropriate legal considerations) to improve the game experience.

### Brand Building
Building a strong brand is vital for attracting and retaining users.

### Scalability
Preparing for future growth is essential to accommodate more users.



## Development

Welcome to the Ultimate Battleships Game! This is a console-based implementation of the classic game of Battleship where a player competes against a computer opponent. The game involves placing ships on a grid and then taking turns to guess the location of each other's ships.

### Board Class

-   **Attributes:**

    -   `board_size`: Size of the board

    -   `num_ships`: Number of ships on the board

    -   `name`: Name of the player or "Computer"

    -   `type`: Type of board ("player" or "computer")

    -   `guesses`: List of tuples representing guessed coordinates

    -   `ships`: List of tuples representing ship coordinates

-   **Methods:**

    -   `__init__(self, board_size, num_ships, name, board_type)`: Initializes the board with the given size, number of ships, name, and type.

    -   `display(self, hide_ships=False)`: Displays the board. If `hide_ships` is True, ships are hidden.

    -   `process_guess(self, x, y)`: Processes a guess and returns whether it's a hit, miss, or repeat.

    -   `add_ship(self, x, y)`: Adds a ship to the board at the specified coordinates.

### Global Scores

-   **Dictionary:**

    -   `scores = {"computer": 0, "player": 0}`

### Helper Functions
----------------

-   `random_point(board_size)`: Returns a random integer between 0 and `board_size - 1`.

-   `valid_coordinates(x, y, board)`: Checks if coordinates are valid and not already occupied.

-   `populate_board(board)`: Places ships randomly on the board.

-   `populate_board_player(board)`: Allows the player to manually place ships on the board.

-   `get_player_guess(board)`: Gets the player's guess input.

-   `get_computer_guess(board)`: Generates a random guess for the computer.

-   `take_turn(board, guess_func)`: Handles a single turn for either player or computer.

-   `play_game(computer_board, player_board)`: Alternates turns between player and computer until the game ends.

-   `new_game()`: Initializes and starts a new game.

### Game Flow
---------

### Initialization

-   Input: Board size, number of ships, player name

-   Create `Board` instances for the computer and player

### Setup Phase

-   Player manually places ships

-   Computer places ships randomly

### Gameplay Phase

-   Alternate turns between player and computer

-   Handle guesses and process hits/misses

-   Update scores

-   Display updated boards and summary

### Endgame

-   Declare the winner based on remaining ships

-   Display final scores

### Relationships
-------------

-   `new_game()` creates `Board` objects and calls `populate_board` or `populate_board_player`.

-   `play_game()` uses helper functions like `get_player_guess`, `get_computer_guess`, and `take_turn`.
  

## Features

1. Manual placement of ships by player.
   
![manual placement](assets/images/ship_placement.png)

2. Random board generation for computer and player cannot see where the computer's ships are.
   
![Random board](assets/images/random_board.png)

3. Accepts user inputs and gives saummary of scores after each round
   
![Round score](assets/images/round_score.png)

4. Input validation for 
- Numbers out of board's range
- Check whether inputs are numbers
- Checks whether the same coordinates are given more than once
  
![Input validation](assets/images/input_validation.png)

## Technologies Used

The main technology used to create this program is Python

### Resources

- Visual Studio Code
- GitHub 
- Heroku


### Accessibility
- Keyboard-only interaction ensures the game is accessible for users with visual impairments when paired with screen readers.
- Clear and concise text-based instructions.


### Frameworks, Libraries & Programs Used
1. Python Standard Library
2. Heroku for deployment to the server.
3. PEP8 Python Validator for Python Code Validation.


## Testing

### 1\. **Testing Methodology**

#### **Unit Testing**

-   Core game functions were tested in isolation to ensure they work as intended.
-   Focus areas:
    -   Board initialization.
    -   Ship placement validation.
    -   Attack logic (hit, miss, repeat).
    -   Game-ending conditions.

#### **Integration Testing**

-   Verified that all components work seamlessly together in a complete game session.

#### **Manual Testing**

-   Simulated multiple game sessions to test user interactions and edge cases.

#### **Static Code Analysis**

-   Used linting tools to identify and fix formatting issues and coding standard violations.

* * * * *

### 2\. **Tools Used**

-   **Linting**: `flake8` and `black` for PEP 8 compliance and formatting.
-   **Manual Testing**: Command-line execution.

* * * * *

### 3\. **Test Cases**

#### **Unit Tests**

| Feature | Test Case Description | Result |
| --- | --- | --- |
| Board Initialization | Verify the board initializes with correct dimensions and empty cells. | ✅ Passed |
| Ship Placement | Ensure valid placement of ships and rejection of overlaps or out-of-bounds positions. | ✅ Passed |
| Attack Logic | Validate outcomes for hits, misses, and repeated coordinates. | ✅ Passed |
| Game End Condition | Confirm the game ends correctly when all ships are sunk. | ✅ Passed |

#### **Edge Cases**

| Scenario | Test Case Description | Result |
| --- | --- | --- |
| Invalid Input Handling | Reject non-numeric or improperly formatted inputs gracefully. | ✅ Passed |
| Boundary Conditions | Prevent out-of-bound attacks or placements. | ✅ Passed |

* * * * *

### 4\. **Static Code Analysis**

-   **Flake8 Results**:
    -   **Warnings**: Addressed all `E501: line too long` warnings.
    -   **Other Issues**: No other significant violations found.

* * * * *

### 5\. **Testing Results**

| Type of Test | Status |
| --- | --- |
| Unit Testing | ✅ Completed |
| Integration Testing | ✅ Completed |
| Manual Testing | ✅ Completed |
| Static Code Analysis | ✅ Completed |

* * * * *


## Future Updates

- Implementing online multiplayer features.
- Adding sound effects and graphical enhancements to improve the user interface.
- Expanding game mechanics, such as power-ups or special ship types.


## Validation
1. Syntax Validation
    Result: The code executes without syntax errors.
   
2. Linter Warnings/Errors (PEP 8 Validation)
   E501: Line Too Long:
    Lines exceed the recommended 79 characters. These have been flagged, and corrections have been applied by splitting lines appropriately.
   
3. Functional Validation
Result: The game logic functions as expected.
    Player Input:
        Validated correctly (e.g., invalid formats are rejected).
        Correct handling of edge cases (e.g., out-of-bounds coordinates).
   
4. Integration Validation
Result: The program runs end-to-end without crashes or critical errors:
    A player can complete a game session from start to finish.
    Errors are gracefully handled with appropriate messages to the user.



## Deployment

### Heroku

The Application has been deployed from GitHub to Heroku by following the steps:

1. Create or log in to your account at heroku.com
2. Create a new app, add a unique app name ( for example corri-construction-p3) and then choose your region
3. Click on create app
4. Go to "Settings"
5. Add required buildpacks (further dependencies). For this project, set it up so Python will be on top and Node.js on bottom
6. Go to "Deploy" and select "GitHub" in "Deployment method"
7. To connect Heroku app to your Github repository code enter your repository name, click 'Search' and then 'Connect' when it shows below.
8. Choose the branch you want to build your app from
9. If preferred, click on "Enable Automatic Deploys", which keeps the app up to date with your GitHub repository
10. Wait for the app to build. Once ready you will see the “App was successfully deployed” message and a 'View' button to take you to your deployed link.

### Branching the GitHub Repository using GitHub Desktop and Visual Studio Code
1. Go to the GitHub repository.
2. Click on the branch button in the left hand side under the repository name.
3. Give your branch a name.
4. Go to the CODE area on the right and select "Open with GitHub Desktop".
5. You will be asked if you want to clone the repository - say yes.
6. GitHub desktop will suggest what to do next - select Open code using Visual Studio Code.
   


## Bugs

The following bugs are tracked and handled, invalid input, out-of-bounds cooedinates, inccorect game end conditions, invalid ship placement, ship overlap, and board display formatting.


## Credits

### Code Used
- Random number generation and validation logic for ship placement were inspired by standard Python documentation.
- Code Institute Portfolio 3: Project Submission lesson  for using the sample code for this Ultimate Battleship game project.

### Content
- Game rules based on the classic Battleship board game from [wikipedia ](https://en.wikipedia.org/wiki/Battleship)

### Acknowledgments
- Special thanks to Code Institute for giving me the opportunity to learn as a full stack software developer.
- Code Institute tutor support for helping me to understsnd the Love Sandwiches sample project, which was the base for this project.
- My mentor Jubril Akolade for teaching me the assessment criteria and general guide and followup of my portfolio project.

### Updated Project in Response to the Assessment Result
- The Ultimate Battleships project code is modified in response to the Assessment requirements feedback given by the he Code Institute Assessment Team.

- **PEP 8 Compliance**: The code has been reviewed and passes through a linter with no significant issues, ensuring adherence to Python's coding standards.
- **Input Validation**: The game includes mechanisms to handle empty or invalid input data effectively, prompting users to provide valid responses.
- **Error Handling**: Exception handling is implemented throughout the code to optimize the user experience, ensuring that the game remains robust and user-friendly.

### How to run the project on Heroku
- open project-3-battleships-vscode
- click "more" on the right top corner
- then click "Run console" 
- then on the "heroku run" command line type "python3 run.py" press enter


