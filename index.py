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
    "maximum_similarity_threshold":0.90
}

bot = ChatBot("chatbot", read_only=True, logic_adapters=[listAdapter])

# Dict questions -> answers
qa_pairs = {
    clean("hi"): ["Hi there", "Hello", "Hey!"],
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

    res = bot.get_response(user_input)

    if res.confidence >= CONFIDENCE_THRESHOLD:

        closest_key = None
        max_similarity = 0
        #Compare with questions (first val of qa_pairs)
        for question in qa_pairs.keys():
            cleaned_question = clean(question)

            #word in common
            input_words = set(cleaned_input.split())
            question_words = set(cleaned_question.split())

            similarity = len(input_words & question_words)

            if similarity > max_similarity:
                max_similarity = similarity
                closest_key = question

        #at least one word in common
        if closest_key and max_similarity > 0:
            print("Chatbot:", random.choice(qa_pairs[closest_key]))
        else:
            print("Chatbot:", listAdapter["default_response"])

    else:
        print("Chatbot:", listAdapter["default_response"])

    print("Confidence:", res.confidence)