#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from cubic_equation import solve

if __name__ == '__main__':
    if len(sys.argv) <= 4:
        print("Usage: python cubic.py a3 a2 a1 a0\n       will solve a3 * x^3 + a2 * x^2 + a1 * x + a0 = 0")
        sys.exit(-1)
    print(solve(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])))
