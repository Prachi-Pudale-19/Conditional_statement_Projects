bill = float(input("Enter food bill amount: ₹"))
membership = input("Are you a member? (Yes/No): ")

print("\n--- Restaurant Bill ---")
name = input("Enter Customer Name: ")
print("Customer Name:", name)

if bill < 0:
    print("Error: Bill amount cannot be negative.")

elif membership == "Yes" or membership == "yes" or membership == "No" or membership == "no":

    if bill < 1000:
        discount = 0
    elif bill < 3000:
        discount = bill * 0.05
    elif bill < 5000:
        discount = bill * 0.10
    else:
        discount = bill * 0.15

    if membership == "Yes" or membership == "yes":
        discount = discount + (bill * 0.05)

    amount_after_discount = bill - discount
    service_charge = amount_after_discount * 0.05
    final_amount = amount_after_discount + service_charge

    print("Original Bill: ₹", bill)
    print("Discount: ₹", discount)
    print("Service Charge: ₹", service_charge)
    print("Final Payable Amount: ₹", final_amount)

    if final_amount >= 5000:
        print("Thank you for being a valued customer")
    else:
        print("Thank you for visiting our restaurant!")

else:
    print("Error: Invalid membership status. Enter Yes or No.")