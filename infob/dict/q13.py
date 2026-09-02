'''1.ASSIGNMENT: HOSPITAL PATIENT RECORD MANAGEMENT SYSTEM:--

A multi-specialty hospital is currently maintaining patient records manually in registers. As the number of patients is increasing, it has become difficult to search, update, and manage records efficiently.

The hospital management has decided to develop a simple Patient Record Management System using Python. The system should store patient information in a nested dictionary where:

Key → Patient ID
Value → Dictionary containing patient details

Each patient record should contain:

Patient Name
Age
Gender
Disease
Doctor Name
Sample Data Structure
{
101:{
    "name":"Ajay",
    "age":35,
    "gender":"Male",
    "disease":"Fever",
    "doctor":"Dr. Sharma"
},
102:{
    "name":"Ravi",
    "age":42,
    "gender":"Male",
    "disease":"Diabetes",
    "doctor":"Dr. Gupta"
}
}
Menu Driven Program

Display the following menu repeatedly until the user chooses Exit.
'''
patients = {
    101: {
        "name": "Ajay",
        "age": 35,
        "gender": "Male",
        "disease": "Fever",
        "doctor": "Dr. Sharma"
    },
    102: {
        "name": "Ravi",
        "age": 42,
        "gender": "Male",
        "disease": "Diabetes",
        "doctor": "Dr. Gupta"
    }
}

while True:

    print("=====================================")
    print(" HOSPITAL PATIENT MANAGEMENT SYSTEM")
    print("=====================================")
    print("1. Add New Patient")
    print("2. Search Patient")
    print("3. Update Patient Disease")
    print("4. Delete Patient Record")
    print("5. Display All Patients")
    print("6. Count Total Patients")
    print("7. Display Patients By Disease")
    print("8. Display Oldest Patient")
    print("9. Display Youngest Patient")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Add New Patient
    if choice == 1:

        patient_id = int(input("Enter Patient ID: "))

        if patient_id in patients:
            print("Patient ID already exists.")
        else:
            name = input("Enter Patient Name: ")
            age = int(input("Enter Age: "))
            gender = input("Enter Gender: ")
            disease = input("Enter Disease: ")
            doctor = input("Enter Doctor Name: ")

            patients[patient_id] = {
                "name": name,
                "age": age,
                "gender": gender,
                "disease": disease,
                "doctor": doctor
            }

            print("Patient Added Successfully")

    # 2. Search Patient
    elif choice == 2:

        patient_id = int(input("Enter Patient ID: "))

        if patient_id in patients:

            patient = patients[patient_id]

            print("\nPatient ID :", patient_id)
            print("Name       :", patient["name"])
            print("Age        :", patient["age"])
            print("Gender     :", patient["gender"])
            print("Disease    :", patient["disease"])
            print("Doctor     :", patient["doctor"])

        else:
            print("Patient Record Not Found")

    # 3. Update Patient Disease
    elif choice == 3:

        patient_id = int(input("Enter Patient ID: "))

        if patient_id in patients:

            new_disease = input("Enter New Disease: ")

            patients[patient_id]["disease"] = new_disease

            print("Disease Updated Successfully")

        else:
            print("Patient Record Not Found")

    # 4. Delete Patient
    elif choice == 4:

        patient_id = int(input("Enter Patient ID: "))

        if patient_id in patients:

            del patients[patient_id]

            print("Patient Record Deleted Successfully")

        else:
            print("Patient Not Found")

    # 5. Display All Patients
    elif choice == 5:

        if len(patients) == 0:
            print("No Patient Records Found")

        else:

            for patient_id, patient in patients.items():

                print("--------------------------------")
                print("Patient ID :", patient_id)
                print("Name       :", patient["name"])
                print("Age        :", patient["age"])
                print("Gender     :", patient["gender"])
                print("Disease    :", patient["disease"])
                print("Doctor     :", patient["doctor"])
                print("--------------------------------")

    # 6. Count Total Patients
    elif choice == 6:

        print("Total Patients :", len(patients))

    # 7. Display Patients By Disease
    elif choice == 7:

        disease = input("Enter Disease: ")

        found = False

        for patient_id, patient in patients.items():

            if patient["disease"].lower() == disease.lower():

                print(patient_id, patient["name"])
                found = True

        if found == False:
            print("No Patient Found")

    # 8. Display Oldest Patient
    elif choice == 8:

        if len(patients) == 0:
            print("No Patient Records Found")

        else:

            oldest_id = max(
                patients,
                key=lambda patient_id: patients[patient_id]["age"]
            )

            oldest = patients[oldest_id]

            print("\nOldest Patient Details")
            print("Patient ID :", oldest_id)
            print("Name       :", oldest["name"])
            print("Age        :", oldest["age"])
            print("Disease    :", oldest["disease"])
            print("Doctor     :", oldest["doctor"])

    # 9. Display Youngest Patient
    elif choice == 9:

        if len(patients) == 0:
            print("No Patient Records Found")

        else:

            youngest_id = min(
                patients,
                key=lambda patient_id: patients[patient_id]["age"]
            )

            youngest = patients[youngest_id]

            print("\nYoungest Patient Details")
            print("Patient ID :", youngest_id)
            print("Name       :", youngest["name"])
            print("Age        :", youngest["age"])
            print("Disease    :", youngest["disease"])
            print("Doctor     :", youngest["doctor"])

    # 10. Exit
    elif choice == 10:

        print("Thank You For Using Hospital Patient Management System")
        break

    else:
        print("Invalid Choice")