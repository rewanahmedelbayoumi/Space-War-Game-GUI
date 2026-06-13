# Space War Game GUI

A space-themed interactive game built using Python, where players control spacecraft to collect objects and earn points in a dynamic environment.

---

## Overview

Space War Game is a GUI-based application that combines gameplay mechanics with Object-Oriented Programming concepts. Players navigate spacecraft to collect balls and special gift boxes while competing for the highest score.

Created on: 17 May 2025

The project demonstrates:
- Game development fundamentals
- GUI design using Tkinter
- Real-time interaction using Turtle graphics
- Object-Oriented Programming concepts

---

## Game Features

### Gameplay
- Control a spacecraft with smooth movement mechanics
- Collect balls to gain points
- Special items (gift boxes) provide bonus points
- Real-time score updates
- Screen wrapping movement system

### Game Modes
- Single Player mode
- Multiplayer mode (2 players)

### Controls

#### Player 1
- Arrow Up: Accelerate
- Arrow Down: Decelerate
- Arrow Left / Right: Rotate

#### Player 2 (Multiplayer)
- W: Accelerate
- S: Decelerate
- A / D: Rotate

---

## GUI Features

- Main menu with game settings
- Color customization for spacecraft and balls
- Interactive buttons and controls
- Score display for each player
- Clean game interface with black space background

---

## OOP Concepts Used

- Inheritance (GameObject base class)
- Encapsulation (private attributes in classes)
- Polymorphism (shared interface with different behaviors)
- Method overriding (custom implementations in child classes)

---

## Tech Stack

| Component     | Technology |
|--------------|-----------|
| Language     | Python |
| Graphics     | Turtle |
| GUI          | Tkinter |
| Concepts     | OOP |

---

## Project Structure


Space-War-Game/
│
├── main.py
├── game_objects.py
├── assets/
├── README.md


---

## Installation & Setup

```bash
git clone https://github.com/rewanahmedelbayoumi/Space-War-Game-GUI.git
cd Space-War-Game-GUI
python main.py
How to Play
Launch the game
Choose spacecraft and ball colors
Select game mode
Start playing
Collect items and score points
Game Mechanics
Balls respawn randomly after being collected
Some balls turn into special gift boxes
Gift boxes give bonus points
Collision detection is handled dynamically
Game runs with continuous update loop
Future Improvements
Sound effects and background music
Power-ups and abilities
Levels and difficulty system
Improved graphics engine
Online multiplayer
