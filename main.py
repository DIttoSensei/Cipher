from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.animation import Animation
from kivy.core.window import Window
from dataset import DataSet
from kivy.clock import Clock
from random import randint
from kivy.core.audio import SoundLoader

class ChatBotWidget(BoxLayout):
    chat_history = StringProperty("")  # Stores the chat history for display
    bg_music = None  # Background music sound object

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dataset = DataSet()  # Initialize the DataSet
        self.is_game_started = False  # Track if the game has started
        self.typewriter_event = None 
        self.typewriter_sound = None 

        # Display initial command list with bold BOT
        self.chat_history = (
            "-----------------------\n"
            "-----------------------\n"
            "       [b]Cipher[/b]\n"
            "-----------------------\n"
            "-----------------------\n"
            
            "\n[b]BOT ->[/b] Please type 'start' to begin or 'exit' to quit\n"
            "\n"
            "\n"
        )
        # Bind keyboard height changes to adjust input area
        Window.bind(on_keyboard_height=self.on_keyboard_height)
        # Store original input area position
        self.input_layout = None

    def start_bg_music(self, music_file='assets/bg_music2.mp3', speed=1.0, loop=True):
        """Start playing background music, with an option to loop or play once."""
        if not music_file:  # Check if the music file is an empty string
            print("No background music to play.")  # Debugging log
            if self.bg_music:
                self.bg_music.stop()
                self.bg_music = None  # Clear the SoundLoader object
            return

        # Stop the current music only if it's different from the new music
        if self.bg_music and self.bg_music.source != music_file:
            print(f"Stopping current music: {self.bg_music.source}")
            self.bg_music.stop()
            self.bg_music = None  # Clear the SoundLoader object

        # Load and play the new music
        print(f"Starting background music: {music_file} at speed {speed}, loop={loop}")  # Debugging log
        self.bg_music = SoundLoader.load(music_file)  # Reload the SoundLoader object
        if self.bg_music:
            self.bg_music.loop = loop  # Set looping based on the parameter
            self.bg_music.pitch = speed  # Set playback speed
            self.bg_music.volume = 1.0  # Ensure volume is set
            self.bg_music.play()
        else:
            print(f"Failed to load music: {music_file}")

    def stop_bg_music(self):
        """Stop playing background music."""
        if self.bg_music:
            print("Stopping background music.")  # Debugging log
            self.bg_music.stop()
            self.bg_music = None  # Clear the SoundLoader object

    def play_typewriter_sound(self):
        """Play the typewriter sound."""
        if not self.typewriter_sound:
            self.typewriter_sound = SoundLoader.load('assets/text.mp3')  # Replace with your sound file path
        if self.typewriter_sound:
            self.typewriter_sound.loop = True  # Loop the sound while the typewriter is active
            self.typewriter_sound.play()

    def stop_typewriter_sound(self):
        """Stop the typewriter sound."""
        if self.typewriter_sound:
            self.typewriter_sound.stop()


    def typewriter_effect(self, text, shake=False, callback=None):
        """
        Display text character by character with an optional shake effect.
        :param text: The full text to display.
        :param shake: Whether to add a shake effect to some characters.
        :param callback: A function to call after the effect is complete.
        """
        self.current_text = ""  # Reset the current text
        self.full_text = text  # Store the full text
        self.shake = shake  # Whether to apply the shake effect
        self.callback = callback  # Callback after completion
        self.char_index = 0  # Start at the first character

        # Start the typewriter sound
        self.play_typewriter_sound()

     # Schedule the typewriter effect
        if self.typewriter_event:
            self.typewriter_event.cancel()
        self.typewriter_event = Clock.schedule_interval(self._add_character, 0.05)

    def _add_character(self, dt):
        """Add one character at a time to the chat history."""
        if self.char_index < len(self.full_text):
            char = self.full_text[self.char_index]

            # Apply shake effect to random characters
            if self.shake and char.isalnum() and randint(0, 4) == 0:  # 20% chance to shake
                char = f"[b]{char}[/b]"  # Example shake effect

            self.current_text += char
            self.chat_history = self.current_text  # Update the chat history
            self.char_index += 1
        else:
            # Stop the typewriter effect
            if self.typewriter_event:
                self.typewriter_event.cancel()
                self.typewriter_event = None


            # Stop the typewriter sound
            self.stop_typewriter_sound()


            # Call the callback function if provided
            if self.callback:
                self.callback()


    def on_parent(self, instance, value):
        """Set input_layout after widget is added to parent."""
        if value:
            self.input_layout = self.ids.input_layout

    def on_keyboard_height(self, window, keyboard_height):
        """Adjust input area position when keyboard appears."""
        if not self.input_layout:
            return
        if keyboard_height > 0:
            # Move input area above keyboard
            Animation(pos=(0, keyboard_height), duration=0.2).start(self.input_layout)
        else:
            # Restore to original position
            Animation(pos=(0, 0), duration=0.2).start(self.input_layout)

    def scroll_to_bottom(self):
        """Animate scroll to bottom of ScrollView."""
        scroll_view = self.ids.scroll_view
        Animation(scroll_y=0, duration=0.3).start(scroll_view)

    def process_input(self, user_input):
        """Process user input and update chat history."""
        if not user_input.strip():
            return  # Ignore empty input

        # Add user input to chat history
        self.chat_history += f"[b]\nUser ->[/b] {user_input}\n"
        self.scroll_to_bottom()  # Scroll after user input

        # Handle 'exit'
        if user_input.lower().strip() == 'exit':
            self.chat_history += "\n[b]BOT ->[/b] Exiting the game. Goodbye!"
            self.stop_bg_music()  # Stop background music
            App.get_running_app().stop()  # Close the app
            return

        # Handle initial 'start' command
        if not self.is_game_started or user_input.lower().strip() == 'start':
            # Reset the game state
            self.dataset.current_node = 'start'  # Reset to the start node
            self.is_game_started = True  # Mark the game as started
            self.played_music_nodes = set()  # Clear played music tracking
            response, bg_music = self.dataset.processing(user_input)
            print(f"Start command bg_music: {bg_music}")  # Debugging
            if bg_music:
                self.start_bg_music(bg_music.get('file'), bg_music.get('speed', 1.0))
            else:
                self.stop_bg_music()
            self.typewriter_effect(f"\n[b]Curator ->[/b] {response}", shake=True)
            self.scroll_to_bottom()
            return

        # Handle riddle answers
        response, bg_music = self.dataset.process_riddle_answer(user_input)
        print(f"Riddle answer bg_music: {bg_music}")  # Debugging

        # Start the background music (if any) before displaying the response
        if bg_music:
            # Play trap or jumpscare music only once
            loop = False if "TRAP" in response or "jumpscare" in bg_music.get('file', '') else True
            self.start_bg_music(bg_music.get('file'), bg_music.get('speed', 1.0), loop=loop)
        else:
            self.stop_bg_music()

        # Check if the response contains "TRAP" or other game-ending conditions
        if "TRAP" in response or "Oh no!" in response or "not the right answer" in response:
            # Play the trap music while displaying the response
            self.typewriter_effect(response, shake=False, callback=self.show_game_over)
            return

        # Handle success conditions
        if "Congratulations" in response or "escape the room" in response:
            # Display the success message first, then show "Game Over"
            self.typewriter_effect(response, shake=False, callback=self.show_game_over)
            self.stop_bg_music()
            self.is_game_started = False
            return

        # Continue the game for non-ending responses
        self.typewriter_effect(response, shake=False)
        self.scroll_to_bottom()

    def show_game_over(self):
        """Display the Game Over message after the typewriter effect finishes."""
        self.typewriter_effect("\n[b]BOT ->[/b] Game over! Type 'start' to play again or 'exit' to quit.")

class ChatBotApp(App):
    def build(self):
        return ChatBotWidget()

if __name__ == "__main__":
    ChatBotApp().run()