# Advice: Make sure you know how this works, refer to the documentation if needed and .kv file


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
        self.timer_seconds = 300  # Set the timer to 5 minute (300 seconds)
        self.timer_event = None  # Event for the countdown timer
        
        Clock.schedule_once(self.set_focus, 0.1)  # Auto-focus on TextInput

        # Bind the screen tap to skip the typewriter effect
        Window.bind(on_touch_down=lambda *args: self.skip_typewriter())

        # Display initial command list with bold BOT
        self.chat_history = (
    "█████████████████████████\n"
    "█████████████████████████\n"
    "██                     \n"
    "██ [b]Cipher ChatBot[/b]\n"
    "██                     \n"
    "█████████████████████████\n"
    "█████████████████████████\n"
    "\n[b]BOT ->[/b] [i]Welcome to Cipher ChatBot![/i]\n"
    "[b]BOT ->[/b] [i]Use HeadPhones for best Experience[/i]\n"
    "[b]BOT ->[/b] [i]Please type 'start' to begin or 'exit' to quit.[/i]\n"
    "\n"
)
        # Bind keyboard height changes to adjust input area
        #Window.bind(on_keyboard_height=self.on_keyboard_height)
        # Store original input area position
        self.input_layout = None

    def play_send_sound(self):
        """Play the send button sound."""
        send_sound = SoundLoader.load('assets/beep.mp3')  # Replace with your sound file path
        if send_sound:
            send_sound.play()

    def start_timer(self):
        """Start the countdown timer."""
        self.timer_seconds = 300  # Reset the timer to 5 minute
        if self.timer_event:
            self.timer_event.cancel()  # Cancel any existing timer
        self.timer_event = Clock.schedule_interval(self.update_timer, 1)  # Update every second
        # Load and play the timer sound

        self.timer_sound = SoundLoader.load('assets/timer.mp3')  # Store the sound object
        if self.timer_sound:
            self.timer_sound.loop = True  # Loop the sound while the timer is running
            self.timer_sound.play()


    def stop_timer(self):
        """Stop the countdown timer."""
        if self.timer_event:
            self.timer_event.cancel()
            self.timer_event = None
        
        #self.timer_sound = SoundLoader.load('assets/timer.mp3')  # Store the sound object
        if self.timer_sound:
            self.timer_sound.stop()

    
    
    def update_timer(self, dt):
        """Update the timer every second."""
        if self.timer_seconds > 0:
            self.timer_seconds -= 1
            minutes = self.timer_seconds // 60
            seconds = self.timer_seconds % 60
            self.ids.timer_label.text = f"{minutes:02}:{seconds:02}"  # Update the timer label
        else:
            # Timer reached zero, stop the timer and trigger Game Over
            if self.timer_event:
                self.timer_event.cancel()
                self.timer_event = None
            self.time_up()

    def time_up(self):
        """Handle the 'Time Up' scenario."""
        self.typewriter_effect(
            "\n[b]Curator ->[/b] Time's up! The collar explodes, taking your head along with it.",
            shake=False,
            callback=lambda: Clock.schedule_once(self.show_game_over, 2)
        )
        self.is_game_started = False  # Mark the game as not started

    def set_focus(self, *args):
        """Ensure the TextInput always has focus."""
        self.ids.user_input.focus = True

    def add_to_input(self, key):
        """Add a key to the TextInput."""
        self.ids.user_input.text += key
        self.set_focus()  # Keep focus on TextInput

    def backspace_input(self):
        """Remove the last character from the TextInput."""
        self.ids.user_input.text = self.ids.user_input.text[:-1]
        self.set_focus()  # Keep focus on TextInput

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

        # Adjust the interval dynamically based on text length
        interval = 0.02 if len(text) < 100 else 0.03  # Longer interval for longer text


     # Schedule the typewriter effect
        if self.typewriter_event:
            self.typewriter_event.cancel()
        self.typewriter_event = Clock.schedule_interval(self._add_character, interval)

    def skip_typewriter(self):
        """Skip the typewriter effect and display the full text immediately."""
        if self.typewriter_event:  # If the typewriter is running
            self.typewriter_event.cancel()  # Cancel the typewriter effect
            self.typewriter_event = None  # Clear the event
            self.stop_typewriter_sound()  # Stop the typewriter sound
            self.chat_history = self.full_text  # Display the full text immediately
            if self.callback:  # If there's a callback, execute it
                self.callback()

    def _add_character(self, dt):
        """Add one character at a time to the chat history."""
        if self.char_index < len(self.full_text):
            char = self.full_text[self.char_index]
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


    def on_focus(self, instance, value):
        if value:
            Clock.schedule_once(lambda dt: self.scroll_to_bottom(), 0.1)
            
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


        # Check if the game is in a "Game Over" state
        if not self.is_game_started:
            if user_input.lower().strip() == 'start':
                # Reset the game state
                self.dataset.current_node = 'start'  # Reset to the start node
                self.is_game_started = True  # Mark the game as started
                self.played_music_nodes = set()  # Clear played music tracking
                self.chat_history += "\n[b]BOT ->[/b] Starting a new game...\n"
                response, bg_music = self.dataset.processing(user_input)
                print(f"Start command bg_music: {bg_music}")  # Debugging
                if bg_music:
                    self.start_bg_music(bg_music.get('file'), bg_music.get('speed', 1.0))
                else:
                    self.stop_bg_music()
                self.typewriter_effect(f"\n[b]Curator ->[/b] {response}", shake=True)
                self.scroll_to_bottom()
                self.start_timer()  # Start the timer when the game begins
            elif user_input.lower().strip() == 'exit':
                self.chat_history += "\n[b]BOT ->[/b] Exiting the game. Goodbye!"
                self.stop_bg_music()  # Stop background music
                self.stop_timer()  # Stop the timer
                App.get_running_app().stop()  # Close the app
            else:
                # Resend the "Game Over" prompt
                self.typewriter_effect("\n[b]BOT ->[/b] Invalid input. Please type 'start' to play or 'exit' to quit.")
            return

        # Handle 'exit'
        if user_input.lower().strip() == 'exit':
            self.chat_history += "\n[b]BOT ->[/b] Exiting the game. Goodbye!"
            self.stop_bg_music()  # Stop background music
            self.stop_timer()  # Stop the timer
            App.get_running_app().stop()  # Close the app
            return

        # Handle riddle answers
        response, bg_music = self.dataset.process_riddle_answer(user_input)
        print(f"Riddle answer bg_music: {bg_music}")  # Debugging

        # Start the background music (if any) before displaying the response
        if bg_music:
            # Play trap or jumpscare music only once
            loop = False if "TRAP" in response or "jumpscare" in bg_music.get('file', '') or "Gory" in bg_music.get('file', '') or "fall_water" in bg_music.get('file', '') else True
            self.start_bg_music(bg_music.get('file'), bg_music.get('speed', 1.0), loop=loop)
        else:
            self.stop_bg_music()

        # Check if the response contains "TRAP" or other game-ending conditions
        if "TRAP" in response or "Oh no!" in response or "not the right answer" in response:
            # Stop the timer
            self.stop_timer()
            # Play the trap music while displaying the response
            self.typewriter_effect(response, shake=False, callback=lambda: Clock.schedule_once(self.show_game_over, 2))
            self.is_game_started = False  # Mark the game as not started
            return

        # Handle success conditions
        if "Congratulations" in response or "escape the room" in response:
            # Stop the timer
            self.stop_timer()
            # Display the success message first, then show "Game Over"
            self.typewriter_effect(response, shake=False, callback=lambda: Clock.schedule_once(self.show_game_over, 2))
            self.stop_bg_music()
            self.is_game_started = False  # Mark the game as not started
            return

        # Continue the game for non-ending responses
        self.typewriter_effect(response, shake=False)
        self.scroll_to_bottom()

        self.set_focus()  # Keep focus on TextInput

    def show_game_over(self, dt=None):
        """Display the Game Over message after the typewriter effect finishes."""
        self.typewriter_effect("\n[b]BOT ->[/b] Game over! Type 'start' to play again or 'exit' to quit.")

class ChatBotApp(App):
    def build(self):
        return ChatBotWidget()

if __name__ == "__main__":
    ChatBotApp().run()
