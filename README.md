# Othello Game with Minimax & Expectimax Algorithms

This project delivers a fully implemented version of the classic board game **Othello (Reversi)** using Python.  
It supports **two-player gameplay** and provides a challenging **AI opponent** powered by the **Minimax** and **Expectimax** algorithms.  

The game includes a graphical board built with `pygame`, smooth turn-based interaction, score tracking, and a proper winner declaration at the end.  

---

## 🚀 Features

- Complete implementation of Othello game rules  
- Interactive 8x8 graphical board using `pygame`  
- Two-player (human vs human) and human vs AI modes  
- **AI opponent** powered by **Minimax** and **Expectimax** algorithms  
- Score calculation and winner declaration  
- Clear game loop and well-structured codebase  

---

## 📂 Project Structure

- **`board.py`** → Handles the Othello board logic (valid moves, placing discs, scoring)  
- **`game.py`** → Manages the game loop, player turns, and declares the winner  
- **`player.py`** → Defines human and AI players (using Minimax or Expectimax)  
- **`minimax.py`** → Implements the Minimax algorithm for decision-making  
- **`expectimax.py`** → Implements the Expectimax algorithm for decision-making  
- **`main.py`** → Entry point to run the game  

---

## 🖥️ How to Run

1. Install dependencies:  
   ```bash
   pip install pygame
   ```

2. Run the game:  
   ```bash
   python main.py
   ```

The game will launch with a graphical board, ready for play.

---

## 🎮 Game Rules (Summary)

- Players alternate placing discs on the board.  
- A move must flank at least one of the opponent's discs horizontally, vertically, or diagonally.  
- Flanked discs are flipped to the current player's color.  
- The game ends when no valid moves remain or the board is full.  
- The player with the most discs wins.  

---

## 🧠 AI Implementation

The **AI agent** evaluates possible moves using:  

- **Minimax** → Considers both players’ best moves, simulating outcomes up to a certain depth.  
- **Expectimax** → Considers both optimal and probabilistic outcomes, making the AI more dynamic.  

Both approaches aim to maximize the AI’s advantage while reducing the opponent’s chances.  

---

## 🔑 Key Concepts in the Algorithms

- **Depth-limited search** → Prevents excessive computation by restricting the lookahead depth  
- **Board evaluation** → Assigns a score based on disc count and board control  
- **Decision-making** → AI selects the move leading to the most favorable evaluated state  

---
