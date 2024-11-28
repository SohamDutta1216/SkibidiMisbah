import asyncio
import platform
import pygame

from src.flappy import Flappy


async def main():
    # Special handling for web platform
    if platform.system() == "Emscripten":
        pygame.display.init()
        pygame.font.init()
        
        # Initialize audio for web
        pygame.mixer.init()
        pygame.mixer.pre_init(44100, -16, 2, 512)
        
        # Set up web-specific display
        pygame.display.set_mode((288, 512), pygame.SCALED)
    
    game = Flappy()
    await game.start()


if __name__ == "__main__":
    asyncio.run(main())
