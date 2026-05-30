print("=== ELECTRONIC PRESCRIPTION VALIDATOR ===")

patient_name = input("Enter patient name: ")
medication = input("Enter medication name: ")
dosage = input("Enter dosage: ")

if patient_name == "" or medication == "" or dosage == "":
    print("\nValidation Result:")
    print("Prescription is incomplete.")
else:
    print("\nValidation Result:")
    print("Prescription is valid.")
    print("Patient:", patient_name)
    print("Medication:", medication)
    print("Dosage:", dosage)

print("\nDisclaimer:")
print("This tool is for educational purposes only.")
