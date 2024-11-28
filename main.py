import asyncio
import platform
import pygame

from src.flappy import Flappy


async def main():
    # Special handling for web platform
    if platform.system() == "Emscripten":
        pygame.display.init()
        pygame.font.init()
        
        # Initialize audio with lower buffer size for web
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.mixer.init()
        
        # Force SCALED mode for web
        pygame.display.set_mode((288, 512), pygame.SCALED | pygame.RESIZABLE)
        
        # Wait for user interaction before starting audio
        await asyncio.sleep(0.1)
    
    game = Flappy()
    await game.start()


if __name__ == "__main__":
    asyncio.run(main())
