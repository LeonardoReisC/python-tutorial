import copy, pprint as p
# generate new_prices by deep copy
# increase products price by 10%
products = [
    {'name': 'Product 5', 'price': 10.00},
    {'name': 'Product 1', 'price': 22.32},
    {'name': 'Product 3', 'price': 10.11},
    {'name': 'Product 2', 'price': 105.87},
    {'name': 'Product 4', 'price': 69.90},
]

new_prices = [{**item, 'price': round(item['price']*1.1, 2)}
              for item in copy.deepcopy(products)]

p.pprint(new_prices)
print()

# sort the products by name in descending order
# generate sorted_products_by_name by deep copy

sorted_products_by_name = copy.deepcopy(products)
sorted_products_by_name.sort(key=lambda x: x['name'], reverse=True)

p.pprint(sorted_products_by_name)
print()

# sort the products by price
# generate sorted_products_by_price by deep copy

sorted_products_by_price = copy.deepcopy(products)
sorted_products_by_price.sort(key=lambda x: x['price'])

p.pprint(sorted_products_by_price)
