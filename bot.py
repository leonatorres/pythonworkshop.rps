import random
from rps import rps

WEATHER = "rainy"
RESPONSES = {
  "What's the weather?":[
    f"The weather is {WEATHER}",
    f"It's {WEATHER} out",
    f"Let me check, it looks {WEATHER}"
  ],

  "Are you a robot?":[
    "What do you think?",
    "Maybe yes, maybe no?",
    "Yes I'm a robot with human feelings"
  ],

  "exit" : "Bye, see you later",

  "defult": "Sorry I didn't understand that."
}

def respond(message): 
  if message in RESPONSES: 
    bot_message = random.choice(RESPONSES[message])
  else:
    bot_message = RESPONSES["defult"]
  return bot_message

def related(message):
  if "weather" in message:
    y_text = "What's the weather?"
  elif "robot" in message:
    y_text = "Are you a robot?"
  elif "exit" in message:
    y_text = "exit"
  elif "game" in message:
    rps()
  else: 
    y_text = ""
  return y_text

def send_message(message):
  print(f"USER: {message}")
  response = respond(message)
  print(f"BOT: {response}")
