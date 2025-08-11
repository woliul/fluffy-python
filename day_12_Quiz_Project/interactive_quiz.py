# Day 12: Interactive Quiz Game - Project Day!

import random

# Use a list to store our questions and answers
# Each item in the list is another list containing the question, options, and correct answer
quiz_questions = [
    ["What is the capital of France?", ["A) London", "B) Berlin", "C) Paris", "D) Rome"], "C"],
    ["What is 7 times 8?", ["A) 49", "B) 56", "C) 64", "D) 72"], "B"],
    ["What is the main color of the sky?", ["A) Green", "B) Blue", "C) Red", "D) Yellow"], "B"],
    ["Which module is used for random numbers?", ["A) math", "B) time", "C) random", "D) sys"], "C"],
    ["What keyword defines a function?", ["A) function", "B) func", "C) def", "D) define"], "C"]
]

def run_quiz(questions):
    """
    Runs the quiz game with a list of questions.
    """
    score = 0
    # Optional: shuffle the questions for a new experience each time
    random.shuffle(questions)

    for question_data in questions:
        question = question_data[0]
        options = question_data[1]
        correct_answer = question_data[2]

        print(f"\nQuestion: {question}")
        for option in options:
            print(option)

        user_answer = input("Your answer (A, B, C, or D): ").upper()
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {correct_answer}.")

    print(f"\nQuiz complete! You got {score} out of {len(questions)} correct.")

# Run the quiz when the script is executed
run_quiz(quiz_questions)
