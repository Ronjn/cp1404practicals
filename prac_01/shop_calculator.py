print("Number of items: ")
NoItems = int(input())
totalPrice = 0

while NoItems < 0:
    print("Invalid number of items!")
    print("Number of items: ")
    NoItems = int(input())

for i in range(0, NoItems, 1):
    print("Price of item: ")
    price = int(input())
    totalPrice = totalPrice + price

if totalPrice > 100:
    totalPrice = 0.9 * totalPrice
    print(f"Total price for {NoItems} items is {totalPrice}")
else:
    print(f"Total price for {NoItems} items is {totalPrice}")
