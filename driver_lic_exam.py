#Program on drivers license exams

#These are the correct answers from the multiply choice questions
answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
incorrect_questions = []
correct_ans = 0

#take input from a file
user_file = open('drivers_exam.txt', 'r')

user_choices = user_file.readline() #reading the file into the user_choices list

user_file.close() #closing the file
#processing inputs
for i in range(len(user_choices)):
    if (user_choices[i] == answers[i]):
        correct_ans += 1
    else :
        incorrect_questions.append(i)

#printing out results
if (correct_ans >= 15):
    print("The student passed the exam")
else :
    print("The student failed the exam")

print(f"The total number of correctly answered questions are {correct_ans}")
print(f"The total number of incorrectly answered questions are {len(incorrect_questions)}")

# list of incorrectly answered question
print("Incorrectly answered question: ", end="")
for i in range(len(incorrect_questions)):
    print(incorrect_questions[i] + 1, end=", ")

print()#moving to newline