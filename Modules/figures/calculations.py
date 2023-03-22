def my_add(a: float, b: float) -> float:
    return str(a + b)

def my_sub(a: float, b: float) -> float:
    return str(a - b)

def my_div(a: float, b:float) -> float:
    if b == 0:
        return "You cannot divide by 0!"
    else: return str(a / b)