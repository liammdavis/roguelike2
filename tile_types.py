from typing import Tuple

import numpy as np #type: ignore

#tile graphics structed type compatible with Console.tiles_rgb
graphic_dt = np.dtype(
    [
        ("ch", np.int32), #unicode codepoint
        ("fg", "3B"), # 3 unsigned bytes for rgb colors
        ("bg", "3B"),
    ]
)

#tile struct used for statically defined tile data
tile_dt = np.dtype(
    [
        ("walkable", np.bool), #true if this tile can be walked over
        ("transparent", np.bool), #true if this tile doesnt block FOV
        ("dark", graphic_dt), #graphics for when this tile is not in FOV
    ]
)

def new_tile(
    *, # enforce the use of keywords, so that parameter order doesnt matter
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.array:
    """Helper Function for defining individual tile types """
    return np.array((walkable, transparent, dark), dtype=tile_dt)


floor = new_tile(
    walkable=True, transparent=True, dark=(ord("."), (225, 225, 225), (50, 50, 150)),
)
wall = new_tile(
    walkable=False, transparent=False, dark=(ord("#"), (225, 225, 225), (0, 0, 100)),
)
