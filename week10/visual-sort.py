from __future__ import annotations  # type hint support
from typing import Any  # support for explicit 'Any' type

import pygame


"""
TODO:
- Indication that pygame is needed
- Comments
"""


def make_list(n: int) -> list[int]:
    """
    Purpose: Makes a list of integers 0 to n
    Parameters: n (int) the length of the list
    Return val: A list of integers 0 to n
    """
    return [i for i in range(n)]


def create_window(width: int, height: int, title: str) -> pygame.surface.Surface:
    pygame.init()
    win = pygame.display.set_mode((width, height), pygame.SCALED)
    pygame.display.set_caption(title)
    return win


def create_font(font_size: int, font_name: str) -> pygame.font.Font:
    return pygame.font.SysFont(font_name, font_size)


def draw_graph(
    win: pygame.surface.Surface,
    font: pygame.font.Font,
    arr: list[int],
    clock: pygame.time.Clock,
    fps: int,
    offsets: list[int],
    bubble_i: int,
    bubble_j: int,
    sorted: bool,
) -> bool:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True

    win.fill((0, 0, 0))

    for draw_i in range(len(arr)):
        bar_width = (win.get_width() - 20) / len(arr)
        bar_height_ratio = (win.get_height() - 100) / len(arr)
        bar_height = int(bar_height_ratio * arr[draw_i]) + 10

        color = (255, 255, 255)
        if draw_i > len(arr) - bubble_i - 1:
            color = (0, 255, 0)
        elif draw_i == bubble_j + offsets[0]:
            color = (255, 0, 0)
        elif draw_i == bubble_j + offsets[1]:
            color = (0, 0, 255)

        rect = (
            int(draw_i * bar_width + 10),
            win.get_height() - bar_height - 90,
            int(bar_width),
            bar_height,
        )
        pygame.draw.rect(win, color, rect)
        pygame.draw.rect(win, (0, 0, 0), rect, 2)

    text = "Sorted"
    if not sorted:
        if arr[bubble_j] > arr[bubble_j + 1]:
            text = "%i > %i -- swap" % (arr[bubble_j], arr[bubble_j + 1])
        else:
            text = "%i <= %i -- no swap" % (arr[bubble_j], arr[bubble_j + 1])

    surf_text = font.render(text, True, (255, 255, 255))
    win.blit(surf_text, ((win.get_width() - surf_text.get_width()) / 2, 530))

    pygame.display.update()
    clock.tick(fps)

    return False


def run(
    win: pygame.surface.Surface, font: pygame.font.Font, fps: int, arr_len: int
) -> None:
    import random  # for shuffle

    """
    Bubble sort
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    """

    arr = make_list(arr_len)
    random.shuffle(arr)

    clock = pygame.time.Clock()

    advance = False
    bubble_i = 0
    while bubble_i < len(arr):
        bubble_j = 0
        while bubble_j < len(arr) - bubble_i - 1:
            advance = pygame.key.get_pressed()[pygame.K_RETURN]

            offsets = [0, 1]
            if advance and arr[bubble_j] > arr[bubble_j + 1]:
                arr[bubble_j], arr[bubble_j + 1] = arr[bubble_j + 1], arr[bubble_j]
                offsets = [1, 0]

            should_exit = draw_graph(win, font, arr, clock, fps, offsets, bubble_i, bubble_j, False)
            if should_exit:
                return

            bubble_j += advance
        bubble_i += advance

    while True:
        should_exit = draw_graph(win, font, arr, clock, fps, offsets, len(arr), -2, True)
        if should_exit:
            return


if __name__ == "__main__":
    win = create_window(800, 600, "Visual Sort: Bubble Sort")
    font = create_font(40, "Calibri")

    run(win, font, 4, 8)

    pygame.quit()
