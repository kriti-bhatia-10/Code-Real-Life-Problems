def validate_translations(question_paper, student_answers, correct_answers):
    
    result={}
    correct_marks_count=0
    
    for question_number, Hindi_word in question_paper.items():
        student_translation = student_answers.get(question_number, "")
        correct_translation = correct_answers.get(Hindi_word, "")

        if student_translation == correct_translation:
            result[question_number]="Correct"
            correct_marks_count += 1
        else:
            result[question_number]=f"Incorrect! The correct answer for '{Hindi_word}' is '{correct_translation}'"

    for question_number, validation in result.items():
        print(f"Question {question_number}: {validation}")

    total_questions = len(question_paper)
    total_marks = correct_marks_count
    percentage_marks = (total_marks * 100) / total_questions

    print(f"Total Marks: {total_marks}")
    print(f"Total Percentage: {percentage_marks:.2f}%")

    Status = "Pass" if percentage_marks >= 50 else "Not Qualified"
    print(f"Status: {Status}")



            
question_paper = {1: 'Namaste', 2: 'Dost', 3: 'Sabji'}
student_answers = {1: 'Hello', 2: 'Friend', 3: 'Fruit'}
correct_answers = {'Namaste': 'Hello', 'Dost': 'Friend', 'Sabji': 'Vegetable'}

validate_translations(question_paper, student_answers, correct_answers)