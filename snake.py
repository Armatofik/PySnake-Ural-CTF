import sys

import pygame
import time
import random
from cip2 import OO0OO0ooO as O0
from cip import O0OO00oo0 as OO

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

res_flag = O0[46]+O0[17]+O0[0]+O0[11]+O0[28]+O0[45]+O0[31]+OO[90]+OO[5]+OO[23]+O0[0]+O0[10]+OO[3]+OO[88]+OO[1]+O0[18]+OO[88]+OO[0]+OO[21]+O0[3]+OO[67]+O0[5]+O0[20]+OO[23]+OO[88]+OO[6]+OO[4]+OO[22]+O0[4]+OO[92]

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snaaaaake')

clock = pygame.time.Clock()

snake_block = 10


font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def Your_score(score):
    pygame.display.set_caption('Snaaaaake. Your Score: ' + str(score))


def our_snake(snake_block, snake_list):
    for i, x in enumerate(snake_list):
        pygame.draw.rect(dis, red, [x[0], x[1], snake_block, snake_block])
        if i != 0:
            pygame.draw.rect(dis, black, [snake_list[i-1][0], snake_list[i-1][1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def message2(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 2])


def gameLoop():
    snake_speed = 15

    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("Game over! C - заново, Q - выход.", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
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

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        if Length_of_snake - 1 >= 30:
            while game_close:
                dis.fill(blue)
                message("Вы побили мой рекорд! Ваш флаг: ", red)
                message2(f"{res_flag}", black)
                Your_score(Length_of_snake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                            game_over = True
                            game_close = False
        elif Length_of_snake - 1 == 10:
            snake_speed = 25
        elif Length_of_snake - 1 == 20:
            snake_speed = 30

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()


gameLoop()
