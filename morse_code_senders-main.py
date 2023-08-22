from microbit import *
import radio

radio.config(group=6)
radio.on()

def send_signal(signal):
    radio.send(signal)
    sleep(200)  # Adjust the interval if needed

while True:
    if button_a.was_pressed():
        display.show('.')
        send_signal('.')
        display.clear()
        
    elif button_b.was_pressed():
        display.show('-')
        send_signal('-')
        display.clear()