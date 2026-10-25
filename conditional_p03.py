name = input("Enter account holder name: ")
balance = float(input("Enter current balance: ₹"))
withdrawal = float(input("Enter withdrawal amount: ₹"))

print("\n--- ATM Transaction ---")
print("Account Holder:", name)

if withdrawal > 0:
    if withdrawal <= balance:
        if withdrawal <= 20000:
            balance = balance - withdrawal
            print("Transaction Status: Successful")
            print("Withdrawn Amount: ₹", withdrawal)
            print("Remaining Balance: ₹", balance)

            if balance < 1000:
                print("Low Balance Warning")
        else:
            print("Transaction Status: Rejected")
            print("Reason: Maximum withdrawal limit is ₹20000")
    else:
        print("Transaction Status: Rejected")
        print("Reason: Insufficient account balance")
else:
    print("Transaction Status: Rejected")
    print("Reason: Withdrawal amount must be greater than ₹0")