#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    a = tuple(map(float, input("Введите список, вещественных элементов: ").split()))
    x = 18.4
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    s = 0
    for item in a:
        if item < x:
            s += 1
    print("Количество элементов списка < C: ", s)

    i = -1
    e = 0
    a = tuple(reversed(a))
    for item in a:
        i += 1
        if item < 0:
            e = i

    s = 0
    for k in range(e):
        s += a[k]
    print("Сумма: ", int(s))

    b = max(a)
    y = b - (b * 0.2)
    new_a1 = [i for i in a if not y <= i <= b]
    new_a2 = [i for i in a if y <= i < b]
    new_a = new_a2 + new_a1
    print(new_a)