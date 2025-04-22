# Yh first off, i know Holy cow this is a lot of code, but i am not going to change it. I am just going to add to it
# Cause trying to change or refactor it is going to be a pain
# If you can make it read from a file for your own sanity, please do so
# But for now, this is the code i am going to use to make the game
# Refer to the README.md for more information on how to use this code
# Also FOLLIOW THE PRCOCESS EXACTLY if you are going with this
# Actually you could just move all the process functtion and call the dataset class in it and call that one in main.py
# But i am not going to do that, cause i am lazy and i am not going to change this code


from kivy.app import App


class DataSet:

    def __init__(self):
        self.dialogue_tree = {
            'start': {

                'type': 'riddle',
                'prompt': """“Oh… that’s wonderful, you’re awake! I was starting to worry you’d sleep through the fun. Here’s the deal, 
my curious guest: you have exactly 5 minutes to escape this little… let’s call it a playroom. Solve the 
challenges I’ve prepared, and you might find a way out. Fail, and that lovely collar around your neck? 
It’s rigged to explode. Tick-tock, darling. Good luck. And also be perceptive, it going to help”

A faint glow flickers to life in the distance, revealing a monitor embedded in the wall. Words scroll across it, pulsing like a heartbeat:

“A man visits his mother’s funeral. At the service, he meets a woman whom he instantly connects with. 
But afterward, he has no way to contact her. Days later, she kills her sister. [b]Why did he do it?[/b]”
A) Because he was psycotic
B) Because he wanted another funeral
C) Because he was a depressed
D) Because he hoped to see her at the funeral
""",
                'answers': ['d'],
                'next': {'d': 'challenge2'},
                'cpu': {'d': 'Correct!!!'},
                'bg_music': {'file' : 'assets/bg_music2.mp3', 'speed': 1.0}

            },

            'challenge2':{

                'type': 'riddle',
                'prompt': """You crawl through the grate. A voice begs: “Free me!” A locked box nearby hums. 
The monitor shows a riddle: “I’m taken from [b]@[/b] mine and shut in a wooden case, 
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
                'prompt' : """You walked into a dark room, ONLY TO FIND 'TRAP' WRITTEN IN BLOOD ON THE WALL!!!, Your coller beeped and exploded [b]_[/b]""",

                'answers': [],
                'next': {},
                'cpu': {},
                'bg_music' : {'file' : 'assets/jumpscare.mp3', 'speed': 1.0}

            },

            "challenge5" : {

                'type' : 'choice',
                'prompt' : """You find yourself in front of two doors.
Above them, a sign reads:

“[b]Both doors lead to truth, but only one leads to life.[/b]”

A voice echoes in the walls:

“One door will give you the answer you want. The other will give you the answer you need.”

Which do you choose?

A) The door to what I want
B) The door to what I need
C) Refuse to choose
D) Break the sign""",

                'answers': ['a', 'b', 'c', 'd'],
                'next': {'a' : 'challenge6', 'b': 'challenge7', 'c': 'termination', 'd': 'sawcut'},
                'cpu': {'a': 'PROCEED!!!', 'b': 'PROCEED!!!' },
                'bg_music' : {'file' : 'assets/bg_music.mp3', 'speed': 1.0}

            },

            "termination" : {

                'type' : 'trap',
                'prompt' : """Beacause you refused to choose, the collar exploded taking your head along with it.(TRAP)""",

                'answers': [],
                'next': {},
                'cpu': {},
                'bg_music' : {'file' : 'assets/boom.mp3', 'speed': 1.0}

            },

            "sawcut" : {

                'type' : 'trap',
                'prompt' : """After breaking the sign, a saw comes out in front AND DIGS INFO YOUR TORSO!!!(TRAP)""",

                'answers': [],
                'next': {},
                'cpu': {},
                'bg_music' : {'file' : 'assets/saw.mp3', 'speed': 1.0}

            },

            "challenge6" : {

                'type' : 'logic',
                'prompt' : """You find yourself in a room with a cracked wall. On it, someone has scratched a message:
"[b]I am always hungry but never eat. I grow bigger the more I consume, yet I am nothing. Feed me right, and I’ll let you through.[/b]"
A table nearby has three objects:

    A loaf of bread
    A mirror
    A shovel

