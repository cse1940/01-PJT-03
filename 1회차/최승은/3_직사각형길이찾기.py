t = int(input()) # test case 수

for i in range(1, t+1):
    a, b, c =  input().split()
    if a == b:
        d = c
    elif a == c:
        d = b
    else:
        d = a
    print(f"#{i} {d}")
    