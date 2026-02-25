from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import random
import re


def clean(text):
    return re.sub(r'[^\w\s]', '', text.lower())


listAdapter = {
    "import_path":"chatterbot.logic.BestMatch",
    "default_response":"Sorry I dont have any answer",
    "maximum_similarity_threshold":0.90
}

# Bot classique
bot = ChatBot("chatbot", read_only=True, logic_adapters=[listAdapter])

# Dict question -> answers
qa_pairs = {
    "hi": ["Hi there", "Hello", "Hey!"],
    "what's your name?": ["I am a chatbot", "You can call me Chatbot"],
    "how old are you?": ["I am very old", "I was created recently"],
}

# Training
trainer = ListTrainer(bot)
for question, answers in qa_pairs.items():
    for answer in answers:
        trainer.train([question, answer])

# Ask user input
while True:
    user_response = input("User: ").lower() 
    res = bot.get_response(user_response)
    if user_response in qa_pairs:
        # Random choice
        print("Chatbot:", random.choice(qa_pairs[user_response]))
    else:
        if res.confidence > 0.8:
            print("Chatbot:", res)
        else:
            print("Chatbot : " + str(listAdapter["default_response"]))
    print("Confidence : ", res.confidence)
    