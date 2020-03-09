# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"


from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction


class InfoAboutServiceCentersForm(FormAction):

    addresses = [("თბილისი", "ყაზბეგის გამზ. 24გ", "სოლო", "09:00-20:00"),
                 ("თბილისი", "ჩიტაძის ქ. 11", "სოლო", "09:00-20:00"),
                 ("თბილისი", "ნუცუბიძის ქუჩა N221 კორპ. 4", "ექსპრესი", "09:00-20:00"),
                 ("ბათუმი", "რუსთაველის ქ. 22", "სოლო", "09:00-20:00"),
                 ("ბათუმი", "ჭავჭავაძის 76", "საცალო", "09:00-20:00"),
                 ("ქუთაისი", "წმინდა ნინოს ქ.#17", "საცალო", "09:00-20:00")]

    def name(self) -> Text:
        return 'info_about_service_centers_form'

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        return ["city", "direction"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "city": self.from_entity(entity="city"),
            "direction": self.from_entity(entity="direction"),
        }

    def validate_city(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        print("validating city")
        return {"city": value}

    def validate_direction(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        print("validating direction")

        return {"direction": value}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict]:
        city = tracker.get_slot("city")
        direction = tracker.get_slot("direction")

        result = list(filter(lambda x: x[0] == city and x[2] == direction, self.addresses))

        if not result:
            dispatcher.utter_message(template="utter_service_centers_not_found")
        else:
            dispatcher.utter_message(text=", ".join(result[0]))

        return [SlotSet("city", None), SlotSet("direction", None)]

class InfoAboutLoansForm(FormAction):



    def name(self) -> Text:
        return 'info_about_loans_form'

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        return ["loan_type", "initial_amount"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "loan_type": self.from_entity(entity="loan_type"),
            "initial_amount": self.from_entity(entity="initial_amount"),
        }

    def validate_loan_type(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        print("validating loan_type")
        return {"loan_type": value}

    def validate_initial_amount(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        print("initial_amount")

        return {"initial_amount": value}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict]:
        dispatcher.utter_message(template="utter_your_info_is_sent_to_call_center")
        dispatcher.utter_message(template="utter_anything_else")

        return [SlotSet("loan_type", None), SlotSet("initial_amount", None)]