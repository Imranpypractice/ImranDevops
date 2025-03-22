cart = []
n = int(input("Enter the number of items you want to add"))

for x in range(n):
    item = input("Enter an item into the cart")
    cart.append(item)
    print(cart)