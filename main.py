import pygame
from constants import *
from variables import player_img, sprites, walls, bullets, stars, enemies
from player import Player
from map import Map

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tanks')

clock = pygame.time.Clock()

background = pygame.Surface((1050, 800))
background_rect = background.get_rect()

font_name = pygame.font.match_font('arial')


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def show_go_screen():
    screen.blit(background, background_rect)
    draw_text(screen, "Tanks!", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Arrow keys move, Space to fire", 22,
              WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "Press up key to begin", 18, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False


def main():
    run = True
    game_over = True

    while run:
        clock.tick(FPS)
        if game_over:
            sprites.empty()
            walls.empty()
            stars.empty()
            enemies.empty()
            show_go_screen()
            game_over = False
            player = Player(player_img.convert())
            sprites.add(player)
            Map()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()

        sprites.update()

        pygame.sprite.groupcollide(walls, bullets, True, True)
        pygame.sprite.groupcollide(stars, bullets, True, True)
        pygame.sprite.groupcollide(enemies, bullets, True, True)

        screen.fill(GRAY)
        sprites.draw(screen)

        pygame.display.flip()

        if len(enemies.sprites()) == 0:
            game_over = True

        if len(stars.sprites()) == 0:
            game_over = True

    pygame.quit()


main()
