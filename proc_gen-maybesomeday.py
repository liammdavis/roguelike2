from __future__ import annotations

import random
from typing import Tuple, Iterator
from game_map import GameMap
import tile_types

import tcod

class NewRoom:
    pass

class RectangularRoom(NewRoom):
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height

    @property
    def center(self) -> Tuple[int, int]:
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)

        return center_x, center_y 

    @property
    def inner(self) -> Tuple[slice, slice]:
        """ 
        Return the inner area of this room as a 2d array
        """
        return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)


class CircularRoom(NewRoom):
    def __init__(self, h: int, k: int, radius: int, x: int, y: int):
        self.h = h
        self.k = k
        self.r = radius
        self.x = x
        self.y = y

    @property
    def inner():
        



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def __init__(self, x: int, y: int, radius: int):
        f = 1 - radius
        ddf_x = 1
        ddf_y = -2 * radius
        x = 0
        y = radius
        self.set(x, y, + radius)
        self.set(x, y - radius)
        self.set(x + radius, y)
        self.set(x - radius, y)

        while x < y:
            if f >= 0:
                y -= 1
                ddf_y += 2
                f += ddf_y
                x += 1
                ddf_x += 2
                f += ddf_x
                self.set(x + x, y + y)
                self.set(x - x, y + y)
                self.set(x + x, y - y)
                self.set(x - x, y - y)
                self.set(x + y, y + x)
                self.set(x - y, y + x)
                self.set(x + y, y - x)
                self.set(x - y, y + x)

        x = x
        y = y

                
    @property
    def center(self) -> Tuple[int, int]
        center_x = int(x)
        center_y = int(y)
        
        return center_x, center_y

    @property
    def intersects
        
                
