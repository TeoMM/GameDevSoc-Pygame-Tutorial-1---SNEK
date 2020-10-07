import pygame
import random

pygame.init()

color_white = (255, 255, 255)
color_yellow = (255, 255, 102)
color_black = (0, 0, 0)
color_red = (213, 50, 80)
color_green = (100, 200, 50)
color_blue = (173, 216, 230)

display_width = 600
display_height = 400

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snek')

clock = pygame.time.Clock()

snake_particle = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("arial", 35)


def show_score(score):
    value = score_font.render("Score: " + str(score), True, color_yellow)
    display.blit(value, [0, 0])


def snake(snake_particle, snake_array):
    for x in snake_array:
        pygame.draw.rect(display, color_black, [
                         x[0], x[1], snake_particle, snake_particle])


def message(msg, color, x, y):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [x, y])


def gameLoop():
    game_closed = False
    game_lost = False

    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    # create snake with length 3
    snake_array = []
    snake_length = 3
    for x in range(snake_length - 1, 0, -1):
        snake_array.append([x1, y1 + x * snake_particle])

    food_posX = round(random.randrange(
        0, display_width - snake_particle) / 10.0) * 10.0
    food_posY = round(random.randrange(
        0, display_height - snake_particle) / 10.0) * 10.0

    while not game_closed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_closed = True

            elif event.type == pygame.KEYDOWN:
                if game_lost == False:
                    if event.key == pygame.K_LEFT:
                        if x1 - snake_particle != snake_array[-2][0]:
                            x1_change = -snake_particle
                            y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        if x1 + snake_particle != snake_array[-2][0]:
                            x1_change = snake_particle
                            y1_change = 0
                    elif event.key == pygame.K_UP:
                        if y1 - snake_particle != snake_array[-2][1]:
                            x1_change = 0
                            y1_change = -snake_particle
                    elif event.key == pygame.K_DOWN:
                        if y1 + snake_particle != snake_array[-2][1]:
                            x1_change = 0
                            y1_change = snake_particle

                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                            game_closed = True
                            game_lost = False
                        if event.key == pygame.K_r:
                            gameLoop()

        if game_lost == True:
            display.fill(color_blue)
            message("LMAO NOOB",
                    color_red, display_width * 0.15, display_height * 0.35)
            message("R - Replay || Q / ESC - Quit", color_red,
                    display_width * 0.15, display_height * 0.50)
            show_score(snake_length - 3)

        else:
            if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
                game_lost = True

            x1 += x1_change
            y1 += y1_change

            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            if snake_Head != snake_array[-1]:
                snake_array.append(snake_Head)
                if len(snake_array) > snake_length:
                    del snake_array[0]

            for x in snake_array[:-1]:
                if x == snake_Head:
                    game_lost = True

            if game_lost == False and x1 == food_posX and y1 == food_posY:
                food_posX = round(random.randrange(
                    0, display_width - snake_particle) / 10.0) * 10.0
                food_posY = round(random.randrange(
                    0, display_height - snake_particle) / 10.0) * 10.0
                snake_length += 1

            display.fill(color_blue)
            pygame.draw.rect(display, color_green, [
                             food_posX, food_posY, snake_particle, snake_particle])

            snake(snake_particle, snake_array)
            show_score(snake_length - 3)

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
