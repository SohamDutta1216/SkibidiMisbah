import random
from typing import List, Tuple

import pygame

from .constants import BACKGROUNDS, PIPES, PLAYERS


class Images:
    numbers: List[pygame.Surface]
    game_over: pygame.Surface
    welcome_message: pygame.Surface
    base: pygame.Surface
    background: pygame.Surface
    player: Tuple[pygame.Surface]
    pipe: Tuple[pygame.Surface]

    def __init__(self) -> None:
        self.numbers = list(
            (
                pygame.image.load(f"assets/sprites/{num}.png").convert_alpha()
                for num in range(10)
            )
        )

        # game over sprite
        self.game_over = pygame.image.load(
            "assets/sprites/gameover.png"
        ).convert_alpha()
        # welcome_message sprite for welcome screen
        self.welcome_message = pygame.transform.scale(
            pygame.image.load("assets/sprites/message.png").convert_alpha(),
            (200, 100),
        )
        # base (ground) sprite
        self.base = pygame.image.load("assets/sprites/base.png").convert_alpha()
        self.randomize()

    def randomize(self):
        # select random background sprites
        rand_bg = random.randint(0, len(BACKGROUNDS) - 1)
        # select random player sprites
        rand_player = random.randint(0, len(PLAYERS) - 1)
        # select random pipe sprites
        rand_pipe = random.randint(0, len(PIPES) - 1)

        self.background = pygame.image.load(BACKGROUNDS[rand_bg]).convert()
        # Scale missy sprite to be smaller if selected
        if rand_player == 2:  # Yellow bird (missy) index
            original = pygame.image.load(
                PLAYERS[rand_player][0]
            ).convert_alpha()
            self.player = tuple(
                pygame.transform.scale(
                    pygame.image.load(PLAYERS[rand_player][i]).convert_alpha(),
                    (original.get_width() // 11, original.get_height() // 11),
                )
                for i in range(3)
            )
        else:
            self.player = tuple(
                pygame.image.load(PLAYERS[rand_player][i]).convert_alpha()
                for i in range(3)
            )
        self.pipe = (
            pygame.transform.flip(
                pygame.image.load(PIPES[rand_pipe]).convert_alpha(),
                False,
                True,
            ),
            pygame.image.load(PIPES[rand_pipe]).convert_alpha(),
        )
