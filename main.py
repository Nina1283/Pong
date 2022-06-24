from microbit import *
import music
import random


# Startposition und Länge des Paddles
paddle_x = 1
paddle_y = 4
paddle_length = 2

# Startposition und Richtung des Balls 
ball_x = 2
ball_y = 1
# Zufällige Startrichtung
direction_x = random.choice([1, -1])
direction_y = random.choice([1, -1])

# Speichere aktuelle Laufzeit
last_ball_update = running_time()
# Ballbewegung alle 400 ms fühlt sich gut an
ball_update_interval = 400

score = 0

while True:
    # Paddlesteuerungen
    # bewege Paddle nach links, wenn möglich
    if button_a.was_pressed() and paddle_x > 0:
        paddle_x = (paddle_x - 1)
    # bewege Paddle nach rechts, wenn möglich
    if button_b.was_pressed() and paddle_x < 3:
        paddle_x = (paddle_x + 1)

    # Ballrichtungsveränderung
    # Bewege den Ball nur alle 400 ms
    if running_time() - last_ball_update > ball_update_interval:
        last_ball_update = running_time()
        
        if (ball_x == 0): # Wenn Ball am linken Rand ist, soll er sich nach rechts bewegen
            direction_x = 1    
        elif (ball_x == 4): # Wenn Ball am rechten Rand ist, soll er sich nach links bewegen
            direction_x = -1

        if (ball_y == 0): # Wenn Ball oben am Rand ist, soll er sich nach unten bewegen
            direction_y = 1
        elif (ball_y == 4): # Wenn Ball unten am Rand ist, dann ist das Spiel vorbei
            break
    
        # Kollisionserkennung - Ball direkt über Paddle
        if ball_y == 3:
            # Ist Ball links?
            if ball_x == paddle_x:
                direction_y = -1
                score = score + 1
                # erhöhe Ballgeschwindigkeit um 10 ms
                ball_update_interval = ball_update_interval - 10
            # Ist Ball rechts?
            elif ball_x == paddle_x + 1:
                direction_y = -1
                score = score + 1
                ball_update_interval = ball_update_interval - 10
            # Ist Ball an linker Ecke?
            elif ball_x == paddle_x - 1:
                direction_y = -1
                direction_x = -1
                if (ball_x == 0): # Wenn Ball am linken Rand ist, soll er sich nach rechts bewegen
                    direction_x = 1
                score = score + 1
                ball_update_interval = ball_update_interval - 10
            # Ist Ball an rechter Ecke?
            elif ball_x == paddle_x + 2:
                direction_y = -1
                direction_x = 1
                if (ball_x == 4): # Wenn Ball am rechten Rand ist, soll er sich nach links bewegen
                    direction_x = -1
                score = score + 1
                ball_update_interval = ball_update_interval - 10

        ball_x = (ball_x + direction_x) # Ball bewegt sich einen Schritt weiter nach rechts oder links
        ball_y = (ball_y + direction_y) # Ball bewegt sich einen Schritt weiter nach oben oder unten
    
    # "Bildschirm" leeren
    display.clear()
    # Zeichne das Paddle
    for offset in range(paddle_length):
        display.set_pixel(paddle_x + offset, paddle_y, 9)
    # Zeichne den Ball
    display.set_pixel(ball_x, ball_y, 9)
    sleep(16) # Bildwiederholrate ca. 60 fps

display.show(Image.SKULL)
set_volume(30)
music.play(music.NYAN, wait=False)
sleep(2000)
display.scroll(score)
sleep(1000)
speaker.off()
