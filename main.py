import math
import pygame
import time
import random


def random_food(size):
    return random.randint(1, size)


def game(width, height, speed):
    pygame.init()
    dis = pygame.display.set_mode((width, height))
    pygame.display.update()

    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    pink = (232, 174, 242)

    pygame.display.set_caption("Lepszy snake")
    game_over = False

    x1 = width / 2
    y1 = height / 2

    x1_c = 0
    y1_c = 0

    score = 0
    # size of snakes head
    x_snake = width * 0.025
    y_snake = width * 0.025

    font_style = pygame.font.SysFont(None, 50)

    def message(msg, color):
        msg = font_style.render(msg, True, color)
        dis.blit(msg, [width / 2, height / 3])

    def scoreDis(score_):
        msg = "Score: " + str(score_)
        msg = font_style.render(msg, True, black)
        dis.blit(msg, [2 * x_snake, height - 5  * x_snake])

    clock = pygame.time.Clock()
    i = 0
    x_food = random_food(width - x_snake)
    y_food = random_food(height - x_snake)


    snake_lenght = 1
    snake_list = []

    def our_snake(snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, black, [x[0], x[1], x_snake, x_snake])

    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)

    lastPressedKey = 'none'

    while not game_over:
        i += 1
        if math.fabs(x1) == width or math.fabs(y1) == height or x1 == 0 or y1 == 0:
            game_over = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if lastPressedKey != 'right':
                        x1_c = -x_snake
                        y1_c = 0
                        lastPressedKey = 'left'

                elif event.key == pygame.K_RIGHT:
                    if lastPressedKey != 'left':
                        x1_c = x_snake
                        y1_c = 0
                        lastPressedKey = 'right'

                elif event.key == pygame.K_DOWN:
                    if lastPressedKey != 'up':
                        y1_c = y_snake
                        x1_c = 0
                        lastPressedKey = 'down'

                elif event.key == pygame.K_UP:
                    if lastPressedKey != 'down':
                        y1_c = -y_snake
                        x1_c = 0
                        lastPressedKey = 'up'

        x1 += x1_c
        y1 += y1_c

        dis.fill(pink)

        if math.fabs(x1 - x_food) < x_snake and math.fabs(y1 - y_food) < x_snake:
            x_food = random_food(width - x_snake)
            y_food = random_food(height - x_snake)
            snake_lenght += 1
            score += 1
            speed += 1

        pygame.draw.rect(dis, red, [x_food, y_food, x_snake, x_snake])
        if len(snake_list) == snake_lenght:
            del snake_list[0]
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        our_snake(snake_list)
        # pygame.draw.rect(dis, black, [x1, y1, x_snake, y_snake])

        scoreDis(score)
        pygame.display.update()
        clock.tick(speed)
    message("You lost", red)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()


if __name__ == '__main__':
    game(800, 800, 10)
