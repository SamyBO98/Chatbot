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


intents = [
    {
        "tag": "greeting",
        "keywords": ["hi", "hello", "hey", "yo"],
        "responses": ["Hi there!", "Hello!", "Hey"]
    },
    {
        "tag": "name",
        "keywords": ["name", "who"],
        "responses": ["I am a chatbot", "You can call me Chatbot"]
    },

    {
        "tag": "age",
        "keywords": ["old", "age"],
        "responses": ["I am very old", "I was created recently"]
    }
]

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
CONFIDENCE_THRESHOLD = 0.2
while True:
    user_input = input("User: ")
    cleaned_input = clean(user_input)
    input_words = set(cleaned_input.split())

    best_intent = None
    best_score = 0

    for intent in intents:
        intent_keywords = set(intent["keywords"])
        common_words = len(input_words & intent_keywords)
        score = common_words / max(len(input_words), 1)
        if score > best_score:
            best_score = score
            best_intent = intent

    if best_score >= CONFIDENCE_THRESHOLD and best_intent is not None:
        print("Chatbot:", random.choice(best_intent["responses"]))
    else:
        print("Chatbot: Sorry I don't have an answer")

    print("Confidence:", round(best_score, 2))