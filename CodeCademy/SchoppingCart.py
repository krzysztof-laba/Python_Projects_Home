class ShoppingCart(object):
	"""Creates shopping cart objects for users of our fine website"""
	items_in_cart = {}
	def __init__(self, customer_name):
		self.customer_name = customer_name
		print("Customer name:", self.customer_name)

	def add_item(self, product, price):
		"""Add product to the cart"""
		if not product in self.items_in_cart:
			self.items_in_cart[product] = price
			print(product, " added.")
		else:
			print(product, " is arleady in the cart.")

	def remove_item(self, product):
		"""Remove product from the cart."""
		if product in self.items_in_cart:
			del self.items_in_cart[product]
			print(product, " removed")
		else:
			print(product, " is not in the cart.")

my_cart = ShoppingCart("Krzysztof Laba")
my_cart.customer_name

my_cart.add_item("Mleko", 3)
my_cart.add_item("Bułka", 0.5)
my_cart.add_item("Ciastko", 2.2)
my_cart.add_item("Jabłko", 1.5)
print(ShoppingCart.items_in_cart)
my_cart.remove_item("Bułka")
print(ShoppingCart.items_in_cart)