
# Dungeon Crawler Game

## Overview
Dungeon Crawler Game is a basic first-person tile-based dungeon crawler inspired by classic RPGs like Ultima 1. The game features procedurally generated mazes, basic character stats, leveling up, and turn-based combat with skeleton enemies.

## Features
- **First-Person View**: Navigate through the dungeon from a first-person perspective.
- **Procedural Generation**: Each dungeon floor is a procedurally generated maze.
- **Turn-Based Combat**: Encounter skeleton enemies and engage in turn-based combat.
- **Character Stats**: Manage your character's health, attack, defense, and level up.
- **Multiple Floors**: Explore multiple floors in the dungeon to reach the treasure.
- **Overhead Map**: View an overhead map of the dungeon with your position and direction marked.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/lainceline/py-dungeon.git
   ```
2. Navigate to the project directory:
   ```bash
   cd dungeon-crawler-game
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Play
- Use `W` to move forward.
- Use `S` to move backward.
- Use `A` to turn left.
- Use `D` to turn right.
- When encountering a skeleton, press `SPACE` to attack during your turn.
- Monitor your health and the skeleton's health on the battle screen.
- Explore the dungeon to reach the treasure at the bottom floor.

## Code Structure
- `main.py`: Main game loop and event handling.
- `constants.py`: Game constants and configuration.
- `player.py`: Player character class and movement logic.
- `skeleton.py`: Skeleton enemy class.
- `dungeon.py`: Dungeon generation and enemy placement.
- `graphics.py`: Rendering logic for the first-person view and overhead map.
- `battle.py`: Battle screen and turn-based combat logic.


## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- Inspired by classic RPGs like Ultima 1.
- ASCII art generated using [TextArt.sh](https://textart.sh/).

## Contact
For any questions or suggestions, feel free to open an issue or contact me at your-email@example.com.
```