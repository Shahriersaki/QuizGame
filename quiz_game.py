def ask_question(question, options, correct_option):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    answer = input("Enter the number of your answer: ")
    return int(answer) == correct_option

def main():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "correct_option": 3
        },
        {
            "question": "What is 2 + 2?",
            "options": ["3", "4", "5", "6"],
            "correct_option": 2
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "correct_option": 2
        }
    ]
    score = 0
    for q in questions:
        if ask_question(q["question"], q["options"], q["correct_option"]):
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect.\n")
    print(f"Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    main()
