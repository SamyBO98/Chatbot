import re
from chatterbot import ChatBot

# Mapping french to number
simple_numbers = {
    "zéro":0, "un":1, "deux":2, "trois":3, "quatre":4, "cinq":5,
    "six":6, "sept":7, "huit":8, "neuf":9, "dix":10, "onze":11, 
    "douze":12, "treize":13, "quatorze":14, "quinze":15, "seize":16,
    "vingt":20, "trente":30, "quarante":40, "cinquante":50,
    "soixante":60, "soixante-dix":70, "quatre-vingt":80, "quatre-vingt-dix":90,
    "cent":100, "mille":1000
}

#Replace words by expr
def replace_operators(expr):
    expr = expr.replace("plus", "+")
    expr = expr.replace("moins", "-")
    expr = expr.replace("fois", "*")
    expr = expr.replace("multiplie par", "*")
    expr = expr.replace("divisé par", "/")
    return expr

#French words to number
def french_words_to_numbers(expr):
    expr = replace_operators(expr.lower())
    for word, num in simple_numbers.items():
        expr = re.sub(r"\b"+word+r"\b", str(num), expr)
    return expr


#print(french_words_to_numbers("quatre plus quatre"))


bot = ChatBot(
    "Math",
    read_only=True,
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.MathematicalEvaluation'
        }
    ]
)

print("--------------Math ChatBot----------------")

while True:
    
    user_response = input("Type Math equation : ")
    converted_input = french_words_to_numbers(user_response.lower())
    print(converted_input)
    response = bot.get_response(converted_input)
    print("Chatbot : " +str(response))

