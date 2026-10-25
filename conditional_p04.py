name = input("Enter student name: ")
percentage = float(input("Enter percentage: "))
income = float(input("Enter annual family income: ₹"))
attendance = float(input("Enter attendance percentage: "))

print("\n--- Scholarship Eligibility ---")
print("Student Name:", name)

if percentage >= 75 and income <= 400000 and attendance >= 75:
    print("Eligibility Status: Eligible")

    if percentage >= 90:
        print("Scholarship Category: Full Scholarship")
    else:
        print("Scholarship Category: Partial Scholarship")
else:
    print("Eligibility Status: Not Eligible")
    print("Scholarship Category: None")

    if percentage < 75 or income > 400000 or attendance < 75:
        print("Reason for Not Eligible:")

        if percentage < 75:
            print("Percentage is below 75%")
        if income > 400000:
            print("Annual family income exceeds ₹4,00,000")
        if attendance < 75:
            print("Attendance is below 75%")