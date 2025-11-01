def reverse_name(name):
    words = name.split()
    return " ".join(words[::-1])

name = input("Enter full name: ")
print("Reversed:", reverse_name(name))
