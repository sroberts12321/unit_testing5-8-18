class User:
	def __init__(self):
		self.list_of_stores = []

	def addStore(self, store):
		if store.name not in self.list_of_stores:
			self.list_of_stores.append(store.name)
		else:
			print("You already have a list for this store")
			return("You already have a list for this store")


class Store:
	def __init__(self, name):
		self.name = name
		self.list_of_items = []
		self.list_of_item_names = []

	def __repr__(self):
		return ('(%s)' % (self.name))

	def add_item(self, *args):
		for item in args:
			if item.item_name not in self.list_of_item_names:
				self.list_of_item_names.append(item.item_name)
				self.list_of_items.append(item)
			else:
				print("You already have that item on this list")
				return("You already have that item on this list")

	def remove_item(self, item_to_remove):
		for item in self.list_of_items:
			if item == item_to_remove:
				self.list_of_items.remove(item)
			else:
				print(f"{item} was not on the shopping list")
				print("Here are the items: ")
				for item in list_of_items:
					print(item)
	def print_list(self):
		print(self.name, ":", self.list_of_items)

class Item:
	def __init__(self, item_name, item_quantity):
		self.item_name = item_name
		self.item_quantity = item_quantity

	def __repr__(self):
		return ('(%s, Amount: %s)' % (self.item_name, self.item_quantity))



#---------------------------------------------------------------------------------
# Objects for testing
#---------------------------------------------------------------------------------
# Target = Store("Target")
# item1 = Item("Eggs", 2)
# item2 = Item("Eggs", 1)
# Gerard = User()

#---------------------------------------------------------------------------------
# Methods for testing
#---------------------------------------------------------------------------------

# Gerard.addStore(Target)
# Target.add_item(item1)
# Target.print_list()
# Target.add_item(item2)
# print(item1.item_name)
# print(item2.item_name)
# Gerard.addStore(Walmart)
# print(Gerard.list_of_stores)