import random

def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hi there! How can I assist you?"
    elif "how are you" in user_input:
        return "I'm just a bot, but thanks for asking!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "i didnt understand that"

def main():
    print("simple chatbot")
    print("what to do")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Bot: Goodbye! Have a great day!")
            break
        else:
            response = get_response(user_input)
            print("Bot:", response)

if __name__ == "__main__":
    main()