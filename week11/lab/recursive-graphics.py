"""
	Description: Draws a flower pattern that gets increasingly smaller
	Author: Millan
	Date: 9/20/22
"""

from __future__ import annotations  # type hint support

try:
    import pygame
except ImportError:
    print("This program requires pygame to run.")
    print("Please install pygame and rerun.")
    exit(1)


def create_window(width: int, height: int, title: str) -> pygame.surface.Surface:
    """
    Purpose: Creates a pygame window
    Parameters: The width of the window (int), the height of the window (int), and the title for the window (str)
    Return Val: The created window (pygame.surface.Surface)
    """
    pygame.init()
    win = pygame.display.set_mode((width, height), pygame.SCALED | pygame.RESIZABLE)
    pygame.display.set_caption(title)
    return win


def draw_flower(
    win: pygame.surface.Surface, pt: tuple[float, float], size: float
) -> None:
    """
    Purpose: Draws a flower
    Parameters: the window to draw to (pygame.surface.Surface), the center of the
        flower (tuple[float, float]), the size of the flower (float)
    Return Val: None
    """
    top_left = (pt[0] - size, pt[1] - size)
    bottom_left = (pt[0] - size, pt[1] + size)
    top_right = (pt[0] + size, pt[1] - size)
    bottom_right = (pt[0] + size, pt[1] + size)

    pygame.draw.circle(win, "#BF616A", top_left, size)
    # Adding the last parameter makes the circle and outline instead of filled in
    pygame.draw.circle(win, "#4C566A", top_left, size, 1)

    pygame.draw.circle(win, "#BF616A", bottom_left, size)
    pygame.draw.circle(win, "#4C566A", bottom_left, size, 1)

    pygame.draw.circle(win, "#BF616A", top_right, size)
    pygame.draw.circle(win, "#4C566A", top_right, size, 1)

    pygame.draw.circle(win, "#BF616A", bottom_right, size)
    pygame.draw.circle(win, "#4C566A", bottom_right, size, 1)

    pygame.draw.circle(win, "#EBCB8B", pt, size)
    pygame.draw.circle(win, "#4C566A", pt, size, 1)


def recusive_flower(
    win: pygame.surface.Surface, pt: tuple[float, float], size: float, depth: int
) -> None:
    """
    Purpose: Draws flowers with increasingly smaller sizes
    Parameters: the window to draw to (pygame.surface.Surface), the center of the
        current flower (tuple[float, float]), the size of the current flower (float),
        and number of flowers remaining to draw (int)
    Return Val: None
    """
    if depth == 0:
        return
    else:
        draw_flower(win, pt, size)

        top_left_center = (pt[0] - size * 1.5, pt[1] - size * 1.5)
        bottom_left_center = (pt[0] - size * 1.5, pt[1] + size * 1.5)
        top_right_center = (pt[0] + size * 1.5, pt[1] - size * 1.5)
        bottom_right_center = (pt[0] + size * 1.5, pt[1] + size * 1.5)

        recusive_flower(win, top_left_center, size / 2.5, depth - 1)
        recusive_flower(win, bottom_left_center, size / 2.5, depth - 1)
        recusive_flower(win, top_right_center, size / 2.5, depth - 1)
        recusive_flower(win, bottom_right_center, size / 2.5, depth - 1)


def main():
    # create a window to use for pygame
    win = create_window(600, 600, "Recursive Flower")

    # pygame event/redraw loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        win.fill("#2E3440")
        recusive_flower(win, (300, 300), 125, 5)
        pygame.display.update()


main()
