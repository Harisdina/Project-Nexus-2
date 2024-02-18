import speech_recognition as sr
import pyttsx3


recognizer = sr.Recognizer()


engine = pyttsx3.init()


menu = {
    "pizza": 10.99,
    "burger": 5.99,
    "pasta": 8.99,
    "sushi": 15.99,
}

def listen_for_command():
    with sr.Microphone() as source:
        speak("Listening for your order...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        speak("You said: " + command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand that.")
        return None

def process_order(order):
    order_items = order.split()
    total_cost = 0

    for item in order_items:
        if item in menu:
            total_cost += menu[item]
        else:
            speak(f"Sorry, we don't have {item} on the menu.")

    if total_cost > 0:
        speak(f"Your total cost is ${total_cost:.2f}. Please proceed to checkout.")

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Welcome to the food ordering chatbot. What would you like to order?")
    for item, price in menu.items():
            speak(f"We have {item} for ${price:.2f}.")
    
    while True:
        command = listen_for_command()

        if command is not None:
            if "order" in command:
                speak("Sure, please tell me what you'd like to order.")
                order = listen_for_command()
                if order:
                    process_order(order)
            elif "menu" in command:
                speak("Sure here is the menu...")
                for item, price in menu.items():
                    speak(f"We have {item} for ${price:.2f}.")
            elif "exit" in command:
                speak("Thank you for using our food ordering chatbot. Goodbye!")
                break
            else:
                speak("I'm sorry, I didn't understand that. You can say 'order' to start an order or 'exit' to exit.")
