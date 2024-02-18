import speech_recognition as sr
import pyttsx3

# Sample food menu (you can replace this with a real menu)
menu = {
    "burger": 5.99,
    "pizza": 7.99,
    "pasta": 6.99,
    "sushi": 10.99,
    "salad": 4.99,
    "exit": 0  # To exit the ordering process
}

def recognize_speech():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your speech.")
        return None

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def order_food():
    speak("Welcome to our food ordering system! Here's our menu:")
    
    while True:
        for item, price in menu.items():
            speak(f"We have {item} for ${price:.2f}.")
        
        speak("What would you like to order? You can say 'exit' to finish ordering.")
        
        user_input = recognize_speech()
        if not user_input:
            continue
        
        user_input = user_input.lower()
        
        if user_input in menu:
            if user_input == "exit":
                speak("Thank you for your order. Your total is $%.2f. Enjoy your meal!" % total)
                break
            
            item_price = menu[user_input]
            total = 0
            total += item_price
            speak(f"You've ordered {user_input}. That will be ${item_price:.2f}. Your total is ${total:.2f}.")
        else:
            speak("I'm sorry, we don't have that item on the menu.")

if __name__ == "__main__":
    
    order_food()
