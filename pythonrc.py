# Web platform initialization
import platform
import asyncio

if platform.system() == "Emscripten":
    import pygame
    
    pygame.display.init()
    pygame.font.init()
    pygame.mixer.init(frequency=44100)
