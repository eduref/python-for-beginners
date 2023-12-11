# Game - Snake

Now, it is your time to show off, what you have learned so far, by implementing the popular game "Snake".

## Basic Concept

1. **Player Control:** The player controls a long snake, which moves around the playing area.
2. **Objective:** The primary objective is to eat items (usually depicted as fruits or dots) that appear at random positions. Each time the snake eats an item, it grows longer.
3. **Challenge:** The game becomes more challenging as the snake grows because the player must avoid the snake running into the screen boundaries or into itself.
4. **Game Over:** The game ends when the snake collides with the screen boundary or itself.

## Project Structure

```
snake_game/
│
├── src/
│   ├── __init__.py
│   └── game_logic.py
│
└── play.py
```

## Getting Started

### Importing from Packages

The from ``snake_game.src.game_logic import SnakeGame`` line in ``play.py`` imports the ``SnakeGame`` class from our ``game_logic.py`` file within the ``snake_game/src`` directory. This structure allows for clean organization of game logic separate from the game execution script.

### Understanding ``__name__=="_main__"``

This Python idiom is used in ``play.py`` to ensure that the game starts only when the script is executed directly (not when imported as a module). When play.py is run, it checks if ``__name__`` is set to ``"__main__"`` and, if so, executes the game.

## Running the Game

To play the game, navigate to the directory containing play.py and execute the following command in your Python environment:

```python
python play.py
```

Enjoy guiding your snake through the challenges and setting high scores!