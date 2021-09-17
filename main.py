from bot import related, send_message

print("BOT : Hello! What is your name?")
user_name = input()

print(f"BOT: Nice to meet you {user_name}")

print("BOT: Ask a question! \n Examples: \n - What's the weather \n - Play game \n - Are you a robot?")


while True:
  my_input = input()

  related_text = related(my_input)
  send_message(related_text)

  if my_input == "exit":
    exit()
