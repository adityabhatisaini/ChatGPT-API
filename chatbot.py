import openai  # Import the OpenAI library

# Set up the OpenAI API key
openai.api_key = "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"  # Replace with your actual API key

print("Welcome to your chatbot! Type 'exit' to quit.")

while True:
    # Get user input
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    try:
        # Send user input to the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use 'gpt-4' if available on your plan
            messages=[
                {"role": "user", "content": user_input}
            ],
            temperature=0.7
        )

        # Extract and print the response
        bot_reply = response['choices'][0]['message']['content']
        print(f"Bot: {bot_reply}")

    except Exception as e:
        print(f"An error occurred: {e}")
