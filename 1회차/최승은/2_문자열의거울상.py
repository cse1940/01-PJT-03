n = int(input())

for i in range(1, n+1):
    test = input()
    result = []
    for ii in test[::-1]:
        if ii == "b":
            result.append("d")
        elif ii == "d":
            result.append("b")
        elif ii == "p":
            result.append("q")
        else:
            result.append("p")
    print(f"#{i} {result}")
        

