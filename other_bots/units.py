from chatterbot import ChatBot

bot = ChatBot(
    "Units",
    read_only=True,
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.UnitConversion'
        }
    ]
)

print("--------------Unit Conversion ChatBot----------------")

while True:
    user_response = input("Ask a question about units : ")
    res = bot.get_response(user_response)
    print("Chatbot : " + str(res))