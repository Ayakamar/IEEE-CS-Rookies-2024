N = int(input())

for _ in range(N):
    A = input()
    if "010" in A or "101" in A:
        print("Good")
    else:
        print("Bad")
