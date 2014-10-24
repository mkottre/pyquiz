pyquiz
======

pyquiz is a utility that reads a file with questions and answers in it and displays the questions in a random order. The question will repeat until you input the correct answer. At the present time, the answer must be entered exactly (including capitalization) as it is in the file in order to be correct.

Usage
=====

Example Usage:

	python pyquiz.py NAME_OF_QUIZ_FILE

For example, if you want to use the supplied quiz file, run:

	python pyquiz.py quiz

Depending on your operating system, you may need to run python3 instead of python. 

Quiz File
=========

The quiz file doesn't have to be named quiz, however, if the name contains spaces you will need to surround the file name in quotes when running pyquiz.

The format of the quiz file is the first question on the first line, followed by the answer to that question on the second line, the second question on the line after that...

Example Quiz Format:

	Question 1 goes here
	Answer to question 1 goes here
	Question 2 goes here
	Answer to question 2 goes here
