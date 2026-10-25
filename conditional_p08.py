name = input("Enter customer name: ")
age = int(input("Enter age: "))
show_type = input("Enter show type (Morning/Evening): ")
day_type = input("Enter day type (Weekday/Weekend): ")

print("\n--- Movie Ticket Booking ---")
print("Customer Name:", name)

if age < 0:
    print("Error: Age cannot be negative.")

elif (show_type == "Morning" or show_type == "morning" or
      show_type == "Evening" or show_type == "evening") and (
      day_type == "Weekday" or day_type == "weekday" or
      day_type == "Weekend" or day_type == "weekend"):

    original_price = 200
    discount = 0
    surcharge = 0

    if age < 12:
        discount = original_price * 0.50
    elif age >= 60:
        discount = original_price * 0.30

    if show_type == "Morning" or show_type == "morning":
        discount = discount + 30

    if day_type == "Weekend" or day_type == "weekend":
        surcharge = 50

    final_price = original_price - discount + surcharge

    print("Original Ticket Price: ₹", original_price)
    print("Discount: ₹", discount)
    print("Weekend Surcharge: ₹", surcharge)
    print("Final Ticket Price: ₹", final_price)

else:
    print("Error: Invalid show type or day type.")