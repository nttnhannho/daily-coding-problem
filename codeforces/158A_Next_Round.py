def main():
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))

    standard_score = scores[k - 1]
    print(len(list(filter(lambda x: x > 0 and x >= standard_score, scores))))


if __name__ == '__main__':
    main()
