import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Definir as dimensões da tela
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo Simples em 2D")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Variáveis do jogador
player_width = 50
player_height = 50
player_x = (WIDTH - player_width) // 2
player_y = HEIGHT - player_height - 30
player_speed = 5

clock = pygame.time.Clock()

# Função principal do jogo
def main():
    global player_x

    # Loop principal do jogo
    while True:
        SCREEN.fill(WHITE)

        # Eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Controles do jogador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed

        # Limitar a posição do jogador dentro da tela
        if player_x < 0:
            player_x = 0
        elif player_x > WIDTH - player_width:
            player_x = WIDTH - player_width

        # Desenhar o jogador
        pygame.draw.rect(SCREEN, RED, (player_x, player_y, player_width, player_height))

        # Atualizar a tela
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
