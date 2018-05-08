import unittest
from grocery_list import *

class TestListApp(unittest.TestCase):

	def setUp(self):
		self.store = Store("Test_Store")
		self.user = User()
		self.item = Item("Eggs", 2)
		self.item2 = Item("Chicken", 1)

	def test_add(self):
		self.store.add_item(self.item, self.item2)
		self.assertEqual([self.item, self.item2], self.store.list_of_items[0:])

	def test_remove(self):
		self.store.add_item(self.item)
		self.store.remove_item(self.item)
		self.assertEqual([], self.store.list_of_items[0:])

	def test_duplicate_store(self):
		self.new_store = Store("Test_Store")
		self.user.addStore(self.store)
		result = self.user.addStore(self.new_store)
		self.assertEqual("You already have a list for this store", result)

	def test_duplicate_items(self):
		self.new_item = Item("Eggs", 2)
		self.store.add_item(self.item)
		result = self.store.add_item(self.new_item)
		self.assertEqual("You already have that item on this list", result)


if __name__ == '__main__':
	unittest.main()


#---------------------------------------------------------------------------------
# #User should be able to create a shopping list 
# #User should be able to add grocery items to a particular shopping list
# #User should not be able to create duplicate lists (lists that have the same shop name)
# #User should not be able to add duplicate items to a list
# #User should be able to display shopping lists along with items of each list
# #User should be able to supply the quantity of each item in the shopping list
# #User should be able to remove items from the shopping list
#---------------------------------------------------------------------------------