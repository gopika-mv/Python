def even(lst):
    for num in lst:
        if num == 237:
            break
        if num % 2 == 0:
            print(num, end=" ")

lst = list(map(int, input("Enter numbers: ").split()))
even(lst)
