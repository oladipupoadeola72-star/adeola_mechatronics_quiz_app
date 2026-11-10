# ============================================================
# ADEOLA MECHATRONICS QUIZ APP
# Welcome to Mechatronics Quiz by Adela!
# A Python-based multiple-choice quiz application.
# ============================================================

def run_quiz():
    questions = [
        {
            "question": "What does PLC stand for?",
            "options": [
                "Programmable Logic Controller",
                "Power Line Converter",
                "Process Level Computer",
                "Programmed Linear Circuit",
            ],
            "answer": 0,
            "explanation": "PLC means Programmable Logic Controller. It is used to automate industrial processes."
        },
        {
            "question": "Which device is commonly used to detect temperature?",
            "options": ["Resistor", "Thermistor", "Capacitor", "Transformer"],
            "answer": 1,
            "explanation": "A thermistor is a temperature-sensitive resistor."
        },
        {
            "question": "Which system uses sensors and feedback to regulate its output?",
            "options": ["Open-loop system", "Manual system", "Closed-loop system", "Mechanical-only system"],
            "answer": 2,
            "explanation": "A closed-loop control system uses feedback to compare the output with the desired value."
        },
        {
            "question": "What does CNC stand for?",
            "options": [
                "Computer Numerical Control",
                "Central Network Circuit",
                "Controlled Numeric Connection",
                "Computer Network Communication",
            ],
            "answer": 0,
            "explanation": "CNC means Computer Numerical Control. It controls machine tools using programmed instructions."
        },
        {
            "question": "Which component converts electrical energy into mechanical motion?",
            "options": ["Sensor", "Actuator", "Motor", "Fuse"],
            "answer": 2,
            "explanation": "An electric motor converts electrical energy into mechanical energy."
        },
        {
            "question": "What is the main function of a sensor?",
            "options": [
                "To store electrical energy",
                "To detect a physical quantity",
                "To increase voltage only",
                "To provide mechanical support",
            ],
            "answer": 1,
            "explanation": "A sensor detects a physical quantity such as temperature, pressure, light or position."
        },
        {
            "question": "Which of these is an example of an actuator?",
            "options": ["Thermocouple", "LDR", "Electric motor", "Pressure sensor"],
            "answer": 2,
            "explanation": "An electric motor is an actuator because it produces movement."
        },
        {
            "question": "What does the term robotics mainly involve?",
            "options": [
                "Design, construction and use of robots",
                "Study of rocks",
                "Only the repair of engines",
                "The study of weather",
            ],
            "answer": 0,
            "explanation": "Robotics involves the design, construction, programming and use of robots."
        },
        {
            "question": "Which device is used to measure electric current?",
            "options": ["Voltmeter", "Ammeter", "Thermometer", "Barometer"],
            "answer": 1,
            "explanation": "An ammeter measures electric current."
        },
        {
            "question": "What is the SI unit of force?",
            "options": ["Watt", "Joule", "Newton", "Pascal"],
            "answer": 2,
            "explanation": "Force is measured in newtons (N)."
        },
        {
            "question": "Which component is commonly used to limit current in a circuit?",
            "options": ["Resistor", "Switch", "Motor", "Battery"],
            "answer": 0,
            "explanation": "A resistor opposes the flow of electric current and can be used to limit it."
        },
        {
            "question": "What is the main purpose of a gearbox?",
            "options": [
                "To detect temperature",
                "To change speed and torque",
                "To measure voltage",
                "To store data",
            ],
            "answer": 1,
            "explanation": "A gearbox changes the relationship between rotational speed and torque."
        },
        {
            "question": "Which control system operates without using feedback?",
            "options": ["Closed-loop system", "Open-loop system", "Feedback system", "Servo system"],
            "answer": 1,
            "explanation": "An open-loop control system does not use feedback to correct its output."
        },
        {
            "question": "What does SCADA stand for?",
            "options": [
                "Supervisory Control and Data Acquisition",
                "System Control and Digital Automation",
                "Sensor Communication and Data Analysis",
                "Supervised Computer and Device Arrangement",
            ],
            "answer": 0,
            "explanation": "SCADA means Supervisory Control and Data Acquisition."
        },
        {
            "question": "Which instrument measures voltage?",
            "options": ["Ammeter", "Voltmeter", "Hygrometer", "Tachometer"],
            "answer": 1,
            "explanation": "A voltmeter measures the potential difference between two points."
        },
        {
            "question": "What is the main function of a microcontroller?",
            "options": [
                "To control electronic devices using a program",
                "To generate petrol",
                "To increase the size of a machine",
                "To measure mass only",
            ],
            "answer": 0,
            "explanation": "A microcontroller is a programmable integrated circuit used to control electronic systems."
        },
        {
            "question": "Which sensor can be used to detect the presence of an object without touching it?",
            "options": ["Proximity sensor", "Ammeter", "Fuse", "Transformer"],
            "answer": 0,
            "explanation": "A proximity sensor detects nearby objects without physical contact."
        },
        {
            "question": "What is the purpose of a power supply in an electronic system?",
            "options": [
                "To provide the required electrical energy",
                "To measure distance",
                "To detect sound only",
                "To transmit mechanical force",
            ],
            "answer": 0,
            "explanation": "A power supply provides electrical energy at the voltage and current required by a system."
        },
        {
            "question": "Which manufacturing machine commonly follows programmed tool paths?",
            "options": ["CNC machine", "Hand saw", "Manual file", "Bench vice"],
            "answer": 0,
            "explanation": "A CNC machine follows programmed instructions to control tool movement."
        },
        {
            "question": "What is feedback in a control system?",
            "options": [
                "Returning information about the output to the control system",
                "Switching off every sensor",
                "Increasing the machine's weight",
                "Removing the power supply",
            ],
            "answer": 0,
            "explanation": "Feedback is information about the system output that is returned to influence control."
        },
    ]

    print("=" * 58)
    print("       WELCOME TO MECHATRONICS QUIZ BY ADELA")
    print("=" * 58)
    print("Test your knowledge of basic Mechatronics Engineering.")
    print(f"\nThere are {len(questions)} multiple-choice questions.")
    print("Choose A, B, C or D for each question.")
    input("\nPress ENTER when you are ready to begin...")

    score = 0
    incorrect_answers = []

    for number, item in enumerate(questions, start=1):
        print("\n" + "-" * 58)
        print(f"QUESTION {number} OF {len(questions)}")
        print(item["question"])

        for index, option in enumerate(item["options"]):
            print(f"  {chr(65 + index)}. {option}")

        while True:
            choice = input("Your answer (A/B/C/D): ").strip().upper()
            if choice in ("A", "B", "C", "D"):
                selected = ord(choice) - 65
                break
            print("Invalid choice. Please enter A, B, C or D.")

        correct_index = item["answer"]
        if selected == correct_index:
            print("Correct!")
            score += 1
        else:
            correct_letter = chr(65 + correct_index)
            print(f"Not quite. The correct answer is {correct_letter}. {item['options'][correct_index]}")
            incorrect_answers.append(
                (number, item["question"], choice, correct_letter,
                 item["options"][correct_index], item["explanation"])
            )

        print("Explanation:", item["explanation"])

    total = len(questions)
    percentage = (score / total) * 100

    if percentage >= 80:
        grade = "Excellent"
        comment = "Outstanding performance. Keep it up!"
    elif percentage >= 60:
        grade = "Very Good"
        comment = "Good work. You have a strong understanding."
    elif percentage >= 50:
        grade = "Good"
        comment = "A fair attempt. Keep studying and practising."
    elif percentage >= 40:
        grade = "Pass"
        comment = "You passed, but there is room for improvement."
    else:
        grade = "Needs Improvement"
        comment = "Keep learning. Review the topics and try again."

    print("\n" + "=" * 58)
    print("                 QUIZ RESULT")
    print("=" * 58)
    print(f"Total questions : {total}")
    print(f"Correct answers : {score}")
    print(f"Wrong answers   : {total - score}")
    print(f"Final score     : {score}/{total}")
    print(f"Percentage      : {percentage:.1f}%")
    print(f"Grade           : {grade}")
    print(comment)

    if incorrect_answers:
        print("\nQUESTIONS TO REVIEW")
        print("-" * 58)
        for number, question, chosen, correct_letter, correct_text, explanation in incorrect_answers:
            print(f"\n{number}. {question}")
            print(f"Your answer: {chosen}")
            print(f"Correct answer: {correct_letter}. {correct_text}")
            print(f"Explanation: {explanation}")
    else:
        print("\nPerfect score! You answered every question correctly.")

    print("\nThank you for taking Mechatronics Quiz by Adela!")
    print("=" * 58)


if __name__ == "__main__":
    run_quiz()
