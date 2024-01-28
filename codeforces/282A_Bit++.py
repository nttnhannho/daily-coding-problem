def main():
    n = int(input())
    operations = []
    for _ in range(n):
        operation = str(input())
        operations.append(operation)

    result = 0
    for operation in operations:
        if '++' in operation:
            result += 1
        elif '--' in operation:
            result -= 1

    print(result)


if __name__ == '__main__':
    main()
