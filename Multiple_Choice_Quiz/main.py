# Create the class for the Questions data set
class Question:
    def __init__ (self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# List the questions prompted to the user
question_prompts = [
    "What colors are apples?\n(a) Red/Green \n(b) Purple \n(c) Orange \n\n",
    "What colors are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "WHat colors are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

# Create the objects class
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

# Determine how many answers were correct
def run_test(list_of_questions):
    score = 0
    for question in list_of_questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score = score + 1

    print("You got " + str(score) + "/" + str(len(list_of_questions)) + " questions correct")

run_test(questions)
