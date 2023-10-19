import pygame

pygame.init()

from ball import Ball
from paddle import Paddle
from settings import BLACK, WHITE, GREY, WIDTH, HEIGHT, FPS, font20, font30, font100, clock, screen
from ai import AI
import random
from enum import Enum

 
def main():
    running = True
    pygame.display.set_caption("Pong")


    #############  start screen ##############
    player1 = Paddle(20, 0, 10, 100, 10, GREY)
    player2 = Paddle(WIDTH-30, 0, 10, 100, 10, GREY)
    init_speed = random.choice([-7, 7])
    ball = Ball(WIDTH//2, HEIGHT//2, 7, 7, WHITE)
    ai1 = AI(player1, ball, 'IMPOSSIBLE')
    ai2 = AI(player2, ball, 'IMPOSSIBLE')
    if init_speed > 0:
        ai1.is_active = False
    else:
        ai2.is_active = False
    players = [player1, player2]
    ais = [ai1, ai2]

    GameMode = Enum('GameMode', ['OnePlayerEasy','OnePlayerMedium', 'OnePlayerHard', 'TwoPlayer'])
    current_select = GameMode.TwoPlayer
    start_game = False
    while running:
        screen.fill(BLACK)

        text = font100.render("PONG", True, WHITE)
        textRect = text.get_rect()
        textRect.center = (WIDTH//2, HEIGHT//4)
        screen.blit(text, textRect)

        text = font30.render("One player", True, WHITE)
        textRectOneP = text.get_rect()
        textRectOneP.center = (WIDTH//4, 3 * HEIGHT//4)
        screen.blit(text, textRectOneP)

        text = font20.render("Easy", True, WHITE)
        textRectOnePEasy = text.get_rect()
        textRectOnePEasy.center = (WIDTH//4, 3 * HEIGHT//4 + 50)
        screen.blit(text, textRectOnePEasy)

        text = font20.render("Medium", True, WHITE)
        textRectOnePMedium = text.get_rect()
        textRectOnePMedium.center = (WIDTH//4, 3 * HEIGHT//4 + 75)
        screen.blit(text, textRectOnePMedium)

        text = font20.render("Hard", True, WHITE)
        textRectOnePHard = text.get_rect()
        textRectOnePHard.center = (WIDTH//4, 3 * HEIGHT//4 + 100)
        screen.blit(text, textRectOnePHard)

        text = font30.render("Two player", True, WHITE)
        textRectTwoP = text.get_rect()
        textRectTwoP.center = (3 * WIDTH//4, 3 * HEIGHT//4)
        screen.blit(text, textRectTwoP)

        if current_select == GameMode.TwoPlayer:
            select_box = pygame.draw.rect(screen, WHITE, textRectTwoP, 1)
        elif current_select == GameMode.OnePlayerEasy:
            select_box = pygame.draw.rect(screen, WHITE, textRectOneP, 1)
            select_box = pygame.draw.rect(screen, WHITE, textRectOnePEasy, 1)
        elif current_select == GameMode.OnePlayerMedium:
            select_box = pygame.draw.rect(screen, WHITE, textRectOneP, 1)
            select_box = pygame.draw.rect(screen, WHITE, textRectOnePMedium, 1)
        elif current_select == GameMode.OnePlayerHard:
            select_box = pygame.draw.rect(screen, WHITE, textRectOneP, 1)
            select_box = pygame.draw.rect(screen, WHITE, textRectOnePHard, 1)
        #set up the different gamemodes and difficulties
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if current_select == GameMode.TwoPlayer or current_select == GameMode.OnePlayerEasy:
                        pass
                    elif current_select == GameMode.OnePlayerMedium:
                        current_select = GameMode.OnePlayerEasy
                    else:
                        current_select = GameMode.OnePlayerMedium
                if event.key == pygame.K_s:
                    if current_select == GameMode.TwoPlayer or current_select == GameMode.OnePlayerHard:
                        pass
                    elif current_select == GameMode.OnePlayerMedium:
                        current_select = GameMode.OnePlayerHard
                    else:
                        current_select = GameMode.OnePlayerMedium
                if event.key == pygame.K_a:
                    if current_select == GameMode.TwoPlayer:
                        current_select = GameMode.OnePlayerEasy 
                if event.key == pygame.K_d:
                    if current_select != GameMode.TwoPlayer:
                        current_select = GameMode.TwoPlayer
                if event.key == pygame.K_SPACE:
                    start_game = True
        
        if start_game:
            break
        #this code handles the collisions for the main screen 
        for i in range(len(players)):
            if pygame.Rect.colliderect(ball.getRect(), players[i].getRect()):
                #section = player.getSection(ball)
                ball.hit2()
                ais[i].is_active = False
                ais[-1 - i].is_active = True

        ai1.update()
        ai2.update()
        ball.update()

        player1.display()
        player2.display()
        ball.display()

        pygame.display.update()
        clock.tick(FPS)  

    ########### end start screen ###########


    # Defining the objects
    player1 = Paddle(20, 0, 10, 100, 10, WHITE)
    player2 = Paddle(WIDTH-30, 0, 10, 100, 10, WHITE)
    ball = Ball(WIDTH//2, HEIGHT//2, 7, 7, WHITE)
    if current_select == GameMode.OnePlayerEasy:
        ai = AI(player2, ball, 'EASY')
    elif current_select == GameMode.OnePlayerMedium:
        ai = AI(player2, ball, 'MEDIUM')
    elif current_select == GameMode.OnePlayerHard:
        ai = AI(player2, ball, 'HARD')
    else:
        ai = None
 
    players = [player1, player2]
 
    # Initial parameters of the players
    player1Score, player2Score = 0, 0
    player1YFac, player2YFac = 0, 0
 
    while running:
        screen.fill(BLACK)
 
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player2YFac = -1
                if event.key == pygame.K_DOWN:
                    player2YFac = 1
                if event.key == pygame.K_w:
                    player1YFac = -1
                if event.key == pygame.K_s:
                    player1YFac = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player2YFac = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player1YFac = 0
 
        # Collision detection for actual gameplay
        for player in players:
            if pygame.Rect.colliderect(ball.getRect(), player.getRect()):
                section = player.getSection(ball)
                ball.hit(section)
       
        ball.update()
        # Updating the objects
        player1.update(player1YFac)
        if current_select != GameMode.TwoPlayer:
            if ai is not None:
                ai.update()
        else:
            player2.update(player2YFac)
        
        #If the ball goes out of bounds the left side, Player 2 scores
        if ball.posx <= 0:
            player2Score += 1
            ball.reset()
            if ai is not None:
                ai.reset()

        # If the ball goes out of bounds on the right side, Player 1 scores
        if ball.posx >= WIDTH:
            player1Score += 1
            ball.reset()
            if ai is not None:
                ai.reset()
 
        # Displaying the objects on the screen
        player1.display()
        player2.display()
        ball.display()
 
        # Displaying the scores of the players
        player1.displayScore("Player 1 : ", player1Score, 100, 20, WHITE)
        player2.displayScore("Player 2: ", player2Score, WIDTH-100, 20, WHITE)
 
        pygame.display.update()
        clock.tick(FPS)    
 
 
if __name__ == "__main__":
    main()
    pygame.quit()