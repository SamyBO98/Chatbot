from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, render_template, request,jsonify
from dotenv import load_dotenv
import requests
import os
import spacy


app = Flask(__name__)


#read_only False = bot can learn from the conversation
#chatterbot.logic.BestMatch = compare message to sentences he knows -> get the closest answer
listAdapter = {
    "import_path":"chatterbot.logic.BestMatch",
    "default_response":"Sorry I dont have any answer",
}

bot = ChatBot("chatbot", read_only=True, 
              logic_adapter=[listAdapter])



#trainer = ChatterBotCorpusTrainer(bot)
#Train on conversation in english (dataset)
#Uncomment to train once to create DB then comment
#trainer.train("chatterbot.corpus.english")


load_dotenv()
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
nlp = spacy.load('en_core_web_lg')




@app.route("/")
def main():
    return render_template("index.html")


@app.route("/get")
def get_chatbot_response():
    userText = request.args.get('userMessage')
    #If we type nothing return error
    if not userText or userText.strip() == "":
        return jsonify({"error": "Please type something"}), 400
    try:
        doc = nlp(userText)
        city = [ent.text for ent in doc.ents if ent.label_ == "GPE"]
        if not city:
            # No city detected
            return jsonify({"error": "No city found in your message"}), 400
        txt = city[0]
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={
                "q": txt,
                "units": "metric",
                "appid": OPENWEATHER_API_KEY
            }
        )

        data = response.json()
        #print(data)
        #print(data.get("cod"))

        #If city not found return error
        if response.status_code == 404 or str(data.get("cod")) == "404":
            return jsonify({"error": "City not found"}), 404
        #response = bot.get_response(userText)
        #if not response or str(response).strip() == "":
        #    return "I’m not sure how to answer that"
        #return str(response)
        return jsonify(data)

    except Exception as e:
        print(e)
        return jsonify({"error": "Server error"}), 500

if __name__ == '__main__':
    # trainer.train("chatterbot.corpus.english")
    app.run(debug=True, threaded=True)
    

'''
#Ask user to type something and paste it to our bot
while True:
    user_response = input("User : ")
    res = bot.get_response(user_response)
    print("Chatbot : " +str(res))
'''