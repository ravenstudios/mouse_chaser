from constants import *
import pygame
import particle


clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

particles = []
length = 10

pygame.init()
pygame.mouse.set_visible(False)





for i in range(length):
    particles.append(particle.Particle())

def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if event.key == pygame.K_r:
                    board.reset()
                if event.key == pygame.K_q:
                    running = False
        draw()
        update()

    pygame.quit()



def draw():
    surface.fill((0, 0, 0))#background

    for particle in particles:
        particle.draw(surface)

    pygame.display.flip()



def update():
    temp_pos = (0, 0)



    for i in range(len(particles)):
        if i == 0:
            temp_pos = particles[i].get_pos()
            particles[i].set_pos(pygame.mouse.get_pos())
        else:
            temp = particles[i].get_pos()
            particles[i].set_pos(temp_pos)
            temp_pos = temp


if __name__ == "__main__":
    main()
