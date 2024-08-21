# Coding Problem: Hindi to English Translation Test

A student is given a set of Hindi words. Each word is assigned a question number. The student has to translate each Hindi word into English.
The answers should be submitted as a dictionary where the keys represent the question number, and the values are the English translations. 

## Examples

## Input : 3 dictionaries
- question_paper= {1: 'Namaste', 2: 'Dost', 3: 'Sabji'}
- correct_answers= {'Namaste': 'Hello', 'Dost': 'Friend', 'Sabji': 'Vegetable'}
- student_answers= {1: 'Hello', 2: 'Friend', 3: 'Vegetable'}

## Output:
- Question 1: Correct
- Question 2: Correct
- Question 3: Correct

## Input : 3 dictionaries
- question_paper= {1: 'Namaste', 2: 'Dost', 3: 'Sabji'}
- correct_answers= {'Namaste': 'Hello', 'Dost': 'Friend', 'Sabji': 'Vegetable'}
- student_answers= {1: 'Hello', 2: 'Friend', 3: 'Fruit'}

## Output:
- Question 1: Correct
- Question 2: Correct
- Question 3: Incorrect! The correct answer for 'Sabji' is 'Vegetable'
