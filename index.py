from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import random
import re

# Normalisation
def clean(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# Bot param
listAdapter = {
    "import_path":"chatterbot.logic.BestMatch",
    "default_response":"Sorry, I don't have an answer",
}

bot = ChatBot("chatbot", read_only=True, logic_adapters=[listAdapter])

# Dict questions -> answers
qa_pairs = {
    clean("hi"): ["Hi there", "Hello", "Hey!"],
    clean("hello"): ["Hi there", "Hello", "Hey!"],
    clean("what's your name?"): ["I am a chatbot", "You can call me Chatbot"],
    clean("how old are you?"): ["I am very old", "I was created recently"],
}

#get best questions
#user: "Hi bot"
# {hi, bot}
# compare to all our qa_pairs
# match with the one who has the most words in it
def find_best_question(user_text, qa_dict):
    user_words = set(clean(user_text).split())
    best_question = None
    max_common = 0
    for question in qa_dict.keys():
        question_words = set(clean(question).split())
        common_words = len(user_words & question_words)
        if common_words > max_common:
            max_common = common_words
            best_question = question
    if max_common > 0:
        return best_question
    return None

# Train
trainer = ListTrainer(bot)
for question, responses in qa_pairs.items():
    for response in responses:
        trainer.train([question, response])

# Ask user Input
CONFIDENCE_THRESHOLD = 0.5 
while True:
    user_input = input("User: ")
    cleaned_input = clean(user_input)

    best_key = None
    best_score = 0

    input_words = set(cleaned_input.split())

    for question in qa_pairs.keys():
        question_words = set(clean(question).split())

        common_words = len(input_words & question_words)

        if len(question_words) > 0:
            score = common_words / len(input_words)
        else:
            score = 0

        if score > best_score:
            best_score = score
            best_key = question

    if best_score >= CONFIDENCE_THRESHOLD:
        print("Chatbot:", random.choice(qa_pairs[best_key]))
    else:
        print("Chatbot: Sorry I dont have any answer")

    print("Confidence:", round(best_score, 2))