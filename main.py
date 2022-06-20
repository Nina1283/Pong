from microbit import *
import random


# Startposition und Länge des Paddles
paddle_x = 0
paddle_y = 4
paddle_length = 2

# Startposition und Richtung des Balls 
ball_x = 2
ball_y = 1
# Zufällige Startrichtung
direction_x = random.choice([1, -1])
direction_y = random.choice([1, -1])

last_update = running_time()

game_over = False

score = 0
update_interval = 400

while not game_over:
    # Paddlesteuerungen
    if button_a.was_pressed() and paddle_x > 0:
        paddle_x = (paddle_x - 1)
    if button_b.was_pressed() and paddle_x < 3:
        paddle_x = (paddle_x + 1)

    # Ballrichtungsveränderung
    if running_time() - last_update > update_interval:
        last_update = running_time()
        
        if (ball_x == 0): # Wenn Ball am linken Rand ist, soll er sich nach rechts bewegen
            direction_x = 1    
        elif (ball_x == 4): # Wenn Ball am rechten Rand ist, soll er sich nach links bewegen
            direction_x = -1

        if (ball_y == 0): # Wenn Ball oben am Rand ist, soll er sich nach unten bewegen
            direction_y = 1
        elif (ball_y == 4): # Wenn Ball unten am Rand ist, dann ist das Spiel vorbei
            game_over = True
            break
    
        # Kollisionserkennung - Ball direkt über Paddle
        if ball_y == 3:
            # Ist Ball links?
            if ball_x == paddle_x:
                direction_y = -1
                score = score + 1
                update_interval = update_interval - 10
            # Ist Ball rechts?
            elif ball_x == paddle_x + 1:
                direction_y = -1
                score = score + 1
                update_interval = update_interval - 10
            # Ist Ball an linker Ecke?
            elif ball_x == paddle_x - 1:
                direction_y = -1
                direction_x = -1
                if (ball_x == 0): # Wenn Ball am linken Rand ist, soll er sich nach rechts bewegen
                    direction_x = 1
                score = score + 1
                update_interval = update_interval - 10
            # Ist Ball an rechter Ecke?
            elif ball_x == paddle_x + 2:
                direction_y = -1
                direction_x = 1
                if (ball_x == 4): # Wenn Ball am rechten Rand ist, soll er sich nach links bewegen
                    direction_x = -1
                score = score + 1
                update_interval = update_interval - 10

        ball_x = (ball_x + direction_x) # Ball bewegt sich einen Schritt weiter nach rechts oder links
        ball_y = (ball_y + direction_y) # Ball bewegt sich einen Schritt weiter nach oben oder unten
    
    display.clear()
    # Zeichne das Paddle
    for offset in range(paddle_length):
        display.set_pixel(paddle_x + offset, paddle_y, 9)
    #sleep(16) #16 Millisekunden Pause

    display.set_pixel(ball_x, ball_y, 9)
    sleep(16) #400 Millisekunden Pause bis Ball sich bewegt

display.show(Image.SKULL)
sleep(5000)
display.scroll(score)
