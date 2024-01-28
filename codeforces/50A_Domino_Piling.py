def main():
    m, n = map(int, input().split())
    standard_domino_pieces_size = 2
    print((m * n) // standard_domino_pieces_size)


if __name__ == '__main__':
    main()
