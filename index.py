from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#read_only False = bot can learn from the conversation
#chatterbot.logic.BestMatch = compare message to sentences he knows -> get the closest answer
bot = ChatBot("chatbot", read_only=False, logic_adapter=["chatterbot.logic.BestMatch"])

#Question and Answer
list_to_train = [
    "hi",
    "hi there",
    "What's your name?",
    "I am a chatbot",
    "How old are you ?",
    "I am very old"

]

list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)