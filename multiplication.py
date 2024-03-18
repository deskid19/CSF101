number = int(input("Enter the number for which you want the multiplication table:"))
limit = int(input("Enter the limit up to which you want the multiplication table generated:"))
print(f"Multiplication Table for {number} :")
for i in range(1, limit + 1):
    print(f"{number} * {i} = {number * i}")
