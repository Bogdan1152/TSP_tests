import math

class Input(Exception):
    pass



def read_int(prompt):
    while True:
        s = input(prompt).strip()

        if s == "":
            print("Помилка: введи число")
            continue

        try:
            n = int(s)
        except ValueError:
            print("Помилка: треба ціле число")
            continue

        if n < MIN_N or n > MAX_N:
            print(f"Помилка: n має бути в межах [{MIN_N}..{MAX_N}]")
            continue

        return n

# обмеження
MIN_N = 2
MAX_N = 100
MIN_COORD = -1000.0
MAX_COORD = 1000.0


def read_points(prompt):
    while True:
        s = input(prompt).strip()

        if s == "":
            print("Помилка: порожній рядок")
            continue

        parts = s.split()
        if len(parts) != 2:
            print("Помилка: формат має бути 'x y'")
            continue

        try:
            x = float(parts[0])
            y = float(parts[1])
        except ValueError:
            print("Помилка: координати мають бути числами")
            continue

        if not math.isfinite(x) or not math.isfinite(y):
            print("Помилка: координати мають бути кінцевими")
            continue

        if not (MIN_COORD <= x <= MAX_COORD) or not (MIN_COORD <= y <= MAX_COORD):
            print(f"Помилка: координати мають бути в межах [{MIN_COORD}..{MAX_COORD}]")
            continue

        return x, y


def check_tsp_points(points):
   
    if len(points) < MIN_N:
        raise Input("Потрібно мінімум 2 міста")

    seen = set()
    for x, y in points:
        key = (x, y)  
        if key in seen:
            raise Input("Два міста з однаковими координатами заборонені")
        seen.add(key)


def euclid(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return math.sqrt(dx * dx + dy * dy)


def build_matrix(points):
    check_tsp_points(points)

    n = len(points)
    matrix = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            d = euclid(points[i], points[j])
            matrix[i][j] = d
            matrix[j][i] = d

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{v:.2f}" for v in row))
