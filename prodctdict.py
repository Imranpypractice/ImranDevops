product = {'phone':100, 'tablet':200, 'laptop':400,'journal':40}
print(product)

deleted_product = input("Enter the name of product to be deleted")
del product[deleted_product]
print(f"Product deleted, here is the list of updated products {product}")
#product = input("Enter product to check the price")
#print(f" Price of the {product} is {product[product]}")

#new_product = input("Enter a product you want to add: ")
#new_product_price = input(f"Enter the price for {new_product}: ")
#product[new_product]=new_product_price
#print(f"Prodcut successfully added , here is an updated list of products {product}")