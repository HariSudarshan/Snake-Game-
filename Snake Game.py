

import random
import pygame

# Initialize pygame
pygame.init()

# Define colors
white = (255, 255, 255)  # snake
black = (0, 0, 0)  # background
red = (255, 0, 0)  # message
orange = (255, 165, 0)  # food

# Set the width and height of the screen
width, height = 600, 400

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hari Snake Game")

clock = pygame.time.Clock()

# Set the snake size and speed
snake_size = 10
snake_speed = 15

message_font = pygame.font.SysFont('Times New Roman', 20)
score_font = pygame.font.SysFont('Times New Roman', 20)

def print_score(score):
    text = score_font.render("Score: " + str(score), True, orange)
    game_display.blit(text, [0, 0])

def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, white, [pixel[0], pixel[1], snake_size, snake_size])

def run_game():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2
    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1

    target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    while not game_over:

        while game_close:
            game_display.fill(black)
            game_over_message = message_font.render("Game Over!!!! Press 1-Quit or 2-Restart ", True, red)
            game_display.blit(game_over_message, [width / 6, height / 3])
            print_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_2:
                        run_game()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_speed
        y += y_speed

        game_display.fill(black)
        pygame.draw.rect(game_display, orange, [int(target_x), int(target_y), snake_size, snake_size])
        snake_pixels.append([x, y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                game_close = True

        draw_snake(snake_size, snake_pixels)
        print_score(snake_length - 1)

        pygame.display.update()

        if x == target_x and y == target_y:
            target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

run_game()




















