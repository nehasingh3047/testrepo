import pygame

from star import Star
print('\n\n')


def run():
    width = 1100
    height = 800
    background_color = (0, 0, 0)

    scrn = pygame.display.set_mode(size=(width, height))
    close = False
    star_list = [Star(width, height)
                 for _ in range(300)]
    clock = pygame.time.Clock()
    while not close:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                close = True
        scrn.fill(background_color)
        for s in star_list:
            s.show(scrn)
        clock.tick(60)
        fps = clock.get_fps()
        # print(fps)
        pygame.display.flip()


if __name__ == '__main__':
    run()
