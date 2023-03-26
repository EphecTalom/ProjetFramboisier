'''
module servant à collecter un signal infra rouge par le biais de get_ir
renvoie le signal sous forme d'un nombre binaire
'''
import RPi.GPIO as GPIO
from time import time
ir_pin=12
def setup():
    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    GPIO.setup(ir_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def binary_aquire(pin, duration):
    # aquires data as quickly as possible
    t0 = time()
    results = []
    while (time() - t0) < duration:
        results.append(GPIO.input(pin))
    return results


def on_ir_receive(pinNo, bouncetime=150):
    # when edge detect is called (which requires less CPU than constant
    # data acquisition), we acquire data as quickly as possible
    data = binary_aquire(pinNo, bouncetime/1000.0)
    oldval=1
    lastindex=0
    index=0

    #print('len data, data: ', len(data), data)
    #print('len gaps,gaps',len(gaps),gaps)
    if len(data) < bouncetime:
        return
    rate = len(data) / (bouncetime / 1000.0)
    pulses = []
    i_break = 0
    # detect run lengths using the acquisition rate to turn the times in to microseconds
    for i in range(1, len(data)):
        if (data[i] != data[i-1]) or (i == len(data)-1):
            pulses.append((data[i-1], int((i-i_break)/rate*1e6)))
            i_break = i

    outbin = ""
    for val, us in pulses:
        if val != 1:
            continue
        if outbin and us > 2000:
            break
        elif us < 1000:
            outbin += "0"
        elif 1000 < us < 2000:
            outbin += "1"
    try:
        return int(outbin, 2)
    except ValueError:
        # probably an empty code
        return None


def destroy():
    GPIO.cleanup()


def get_ir():
    setup()
    try:
        print("Waiting for signal")
        GPIO.wait_for_edge(ir_pin, GPIO.FALLING)
        code = on_ir_receive(ir_pin)
        if code:
            return(code)
        else:
            print("Invalid code")
    except KeyboardInterrupt:
        # User pressed CTRL-C
        # Reset GPIO settings
        print("Ctrl-C pressed!")
    except RuntimeError:
        # this gets thrown when control C gets pressed
        # because wait_for_edge doesn't properly pass this on
        pass
    destroy()
    print("exit")

def dane_Elec(code):
    if code == 2155831455:
        return '1'
    if code == 2155841910:
        return '2'
    if code == 2155840125:
        return '3'
    if code == 2155833495:
        return '4'
    if code == 2155807485:
        return '5'
    if code == 2155850325:
        return '6'
    if code == 2155839870:
        return '7'
    if code == 2155811565:
        return '8'
    if code == 2155823805:
        return '9'
    if code == 2155819725:
        return '0'
    if code == 2155868175:
        return 'goto'
    if code == 2155813350:
        return 'slow'
    if code == 2155809015:
        return 'option'
    if code == 2155837575:
        return 'play'
    if code == 2155847775:
        return 'stop'
    if code == 2155813095:
        return 'pause'
    if code == 2155864095:
        return 'prew'
    if code == 2155808505:
        return 'next'
    if code == 2155843695:
        return 'fr'
    if code == 2155853895:
        return 'ff'
    if code == 2155831965:
        return 'subtitle'
    if code == 2155819215:
        return 'display'
    if code == 2155807230:
        return 'audio'
    if code == 2155825590:
        return 'zoom'
    if code == 2155811055:
        return 'time shift'
    if code == 2155851855:
        return 'repeat'
    if code == 2155827375:
        return 'select'
    if code == 2155815390:
        return 'confirm'
    if code == 2155815135:
        return 'return'
    if code == 2155810545:
        return 'setup'
    if code == 2155821255:
        return 'power'
    if code == 2155844205:
        return 'tv system'
    if code == 2155817175:
        return 'mute'
    if code == 2155864605:
        return 'rec'
    if code == 2155817685:
        return 'browser'
    if code == 2155858485:
        return 'timer'
    if code == 2155864350:
        return 'copy'
    if code == 2155862055:
        return 'guide'
    if code == 2155839615:
        return 'vol-'
    if code == 2155809525:
        return 'vol+'
    if code == 2155855935:
        return 'up'
    if code == 2155823295:
        return 'down'
    if code == 2155835535:
        return 'left'
    if code == 2155829415:
        return 'right'
    if code == 2155845735:
        return 'enter'
while True:
    dane_Elec(get_ir())
