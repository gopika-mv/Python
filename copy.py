try:
    with open('file1.txt', 'r') as s:
        with open('file2.txt', 'w') as d:
            for line in s:
                d.write(line)

    print("File copied successfully from 'file1.txt' to 'file2.txt'")

except FileNotFoundError:
    print("Error: 'file1.txt' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
