# Web platform initialization
import platform
import asyncio
import os

if platform.system() == "Emscripten":
    import pygame
    
    # Web-specific initialization
    os.environ['SDL_AUDIODRIVER'] = 'javascript'
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
    
    pygame.display.init()
    pygame.font.init()
    
    # Safe audio initialization
    try:
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.mixer.init()
    except:
        print("Web audio initialization failed - continuing without audio")

asyncio.run(web_init()) 