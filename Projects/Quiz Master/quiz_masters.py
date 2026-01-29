questions = [
    {
        "question": "What is the capital of Nepal?",
        "options": [
            "A. Kathmandu",
            "B. Pokhara",
            "C. Lalitpur",
            "D. Biratnagar"
        ],
        "answer": "A"
    },
    {
        "question": "What is the capital of Japan?",
        "options": [
            "A. Beijing",
            "B. Tokyo",
            "C. New Delhi",
            "D. Washington DC"
        ],
        "answer": "B"
    },
    {
        "question": "Which language is used for Data Science?",
        "options": [
            "A. HTML",
            "B. Python",
            "C. CSS",
            "D. XML"
        ],
        "answer": "B"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Personal Unit",
            "C. Central Program Unit",
            "D. Control Processing User"
        ],
        "answer": "A"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(" Wrong!")

print("\n Quiz Completed!")
print("Your final score:", score, "/", len(questions))
