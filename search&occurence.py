def search_count(lst, item):
    return lst.count(item)

lst = input("Enter list elements: ").split()
item = input("Enter item to search: ")
print("Occurrences:", search_count(lst, item))
