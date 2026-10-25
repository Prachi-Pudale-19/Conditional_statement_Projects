name = input("Enter customer name: ")
amount = float(input("Enter purchase amount: "))
customer_type = input("Enter customer type (Regular/Premium): ")

discount = 0

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 3000 and amount < 5000:
    discount = amount * 0.10
elif amount >= 1000 and amount < 3000:
    discount = amount * 0.05
else:
    discount = 0

if customer_type == "Premium" or customer_type == "premium":
    if amount > 0:
        discount = discount + (amount * 0.05)

final_amount = amount - discount

if final_amount >= 2000:
    delivery = 0
else:
    delivery = 100

payable = final_amount + delivery

print("\n--- Shopping Checkout ---")
print("Customer Name:", name)
print("Discount Amount: ₹", discount)
print("Delivery Charge: ₹", delivery)
print("Final Payable Amount: ₹", payable)