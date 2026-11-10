# Mechatronics Quiz App
# This program tests basic knowledge of mechatronics and calculates the user's score.

# Store the quiz questions, options, and correct answers in lists.
questions = [
    "What does PLC stand for?",
    "Which device is commonly used to measure temperature?",
    "Which system uses sensors and feedback to control a process?",
    "What does CNC stand for?",
    "Which component converts electrical energy into mechanical motion?"
]

options = [
    ["A. Programmable Logic Controller", "B. Power Line Circuit", "C. Personal Logic Computer"],
    ["A. Thermistor", "B. Resistor", "C. Capacitor"],
    ["A. Open-loop system", "B. Closed-loop system", "C. Manual system"],
    ["A. Computer Numerical Control", "B. Central Network Circuit", "C. Control Number Computer"],
    ["A. Transformer", "B. Motor", "C. Fuse"]
]

answers = ["A", "A", "B", "A", "B"]


def get_answer(question_number):
    """Display one question and return a valid answer from A, B, or C."""
    print("\n" + questions[question_number])

    for option in options[question_number]:
        print(option)

    # Keep asking until the user enters a valid option.
    while True:
        user_answer = input("Choose A, B, or C: ").strip().upper()

        if user_answer in ["A", "B", "C"]:
            return user_answer
        else:
            print("Invalid input. Please enter A, B, or C.")


def calculate_percentage(score, total):
    """Return the quiz score as a percentage."""
    return (score / total) * 100


def get_grade(percentage):
    """Return a grade based on the percentage."""
    if percentage >= 80:
        return "Excellent"
    elif percentage >= 60:
        return "Good"
    elif percentage >= 50:
        return "Pass"
    else:
        return "Keep practising"


def run_quiz():
    """Run the quiz, mark answers, and show the final result."""
    score = 0
    incorrect_questions = []

    print("================================")
    print("       MECHATRONICS QUIZ")
    print("================================")
    print("Answer each question by choosing A, B, or C.")

    # The loop displays and marks every question.
    for i in range(len(questions)):
        user_answer = get_answer(i)

        if user_answer == answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is", answers[i])
            incorrect_questions.append(questions[i])

    percentage = calculate_percentage(score, len(questions))
    grade = get_grade(percentage)

    print("\n========== QUIZ RESULT ==========")
    print("Your score:", score, "out of", len(questions))
    print("Percentage:", round(percentage, 1), "%")
    print("Grade:", grade)

    # Own twist: show the questions the user should revise.
    if incorrect_questions:
        print("\nQuestions to revise:")
        for question in incorrect_questions:
            print("-", question)
    else:
        print("\nPerfect score! You answered every question correctly.")

    print("\nThank you for using the Mechatronics Quiz App.")


# Start the program.
run_quiz()
