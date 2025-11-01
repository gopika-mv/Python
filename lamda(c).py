remove_short = lambda lst: [s for s in lst if len(s) >= 5]

strings = input("Enter list of strings: ").split()
print("Filtered List:", remove_short(strings))