There’s a wide, dark mouth-like hole in the center of the floor, surrounded by old bloodstains.

What do you put into the hole to open the hidden door?
Type either 'bread', 'mirror', or 'shovel' to proceed.""",

                'answers': ['shovel'],
                'next': {'shovel': 'challenge8'},
                'cpu': {'shovel': 'You placed the shovel in....................nothing happened....you may go!!!'},
                'bg_music' : {'file' : 'assets/bg_music3.mp3', 'speed': 1.0}

            },

            "challenge7" : {

                'type' : 'decode',
                'prompt' : """You walked into a dark room, and the door locked behind you. lights flickered on, revealing a table with a note.
The note reads: "Decode the message to escape. Who is this letter addressed to?
/LETTER/

Dear [b][][][][][][/b],

My hands tremble, stained with [b]D[/b]read, as I write in this fading light. The mirror reflects only your [b]A[/b]bsent gaze, cold and near. My breath, [b]T[/b]hin and frayed, catches on the silence. 
ev[b]E[/b]ry night, I feel your shadow’s weight upon my chest. This [b]H[/b]aunting ink is all I leave, unanswered, lost.""",

                'answers': ['death'],
                'next': {'death': 'challenge9'},
                'cpu': {'death': 'You decoded the message correctly!!! Proceed!!!'},
                'bg_music' : {'file' : 'assets/bg_music3.mp3', 'speed': 1.0}


            },

            "challenge8" : {

                'type' : 'decode',
                'prompt' : """You proceded to the next room, and the [b]D[/b]oor locked behind you. lights flickered on, revealing a table with a note.
The note reads:
[b]".moor siht ni edih nac I .I ylno tuoba kniht ,pu em lloR"[/b]

A monitor flickers ready to accept an input and it says: "Be precise with your answer."
                """,

                'answers': ['roll me up, think about only i. i can hide in this room.'],
                'next': {'roll me up, think about only i. i can hide in this room.': 'challenge11'},
                'cpu': {'roll me up, think about only i. i can hide in this room.' : 'The monitor flickers and the door opens, you may proceed!!!'},
                'bg_music' : {'file' : 'assets/light.mp3', 'speed': 1.0}

            },

            "challenge9" : {

                'type' : 'choice',
                'prompt' : """You enter a small room made entirely of mirrors. [b]I[/b]n the center stands a single chair facing a mirror, and carved into the glass in shaky handwriting:
    [b]"One of me is not like the rest. I see what you see, but I lie when you don’t. Find me and leave."[/b]
Below the mirror are five buttons, each labeled with a word:

A) Fear
B) Memory
C) Truth
D) Doubt
E) Madness

A voice whispers behind the glass:

“You only get one press. Choose the mirror that doesn’t want to be seen.”
Which button do you press?""",

                'answers': ['d', 'a', 'b', 'c', 'e'],
                'next': {'d': 'challenge12', 'a': 'challenge10', 'b': 'challenge10', 'c': 'challenge10', 'e': 'challenge10'},
                'cpu': {'d' : 'The glass shatters, revealing a hidden door. You may proceed!!!', 'a' : 'An hidden hatch below opens, hence you fall', 'b' : 'An hidden hatch below opens, hence you fall', 'c' : 'An hidden hatch below opens, hence you fall', 'e' : 'An hidden hatch below opens, hence you fall'},
                'bg_music' : {'file' : '', 'speed': 1.0}

            },

            "challenge10" : {

                'type' : 'trap',
                'prompt' : """As You fell, mul[b]T[/b]iple spaers from the floor digged into your flesh (TRAP)""",

                'answers': [],
                'next': {},
                'cpu': {},
                'bg_music' : {'file' : 'assets/stab.mp3', 'speed': 1.0}

            },

            "challenge11" : {

                'type' : 'decode',
                'prompt' : """A dusty old TV turns on as you enter the room.
The screen shows [b]T[/b]his message:

"I speak in numbers.
You see: 10 - 7 - 4 - 1 - ?"

It loops, over and over. Static crackles behind it.
At the bottom, one word fades in and out:

    [b]“HELLO”[/b]

There’s a keypad beneath the screen.

