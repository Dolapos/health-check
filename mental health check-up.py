# Mental Health Check-up Program
import time

print('Welcome to the Mental Health Check-Up program.')
print(sep='\n')
time.sleep(3)
print('A list of questions will be generated.')
time.sleep(3)
print('Please respond accordingly.')
time.sleep(3)
print(sep='\n')
name = input('What is your name? ')
print(sep='\n')
age = input('How old are you? ')
print(sep='\n')
gender = input('What is your gender? ')
print(sep='\n')

# Define a list of questions
questions = [
    "Over the last 2 weeks, how often have you felt little interest or pleasure in doing things?",
    "Over the last 2 weeks, how often have you been feeling down, depressed, or hopeless?",
    "Over the last 2 weeks, how often have you been feeling nervous, anxious, or on edge?",
    "Over the last 2 weeks, how often have you been unable to stop or control worrying?",
    "Over the last 2 weeks, how often have you been bothered by feeling afraid as if something awful might happen?",
    "Over the last 2 weeks, how often have you been feeling irritable or having angry outbursts?",
    "Over the last 2 weeks, how often have you been having trouble falling or staying asleep, or sleeping too much?",
    "Over the last 2 weeks, how often have you been feeling tired or having little energy?",
    "Over the last 2 weeks, how often have you been having trouble concentrating on things such as reading a book, watching television, or working on a computer?",
    "Over the last 2 weeks, how often have you been moving or speaking so slowly that other people could have noticed? Or so fidgety or restless that you have been moving a lot more than usual?",
    "Over the last 2 weeks, how often have you been having thoughts that you would be better off dead or of hurting yourself in some way?"]

# Define a list of possible answers
answers = ["Not at all", "Several days", "More than half the days", "Nearly every day"]

# Define a function to ask the questions and get the patient's answers
def ask_questions():
    print("Please answer the following questions based on how you have been feeling over the last 2 weeks:")
    patient_answers = []
    for question in questions:
        print(question)
        for i, answer in enumerate(answers):
            print(f"{i + 1}: {answer}")
        while True:
            choice = input("Your choice: ")
            if choice.isdigit() and 1 <= int(choice) <= len(answers):
                break
            print("Invalid choice. Please choose a number between 1 and", len(answers))
        patient_answers.append(int(choice))
    return patient_answers

# Define a function to analyze the patient's answers and provide a mental health assessment
def analyze_answers(patient_answers):
    total_score = sum(patient_answers)
    if total_score >= 20:
        print("Based on your responses, it seems like you may be experiencing symptoms of a mental health condition. We recommend seeking help from a mental health professional for a proper diagnosis and treatment plan.")
    elif 10 <= total_score < 20:
        print("Based on your responses, it's possible that you may be experiencing mild symptoms of a mental health condition. We recommend monitoring your symptoms and seeking help from a mental health professional if they persist or worsen.")
    else:
        print("Based on your responses, it seems like you may not be experiencing significant symptoms of a mental health condition. However, if you ever feel like you need support or guidance, it's always a good idea to seek help from a mental health professional.")

# Call the functions to run the program
patient_answers = ask_questions()
analyze_answers(patient_answers) 