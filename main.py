import pygame
import math

window_size = (640, 480)

# Initialize pygame

pygame.init()
screen = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()

# Assets

font_message = pygame.font.Font('fonts/JF-Dot-MPlus10.ttf', 10)

# Main Loop

running = True
frame = 0

while running:

    # Event polling

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear main surface

    screen.fill('black')

    # Font rendering

    color = (255, 255 - 128 * (math.floor(frame / 2) % 2), 255)
    message = 'これはpygameでフォント描画をするサンプルです.'
    message_surface = font_message.render(message, False, color)
    msg_w, msg_h = message_surface.get_size()
    screen.blit(message_surface, (window_size[0] / 2 - msg_w / 2, window_size[1] / 2 - msg_h / 2))

    # Render to display

    pygame.display.flip()

    # 60fps wait

    clock.tick(60)

    frame += 1



