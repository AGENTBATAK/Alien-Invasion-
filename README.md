# Alien Invasion

## Introduction

Alien Invasion is a 2D arcade-style shooting game developed using Python and the Pygame library. The main objective of the game is to control a spaceship, destroy incoming alien fleets, survive enemy attacks, and achieve the highest score possible.

This project was created as a learning-based game development project to understand concepts such as:

* Object-Oriented Programming in Python
* Pygame fundamentals
* Sprite handling
* Collision detection
* Score management
* Game loops and event handling
* Dynamic difficulty systems

The game includes multiple gameplay features such as:

* Bullet firing system
* Alien fleet generation
* Increasing difficulty levels
* Score and high score system
* Ship life system
* Fleet movement and collision handling

---

# Technologies Used

* Python 3.13
* Pygame 2.6.1

---

# Project Structure

Note: This project also includes a custom `keybind.dll` and related C++ files for experimental/native key handling on Windows systems. These files are intentionally kept in the repository.

```text
Alien-Invasion/
│
├── gam_images/
├── alien.py
├── alien_invasion.py
├── bullet.py
├── button.py
├── game_stats.py
├── keybind.py
├── scoreboard.py
├── setting.py
├── ship.py
├── keybind.dll
├── Key_controls.cpp
├── keybind.cpp
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Installation

## Step 1: Clone the Repository

```bash
git clone https://github.com/AGENTBATAK/Alien-Invasion-.git
```

## Step 2: Open the Project Folder

```bash
cd Alien-Invasion-
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Run the Game

```bash
python alien_invasion.py
```

---

# Controls

| Key             | Action      |
| --------------- | ----------- |
| W / Up Arrow    | Move Up     |
| S / Down Arrow  | Move Down   |
| A / Left Arrow  | Move Left   |
| D / Right Arrow | Move Right  |
| Space           | Fire Bullet |

---

# Gameplay Features

## 1. Alien Fleet System

Aliens are automatically generated in rows and columns. The fleet moves horizontally and changes direction after touching screen edges.

## 2. Bullet Collision System

Bullets collide with aliens using Pygame sprite collision detection.

## 3. Score System

The score increases whenever an alien is destroyed.

## 4. High Score System

The game tracks the highest score achieved during runtime.

## 5. Level System

Whenever all aliens are destroyed, the level increases and game speed becomes faster.

## 6. Ship Life System

The player has limited lives displayed at the top-left corner using small ship icons.

---

# Customization

The project is easy to modify and customize.

## Change Ship Image

Replace the ship image inside the `images/` folder.

You can also resize the ship inside `ship.py` using:

```python
pygame.transform.scale()
```

## Change Background Color

Inside `setting.py`:

```python
self.bg_color = (0, 0, 0)
```

You can modify the RGB values to any color.

## Change Bullet Color

Inside `setting.py`:

```python
self.bullet_color = (255, 255, 255)
```

## Change Alien Speed

Inside `setting.py`:

```python
self.alien_speed
```

## Change Maximum Bullets

Inside `setting.py`:

```python
self.bullets_allowed
```

## Change Ship Lives

Inside `setting.py`:

```python
self.ship_limit
```

---

# Native DLL Information

This project includes a custom Windows DLL:

```text
keybind.dll
```

The DLL is used for experimental/native key handling functionality.

Important points:

* The DLL is currently Windows-specific.
* The project is mainly designed and tested on Windows.
* Linux and MacOS users may need alternative implementations.
* Python and DLL compatibility may depend on architecture and Python version.

Related files:

```text
keybind.dll
Key_controls.cpp
keybind.cpp
```

---

# Common Issues and Fixes

## 1. Pygame Not Installed

Error:

```text
ModuleNotFoundError: No module named 'pygame'
```

Solution:

```bash
pip install pygame
```

---

## 2. Image Not Found Error

Error:

```text
FileNotFoundError
```

Solution:

* Make sure the `images` folder exists.
* Verify image file names and extensions.
* Check that paths inside the code are correct.

---

## 3. Ship or Alien Too Large

Solution:
Resize images using:

```python
pygame.transform.scale(image, (width, height))
```

---

## 4. Scoreboard Not Updating

Solution:
Ensure methods like:

```python
prep_score()
prep_level()
prep_high_score()
```

are called after updating values.

---

## 5. Git Tracking **pycache** Files

Solution:
Use `.gitignore` and remove cached files:

```bash
git rm -r --cached __pycache__
```

---

# Future Improvements

Possible future features that can be added:

* Sound effects and background music
* Main menu system
* Pause feature
* Multiple enemy types
* Boss fights
* Power-ups
* Save system for high scores
* Multiplayer mode
* Animated explosions

---

# Learning Outcomes

This project helped in understanding:

* Game development basics
* Python class structure
* Event-driven programming
* Pygame sprite handling
* Debugging and error fixing
* Git and GitHub workflow

---

# Conclusion

Alien Invasion is a beginner-friendly Python game project that demonstrates how a complete arcade game can be developed using Pygame. The project focuses on clean structure, modular design, and expandable gameplay mechanics.

The game can be further improved with better graphics, animations, sounds, and advanced gameplay systems.

---

# Author

Developed by AGENTBATAK
