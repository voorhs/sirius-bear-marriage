import numpy as np
from dataclasses import dataclass
import math

from .data import ColoredPoint


@dataclass
class Statistics:
    mean: float
    std: float
    min: float
    max: float
    sum: float


def euclid_distance(pair: tuple[ColoredPoint, ColoredPoint]) -> float:
    a, b = pair
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


def get_distances(pairs: list[tuple[ColoredPoint, ColoredPoint]]):
    all_distances = np.array([euclid_distance(p) for p in pairs])
    statistics = dict(
        mean=float(all_distances.mean()),
        std=float(all_distances.std()),
        min=float(all_distances.min()),
        max=float(all_distances.max()),
        sum=float(all_distances.sum()),
    )
    return all_distances, statistics
