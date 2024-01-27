def main():
    num = int(input())
    views = []
    for _ in range(num):
        view = map(int, input().split())
        views.append(view)

    count = 0
    for view in views:
        if sum(view) >= 2:
            count += 1

    print(count)


if __name__ == '__main__':
    main()
