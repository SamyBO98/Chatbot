from chatterbot import ChatBot

#read_only False = bot can learn from the conversation
#chatterbot.logic.BestMatch = compare message to sentences he knows -> get the closest answer
bot = ChatBot("chatbot", read_only=False, logic_adapter=["chatterbot.logic.BestMatch"])