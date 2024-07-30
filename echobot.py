from http import client
from botbuilder.core import TurnContext
import logging
import requests
import json
import urllib
import webbrowser

class EchoBot:
        
    async def on_turn(self, turn_context: TurnContext):
        user_message = turn_context.activity.text.lower().strip()
        
        logging.info(f"Received message: {user_message}") #using logging because inputs got confused sometimes
        
        if "hello" in user_message:
            await turn_context.send_activity("Hello! How can I help you today?")
        elif " hi " in user_message:
            await turn_context.send_activity("Hello! How can I help you today?")
        elif "help" in user_message:
            await turn_context.send_activity("What do you need assistance with?")
        elif "api" in user_message:
            await turn_context.send_activity("Enter the URL like this: url: ")
            data = self.fetch()
        elif "url:" in user_message:
            await turn_context.send_activity("Opening URL...")
            url = user_message[4:]
            response = requests.get(url)
            webbrowser.open(url)
        elif "done" in user_message:
            await turn_context.send_activity("Goodbye!")            
            exit()
        else:
            await turn_context.send_activity("I didn't understand. Please try again. To exit, type DONE.")
      
    async def exit():
        await client.cancel_all_dialogs()
    


def fetch(self):
        try:
            url = str(input())
            response = requests.get(url)
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error("Try again.")
            return "Error."
        
#Setup logging        
logging.basicConfig(level=logging.INFO)
