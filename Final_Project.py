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
		print "NOW GO MAKE IT HAPPEN!"
		for item in self.my_list:
			print item

my_bucket_list = BucketList() # create a new instance of bucket list
#get input from user 
while True:
	user_input = raw_input("What's the most dangerous thing on your bucket list? ")
	#user_input = raw_input("What would you do if you had unlimited money? ")
	#user_input = raw_input("What would you do if you had unlimited time? ")
	#user_input = raw_input("What skills do you want to learn? ")
	#user_input = raw_input("If you're all finished, write exit! ")
	if user_input == "exit!":
		break
	my_bucket_list.add(user_input) #call the add method on my_to_do_list
	#my_bucket_list.add("Explore the Amazons in Brazil") #call the add method on my_to_do_list

my_bucket_list.print_bucket()

#want to make it look pretty
#



	