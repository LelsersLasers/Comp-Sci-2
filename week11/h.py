from __future__ import annotations  # type hint support
from typing import Any  # support for explicit 'Any' type

import time

try:
    import pygame
except ImportError:
    print("This program requires pygame to run.")
    print("Please install pygame (pip install pygame) and rerun.")
    exit(1)


def create_window(width: int, height: int, title: str) -> pygame.surface.Surface:
    pygame.init()
    win = pygame.display.set_mode((width, height), pygame.SCALED | pygame.RESIZABLE)
    pygame.display.set_caption(title)
    return win


# def draw_h(win: pygame.surface.Surface, pt: tuple[float, float], size: float) -> None:
# 	top_left = (pt[0] - size, pt[0] - size)
# 	middle_left = (pt[0] - size, pt[0])
# 	bottom_left = (pt[0] - size, pt[0] + size)
# 	top_right = (pt[0] + size, pt[0] - size)
# 	middle_right = (pt[0] + size, pt[0])
# 	bottom_right = (pt[0] + size, pt[0] + size)

# 	pygame.draw.line(win, (255, 255, 255), top_left, bottom_left)
# 	pygame.draw.line(win, (255, 255, 255), top_right, bottom_right)
# 	pygame.draw.line(win, (255, 255, 255), middle_left, middle_right)


def recusive_h(
    win: pygame.surface.Surface, pt: tuple[float, float], size: float, depth: int
) -> None:
    if depth == 0:
        return

    top_left = (pt[0] - size, pt[1] - size)
    middle_left = (pt[0] - size, pt[1])
    bottom_left = (pt[0] - size, pt[1] + size)
    top_right = (pt[0] + size, pt[1] - size)
    middle_right = (pt[0] + size, pt[1])
    bottom_right = (pt[0] + size, pt[1] + size)

    pygame.draw.line(win, (255, 255, 255), top_left, bottom_left)
    pygame.draw.line(win, (255, 255, 255), top_right, bottom_right)
    pygame.draw.line(win, (255, 255, 255), middle_left, middle_right)

    recusive_h(win, top_left, size / 2.5, depth - 1)
    recusive_h(win, bottom_left, size / 2.5, depth - 1)
    recusive_h(win, top_right, size / 2.5, depth - 1)
    recusive_h(win, bottom_right, size / 2.5, depth - 1)


def main():
    win = create_window(600, 600, "H Recursion")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        win.fill((0, 0, 0))
        recusive_h(win, (300, 300), 150, 5)
        pygame.display.update()


main()
