S = input()
hello = "hello"
j = 0

for char in S:
    if char == hello[j]:
        j += 1
        if j == 5:
            print("YES")
            break
else:
    print("NO")
