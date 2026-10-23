# Practical 5 - Practice Question 10: Suspicious IP occurrences

# Count occurrences of the watched IP and stop on its third appearance.
suspicious_ip = input("Suspicious IP to watch: ").strip()
logins = input("Login IP addresses separated by spaces: ").split()
count = 0
for ip in logins:
    if ip == suspicious_ip:
        count += 1
    if count == 3:
        print("Scanner halted: suspicious IP appeared three times.")
        break
    print("Checked:", ip)
else:
    print("Scan completed without three suspicious occurrences.")
