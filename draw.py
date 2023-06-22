from random import randrange

from PIL.ImageDraw import ImageDraw as ImageDraw
import numpy as np
import cv2


def draw_rectangle(
    image: np.ndarray, 
    color: int | None = None,
    thickness: int | None = None,
) -> np.ndarray:
    """
    desenha um retangulo em um local aleatório da imagem
    """
    x1 = randrange(image.shape[1])
    y1 = randrange(image.shape[0])
    
    x2 = randrange(image.shape[1])
    y2 = randrange(image.shape[0])

    if color is None:
        color = randrange(256)

    if thickness is None:
        thickness = randrange(1, max(2, min(image.shape) // 100))

    return cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)


def draw_square(
        image: np.ndarray,
        edge: int | None = None,
        color: int | None = None,
        thickness: int | None = None, 
    ) -> np.ndarray:
    """
    desenha um quadrado aleatoriamente na imagem
    """
    if edge is None:
        edge = min(image.shape) // 10
    
    x1 = randrange(image.shape[1] - edge)
    y1 = randrange(image.shape[0] - edge)
    
    x2 = x1 + edge
    y2 = y1 + edge

    if color is None:
        color = randrange(256)

    if thickness is None:
        thickness = randrange(1, max(2, min(image.shape) // 100))

    return cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)


def draw_line(
        image: np.ndarray, 
        color: int | None = None, 
        thickness: int | None = None,
    ) -> np.ndarray:
    """
    desenha uma linha em lugares aleatorios da imagem
    """
    x1 = randrange(image.shape[1])
    y1 = randrange(image.shape[0])
    
    # x2 = x1 + 1
    # y2 = y1 + 1
    x2 = randrange(image.shape[1])
    y2 = randrange(image.shape[0])

    if color is None:
        color = randrange(256)

    if thickness is None:
        thickness = randrange(1, max(2, min(image.shape) // 100))

    return cv2.line(image, (x1, y1), (x2, y2), color, thickness)
