# Practical 8 - Practice Question 2: Patient temperatures

# Select the patient ID whose nested temperature is greatest.
patients = {"P001":{"name":"Asha", "temp":98.6}, "P002":{"name":"Ravi", "temp":101.2},
            "P003":{"name":"Neha", "temp":99.1}}
highest = max(patients, key=lambda key: patients[key]["temp"])
print("Highest temperature:", highest, patients[highest])
patients["P003"]["temp"] = 100.4
print("Updated P003:", patients["P003"])