The question is unspoken, but clear:
What number comes next?""",

                'answers': ['-2'],
                'next': {'-2' : 'challenge16'},
                'cpu': {'-2' : 'The screen flickers you may Proceed!!!'},
                'bg_music' : {'file' : 'assets/bg_music4.mp3', 'speed': 1.0}

            },

            "challenge12" : {

                'type' : 'choice',
                'prompt' : """You’re in a pitch-black hallway.
Somewhere behind you, slow wet footsteps echo through the silence.
You don’t see it… but it sees you.

Suddenly, a flickering light reveals four doors in front of you.
Above them, a message glitches across the wall:

    “It walks. You think. One of these saves you.
    One of these kills you. Two will make you stay… forever.”

The doors are labeled:

A) RUN
B) HIDE
C) SCREAM
D) STAND STILL

You hear the footsteps getting louder.""",

                'answers': ['a', 'b', 'c', 'd'],
                'next': {'a': 'challenge14', 'b': 'challenge14', 'c': 'challenge14', 'd': 'challenge13'},
                'cpu': {'d' : 'The Strange figure came close......it ignored you and a door opened.'},
                'bg_music' : {'file' : 'assets/walk.mp3', 'speed': 1.0}

            },

            "challenge13" : {

                'type' : 'riddle',
                'prompt' : """You enter a cold, dark chamber.
There’s nothing but a speaker mounted to the wall…
And a metal chair facing it, bolted to the floor.

As you sit, the speaker bursts to life with blood-curdling screaming — nonstop, shrill, human, but not quite.
Over the screams, a distorted voice whispers a riddle:

   [b]“I am always louder when you try to run.
    I starve if you look me in the eyes.
    I feed when you flinch,
    And I die when you lie.” [/b]

    “What am I?”

The screaming grows louder. You have to stay focused.
Your pulse races. You want to cover your ears.
But if you answer wrong… you die!!!""",

                'answers': ['fear'],
                'next': {'fear' : 'challenge15'},
                'cpu': {'fear' : 'The screaming stops yet it [b]lingers.[/b] You may proceed!!!'},
                'bg_music' : {'file' : 'assets/girl_scream.mp3', 'speed': 1.0}

            },

            "challenge14" : {

                'type' : 'trap',
                'prompt' : """THE FIGURE KILLED Y[b]O[/b]U!!!(TRAP)""",

                'answers': [],
                'next': {},
                'cpu': {},
                'bg_music' : {'file' : 'assets/figure_growl.mp3', 'speed': 1.0}

            },

            "challenge15" : {

                'type' : '',
                'prompt' : """You found a table, on it is a note and p[b]E[/b]n.

The note says: [_ _ _ _ _]

There is no hint. No context.

