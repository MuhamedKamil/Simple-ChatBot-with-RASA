from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

#--------------------------------------------------------------------------------------------------
# Note
# class Answer_fine is an action taken by ChatBot when the user ask how are you , how do you do ...
# action here is message 
#--------------------------------------------------------------------------------------------------
class Answer_fine(Action):
     def name(self) -> Text:
         return "Answer_fine"

     def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message("Iam fine and you?")

         return []

#----------------------------------------------------------------------------------------------------
# Note
# class Answer_nationality is an action taken by ChatBot when the user ask where are you from ... etc
# action here is message 
#----------------------------------------------------------------------------------------------------

class Answer_nationality(Action):
     def name(self) -> Text:
         return "Answer_nationality"

     def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message("Dear mohamed Iam chatbot , and you?")

         return []
