# Coding Problem: Hindi to English Translation Test

You are tasked with creating a translation validation system for a Hindi to English translation test. In this test, students are given a set of Hindi words as questions, and they must provide the correct English translations as answers. Both the questions and answers should be represented as dictionaries.

## Requirements:

## Question Paper:

Create a dictionary named question_paper where each key is a unique question number (integer), and the corresponding value is a Hindi word (string) that needs to be translated.
- question_paper= {1 : 'Namaste', 2 : 'Dost', 3 : 'Sabji'}

## Student's Answers:

Create another dictionary named student_answers where each key corresponds to the question number, and the value is the student's English translation for the given Hindi word.
- student_answers= {1 : 'Hello', 2 : 'Friend', 3 : 'Fruit'}

## Correct Answers:

Create another dictionary named correct_answers that maps Hindi words to their correct English translations.
- correct_answers= {'Namaste' : 'Hello', 'Dost' : 'Friend', 'Sabji' : 'Vegetable'}

## Task:
Write a Python function named validate_translations(question_paper, student_answers, correct_answers) that takes 3 dictionaries as input:

- question_paper: Dictionary containing question numbers and corresponding Hindi words.
- student_answers: Dictionary containing question numbers and corresponding English translations provided by the student.
- correct_answers: Dictionary containing correct Hindi-to-English translations.
  Functionality:

## Functionality:

1. The function should compare the student's answers with the correct translations.
- If the student’s translation is correct, it should record a "Correct!" response.
- If the translation is incorrect or missing, it should provide the correct translation in the feedback.

2. The function should calculate the student's score:
- 1 mark for each correct answer.
- Total marks are the total number of questions.

3. After displaying the individual results, the function should output:
- The total marks scored by the student.
- The total percentage.
- If the percentage is 50% or more, display "Status: Pass". Otherwise, display "Status: Not Qualified".

## Output should look like this:

- Question 1: Correct
- Question 2: Correct
- Question 3: Incorrect! The correct answer for 'Sabji' is 'Vegetable'
- Total Marks: 2
- Total Percentage: 66.67%
- Status: Pass