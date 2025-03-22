product = ['phone', 'tablet', 'laptop','journal']
#displaying products
print(f" Current list of items : {product}")

#asking user to remove a product
#remove_item = input("Enter product to remove from the above list:")
#product.remove(remove_item)

#displaying the entire list after removing item
#print(f"Current list of tems :{product}")

#code to add items
#add_item = input("Enter prodcut to add:")
#product.append(add_item)
#print(f"Current list of tems :{product}")

#Adding item at a specific position
add_item = input("Enter product to add: ")
add_after = input(f"After which product do you want to place {add_item} ")

index = product.index(add_after)
product.insert(index-1,add_item)
print(f"Current list of tems :{product} ")