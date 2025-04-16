from kivy.core.audio import SoundLoader

sound = SoundLoader.load('assets/jumpscare.mp3')
if sound:
    print(f"Sound loaded: {sound.source}")
    print(f"Sound length: {sound.length} seconds")
    sound.play()
else:
    print("Failed to load sound")