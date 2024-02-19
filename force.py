print("Newton's Second law of Motion ")
print("---------------------------------------")

#  Determine the missing values
print("Select the missing value:")
print("1. Mass(m)")
print("2. Acceleration (a)")
print("3. Force (F)")
missing_value_choice = input("Enter the option number for the missing value:")

# Prompt the user to enter the other two values 
if missing_value_choice == "1":
     a = float(input("Enter accelaeration (a): "))
     F = float(input("Enter force (F): "))
     m = F / a
     print(f"mass (m) = {m})")

elif missing_value_choice == "2":
     m = float(input("Enter mass (m): "))
     F = float(input("Enter force (F) "))
     a = F / m
     print(f"Acceleration (a) = {a}")

elif missing_value_choice == "3":
     m = float(input("Enter mass (m): "))
     a = float(input("Enter acceration (a): "))
     F = m * a
     print(f"Force (F) = {F}")

else:
     print("invalid option selected for the missing value." )
     