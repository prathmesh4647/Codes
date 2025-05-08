def chatbot():
    print("Hello! i am your hotel chatbot. Type 'bye' to exit.\n")
    print("you can ask questions like:")
    print("- What are your checking hours?")
    print("- What are your checkout hours?")

    while True:
        user_input = input("You: ").lower()
    
        if user_input =="bye":
            print("ChatBot: Thank you for contacting us! Have a great day!")
            break
    # Predefined responses
        greetings = ["hello", "hi", "hey"]

        responses = {
            "what are your checking hours": "Our check-in hours are from 2pm to 11pm.",
            "what are your checkout hours": "Our checkout hours are from 7am to 12pm.",
            "do you have a swimming pool": "Yes, we have a swimming pool available for all guests.",
            "is breakfast included": "Yes, breakfast is included in your stay.",
            "do you have a gym": "Yes, we have a gym available for all guests.",
            "is parking available": "Yes, we have free parking available for all guests."
        }

    # Check for greetings
        if user_input in greetings:
            print("ChatBot: Hello! How can i help you?")
        elif user_input in responses:
            print(f"ChatBot: {responses[user_input]}")
        else:
            print("ChatBot: I don't understand. Try asking full questions like 'What are your checking hours?'")
    
chatbot()