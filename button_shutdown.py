from gpiozero import Button
from subprocess import check_call
from signal import pause

def shutdown():
    check_call(['ls', '-lisa'])

shutdown_btn = Button(17)
shutdown_btn.when_pressed = shutdown

pause()
