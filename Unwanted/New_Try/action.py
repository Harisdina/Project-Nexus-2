from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random

class ActionProcessOrder(Action):
    def name(self):
        return "action_process_order"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        food_item = tracker.get_slot("food_item")
        menu = {
            "pizza": 10.99,
            "burger": 5.99,
            "pasta": 8.99,
            "sushi": 15.99,
        }

        if food_item in menu:
            cost = menu[food_item]
            dispatcher.utter_message(text=f"You ordered {food_item}. Your total cost is ${cost:.2f}. Please proceed to checkout.")
        else:
            dispatcher.utter_message(text=f"Sorry, we don't have {food_item} on the menu.")

        return []

class ActionUnknownIntent(Action):
    def name(self):
        return "action_unknown_intent"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        responses = ["I'm sorry, I didn't understand that.", "I didn't get that. Can you please rephrase?", "I'm not sure what you mean."]
        dispatcher.utter_message(text=random.choice(responses))
        return []
 