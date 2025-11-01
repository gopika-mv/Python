def dig(digits):
    return int("".join(digits))

digits = input("Enter digits separated by space: ").split()
print("Number:", dig(digits))
