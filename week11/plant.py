# from __future__ import annotations  # type hint support
# from typing import Any  # support for explicit 'Any' type

# import time
# import random
# import math

# try:
#     import pygame
# except ImportError:
#     print("This program requires pygame to run.")
#     print("Please install pygame (pip install pygame) and rerun.")
#     exit(1)

# window_w = 600
# window_h = 600

# base_pt = (300, 550)
# base_size = 200
# depth = 5

# angle_spread = 15

# bg_color = (0, 0, 0)
# plant_color = (255, 255, 255)


# def deg_to_rad(deg: float) -> float:
#     return deg * math.pi / 180


# def create_window(width: int, height: int, title: str) -> pygame.surface.Surface:
#     pygame.init()
#     win = pygame.display.set_mode((width, height), pygame.SCALED | pygame.RESIZABLE)
#     pygame.display.set_caption(title)
#     return win


# def recusive_plant(
#         win: pygame.surface.Surface, pt: tuple[float, float], base_angle: float, size: float, depth: int
# ) -> None:

#     if depth < 0:
#         return

#     angle = random.randrange(base_angle - angle_spread, base_angle + angle_spread)
#     rad = deg_to_rad(angle + 90)
#     x_change = math.cos(rad) * size
#     y_change = math.sin(rad) * size
#     end = (pt[0] - x_change, pt[1] - y_change)

#     pygame.draw.line(win, (255, 255, 255), pt, end)
#     for i in range(3):
#         recusive_plant(win, end, angle, size / 2, depth - 1)


# def main():
#     win = create_window(window_w, window_h, "H Recursion")

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 return
#         win.fill(bg_color)
#         recusive_plant(win, base_pt, 0, base_size, depth)
#         pygame.display.update()


# main()
