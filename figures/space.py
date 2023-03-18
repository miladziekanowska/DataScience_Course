def cuboid_volume(base_a: float, base_b: float, height: float) -> float:
    return base_a * base_b * height

def roller_volume(radius: float, height: float) -> float:
    return ((radius ** 2) * 3.14) * height