"""1. Create a to do list class, the class will have an 

Attributes:
	my_list

Methods:
	add(string) : Adds an item to my_list.
	remove() : Removes an item from my_list.
	print() : Prints and formats the entire list. 
"""

class BucketList(object):
	def __init__(self):
		self.my_list = []

	def add(self, item):
		self.my_list.append(item)

	def print_bucket(self):
		print "DO OR DIE"
		for item in self.my_list:
			print item

my_bucket_list = BucketList() # create a new instance of a to do list
my_bucket_list.add("Hike up Mt. Kili") #call the add method on my_to_do_list
my_bucket_list.add("Explore the Amazons in Brazil") #call the add method on my_to_do_list
my_bucket_list.print_bucket()



	