from gpiozero import LEDBoard
from signal import pause

leds = LEDBoard(10, 17, 27, 22, 18, pwm=True)

leds.value = (0.2, 0.4, 0.6, 0.8, 1.0)

pause()
