def main():
    num = int(input())
    long_words = []
    for _ in range(num):
        long_word = str(input())
        long_words.append(long_word)

    for word in long_words:
        word_length = len(word)
        if word_length <= 10:
            print(word)
        else:
            first = word[0]
            middle = word_length - 2
            last = word[-1]
            print(f'{first}{middle}{last}')


if __name__ == '__main__':
    main()
