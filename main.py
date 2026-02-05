
from tsp import print_matrix, read_int, read_points, check_tsp_points, build_matrix, Input

def main():
 
    n = read_int("Введіть кількість міст: ")

    points = []
    print("\nКоординати у форматі: x y\n")


    for i in range(n):
        while True:
            x, y = read_points(f"Місто {i+1}: ")
            points.append((x, y))

            try:
                check_tsp_points(points) if len(points) >= 2 else None
                break
            except Input as e:
                print("Помилка:", e)
                points.pop()

    matrix = build_matrix(points)

    print("\nМатриця відстаней:")
    print_matrix(matrix)


if __name__ == "__main__":
    main()
