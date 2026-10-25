name = input("Enter guest name: ")
room_type = input("Enter room type (Standard/Deluxe/Suite): ")
nights = int(input("Enter number of nights: "))

print("\n--- Hotel Booking Details ---")
print("Guest Name:", name)

if nights > 0:
    if room_type == "Standard" or room_type == "standard":
        price = 2000
    elif room_type == "Deluxe" or room_type == "deluxe":
        price = 3500
    elif room_type == "Suite" or room_type == "suite":
        price = 6000
    else:
        price = 0
        print("Error: Invalid room type")

    if price > 0:
        room_charge = price * nights

        if nights >= 10:
            discount = room_charge * 0.20
        elif nights >= 5:
            discount = room_charge * 0.10
        else:
            discount = 0

        final_amount = room_charge - discount

        print("Room Type:", room_type)
        print("Number of Nights:", nights)
        print("Room Charge: ₹", room_charge)
        print("Discount: ₹", discount)
        print("Final Booking Amount: ₹", final_amount)
else:
    print("Error: Number of nights must be greater than 0")