# python-cubic-equation
Python method to get numerical solutions of a cubic equation (including imaginary number).

## Support

- cubic equation
- quadratic equation
- linear equation

## Usage

`a3 * x^3 + a2 * x^2 + a1 * x + a0 = 0` will be solved by command below.

```python
from cubic_equation import solve
solutions = solve(a3, a2, a1, a0)
```


### Example

`x^3 - 2x^2 - 3x + 4 = 0`


```python
>>> from cubic_equation import solve
>>> a3, a2, a1, a0 = 1, -2, -3, 4
>>> solve(a3, a2, a1, a0)
((2.5615528128088303+0j), (-1.5615528128088303+0j), (0.9999999999999999+0j))
```

or you can use `solve.py` from bash

```bash
$ ./solve.py 1 -2 -3 4
((2.5615528128088303+0j), (-1.5615528128088303+0j), (0.9999999999999999+0j))
```


`x^2 - 2x + 1 = 0`

```python
>>> solve(0, 1, -2, 1)
1.0
```

`x^2 + 1 = 0`

```python
>>> solve(0, 1, 0, 1)
(1j, (-0-1j))
```
