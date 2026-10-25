name = input("Enter customer name: ")
plan = input("Enter plan type (Basic/Standard/Premium): ")
extra_data = float(input("Enter extra data used in GB: "))

print("\n--- Mobile Data Bill ---")
print("Customer Name:", name)

if extra_data < 0:
    print("Error: Negative data usage is invalid.")

else:
    if plan == "Basic" or plan == "basic":
        base_charge = 299
    elif plan == "Standard" or plan == "standard":
        base_charge = 499
    elif plan == "Premium" or plan == "premium":
        base_charge = 799
    else:
        base_charge = 0
        print("Error: Invalid plan type.")

    if base_charge > 0:
        extra_charge = extra_data * 20

        if extra_data > 10:
            surcharge = 100
        else:
            surcharge = 0

        final_bill = base_charge + extra_charge + surcharge

        print("Plan Type:", plan)
        print("Base Plan Charge: ₹", base_charge)
        print("Extra Data Charge: ₹", extra_charge)
        print("Surcharge: ₹", surcharge)
        print("Final Bill: ₹", final_bill)
