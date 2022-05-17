import pyttsx3


def convert_text(text):
    engine = pyttsx3.init()
    engine.save_to_file(text, 'last_sound.mp3')
    engine.runAndWait()
    return
