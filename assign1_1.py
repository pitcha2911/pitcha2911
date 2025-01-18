import machine

button = machine.Pin(35, machine.Pin.IN)
led_red = machine.Pin(16, machine.Pin.OUT)

button_pressed = False


while True:
    if button.value() == 1 and not button_pressed:
        led_red.on()
        time.sleep(0.5)
        button_pressed = True
        
   elif button.value() == 0 and button_pressed:
        led_red.off()
        button_pressed = False



