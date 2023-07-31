def main() -> None:
    N, D = map(int, input().split())
    S = [input() for _ in range(N)]
    counter = 0
    counters = [0]
    for i in range(D):
        maru_counter = 0
        for j in range(N):
            if S[j][i] == "o":
                maru_counter += 1
            if S[j][i] == "x":
                counters.append(counter)
                counter = 0
        if maru_counter == N:
            counter += 1
        else:
            counters.append(counter)
            counter = 0
    counters.append(counter)

    print(max(counters))


if __name__ == "__main__":
    main()
