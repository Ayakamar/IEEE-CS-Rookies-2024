def encrypt_Original(Q,S):
    key = "PgEfTYaWGHjDAmxQqFLRpCJBownyUKZXkbvzIdshurMilNSVOtec#@_!=.+-*/"
    original = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    if Q == 1: 
        encrypted = ""
        for char in S:
            if char in original:
                index = original.index(char)
                encrypted += key[index]
            else:
                encrypted += char
        return encrypted
    elif Q == 2:  
        decrypted = ""
        for char in S:
            if char in key:
                index = key.index(char)
                decrypted += original[index]
            else:
                decrypted += char
        return decrypted
    else:
        return "Invalid input for Q"

Q = int(input())
S = input()

print(encrypt_Original(Q,s))
