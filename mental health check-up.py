#Mental Health Check-Up

import time

class CheckUp:
    def __init__(self, name = None, age = None, gender = None):
        self.questions = ["Over the last 2 weeks, how often have you felt little interest or pleasure in doing things?",
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

        self.answers = ["Not at all", "Several days", "More than half the days", "Nearly every day"]
        self.name = name
        self.age = age
        self.gender = gender

    def info(self):
        print('Welcome to the Mental Health Check-Up program.')
        print(sep='\n')
        time.sleep(3)
        print('A list of questions will be generated.')
        time.sleep(3)
        print('Please respond accordingly.')
        time.sleep(3)
        print(sep='\n')
        self.name = input('What is your name? ')
        print(sep='\n')
        self.age = input('How old are you? ')
        print(sep='\n')
        self.gender = input('What is your gender? ')
        print(sep='\n')

    # Define a function to ask the questions and get the patient's answers
    def ask_questions(self, patient_answers = None):
        print("Please answer the following questions based on how you have been feeling over the last 2 weeks:")
        self.patient_answers = []
        for question in self.questions:
            time.sleep(2)
            print(sep='\n')
            print(question)
            for i, answer in enumerate(self.answers):
                print(f"{i + 1}: {answer}")
            while True:
                choice = input("Your choice: ")
                if choice.isdigit() and 1 <= int(choice) <= len(self.answers):
                    break
                print(sep='\n')
                print("Invalid choice. Please choose a number between 1 and", len(self.answers))
            self.patient_answers.append(int(choice))
        return self.patient_answers

    # Define a function to analyze the patient's answers and provide a mental health assessment
    def analyze_answers(self):
        total_score = sum(self.patient_answers)
        if (total_score) >= 20:
            print(sep='\n')
            print(f"Name: {self.name}")
            print(f"Age: {self.age}")
            print(f"Gender: {self.gender}")
            print(sep='\n')
            print(
                "Based on your responses, it seems like you may be experiencing symptoms of depression. We recommend seeking help from a mental health professional for a proper diagnosis and treatment plan.")
            print(sep='\n')
            print(
                "If you feel actively suicidal or have a plan, please call the National Suicide Prevention Lifeline at 1-800-273-8255, or text MHA to 741-741 to talk to a trained counselor from the Crisis Text Line.")
        elif 10 <= total_score < 20:
            print(sep='\n')
            print(f"Name: {self.name}")
            print(f"Age: {self.age}")
            print(f"Gender: {self.gender}")
            print(sep='\n')
            print(
                "Based on your responses, it's possible that you may be experiencing mild symptoms of depression. We recommend monitoring your symptoms and seeking help from a mental health professional if they persist or worsen.")
            print(sep='\n')
            print(
                "If you feel actively suicidal or have a plan, please call the National Suicide Prevention Lifeline at 1-800-273-8255, or text MHA to 741-741 to talk to a trained counselor from the Crisis Text Line.")
        else:
            print(sep='\n')
            print(f"Name: {self.name}")
            print(f"Age: {self.age}")
            print(f"Gender: {self.gender}")
            print(sep='\n')
            print("Based on your responses, it seems like you may not be experiencing significant symptoms of depression. However, if you ever feel like you need support or guidance, it's always a good idea to seek help from a mental health professional.")
            print(sep='\n')
            print("If you feel actively suicidal or have a plan, please call the National Suicide Prevention Lifeline at 1-800-273-8255, or text MHA to 741-741 to talk to a trained counselor from the Crisis Text Line.")

def main():
    start = CheckUp()
    start.info()
    start.ask_questions()
    start.analyze_answers()

if __name__ == '__main__':
    main()
