# -*- coding: utf-8 -*-

import cmath
import math


def solve(a3, a2, a1, a0):
    """ Numeric solutions of a cubic equation

    a3 * x^3 + a2 * x^2 + a1 * x + a0 = 0
    """
    a3, a2, a1, a0 = map(float, [a3, a2, a1, a0])

    if a3 == a2 == a1 == 0:
        raise ValueError("a3, a2 or a1 should be non-zero value.")

    if a3 == a2 == 0:
        return - a0 / a1,

    if a3 == 0:
        if a1 ** 2 - 4 * a2 * a0 == 0:
            return -a1 / (2.0 * a2),

        x0 = (-a1 + cmath.sqrt(a1 ** 2 - 4 * a2 * a0)) / (2.0 * a2)
        x1 = (-a1 - cmath.sqrt(a1 ** 2 - 4 * a2 * a0)) / (2.0 * a2)
        return x0, x1

    # Cardano's method
    A2 = a2 / a3
    A1 = a1 / a3
    A0 = a0 / a3

    p = A1 - (A2 ** 2) / 3.0
    q = A0 - A1 * A2 / 3.0 + 2 * (A2 ** 3) / 27.0
    u = (q / 2.0) ** 2 + (p / 3.0) ** 3

    if u >= 0:
        k0 = -q / 2.0 + math.sqrt(u) ** (1 / 3.0)
        k1 = -q / 2.0 - math.sqrt(u) ** (1 / 3.0)
    else:
        k0 = (-q / 2.0 + cmath.sqrt(u)) ** (1 / 3.0)
        k1 = (-q / 2.0 - cmath.sqrt(u)) ** (1 / 3.0)
    omega1 = (-1 + 1j * math.sqrt(3)) / 2.0
    omega2 = (-1 - 1j * math.sqrt(3)) / 2.0
    y0 = k0 + k1
    y1 = omega1 * k0 + omega2 * k1
    y2 = omega2 * k0 + omega1 * k1

    return y0 - (A2 / 3.0), y1 - (A2 / 3.0), y2 - (A2 / 3.0)
