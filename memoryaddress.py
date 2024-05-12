#def find_first_repeating_character(s):
    #character_number={}
    #for i in s:
        #character_number.append(i)
        
def find_first_repeating_character(s):
    character_number={}
    for i in s:
        if i in character_number:
            return i, id(i)
        else:
            character_number[i] = True
    return None, None

# Example usage:
input_string = "hello"
repeating_letter, memory_address = find_first_repeating_character(input_string)
if repeating_letter:
    print("First repeating character:", repeating_letter)
    print("Memory address:", memory_address)
else:
    print("No repeating character found.")
