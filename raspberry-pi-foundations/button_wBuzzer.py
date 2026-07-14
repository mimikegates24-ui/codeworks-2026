from gpiozero import Button, TonalBuzzer
from gpiozero.tones import Tone
from time import sleep

# GPIO pins
button = Button(14)
buzzer = TonalBuzzer(17)

tempo = 180
whole_note = (60000 * 4) / tempo

# Note frequencies
E5 = 659
D5 = 587
FS4 = 370
GS4 = 415
CS5 = 554
B4 = 494
D4 = 294
E4 = 330
A4 = 440
CS4 = 277

melody = [
    (E5, 8),
    (D5, 8),
    (FS4, 4),
    (GS4, 4),
    (CS5, 8),
    (B4, 8),
    (D4, 4),
    (E4, 4),
    (B4, 8),
    (A4, 8),
    (CS4, 4),
    (E4, 4),
    (A4, 2),
]

def play_song():
    print("Playing...")

    for frequency, divider in melody:
        note_duration = whole_note / divider
        play_time = note_duration * 0.9 / 1000
        pause_time = note_duration / 1000

        buzzer.play(Tone.from_frequency(frequency))
        sleep(play_time)
        buzzer.stop()
        sleep(max(0, pause_time - play_time))

print("Press the button to play the tune.")

while True:
    button.wait_for_press()
    play_song()
    button.wait_for_release()