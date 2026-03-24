print("AI Bot: Hello! Ask me something.")

while True:

    user = input("You: ").lower()

    if "hello" in user:
        print("AI Bot: Hi there!")

    elif "your name" in user:
        print("AI Bot: I am your Python AI bot.")

    elif "how are you" in user:
        print("AI Bot: I'm doing great!")

    elif "bye" in user:
        print("AI Bot: Goodbye!")
        break

    else:
        print("AI Bot: I don't understand.")