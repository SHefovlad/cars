import math
def okr(pl_x, pl_y, okr_b, a = 0, b = 0):
    angle = okr_b
    a = 100 * math.cos(angle) + pl_x - 25
    b = 100 * math.sin(angle) + pl_y - 25
    return (a, b)
