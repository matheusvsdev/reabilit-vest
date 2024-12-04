import pygame
import random
import sys

# Constantes
BALL_RADIUS = 20
BALL_SPEED = 50.0
SIMULATION_TIME = 60 # 1 minuto

# Enum para os níveis de dificuldade
class Level:
    EASY = 1
    INTERMEDIATE = 2
    HARD = 3
    RETURN = 4

# Enum para os tipos de simulação
class SimulationType:
    VERTICAL =1
    HORIZONTAL = 2
    FIND_THE_BALL = 3
    RANDOM = 4

# Classe Ball
class Ball:
    def __init__(self, level):
        self.shape = pygame.Rect(0, 0, BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.x_speed = 0
        self.y_speed = 0

        if level == Level.EASY:
            self.x_speed = BALL_SPEED / 10.0
            self.y_speed = BALL_SPEED / 10.0
        elif level == Level.INTERMEDIATE:
            self.x_speed = BALL_SPEED / 4.0
            self.y_speed = BALL_SPEED / 4.0
        elif level == Level.HARD:
            self.x_speed = BALL_SPEED / 2.0
            self.y_speed = BALL_SPEED / 2.0

# Função para criar a bolinha
def create_ball(level):
    ball = Ball(level)
    ball.shape.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    return ball

# Função para criar a simulação
def create_simulation(screen, level, type_simulation):
    ball = create_ball(level)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial', 24)
    start_time = pygame.time.get_ticks()

    # Contagem regressiva de 5 segundos para iniciar simulação
    for i in range(5, 0, -1):
        screen.fill((0, 0, 0))

        font_chronometer = pygame.font.SysFont('Arial', 256)
        text_chronometer = font_chronometer.render(str(i), True, (255, 255, 255))
        screen.blit(text_chronometer, (SCREEN_WIDTH // 2 - text_chronometer.get_width() // 2,
                                       SCREEN_HEIGHT // 2 - text_chronometer.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(1000)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if SCREEN_WIDTH - 120 < event.pos[0] < SCREEN_WIDTH and SCREEN_HEIGHT - 70 < event.pos[1] < SCREEN_HEIGHT:
                    return

        if type_simulation == SimulationType.VERTICAL:
            ball.shape.move_ip(0, ball.y_speed)
            if ball.shape.top < 0:
                ball.shape.top = 0
                ball.y_speed = -ball.y_speed
            elif ball.shape.bottom > SCREEN_HEIGHT:
                ball.shape.bottom = SCREEN_HEIGHT
                ball.y_speed = -ball.y_speed

        elif type_simulation == SimulationType.HORIZONTAL:
            ball.shape.move_ip(ball.x_speed, 0)
            if ball.shape.left < 0:
                ball.shape.left = 0
                ball.x_speed = -ball.x_speed
            elif ball.shape.right > SCREEN_WIDTH:
                ball.shape.right = SCREEN_WIDTH
                ball.x_speed = -ball.x_speed
        elif type_simulation == SimulationType.FIND_THE_BALL:
            ball.shape.center = (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
        elif type_simulation == SimulationType.RANDOM:
            ball.shape.move_ip(ball.x_speed, ball.y_speed)
            if ball.shape.left < 0:
                ball.shape.left = 0
                ball.x_speed = -ball.x_speed
            elif ball.shape.right > SCREEN_WIDTH:
                ball.shape.right = SCREEN_WIDTH
                ball.x_speed = -ball.x_speed
            if ball.shape.top < 0:
                ball.shape.top = 0
                ball.y_speed = -ball.y_speed
            elif ball.shape.bottom > SCREEN_HEIGHT:
                ball.shape.bottom = SCREEN_HEIGHT
                ball.y_speed = -ball.y_speed

        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - start_time) / 1000
        if elapsed_time >= SIMULATION_TIME:
            return

        screen.fill((0, 0, 0))
        pygame.draw.ellipse(screen, (255, 0, 0), ball.shape)
        text_chronometer = font.render(str(int(SIMULATION_TIME - elapsed_time)), True, (255, 255, 255))
        screen.blit(text_chronometer, (10, 10))
        pygame.draw.rect(screen, (0, 0, 255), (SCREEN_WIDTH - 120, SCREEN_HEIGHT - 70, 100, 50))
        text_stop = font.render('Parar', True, (255, 255, 255))
        screen.blit(text_stop, (SCREEN_WIDTH - 100, SCREEN_HEIGHT - 60))
        pygame.display.flip()

        if type_simulation == SimulationType.FIND_THE_BALL:
            if level == Level.EASY:
                pygame.time.delay(1500)
            elif level == Level.INTERMEDIATE:
                pygame.time.delay(1000)
            elif level == Level.HARD:
                pygame.time.delay(500)
        else:
            clock.tick(60)

# Função para criar o menu de seleção de nível
def select_level(screen):
    font = pygame.font.SysFont('Arial', 24)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if SCREEN_WIDTH // 2 - 150 < event.pos[0] < SCREEN_WIDTH // 2 - 50 and SCREEN_HEIGHT // 2 - 25 < \
                        event.pos[1] < SCREEN_HEIGHT // 2 + 25:
                    return Level.EASY
                elif SCREEN_WIDTH // 2 - 50 < event.pos[0] < SCREEN_WIDTH // 2 + 50 and SCREEN_HEIGHT // 2 - 25 < \
                        event.pos[1] < SCREEN_HEIGHT // 2 + 25:
                    return Level.INTERMEDIATE
                elif SCREEN_WIDTH // 2 + 50 < event.pos[0] < SCREEN_WIDTH // 2 + 150 and SCREEN_HEIGHT // 2 - 25 < \
                        event.pos[1] < SCREEN_HEIGHT // 2 + 25:
                    return Level.HARD
                elif SCREEN_WIDTH - 120 < event.pos[0] < SCREEN_WIDTH and SCREEN_HEIGHT - 70 < event.pos[
                    1] < SCREEN_HEIGHT:
                    return Level.RETURN

        screen.fill((0, 0, 0))
        text_level = font.render('Selecione o nível:', True, (255, 255, 255))
        screen.blit(text_level, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))

        pygame.draw.rect(screen, (0, 0, 255), (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 25, 100, 50))
        text_easy = font.render('Fácil', True, (255, 255, 255))
        screen.blit(text_easy, (SCREEN_WIDTH // 2 - 130, SCREEN_HEIGHT // 2 - 15))

        pygame.draw.rect(screen, (0, 0, 255), (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 25, 100, 50))
        text_intermediate = font.render('Médio', True, (255, 255, 255))
        screen.blit(text_intermediate, (SCREEN_WIDTH // 2 - 30, SCREEN_HEIGHT // 2 - 15))

        pygame.draw.rect(screen, (0, 0, 255), (SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT // 2 - 25, 100, 50))
        text_hard = font.render('Difícil', True, (255, 255, 255))
        screen.blit(text_hard, (SCREEN_WIDTH // 2 + 70, SCREEN_HEIGHT // 2 - 15))

        pygame.draw.rect(screen, (0, 0, 255), (SCREEN_WIDTH - 120, SCREEN_HEIGHT - 70, 100, 50))
        text_return = font.render('Voltar', True, (255, 255, 255))
        screen.blit(text_return, (SCREEN_WIDTH - 100, SCREEN_HEIGHT - 60))

        pygame.display.flip()
        pygame.time.Clock().tick(60)



def main():
    pygame.init()
    info = pygame.display.Info()

    global SCREEN_WIDTH, SCREEN_HEIGHT
    SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('ReabilitVest')
    font = pygame.font.SysFont('Arial', 24)

if __name__ == '__main__':
    main()

