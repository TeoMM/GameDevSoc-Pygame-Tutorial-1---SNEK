import pygame
import time
import random

pygame.init()

color_yellow = (255, 255, 102)
color_black = (0, 0, 0)
color_red = (213, 50, 80)
color_green = (0, 255, 0)
color_blue = (50, 153, 213)

display_width = 600
display_height = 400

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('SNEK WITH PYTON')


snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("arial", 35)


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, color_yellow)
    display.blit(value, [0, 0])


def snake(snake_block, snake_Array):
    for x in snake_Array:
        pygame.draw.rect(display, color_black, [
                         x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [display_width * 0.15, display_height * 0.30])


def gameLoop():
    game_over = False
    game_close = False

    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    snake_Array = []
    snake_length = 1

    food_x = round(random.randrange(
        0, display_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(
        0, display_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            display.fill(color_blue)
            message("You a dum dum, R - restart || Q / ESC - Quit", color_red)
            Your_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        display.fill(color_blue)
        pygame.draw.rect(display, color_green,
                         [food_x, food_y, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_Array.append(snake_Head)
        if len(snake_Array) > snake_length:
            del snake_Array[0]

        for x in snake_Array[:-1]:
            if x == snake_Head:
                game_close = True

        snake(snake_block, snake_Array)
        Your_score(snake_length - 1)
        pygame.display.update()

        # if you eat food, generate another
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(
                0, display_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(
                0, display_height - snake_block) / 10.0) * 10.0
            snake_length += 1

    pygame.quit()
    quit()


gameLoop()
