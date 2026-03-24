# list
# a=[1,2,3,4,5]
# print(type(a))
# print(a)
# a=[1,2,"hey",a]
# print(len(a))
# print(a[0])
# a=[1,2,"hello",1,3,4,6,8]
# print(len(a))
# print(a[1:5])
# print(a[:5])
# print(a[1:])
# print(a[:])
# user_info = {
#     "name": "Bigyan",
#     "phone": [
#         {"type": "ntc", "number": 9862970819},
#         {"type": "ncell", "number": 9701783360}
#     ]
# }

# name = "Bigyan"
# type1 = "ntc"
# num1 = 9862970819
# type2 = "ncell"
# num2 = 9701783360

# print("My name is", name, "and my", type1, "number is", num1, "and", type2, "number is", num2)


# user_info={
#     "name":"Bigyan Mahatara",
#     "age": 25,
#     "addres":"Sankhamul-31,kathmandu, Nepal",
#     "email":"sciencecrazy762@gmail.com",
#     "phone":[
#         {"type":"ntc","number":9862970819},
#         {"type":"ncell","number":9701783360}
#     ]
# }
# name="Bigyan Mahatara"
# age=25
# address="sankhamul-31,kathmandu, Nepal"
# email="sciencecrazy762@gmail.com"
# type1="ntc"
# num1=962970819
# type2="ncell"
# num2=970178360
# print("My name is", name, "and my age is", age, "I live in", address, "my email address is" ,email,  "and my",type1,  "number is", num1, "and", type2, "number is", num2)
# print("My name is", name, "and my age is", age, "I live in", address, "my email address is", email, "and my", type1, "number is", num1, "and", type2, "number is", num2)
 
# phonebook = {
#      "Bigyan": {
#          "phone":9862970819,
#          "email":"bigyan@gmail.com",
#          "city":"Kathmandu"
#      },
#      "Dhurba":{
#          "phone":9806626148,
#          "email":"dhurba@gmail.com",
#          "city":"Lalitpur"
#      },
#      "Bidhya":{
#          "phone":976871992,
#          "email":"bidhya@gmail.com",
#          "city":"Bhaktapur"
#      }
#  }

# print(phonebook["Bigyan"]["phone"])
# print(phonebook["Dhurba"]["phone"])
# print(phonebook["Bidhya"]["phone"])
# print(f"Bigyan phone: {phonebook['Bigyan']['phone']}")
# print(f"Dhurba phone: {phonebook['Dhurba']['phone']}")
# print(f"Bidhya phone: {phonebook['Bidhya']['phone']}")

"""
AI Voice Assistant using Python
Requirements:
    pip install anthropic SpeechRecognition pyttsx3 pyaudio

On Linux, also run:
    sudo apt-get install portaudio19-dev python3-pyaudio espeak

On Mac:
    brew install portaudio
"""

import anthropic
import speech_recognition as sr
import pyttsx3
import sys

# ──────────────────────────────────────────────
# Configuration
# ──────────────────────────────────────────────
ANTHROPIC_API_KEY = "your-api-key-here"   # ← Replace with your key
MODEL = "claude-sonnet-4-20250514"
SYSTEM_PROMPT = (
    "You are a helpful, concise voice assistant. "
    "Keep responses short and conversational (1-3 sentences max) "
    "since they will be spoken aloud. Be friendly and direct."
)

# ──────────────────────────────────────────────
# Text-to-Speech Engine Setup
# ──────────────────────────────────────────────
def init_tts():
    engine = pyttsx3.init()
    engine.setProperty("rate", 165)       # Speed (words per minute)
    engine.setProperty("volume", 1.0)     # Volume 0.0 – 1.0

    # Pick a nicer voice if available
    voices = engine.getProperty("voices")
    for voice in voices:
        if "english" in voice.name.lower() or "zira" in voice.name.lower():
            engine.setProperty("voice", voice.id)
            break
    return engine


def speak(engine, text: str):
    print(f"\n🤖 Assistant: {text}\n")
    engine.say(text)
    engine.runAndWait()


# ──────────────────────────────────────────────
# Speech-to-Text
# ──────────────────────────────────────────────
def listen(recognizer: sr.Recognizer, mic: sr.Microphone) -> str | None:
    print("🎙️  Listening... (speak now)")
    try:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=6, phrase_time_limit=15)

        print("⟳  Recognising...")
        text = recognizer.recognize_google(audio)
        print(f"👤 You: {text}")
        return text

    except sr.WaitTimeoutError:
        print("⏱  No speech detected.")
        return None
    except sr.UnknownValueError:
        print("❓ Could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"❌ Speech recognition error: {e}")
        return None


# ──────────────────────────────────────────────
# Claude API Call
# ──────────────────────────────────────────────
def ask_claude(client: anthropic.Anthropic, history: list, user_text: str) -> str:
    history.append({"role": "user", "content": user_text})

    response = client.messages.create(
        model=MODEL,
        max_tokens=300,
        system=SYSTEM_PROMPT,
        messages=history,
    )

    reply = response.content[0].text
    history.append({"role": "assistant", "content": reply})
    return reply


# ──────────────────────────────────────────────
# Main Loop
# ──────────────────────────────────────────────
def main():
    print("=" * 50)
    print("  🎙️  AI Voice Assistant  (Python + Claude)")
    print("=" * 50)
    print("  Say 'quit' or 'exit' to stop.\n")

    # Initialise components
    client   = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    tts      = init_tts()
    recognizer = sr.Recognizer()
    mic      = sr.Microphone()
    history: list = []

    speak(tts, "Hello! I'm your AI assistant. How can I help you today?")

    while True:
        user_input = listen(recognizer, mic)

        if user_input is None:
            continue

        # Exit commands
        if user_input.strip().lower() in {"quit", "exit", "stop", "bye", "goodbye"}:
            speak(tts, "Goodbye! Have a great day!")
            break

        # Get AI response
        print("⟳  Thinking...")
        try:
            reply = ask_claude(client, history, user_input)
            speak(tts, reply)
        except anthropic.APIError as e:
            print(f"❌ API Error: {e}")
            speak(tts, "Sorry, I ran into an error. Please try again.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Interrupted. Goodbye!")