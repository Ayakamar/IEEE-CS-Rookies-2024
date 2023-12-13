def check_code(A, B, code):
   
    if len(code) != A + B + 1:
        return "No"

    # Check if the character at position A+1 is '-'
    if code[A] != '-':
        return "No"

    # Check if all other characters are digits
    digits = set('0123456789')
    if not all(char in digits for char in code[:A] + code[A + 1:]):
        return "No"

    return "Yes"

# Function to get user input
def get_input():
    A, B = map(int, input().split())
    code = input()
    return A, B, code

# Main program
A, B, code = get_input()
result = check_code(A, B, code)
print(result)
