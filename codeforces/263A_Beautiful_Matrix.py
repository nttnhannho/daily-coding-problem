def main():
    matrix = []
    for _ in range(5):
        row = list(map(int, input().split()))
        matrix.append(row)

    best_index = (3, 3)
    step_count = 0
    for row_i, row in enumerate(matrix, start=1):
        if 1 in row:
            one_index = tuple((row_i, row.index(1) + 1))
            step_count = abs(one_index[0] - best_index[0]) + abs(one_index[1] - best_index[1])

    print(step_count)


if __name__ == '__main__':
    main()
