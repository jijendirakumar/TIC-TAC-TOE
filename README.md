# TIC-TAC-TOE
This is a simple command-line Tic-Tac-Toe game in Python where you (Player X) play against an unbeatable AI (Player O) powered by the Minimax algorithm with Alpha-Beta pruning.

🎯 Features
Playable in the terminal
AI uses the Minimax algorithm for optimal decision-making
Alpha-Beta pruning improves performance
Detects win, loss, or tie conditions
Input validation and user-friendly prompts

🧠 How It Works
The AI uses Minimax, a decision rule for minimizing the possible loss in a worst-case scenario.
Alpha-Beta pruning is used to cut off unnecessary branches in the decision tree, making the algorithm faster and more efficient.
The game is played on a standard 3x3 board.

🚀 How to Run
1. Clone the Repository
  git clone https://github.com/your-username/tic-tac-toe-ai.git
  cd tic-tac-toe-ai
2. Run the Game
  Make sure you have Python 3 installed.
  python tic_tac_toe.py

🕹️ Gameplay
You'll be prompted to enter your move as two integers (row and column), both between 0 and 2.
Example input: 1 2 places your move on row 1, column 2.
The AI will make its move right after yours.
The game ends when someone wins or the board is full (tie).

📂 File Structure
  bash
  Copy
  Edit
  tic_tac_toe_ai/
  ├── tic_tac_toe.py   # Main game logic and AI
  └── README.md        # Project description

✅ Sample Output
Tic-Tac-Toe! You are X, AI is O.
  _ _ _
0|     |
1|     |
2|     |

Enter row and column (0-2): 0 0

X _ _
_ _ _
_ _ _

AI's turn...
X _ _
_ O _
_ _ _

🤖 Technologies Used
    
Python 3
Minimax algorithm
Alpha-Beta pruning
