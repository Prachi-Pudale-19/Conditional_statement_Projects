name = input("Enter employee name: ")
salary = float(input("Enter monthly salary: ₹"))
experience = int(input("Enter years of experience: "))
rating = int(input("Enter performance rating (1-5): "))

print("\n--- Employee Bonus Details ---")
print("Employee Name:", name)

if rating < 1 or rating > 5:
    print("Invalid Rating! Enter a rating between 1 and 5.")

else:
    if experience >= 10 and rating >= 4:
        bonus_percent = 20
    elif experience >= 5 and rating >= 4:
        bonus_percent = 15
    elif experience >= 2 and rating >= 3:
        bonus_percent = 10
    else:
        bonus_percent = 0

    bonus_amount = salary * bonus_percent / 100
    final_salary = salary + bonus_amount

    print("Bonus Percentage:", bonus_percent, "%")
    print("Bonus Amount: ₹", bonus_amount)
    print("Final Salary: ₹", final_salary)

    if rating == 5:
        print("Performance Message: Excellent Performer")
    else:
        print("Performance Message: Keep Improving")