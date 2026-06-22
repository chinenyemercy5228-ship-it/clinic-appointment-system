patients = []


def add_patient():
    name = input("Enter patient name: ")
    phone = input("Enter phone number: ")
    appointment = input("Enter appointment date: ")

    patient = {
        "name": name,
        "phone": phone,
        "appointment": appointment
    }

    patients.append(patient)

    print("Patient added successfully")


def view_patients():

    for patient in patients:
        print("----------------")
        print("Name:", patient["name"])
        print("Phone:", patient["phone"])
        print("Appointment:", patient["appointment"])


def search_patient():

    search_name = input("Enter patient name: ")

    for patient in patients:

        if patient["name"] == search_name:
            print("Patient Found")
            print(patient)
            return

    print("Patient not found")


while True:

    print("""
    Clinic Appointment System

    1. Add Patient
    2. View Patients
    3. Search Patient
    4. Exit
    """)

    choice = input("Choose an option: ")


    if choice == "1":
        add_patient()

    elif choice == "2":
        view_patients()

    elif choice == "3":
        search_patient()

    elif choice == "4":
        print("System closed")
        break

    else:
        print("Invalid option")