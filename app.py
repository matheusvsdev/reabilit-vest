import pygame
import random
import sys

# Constantes
BALL_RADIUS = 20
BALL_SPEED = 50.0
SIMULATION_TIME = 60 # 1 minuto

# Enum para os níveis de dificuldade
class Level:
    FACIL = 1
    MEDIO = 2
    DIFICIL = 3
    VOLTAR = 4

# Enum para os tipos de simulação
class SimulationType:
    VERTICAL =1
    HORIZONTAL = 2
    FIND_THE_BALL = 3
    RANDOM = 4