But... you feel like you've written this before.""",

                'answers': ['death'],
                'next': {'death': 'challenge16'},
                'cpu': {'death': 'You wrote daeth.......nothing happened, you continue moving forward.'},
                'bg_music' : {'file' : 'assets/bg_music3.mp3', 'speed': 1.0}

            },

            "challenge16" : {

                'type' : 'choice',
                'prompt' : """You continue down the hallway, and in the distance, you see a [b]S[/b]hadowy figure.

The figure approches you and said:
[b]ENTITY:[/b] "You always come back, don’t you? Even when [i]he[/i] dies..."
It step closer, staring [i]through[/i] you.

[b]ENTITY:[/b] "Tell me, how many times have you died?" 
A) i lost count
B) too many
C) infinite
D) doesn’t matter""",

                'answers': ['a', 'b', 'c', 'd'],
                'next': {'a': 'challenge17', 'b': 'challenge17', 'c': 'challenge17', 'd': 'challenge17'},
                'cpu': {
                        'a': "The figure smiles. Not at you. [i]At the one behind your eyes.[/i]",
                        'b': "They nod. 'Good. That means you’re learning.'",
                        'c': "They whisper: 'Only you remember. That’s your curse… or your edge.'",
                        'd': "Silence. Then a nod. The room bends. Time [b]shifts.[/b]"
                        },
                'bg_music' : {'file' : 'assets/', 'speed': 1.0}

            },

            "challenge17" : {

                'type' : 'choice',
                'prompt' : """You step into a dimly lit room.
There’s a figure crouched in front of the only door — chewing. Loudly. Wet, gnawing sounds.

It doesn’t look up.

The door behind it is open just enough to see… light.
Escape? Maybe.

You get one chance to act.

What do you do?

    A) Approach slowly.
    B) Ask what it’s eating.
    C) Rush past to the door.
    D) Throw something to distract it.
    E) Say nothing and wait.""",

                'answers': ['a', 'b', 'c', 'd', 'e'],
                'next': {'a' : 'scream', 'b' : 'challenge18', 'c' : 'chomp', 'd' : 'challenge19', 'e' : 'jumpe'},
                'cpu': {'b' : 'The figure whispers: “I saved you a piece.” You took it and went your way.',
                        'a' : '',
                        'c' : '',
                        'd' : 'It snarls — but turns. You slip through the door before it notices.',
                        'e': ''},
                'bg_music' : {'file' : 'assets/eating.mp3', 'speed': 1.0}

            },

            "scream" : {

                'type' : 'trap',
                'prompt' : """(TRAP) You try to be careful… but you enter its space. The figure doesn’t like surprises.
It lashes out. You die confused.""",

                'answers': [],
                'next': {},
                'cpu': {},
                'bg_music' : {'file' : 'assets/scream.mp3', 'speed': 1.0}

            },

            "chomp" : {

                'type' : 'trap',
                'prompt' : """(TRAP) This is impulsive.
Fear takes over logic.
The figure is fast — faster than you think.

You don’t make it.""",

                'answers': [],
                'next': {},
                'cpu': {},
                'bg_music' : {'file' : 'assets/roar.mp3', 'speed': 1.0}

            },

            "jumpe" : {

                'type' : 'trap',
                'prompt' : """(TRAP) This is inaction. You hesitate.
Time stretches… then the figure notices you.
It was hungry. Now it’s done. And you’re next.""",

                'answers': [],
                'next': {},
                'cpu': {},
                'bg_music' : {'file' : 'assets/roar2.mp3', 'speed': 1.0}

            },

            "challenge18" : {

                'type' : 'logic',
                'prompt' : """You walk into a [b]N[/b]arrow room.
Everything is perfectly still — yet something feels off.

A mechanical voice echoes:

    “I wake you up,
    yet you always ignore me.
    You set me every night,
    but curse me every morning.”

The walls are lined with buttons, all numbered, all silent.
Only one unlocks the next door.

The voice continues:

    “You trust me with your future,
    but silence me in your present.
    And when I fail…
    you say it’s [i]your[/i] fault.”

What am I?""",

                'answers': ['alarm'],
                'next': {'alarm': 'challenge21'},
                'cpu': {'alarm' : 'The door opens, you may proceed!!!'},
                'bg_music' : {'file' : 'assets/music_box.mp3', 'speed': 1.0}

            },

            "challenge19" : {

                'type' : 'info',
                'prompt' : """You enter a room filled with shelves.
Each one holds a small box. Some are labeled: “2015,” “8th grade,” “That birthday.”

One box is open.
Inside is a tiny object you can’t quite remember owning.
A dusty cassette player sits nearby, already playing.

    [b][crackling voice][/b]
    “You only come back to me when you’re tired.
    When the world gets too loud.
    When you want to feel like you used to.
    I wait for you, always,
    but you pretend I never mattered.”

The door won’t open unless you name what’s missing.""",

                'answers': ['nostalgia'],
                'next': {'nostalgia' : 'breakpoint'},
                'cpu': {'nostalgia' : 'The door opens, you proceed!!!'},
                'bg_music' : {'file' : 'assets/', 'speed': 1.0}

            },

            "breakpoint" : {

                'type' : 'breakpoint',
                'prompt' : """As you proceed, you noticed a crack in the wall.
What do you do?

A) Ignore it and move on.
B) Investigate the crack.""",

                'answers': ['a', 'b'],
                'next': {'a': 'challenge20', 'b': 'special_path'},
                'cpu': {'a' : 'You ignored the crack and moved on.',
                        'b' : 'You investigated the crack and it broke open, revealing a hidden path.'},
                'bg_music' : {'file' : 'assets/note.mp3', 'speed': 1.0}

            },

            "special_path" : {

                'type' : 'extra',
                'prompt' : """As you proceed, you noticed this path is unusual than the others.
You [b]S[/b]ee a door at the end of the path.
You tried to open it, but it wouldn't budge.
You noticed a keypad next to the door.

[_ _ _ _ _ _ _ _ _ _ _ _ _ ]
[b]Enter the code to open the door.[/b]""",

                'answers': ['@_dittosensei'],
                'next': {'@_dittosensei' : 'w'},
                'cpu': {'@_dittosensei': 'The door opened and suddenly a bright white light shined!!!!!!!!' },
                'bg_music' : {'file' : 'assets/horror2.mp3', 'speed': 1.0}

            },

            "challenge20" : {

                'type' : 'riddle',
                'prompt' : """You found yours[b]E[/b]lf in a room with a very bright light.
A voice echoes in the room:
Answer me this and thy shall see the dark:

I’m with you every day,
But you never see me at play.
I follow your every move,
Yet never show myself to prove.

I hold your secrets tight,
But can't share a single sight.
I am the one you trust most,
But I don't ever make a boast.

I never sleep, I never rest,
But I don't carry weight, I don’t protest.
You know me well, and I know you too,
But when I leave, it's hard to find the clue.

What am I?""",

                'answers': ['shadow'],
                'next': {'shadow' : 'challenge21'},
                'cpu': {'shadow' : 'The light turned off and a hatch opened, you crawled inside.'},
                'bg_music' : {'file' : 'assets/bg_music5.mp3', 'speed': 1.0}

            },

            "challenge21" : {

                'type' : 'decode',
                'prompt' : """You crawl through the narrow hatch, heart racing.
Just as you see the exit door ahead, you feel a sharp clink around your neck.
The collar tightens, and a voice crackles through the air:

    “In other to pass, Tell me what this numbers hold."

"Each number corresponds to a letter, and the answer will unlock your escape.”

The screen before you flickers and shows the numbers:

8-5-12-12-15-23

.”""",

                'answers': ['hellow'],
                'next': {'hellow' : 'challenge22'},
                'cpu': {'hellow' : 'The collar loosened and the door opened, you exited!!!'},
                'bg_music' : {'file' : 'assets/beepbeepbeep.mp3', 'speed': 1.0}

            },

            "challenge22" : {

                'type' : 'choice',
                'prompt' : """You fell into a room full of water, gasping for air. The room is completely flooded, and water rises rapidly.
There’s no time to waste. In the distance, you see a faint glimmer through the water. The rising water is already at your waist.
A single breath, and you know you need to make a choice quickly.

You have five choices:You awaken, gasping for air. The room is completely flooded, and water rises rapidly.
There’s no time to waste. In the distance, you see a faint glimmer through the water. The rising water is already at your waist.
A single breath, and you know you need to make a choice quickly.

You have five choices:

A) Swim toward the glimmer in the distance, hoping it leads to a way out.
B) Climb onto a ledge, hoping it will carry you above the rising water.
C) Search for a grate in the floor, thinking there’s a way out below the water.
D) Try to break the window, thinking it might be a way to escape.
E) Sit still and conserve energy, hoping the water will stop rising soon.

What do you do?""",

                'answers': ['a', 'b', 'c', 'd', 'e'],
                'next': {'a': 'challenge24', 'b': 'challenge23', 'c': 'drown_down', 'd': 'drown_no', 'e' : 'drown_still'},
                'cpu': {'a' : 'You swam towards the glimmer, you found an exit, you escaped.',
                        'b' : 'you climbed onto a ledge, you found an exit, you escaped.',},
                'bg_music' : {'file' : 'assets/fall_water.mp3', 'speed': 1.0}

            },

            "drown_down" : {

                'type' : 'trap',
                'prompt' : """(TRAP) You swam down, but the water was too deep. You drowned.""",

                'answers': [],
                'next': {},
                'cpu': {},
                'bg_music' : {'file' : 'assets/drowning.mp3', 'speed': 1.0}

            },

            "drown_no" : {

                'type' : 'trap',
                'prompt' : """(TRAP) You realised there is no window, you drowned.""",

                'answers': [],
                'next': {},
                'cpu': {},
                'bg_music' : {'file' : 'assets/drowning.mp3', 'speed': 1.0}

            },

            "drown_still" : {

                'type' : 'trap',
                'prompt' : """(TRAP) You sat still, but the water kept rising. You drowned.""",

                'answers': [],
                'next': {},
                'cpu': {},
                'bg_music' : {'file' : 'assets/drowning.mp3', 'speed': 1.0}

            },

            "challenge23" : {

                'type' : 'logic',
                'prompt' : """A voice lingers in the air, you reconized it but move on.
You find yourself in a narrow corridor lit by a single red bulb.
The floor is littered with your own bloodied footsteps, repeating like a trail — walking forward, turning, returning.
You’ve been here before. You know it. But this time, at the end of the hall…

There are two doors. Identical.

Above one:

    A)[b]“The one you always choose.”[/b]

Above the other:

    B)[b]“The one you never try.”[/b]

An echo crawls into your ear:

    “Only one of them breaks the loop. The other brings you back here... again.”""",

                'answers': ['a', 'b'],
                'next': {'b' : 'challenge25', 'a': 'crazy_sound'},
                'cpu': {'b' : 'The door opens, and a voice speaks, "you near the end....and it seems you are not wearing his face anymore......are you"!!!',},
                'bg_music' : {'file' : 'assets/horror3.mp3', 'speed': 1.0}

            },

            "challenge24" : {

                'type' : 'logic',
                'prompt' : """A voice lingers in the air, you reconized it but move on.
You enter a room with no windows.
Only a broken mirror sits across from you.
You see your reflection — but it’s [i]smiling[/i]. You are not.

On the wall behind you, words appear, scratched violently into the concrete:

    "One of us remembers. One of us resets."
    "Only the [b]truth[/b] walks free."

Two prompts appear before the mirror:
🔲 A): “I am the reflection.”
🔲 B): “I am the original.”""",

                'answers': ['a', 'b'],
                'next': {'a' : 'challenge25', 'b': 'crazy_sound'},
                'cpu': {'a' : 'The mirror shatters, revealing a hidden door. A voice speaks, "you near the end....and it seems you are not wearing his face anymore......are you"!!!',},
                'bg_music' : {'file' : 'assets/horror3.mp3', 'speed': 1.0}

            },

            "crazy_sound" : {

                'type' : 'trap',
                'prompt' : """(TRAP) The lingering voice yelled, killing you instantly.""",

                'answers': [],
                'next': {},
                'cpu': {},
                'bg_music' : {'file' : 'assets/jumpscare2.mp3', 'speed': 1.0}

            },

            "challenge25" : {

                'type' : 'riddle',
                'prompt' : """You found a cold room with door and a computer.
The screen flickers on.............  
Five names appear, then vanish.

[b]“He tried.  
She failed.  
They screamed.  
It ran.  
You watched.”[/b]

A pause.............

Then, one final line:

[b]“Who’s still here?”[/b]

The cursor blinks.  
It waits for an answer.....""",

                'answers': ['me'],
                'next': {'me' : 'vb'},
                'cpu': {'me' : 'The screen flickers, and the door opens. You step through.'},
                'bg_music' : {'file' : 'assets/', 'speed': 1.0}

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
                cpu_response = current_node['cpu'].get(answer, "Result!")

                # Update the current node to the next node
                self.current_node = next_node_key

                # Get the next node's prompt
                next_node = self.dialogue_tree.get(next_node_key)

                if next_node:
                    # Debugging: Print the next node and its bg_music
                    print(f"Next node: {next_node_key}, bg_music: {next_node.get('bg_music')}")
                    return f"[b]\nCurator ->[/b] {cpu_response}\n\n[b]Next:[/b]\n{next_node['prompt']}", next_node.get('bg_music')

                # If there's no next node, end the game
                return f"[b]\nCurator ->[/b] {cpu_response}\n\nCongratulations! You've escaped the room!", bg_music

        # If no valid answer is found, return an error message
        self.current_node = 'start'  # Reset to start node
        return "[b]\nCurator ->[/b] Oh no! That's not the right answer. Too bad! (The collar explodes taking your head along with it.)", {'file': 'assets/Gory.mp3', 'speed': 1.0}