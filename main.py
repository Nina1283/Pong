from microbit import *

paddle_x = 0
paddle_y = 4
paddle_length = 2

while True:
    if button_a.was_pressed() and paddle_x > 0:
        paddle_x = (paddle_x - 1)
    if button_b.was_pressed() and paddle_x < 3:
        paddle_x = (paddle_x + 1)
    
    display.clear()
    # Zeichne das Paddle
    for offset in range(paddle_length):
        display.set_pixel(paddle_x + offset, paddle_y, 9)
    sleep(16) #16 Millisekunden Pause
