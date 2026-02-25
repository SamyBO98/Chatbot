from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask

#read_only False = bot can learn from the conversation
#chatterbot.logic.BestMatch = compare message to sentences he knows -> get the closest answer
listAdapter = {
    "import_path":"chatterbot.logic.BestMatch",
    "default_response":"Sorry I dont have any answer",
}

bot = ChatBot("chatbot", read_only=True, 
              logic_adapter=[listAdapter])



trainer = ChatterBotCorpusTrainer(bot)
#Train on conversation in english (dataset)
trainer.train("chatterbot.corpus.english")


#Ask user to type something and paste it to our bot
while True:
    user_response = input("User : ")
    res = bot.get_response(user_response)
    print("Chatbot : " +str(res))
    