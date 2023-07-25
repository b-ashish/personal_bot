# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
# pip install pandas
# pip install openpyxl

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction
import pandas as pd
import os
import datetime



dir = os.getcwd()
par_dir = os.path.dirname(dir)
path = os.path.join(dir,par_dir,'home_bot','user_info','Payment_details.xlsx')
print(path)

df = pd.read_excel(path)




class ActionProcess(Action):
    def name(self) -> Text:
        return "action_process_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            entity = tracker.latest_message['entities']
            date = entity[0]['value']
            date_format = "%d/%m/%Y"
            new_date = datetime.datetime.strptime(date,date_format).date()

            print("*"*50)
            print(new_date)
            print("*"*50)


            if os.path.exists(path):
                df = pd.read_excel(path)
                df['Date'] = pd.to_datetime(df['Date']).dt.date

                if df['Date'].isin([new_date]).any():
                    info = df[df['Date']== new_date]
                    comp = info['Component'].to_string()[2:]
                    items = info['Items'].to_string()[2:]
                    price = info['Price(Lacs)'].to_numpy()[0]*100000

                    result = f'''On date {date} following work is done: \n
                    Component : {comp} \n
                    Items : {items} \n
                    Money spent: {price} Rs'''

                    print(result)
                else:
                    result = "No data available for given date"
        
                dispatcher.utter_message(text=f"You selected: \n{result}")

            else:

                dispatcher.utter_message(text="No path found")
        except Exception as e:
            dispatcher.utter_message(text=e)

        return []
    
class ActionProcess(Action):
    def name(self) -> Text:
        return "action_process_component"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entity = next(tracker.get_latest_entity_values('structure'),None)

        if entity:
            comp = df[df['Component']==entity]
            table_data = [['Date','Items', 'Price']]

            if comp.shape[0]>1:
                for i in range(comp.shape[0]):
                    date = pd.to_datetime(comp['Date'].values[i]).date()
                    new_date = str(date.strftime('%Y-%m-%d'))
                    items = comp['Items'].values[i]
                    price = str(int(comp['Price(Lacs)'].values[i] * 100000))
                    table_data.append([new_date,items,price])

            else:
                date = pd.to_datetime(comp['Date'].values[0]).date()
                new_date = str(date.strftime('%Y-%m-%d'))
                items = "".join((comp['Items'].values))
                price = str(int(comp['Price(Lacs)'].values* 100000))
                table_data.append([new_date,items,price])

            print(type(price))
            table_string = "\n".join(["\t".join(row) for row in table_data])
            print(table_string)
        dispatcher.utter_message(text=f"```\n{table_string}\n```")
        return[]
    
# creating action for components
class ActionProcess(Action):
    def name(self) -> Text:
        return "action_process_unique_list"
        

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        unique_list = list(df['Component'].unique())
        buttons = []
        for value in unique_list:
            buttons.append({
            "title": value,
            "payload": f"/comp_info{{\"structure\": \"{value}\"}}"
            })
            
        # Create buttons
        dispatcher.utter_message(buttons = buttons, response="utter_comp")
        entity = next(tracker.get_latest_entity_values('structure'),None)
        if entity!=None:
            tracker.followup_action("action_process_component")
        return [SlotSet('structure',entity)] 



    
