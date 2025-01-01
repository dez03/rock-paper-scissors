# Rock Paper Scissors

A simple **Rock Paper Scissors** game implemented in Python, where you play against a bot. The game is error-proof and allows you to play multiple rounds until you choose to stop.

---

## How It Works

1. **Gameplay**:
   - You type your choice: `rock`, `paper`, or `scissors`.
   - The bot randomly picks one of the three options.
   - The winner is determined based on standard Rock Paper Scissors rules:
     - **Rock beats Scissors**
     - **Paper beats Rock**
     - **Scissors beats Paper**
   - If your choice matches the bot's choice, it's a tie.

2. **Stop the Game**:
   - To exit the game at any time, type `stop`.

3. **Input Validation**:
   - If you enter anything other than `rock`, `paper`, `scissors`, or `stop`, the game prompts you to enter a valid choice and restarts the input loop.

---

## Features

- **Error Handling**:
  - Ensures the player enters valid input.
  - Keeps asking until a valid choice is provided.

- **Continuous Play**:
  - The game keeps running until the player types `stop`.

- **Dynamic Bot Interaction**:
  - The bot randomly selects its move each round.

- **User-Friendly**:
  - Provides clear feedback and instructions for every step.

---

## How to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/rock-paper-scissors.git
   cd rock-paper-scissors