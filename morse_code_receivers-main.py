from microbit import *
import radio

radio.config(group=6)
radio.on()

morse_code_map = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G",
    "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N",
    "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U",
    "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z",
    ".----": "1", "..---": "2", "...--": "3", "....-": "4", ".....": "5",
    "-....": "6", "--...": "7", "---..": "8", "----.": "9", "-----": "0"
}

# Define your substitution cipher mapping
cipher_map = {
    "A": "Q", "B": "R", "C": "S", "D": "T", "E": "U", "F": "V", "G": "W",
    "H": "X", "I": "Y", "J": "Z", "K": "A", "L": "B", "M": "C", "N": "D",
    "O": "E", "P": "F", "Q": "G", "R": "H", "S": "I", "T": "J", "U": "K",
    "V": "L", "W": "M", "X": "N", "Y": "O", "Z": "P",
    "1": "9", "2": "8", "3": "7", "4": "6", "5": "5",
    "6": "4", "7": "3", "8": "2", "9": "1", "0": "0"
}

def decode_morse(morse_word):
    decoded_word = ''.join([morse_code_map.get(code, '') for code in morse_word.split(' ')])
    decoded_message = ''.join([cipher_map.get(decoded_word[i:i+2], '?') for i in range(0, len(decoded_word), 2)])
    return decoded_message

def receive_morse():
    morse_code = ''
    while True:
        signal = radio.receive()
        if signal:
            morse_code += signal
        else:
            break
    return morse_code

while True:
    morse_signal = receive_morse()
    decoded_message = decode_morse(morse_signal)
    display.scroll(decoded_message)
    sleep(4000)  # Display for 4 seconds, adjust as needed
    display.clear()
