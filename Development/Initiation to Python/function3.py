def length(string, *args, plus_everything=False):
    if args:
        lengths = [len(string)]
        for a in args:
            lengths.append(len(a))
        if plus_everything:
            lengths = sum(lengths)
        return lengths
    return len(string)


def main():
    print(length("Hello"))
    print(length("Hello", "how", "are", "you?", plus_everything=True))

if __name__ == "__main__":
    main()