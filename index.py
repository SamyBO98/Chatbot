from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#read_only False = bot can learn from the conversation
#chatterbot.logic.BestMatch = compare message to sentences he knows -> get the closest answer
listAdapter = {
    "import_path":"chatterbot.logic.BestMatch",
    "default_response":"Sorry I dont have any answer",
}

bot = ChatBot("chatbot", read_only=True, 
              logic_adapter=[listAdapter])

#Question and Answer
list_to_train = [
    "Hi",
    "Hi there",
    "What's your name?",
    "I am a chatbot",
    "How old are you ?",
    "I am very old",
    "Why are you so mad ?",
    "I am not",
    "Test",
    "Test validate",
    "Can you help me ?",
    "Of course how can I help you ?",
    "What game do you like ?",
    "I love League of Legends",
    "Are you ok ?",
    "Always ok"

]

list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)

#Ask user to type something and paste it to our bot
while True:
    user_response = input("User : ")
    res = bot.get_response(user_response)
    if(res.confidence > 0.9):
        print("Chatbot : " +str(res))
    else:
        print("Chatbot : " + str(listAdapter["default_response"]))
    
    print("Confidence : ", res.confidence)