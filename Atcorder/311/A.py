def main():
    N = int(input())
    s = input()

    indexes = [s.find(_str) for _str in ["A", "B", "C"]]

    print(max((s, ["A", "B", "C"])) + 1)


if __name__ == "main":
    main()
