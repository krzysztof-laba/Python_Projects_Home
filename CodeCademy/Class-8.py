class Animal(object):
	"""Makes cute animals."""
	is_alive = True
	healf = "good"
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def description(self):
		print(self.name)
		print(self.age)
	def sentence(self):
		print("**********************")
		print("Hippo has name", self.name, "and his age is", self.age)

hippo = Animal("Alex", 25)
# hippo.description()


hippo.sentence()

sloth = Animal("Lazy", 100)
ocelot = Animal("Goat", 7)

print(hippo.healf)
print(sloth.healf)
print(ocelot.is_alive)
print(sloth.sentence())