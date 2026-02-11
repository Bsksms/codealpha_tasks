def get_bot_response(user_input):
    """Function to match user input with predefined responses."""
    
    user_input = user_input.lower().strip()

    
    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you today?"
    
    elif "how are you" in user_input:
        return "I'm just a bunch of code, but I'm doing great! Thanks for asking."
    
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"
    
    else:
        return "I'm sorry, I don't understand that. Could you try saying 'hello'?"

def start_chatbot():
    print("--- Basic Python Chatbot ---")
    print("Type 'bye' to end the conversation.")
    
    while True:
        user_text = input("You: ")
        
        
        response = get_bot_response(user_text)
        
        print(f"Bot: {response}")
        
        
        if "bye" in user_text.lower():
            break


if __name__ == "__main__":
    start_chatbot()
    