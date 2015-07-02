"""1. Create a Bucket List class, the class will have

Attributes:
	my_list

Methods:
	add(string) : Adds an item to my_list.
	remove() : Removes an item from my_list.
	print() : Prints and formats the entire list. 
"""

print "Bucket List Time!"
print "Let's create an awesome Bucket List of the things you've always dreamed of doing!"

class BucketList(object):
	def __init__(self):
		self.my_list = []

	def add(self, item):
		self.my_list.append(item)

	def print_bucket(self):
		print "NOW GO MAKE IT HAPPEN!"
		#for item in self.my_list:
		#	print item

my_bucket_list = BucketList() # create a new instance of bucket list
responses = {}
question1="What's the most dangerous thing you want to do? "
question2="What's the scariest thing you want to do? "
question3="What languages do you want to learn? "
question4="What countries do you want to visit? "
question5="What animals do you want to come face to face with? "
question6="Is there somewhere that you want to volunteer? "
question7="Is there someone you always wanted to meet? "
question8="If you're all finished, write exit! "

#get input from user 
while True:
	user_input = raw_input("What's the most dangerous thing you want to do? ") 
	responses[question1]=user_input
	user_input = raw_input("What's the scariest thing you want to do? ")
	responses[question2]=user_input
	user_input = raw_input("What languages do you want to learn? ")
	responses[question3]=user_input
	user_input = raw_input("What countries do you want to visit? ")
	responses[question4]=user_input
	user_input = raw_input("What animals do you want to come face to face with? ")
	responses[question5]=user_input
	user_input = raw_input("Is there somewhere that you want to volunteer? ")
	responses[question6]=user_input 
	user_input = raw_input("Is there someone you always wanted to meet? ")
	responses[question7]=user_input
	user_input = raw_input("If you're all finished, write exit! ")
	responses[question8]=user_input
	if user_input == "exit!":
		break
print responses

my_bucket_list.print_bucket()

#build a string in the format that I want, so create a for loop that goes through each item (key:value pair) in the dict
#google looping through a dictionary

bucket_list_file = open("bucket_list_file.txt", 'w+')
bucket_list_file.write(str(responses))
bucket_list_file.close()

#how do I want to make it look pretty? 