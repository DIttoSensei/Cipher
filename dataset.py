from kivy.app import App


class DataSet:

    def __init__(self):
        self.dialogue_tree = {
            'start': {

                'type': 'riddle',
                'prompt': """“Oh… that’s wonderful, you’re awake! I was starting to worry you’d sleep through the fun. Here’s the deal, 
my curious guest: you have exactly 3 minutes to escape this little… let’s call it a playroom. Solve the 
challenges I’ve prepared, and you might find a way out. Fail, and that lovely collar around your neck? 
It’s rigged to explode. Tick-tock, darling. Good luck.”

A faint glow flickers to life in the distance, revealing a monitor embedded in the wall. Words scroll across it, pulsing like a heartbeat:

“What speaks without a mouth and hears without ears? I have no body, but come alive with the wind. What am I?”
""",
                'answers': ['echo'],
                'next': {'echo': 'challenge2'},
                'cpu': {'echo': 'Correct!!!'},
                'bg_music': {'file' : 'assets/bg_music2.mp3', 'speed': 1.0}

            },

            'challenge2':{

                'type': 'riddle',
                'prompt': """You crawl through the grate. A voice begs: “Free me!” A locked box nearby hums. 
The monitor shows a riddle: “I’m taken from a mine and shut in a wooden case, 
from which I’m never released, yet used by all. What am I?”""",
                    
                
                'answers': ['pencil lead', 'graphite'],
                'next': {'pencil lead': 'challenge3', 'graphite': 'challenge3'},
                'cpu': {'pencil lead': 'Correct!!!', 'graphite': 'Correct!!!'},
                'bg_music': {'file' : 'assets/bg_music2.mp3', 'speed': 1.0}


            },

            "challenge3" : {

                'type' : 'choice',
                'prompt' : """You can ask one of the two guards, who knows the truth, one question to figure out which door leads to serenity. 
However, one guard always tell the truth, and the other always lies, you don't know which guard is which.
[b]WHAT DO YOU ASK[/b]
A) 'Which door leads to serenity?'
B) 'If i were to ask the other guard which door leads to serenity, what would they say?'""",

                'answers': ['a', 'b'],
                'next': {'a': 'challenge4', 'b': 'challenge5'},
                'cpu': {'a': 'YOU MAY PASS!!!', 'b': 'YOU MAY PASS!!!'},
                'bg_music' : {'file' : '', 'speed': 1.0}

            },

            "challenge4" : {

                'type' : 'trap',
                'prompt' : """You walked into a dark room, ONLY TO FIND 'TRAP' WRITTEN IN BLOOD ON THE WALL!!!, Your coller beeped and exploded""",

                'answers': [],
                'next': {},
                'cpu': {},
                'bg_music' : {'file' : 'assets/jumpscare.mp3', 'speed': 1.0}

            },

           
        }
        self.current_node = 'start'  # Track the current node in the dialogue tree

    def processing(self, user_input):
        # Normalize user input to lowercase for case-insensitive matching
        user_input = user_input.lower().strip()

        # Get the current node
        current_node = self.dialogue_tree.get(self.current_node)

        # Check if the current node exists
        if not current_node:
            return "\nBOT -> Error: Current node not found in dialogue tree.", None

        # Get the background music information
        bg_music = current_node.get('bg_music')

        # Debugging: Print the current node and bg_music
        print(f"Processing node: {self.current_node}, bg_music: {bg_music}")

        # Return the prompt and background music
        return current_node['prompt'], bg_music
    
        
    def process_riddle_answer(self, user_input):
        # Normalize user input to lowercase for case-insensitive matching
        user_input = user_input.lower().strip()

        # Get the current node
        current_node = self.dialogue_tree.get(self.current_node)

        # Check if the current node exists
        if not current_node:
            return "\nCurator -> Error: Current node not found in dialogue tree.", None

        # Get the background music information
        bg_music = current_node.get('bg_music')

        # Debugging: Print the current node and bg_music
        print(f"Processing riddle answer for node: {self.current_node}, bg_music: {bg_music}")

        # Check if the user's input matches any valid answer in the current node
        for answer in current_node['answers']:
            if answer in user_input:
                # If the answer is correct, retrieve the next node and CPU response
                next_node_key = current_node['next'].get(answer)
                cpu_response = current_node['cpu'].get(answer, "Correct!")

                # Update the current node to the next node
                self.current_node = next_node_key

                # Get the next node's prompt
                next_node = self.dialogue_tree.get(next_node_key)

                if next_node:
                    # Debugging: Print the next node and its bg_music
                    print(f"Next node: {next_node_key}, bg_music: {next_node.get('bg_music')}")
                    return f"[b]\nCurator ->[/b] {cpu_response}\n\n[b]Next Challenge:[/b]\n{next_node['prompt']}", next_node.get('bg_music')

                # If there's no next node, end the game
                return f"[b]\nCurator ->[/b] {cpu_response}\n\nCongratulations! You've escaped the room!", bg_music

        # If no valid answer is found, return an error message
        self.current_node = 'start'  # Reset to start node
        return "[b]\nCurator ->[/b] Oh no! That's not the right answer. Too bad! (The collar explodes taking your head along with it.)", None