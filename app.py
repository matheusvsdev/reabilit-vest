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

