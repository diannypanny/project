print "Bucket List Time!"
print "Let's create an awesome Bucket List of the things you've always dreamed of doing!"

responses = {}
question1="What's the most dangerous thing you want to do? "
question2="What's the scariest thing you want to do? "
question3="What languages do you want to learn? "
question4="What countries do you want to visit? "
question5="What animals do you want to come face to face with? "
question6="Where do you want to volunteer? "
question7="Who have you always wanted to meet? "
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
	user_input = raw_input("Where do you want to volunteer? ")
	responses[question6]=user_input 
	user_input = raw_input("Who have you always wanted to meet? ")
	responses[question7]=user_input
	user_input = raw_input("If you're all finished, write exit! ")
	#responses[question8]=user_input
	if user_input == "exit!":
		break

#print responses
bucket_list_file = open("bucket_list_file.txt", 'w+')

bucket_list_file.write("WELCOME TO YOUR BUCKET LIST!\n\n") 
print "WELCOME TO YOUR BUCKET LIST!"

count = 1
for question in responses: #for each key (question) the value (user's answer) will print
	print question, responses[question]
	bucket_list_file.write(str(count) + ". " + question + "\n" + responses[question] + "\n") 
	count += 1

bucket_list_file.write("\nNOW GO MAKE YOUR DREAMS COME TRUE!\n") 
print "NOW GO MAKE YOUR DREAMS COME TRUE!"

bucket_list_file.close()

