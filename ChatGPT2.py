import openai
import pyttsx3
import speech_recognition as sr

# Set your OpenAI GPT-3.5 API key
api_key = "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"

# Function to interact with the GPT-3.5 model
def get_response(prompt):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can choose a different engine based on your plan.
        prompt=prompt,
        max_tokens=150  # Adjust the response length as needed.
    )
    return response.choices[0].text.strip()

# Function for text-to-speech
def speak(response):
    engine = pyttsx3.init()
    engine.say(response)
    engine.runAndWait()

# Main loop for interacting with the chatbot
def main():
    print("Hello! I'm your chatbot assistant. How can I help you today? (say 'exit' to quit)")

    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        try:
            user_input = recognizer.recognize_google(audio)
            print(f"User: {user_input}")
            if user_input.lower() == "exit":
                break

            # Add some context to the prompt if needed
            prompt = f"User: {user_input}\nChatbot: "
            response = get_response(prompt)
            print(response)

            # Speak the response using TTS
            speak(response)

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand your speech. Please try again.")
        except sr.RequestError as e:
            print(f"Error occurred while accessing Google Speech Recognition service: {e}")
            break
        except Exception as e:
            print(f"Error occurred: {e}")
            break

if __name__ == "__main__":
    main()
