import os
from typing import Union

import keyboard
import pygame
from pygame import Surface, SurfaceType

__author__ = "Shevan Fernando"
__email__ = "w.k.b.s.t.fernando@gmail.com"
__version__ = "1.0"
__license__ = "GNU"

# initialize pygame
pygame.init()


def __create_screen(display=1, width=1280, height=720) -> Union[Surface, SurfaceType]:
    """
    Create screen and return screen obj

    :rtype: Union[Surface, SurfaceType]
    """
    if pygame.display.get_num_displays() > 1:
        print("Detect dual monitors")
        os.environ["SDL_VIDEO_WINDOW_POS"] = f"{1920 * display},{1080 - height}"
    else:
        print("No dual monitors")
        os.environ["SDL_VIDEO_WINDOW_POS"] = f"{0},{0}"
    return pygame.display.set_mode((width, height), flags=pygame.FULLSCREEN | pygame.NOFRAME)


def __block_function_keys():
    """
    Block function keys

    :rtype: object
    """
    keyboard.block_key("alt")  # disable alt key
    keyboard.block_key("alt gr")
    keyboard.block_key("left windows")
    keyboard.block_key("shift")  # disable shift key
    keyboard.block_key("left shift")
    keyboard.block_key("right alt")
    keyboard.block_key("right ctrl")
    keyboard.block_key("ctrl")  # disable ctrl key
    keyboard.block_key("left alt")
    keyboard.block_key("right shift")
    keyboard.block_key("left ctrl")
    keyboard.block_key("right windows")
    keyboard.block_key("windows")  # disable Windows key
    keyboard.block_key("esc")  # disable esc key


NAME = "ExProctor"

if __name__ == '__main__':
    print("Start exproctor desktop application...")

    __block_function_keys()

    width, height = pygame.display.list_modes()[0]

    pygame.display.set_caption(NAME)

    screen = __create_screen(width=width, height=height)

    font = pygame.font.Font(None, int(height / 2))
    text = font.render(NAME, True, (249, 128, 18))
    text_rect = text.get_rect(center=((width / 2), (height / 2)))

    while True:
        # set background color as BLACK
        screen.fill((0, 0, 0))
        screen.blit(text, text_rect)
        pygame.display.update()
