# Initialize empty lists and a dictionary
students_list = []
students_dict = {}

    # Prompt user for student information
name = input("Enter student name: ")
age = input("Enter student age: ")
grade = input("Enter student grade: ")

    # Add information to lists and dictionary
students_list.append(name)
students_dict[name] = {"Age": age, "Grade": grade}

print("Student information added successfully.")


    # Print student details from the dictionary
print("Student Details:")
for name, info in students_dict.items():
    print(f"Name: {name}, Age: {info['Age']}, Grade: {info['Grade']}")


    # Search for a student by name
name_to_search = input("Enter student name to search: ")
if name_to_search in students_dict:
    info = students_dict[name_to_search]
    print(f"Student Found - Name: {name_to_search}, Age: {info['Age']}, Grade: {info['Grade']}")
else:
    print(f"Student not found!")


    # Remove a student by name
name_to_remove = input("Enter student name to remove: ")
if name_to_remove in students_dict:
    students_list.remove(name_to_remove)
    del students_dict[name_to_remove]
    print(f"Student '{name_to_remove}' removed successfully.")
    print("Updated Student details: ", students_dict)
else:
    print(f"Student not found!")