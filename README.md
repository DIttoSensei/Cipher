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
    ```bash
    pip install -r requirements.txt

3. Run the application:
    ```bash
    python main.py


## Customization

1. **Add New Challenges**:
    Edit the dialogue_tree in dataset.py to add new challenges, riddles, or traps.

2. **Change Background Music**:
    Replace or add music files in the assets/ directory and update the bg_music key in dataset.py.

## How to build Apk
Now you need to pay absolute attention here, to build for APK i used linux, to be more specific i used kali linux as my development environment (Vm ware), cause for some reason i can't get it to build on windows.

Regardless of which distro you use i'm pretty sure it still the same:

1. Create a folder in your document directory or whatever location you please.

2. Add the main.py, dataset.py, chatbot.kv and buildozer.spec ( i assume you have edited the .spec file to suit your apk needs )

3. Create a virtual environment and activate it
    ```bash
    python3.10 -m venv venv
    source venv/bin/activate


4. Make sure your virtual environment is running python 10 that is if you encounter build error later on but python 10 was the version i used along with java sdk 17

5. Install buildozer
    ```bash
    pip install buildozer

6. Run:
    ```bash
    buildozer andriod debug

7. The build process should begin. Now if you encounter errors of pakages not installing properly for the build process, go to the target folder prompting the error and install it manually, either by zip of by git, make sure the paths are the same. After all that you shold be good, most errors you should encounter are: Python version, SDK version, files not found in path ( Install manually )

8. Run step 6 again, and by all means should you run:
    ```bash
    buildozer andriod clean

This is basically claering all your hard work. Another ALternative is using goggle collab, install buildozer and run build.

## How To Edit Code
A quick rundown on how the code works, the main.py and chatbot.kv handles the main code process and interface, .kv is more in charge of the interface which are then called in main to correspond with specific functions and input.

So not much should be change except from the interface if ypou want, or how input are being processed. In dataset.py, you have a dialogue tree that structures how input and cpu responses should interact including music and branches. refer to 1.png in the assets folder.

If you are going to edit datasets, use template.txt and follow how they are being arranges and edit away. All you need is to structure your dialogue accordingly, the system wil process the rest as it should.


## Credits

- **Developer:** Andrew Richard (Dittosensei)
- **Framwork:** Kivy
- **Build Tools:** Buildozer
- **Audio:** Gory Explosion FX" By Lux Aeterna, All artist on pixabay.com (sorry couldn't trace their names lost the credit file i once wrote)