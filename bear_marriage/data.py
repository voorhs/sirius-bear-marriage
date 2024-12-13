from io import BytesIO
from dataclasses import dataclass

import numpy as np
import numpy.typing as npt


@dataclass
class ColoredPoint:
    x: float
    y: float
    black: bool  # True means point is black, False means it's white

    def __lt__(self, other: "ColoredPoint") -> bool:
        return (self.x, self.y) < (other.x, other.y)

    def __eq__(self, other: "ColoredPoint") -> bool:
        return (self.x, self.y, self.black) == (other.x, other.y, other.black)


def color_points(points: npt.NDArray[np.float32], black: bool):
    return [ColoredPoint(x, y, black) for x, y in points.tolist()]


def sample_data(n: int, seed: int | None = 0) -> list[ColoredPoint]:
    if seed is not None:
        np.random.seed(seed)
    all_points = np.random.uniform(-1, 1, size=(2 * n, 2))
    blacks, whites = all_points[:n], all_points[n:]
    return color_points(blacks, black=True) + color_points(whites, black=False)


def read_points(file: BytesIO) -> list[ColoredPoint]:
    lines = [line.decode() for line in file.readlines()]
    del lines[0]  # header
    res = []
    for line in lines:
        if len(line.strip()) == 0:
            continue
        _, x, y, black = line.split()
        res.append(ColoredPoint(float(x), float(y), black == "1"))
    return res
