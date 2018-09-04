import math

import pytest

from cubic_equation import solve


@pytest.mark.parametrize("a,solutions", [
    [[0, 0, 1, -1], [1]],
    [[0, 1, -2, 1], [1]],
    [[0, 1, 0, 1], [1j, -1j]],
    [[1, -2, -1, 2], [2, -1, 1]],
    [[2, -3, -5, 6], [2, -3 / 2, 1]],
    [[4, -2, -6, 3], [math.sqrt(6) / 2, -math.sqrt(6) / 2, 1 / 2]],
    [[1, -1, -3, -1], [1 + math.sqrt(2), -1, 1 - math.sqrt(2)]],
    [[1, -5, 8, -6], [3, 1 + 1j, 1 - 1j]],
    [[1, -3, 7, -5], [1, 1 + 2j, 1 - 2j]],
])
def test_solve(a, solutions):
    a3, a2, a1, a0 = a
    result = solve(a3, a2, a1, a0)
    for e, r in zip(solutions, result):
        assert pytest.approx(e.real) == r.real
        assert pytest.approx(e.imag) == r.imag
