# Outer loop to iterate through numbers from 1 to 9
for i in range(1, 10):
    # Check if the current number is 7
    if i == 3:
        print("Skipping 3 in the inner loop")
        continue  # Break out of the outer loop when reaching 7
    elif i == 7:  # Skip printing 3
        print("Reached 7, breaking outer loop")  # Print the number
        break
    print(i)# Move to the next line after printing each set of numbers
    


    
