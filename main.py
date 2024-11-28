import asyncio
import platform

from src.flappy import Flappy


async def main():
    # Special handling for web platform
    if platform.system() == "Emscripten":
        import pygame

        pygame.display.init()
        pygame.font.init()

    game = Flappy()
    await game.start()


if __name__ == "__main__":
    asyncio.run(main())
