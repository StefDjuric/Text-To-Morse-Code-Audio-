from winsound import Beep
from time import sleep

morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
              'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..',

              }


# Morse Code Input
def play_morse() -> None:
    """Plays morse code from given text"""
    morse_text = input("Enter a text sequence: ").upper()
    for char in morse_text:
        if char == ' ':
            sleep(2)
        else:
            for elem in morse_dict[char]:
                if elem == '.':
                    Beep(frequency=500, duration=850)
                else:
                    Beep(frequency=500, duration=1100)


# Main
play_morse()
