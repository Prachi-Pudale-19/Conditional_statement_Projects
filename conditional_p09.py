name = input("Enter customer name: ")
age = int(input("Enter age: "))
risk = input("Enter occupation risk (Low/Medium/High): ")
smoker = input("Are you a smoker? (Yes/No): ")

base_premium = 10000
additional = 0

print("\n--- Insurance Premium Details ---")
print("Customer Name:", name)

if age < 18:
    print("Eligibility: Not Eligible")
    print("Reason: Age must be 18 or above")

elif ((risk == "Low" or risk == "low" or
       risk == "Medium" or risk == "medium" or
       risk == "High" or risk == "high") and
      (smoker == "Yes" or smoker == "yes" or
       smoker == "No" or smoker == "no")):

    if age > 50:
        additional = additional + 5000

    if risk == "High" or risk == "high":
        additional = additional + 7000
    elif risk == "Medium" or risk == "medium":
        additional = additional + 3000

    if smoker == "Yes" or smoker == "yes":
        additional = additional + 5000

    final_premium = base_premium + additional

    print("Eligibility: Eligible")
    print("Base Premium: ₹", base_premium)
    print("Additional Charges: ₹", additional)
    print("Final Premium: ₹", final_premium)

    if additional >= 10000:
        print("Risk Message: High Risk Policy")
    else:
        print("Risk Message: Normal Risk Policy")

else:
    print("Error: Invalid occupation risk or smoking status")