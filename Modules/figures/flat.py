def rectangle_area(edge_a: float, edge_b: float) -> float:
    return edge_a * edge_b

def rectangle_circuit(edge_a: float, edge_b: float) -> float:
    return (2 * edge_b) + (2 * edge_a)

def is_square(edge_a: float, edge_b: float) -> float:
    if edge_a == edge_b:
        return True

def circle_circuit(radius: float) -> float:
    return (radius ** 2) * 3.14

def cicrle_square(radius: float) -> float:
    return 2 * radius * 3.14
