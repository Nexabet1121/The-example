# This proggram simulates shopping and displaying receipts


# Get info for item 1
item1 = input("Enter first item: ")
quantity1 = int(input(f"Enter the quantity of {item1}: "))
price1 = float(input(f"Enter the prise of {item1}: "))
print()

# Get info for item 2
item2 = input("Enter second item: ")
quantity2 = int(input(f"Enter the quantity of {item2}: "))
price2  = float(input(f"Enter the prise of {item2}: "))
print()


# Get info for item3
item3 = input("Enter third item: ")
quantity3 = int(input(f"Enter the quantity of {item3}: "))
price3 = float(input(f"Enter the prise of {item3}: "))
print()


# Diplay top of the receipt
print("thanks for shopping at totally not a scam bussiness")
print("-*-" * 17)
print()
item = "ITEM"
quantity = "QUANTITY"
item_total = "ITEM TOTAL"
print(f"{item:<20}{quantity:<15}{item_total}")
print()
print(f"{item1:<20}{quantity1:<15}${price1 * quantity1: .2f}\n")
print(f"{item2:<20}{quantity2:<15}${price2 * quantity2: .2f}\n")
print(f"{item3:<20}{quantity3:<15}${price3 * quantity3: .2f}\n")

# Calculate subtotal

subtotal = (price1 * quantity1) + (price2 * quantity2) + (price3 * quantity3)
print(f"Subtotal: ${subtotal: .2f}")

# Calculate tax
tax = subtotal * 0.07
print(f"tax owed: ${tax: .2f}\n")
# calculate total
total = subtotal + tax
print(f"TOTAL OWED: ${total: .2f}\n")
      












