import random, sys

quiz_file = open(sys.argv[1], 'r') # Opens the quiz file, supplied by the command line argument, as read-only
quiz = quiz_file.readlines() # Creates a list with each element being either a question or an answer
questions = [] # Creates an empty questions list
answers = [] # Creates an empty answers list
number_of_questions = len(quiz) // 2 # Since every question and answer use 2 lines, divide the number of lines in the file by 2 to get the number of questions

for x in range(0, number_of_questions):
	i = x * 2
	questions.append(quiz[i].strip('\n')) # Fill the questions list with the questions from the file
	answers.append(quiz[i+1].strip('\n')) # Fill the answers list with the answers from the file

for x in range(0, number_of_questions):
	print("\n============================")
	random_num = random.randint(0, number_of_questions - 1) # Generates a random number between 0 and the number of questions
	break_loop = False # Used to break the loop when the correct answer is entered
	while break_loop != True: # Loops until the correct answer is entered
		user_input = input("\n" + questions[random_num] + "\n") # Prints the question
		if user_input == answers[random_num]: # If correct, break out of the loop
			print("\nCorrect!")
			break_loop = True
		else: # The answer is wrong so repeat the loop
			print("Try again")
	
	del questions[random_num] # Removes the question from the list so it cannot be displayed again
	del answers[random_num] # Removes the answer from the list so it cannot be displayed again
	number_of_questions -= 1 # Since we removed a question, the number of questions is now 1 less than before
