# Web platform initialization
import platform
import asyncio
import os

async def web_init():
    if platform.system() == "Emscripten":
        import pygame
        
        os.environ['SDL_AUDIODRIVER'] = 'javascript'
        
        pygame.display.init()
        pygame.font.init()
        
        # Initialize audio with web-safe settings
        try:
            pygame.mixer.pre_init(44100, -16, 2, 512)
            pygame.mixer.init()
        except:
            print("Audio initialization failed")

asyncio.run(web_init()) 