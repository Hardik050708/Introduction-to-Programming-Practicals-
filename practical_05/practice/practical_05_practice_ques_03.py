# Practical 5 - Practice Question 3: Emergency triage

# break stops normal queue processing when a critical status appears.
patients = input("Patient statuses separated by spaces: ").lower().split()
for position, status in enumerate(patients, 1):
    if status == "critical":
        print("Emergency at patient", position)
        break
    print("Processed patient", position)
