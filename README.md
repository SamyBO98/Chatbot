# Flask Chatbot with Weather Integration

![Python](https://img.shields.io/badge/Python-3.11-blue) ![Flask](https://img.shields.io/badge/Flask-2.3-green) ![ChatterBot](https://img.shields.io/badge/ChatterBot-1.0.5-orange) ![spaCy](https://img.shields.io/badge/spaCy-3.7.2-lightgrey)

## Description

This project is an **interactive chatbot** developed in Python using Flask.  
It can respond to general questions using **ChatterBot** and provide **weather information for a city** using the OpenWeather API and **spaCy** for entity recognition.  

The project combines natural language processing (NLP) and external API integration to create a simple and effective user experience.

## Features

1. **General Chat**  
   - Automatic responses based on ChatterBot training.  
   - Default response if the bot does not understand the question: `"Sorry I don’t have any answer"`.

2. **City Weather**  
   - Automatic detection of city names in user input using **spaCy**.  
   - Fetches real-time weather information from the **OpenWeather API**.  
   - Handles errors: city not found, empty input, or server issues.

3. **Web Interface**  
   - Simple web page (`index.html`) to chat with the bot and display responses.

## Installation

1. Clone the project:  
```bash
git clone https://github.com/SamyBO98/Chatbot.git
cd Chatbot
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1 
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Add your OpenWeather API key in a .env file:
OPENWEATHER_API_KEY=your_api_key

## Usage
```bash
python app.py
```
