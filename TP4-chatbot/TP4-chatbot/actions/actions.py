from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionOrderFood(Action):
    def name(self) -> Text:
        return "action_order_food"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Your logic to handle the order_food intent
        dispatcher.utter_message("Sure, I can help you with that!")
        
        return []

class ActionAskPrice(Action):
    def name(self) -> Text:
        return "action_ask_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Your logic to handle the ask_price intent
        dispatcher.utter_message("The price varies depending on the dish.")
        
        return []

class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Your logic to handle the greet intent
        dispatcher.utter_message("Hello!")
        
        return []

# Define other action classes similarly for other intents...

# Mapping of intents to action names
ACTION_MAPPING = {
    "order_food": ActionOrderFood,
    "ask_price": ActionAskPrice,
    "greet": ActionGreet,
    # Add mappings for other intents...
}
