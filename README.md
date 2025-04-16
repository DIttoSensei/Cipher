# Cipher Chatbot

Cipher is an interactive chatbot application built using Python and Kivy. It features a text-based adventure game where users solve riddles and navigate through challenges. The app includes background music, sound effects, and a typewriter effect for immersive storytelling.

---

## Features

- **Interactive Gameplay**: Solve riddles and make choices to progress through the game.
- **Dynamic Background Music**: Background music changes based on the current challenge.
- **Trap Sounds**: Special sounds play during critical moments, such as traps or jumpscares.
- **Typewriter Effect**: Text is displayed with a typewriter animation for better user experience.
- **Game Reset**: Restart the game anytime by typing "start".

---

## Requirements

- **Python 3.x**
- **Kivy Framework**
- **Buildozer** (for building Android APKs)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/DIttoSensei/Cipher.git
   cd cipher-chatbot

2. Install the required dependencies:
    pip install -r requirements.txt

3. Run the application:
    python main.py


## Customization

1. Add New Challenges:
    Edit the dialogue_tree in dataset.py to add new challenges, riddles, or traps.

2. Change Background Music:
    Replace or add music files in the assets/ directory and update the bg_music key in dataset.py.


## Credits

- **Developer:** Andrew Richard
- **Framwork:** Kivy
- **Build Tools:** Buildozer