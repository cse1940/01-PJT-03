
t = int(input())
for i in range(1, t+1):
    n = int(input())
    income = list(map(int, input().split()))
    average = sum(income) / n

    ans = 0
    for ii in income:
        if average >= ii:
            ans += 1
    print(f"#{i} {ans}")


