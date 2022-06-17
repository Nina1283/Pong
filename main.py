from microbit import *


paddle_x = 0
paddle_y = 4
paddle_length = 2

ball_x = 2
ball_y = 0
direction_x = 1
direction_y = 1
last_update = running_time()

while True:
    if button_a.was_pressed() and paddle_x > 0:
        paddle_x = (paddle_x - 1)
    if button_b.was_pressed() and paddle_x < 3:
        paddle_x = (paddle_x + 1)

    if running_time() - last_update > 400:
        last_update = running_time()
        
        if (ball_x == 0):
            direction_x = 1
        elif (ball_x == 4):
            direction_x = -1

        if (ball_y == 0):
            direction_y = 1
        elif (ball_y == 4):
            direction_y = -1
    
        ball_x = (ball_x + direction_x) # Ball bewegt sich einen Schritt weiter nach rechts oder links
        ball_y = (ball_y + direction_y)
    
    display.clear()
    # Zeichne das Paddle
    for offset in range(paddle_length):
        display.set_pixel(paddle_x + offset, paddle_y, 9)
    #sleep(16) #16 Millisekunden Pause

    display.set_pixel(ball_x, ball_y, 9)
    sleep(16) #400 Millisekunden Pause bis Ball sich bewegt
