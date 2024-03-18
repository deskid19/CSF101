from queue import Queue
#initiate patient queue
patient_name= Queue()
current_patient_name = None

# menu-driven program for desktop manager
while True:
    print("Desk Manager - Patient Registration and Appiontment System")
    print("1. Register Patient")
    print("2. Remove Patient after Meeting Doctor")
    print("3. Display Patient Queue")
    print("4. Exit")

    task = int(input("Enter your choice(just enter the option number): "))
    if task == 1:
        name = input("Enter Patient Name: ")
        patient_name.put(name)
        current_patient_name = name
        print(f"Patient {name} registered")

    elif task == 2:
        patient_name.get()
        print(f"Patient {patient_name} removed after meeting the doctor")
    elif task == 3:
        print("Current Patient Queue: ")
        print(patient_name.queue)
    elif task == 4:
        print("Exiting program...")
    else:
        print("Invalid Input")