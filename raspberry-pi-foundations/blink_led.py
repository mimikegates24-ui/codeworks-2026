# traffic lights

from gpiozero import LED
From time import sleep

LedGreen =LED(2)
LedYellow =LED(4)
LedRed =LED(17)
LedOrange =LED(27)

while True:
    LedGreen.off()
    LedYellow.off()
    LedOrange.off()
    LedRed.on()
    sleep(3)
    LedGreen.off()
    LedYellow.off()
    LedOrange.on()
    LedRed.off()
    sleep(4)
    LedGreen.off()
    LedYellow.on()
    LedOrange.off()
    LedRed.off()
    sleep(5)
    LedGreen.on()
    LedYellow.off()
    LedOrange.off()
    LedRed.off()