import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
screen.fill((255, 255, 255))

color_ball = (255, 0, 0)
radius = 25
x, y = 200, 150
clock = pygame.time.Clock()

done = False

while not done:
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, color_ball, (x, y), radius)
        pygame.display.update()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP] and y - radius > 0:
                y -= 20  # Move up by 20 pixels
        elif pressed[pygame.K_DOWN] and y + radius < 300:
                y += 20  # Move down by 20 pixels
        elif pressed[pygame.K_LEFT] and x - radius > 0:
                x -= 20  # Move left by 20 pixels
        elif pressed[pygame.K_RIGHT] and x + radius < 400:
                x += 20  # Move right by 20 pixels

        clock.tick(60)

        pygame.display.flip()

