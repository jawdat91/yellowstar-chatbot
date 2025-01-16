from flask import Flask, request
from db import Database
from email_service import EmailService
from intent_analyzer import IntentAnalyzer
from telegram_bot import TelegramBot
from config import TELEGRAM_BOT_TOKEN
from datetime import datetime
from Vacation_handler import Vacation_handler
from SickReport_handler import SickReport_handler


app = Flask(__name__)

confirmation_states = {}
vacation_states = {}

# Webhook endpoint for Telegram bot
@app.route(f"/{TELEGRAM_BOT_TOKEN}", methods=['POST'])
def telegram_webhook():
    data = request.get_json()
    print(f"Received data: {data}")  # Debugging statement

    if "message" in data:
        chat_id = data['message']['chat']['id']
        user_input = data['message']['text'].strip().lower()  # Converted to lowercase for easier comparison

        print(f"Chat ID: {chat_id}")  # Debugging statement

        # Check if user is in confirmation state
        if chat_id in confirmation_states and confirmation_states[chat_id]:
            if user_input == "ja":
                # User confirmed the sick report
                user_id = confirmation_states[chat_id]  # Get the stored user_id
                user = Database.get_user_by_telegram_id(chat_id)  # Retrieve user info again
                if user:
                    user_id, user_name = user  

                    # Check if the user has already reported sick
                    if SickReport_handler.has_already_reported_sick(user_id):
                        TelegramBot.send_message(chat_id, "Je hebt je vandaag al ziekgemeld.")
                        print(f"User {user_id} heeft zich al ziekgemeld voor vandaag.")  # Debugging statement
                    else:
                        # Ziekmelding opslaan
                        SickReport_handler.save_sick_report(user_id)  # Save the sick report
                        print(f"Ziekmelding geregistreerd voor gebruiker {user_id}.")  # Debugging statement
                        
                        # Save sick report.
                        TelegramBot.send_message(chat_id, "Je ziekmelding is succesvol ingediend.")
                        
                        # Send an email to HR and the project manager
                        EmailService.send_email_via_smtp(
                            user_id,
                            username= user_name
                        )
                        print(f"E-mail verzonden naar HR voor gebruiker {user_id}.")  # Debugging statement


            elif user_input == "nee":
                    TelegramBot.send_message(chat_id, "Ziekmelding is geannuleerd.")
            else:
                TelegramBot.send_message(chat_id, "Ongeldige invoer. Antwoord alstublieft met 'ja' of 'nee'.")

            
            # Clear the confirmation state after the response
            confirmation_states.pop(chat_id, None)
            return "ok", 200
        
        # Check if user is in vacation request process
        elif chat_id in vacation_states:
            state_data = vacation_states[chat_id]
            print(f"Current state data: {state_data}")  # Debugging statement
            
            print(f"Chat ID: {chat_id}")  # Debugging statement

            if state_data['step'] == 'start_date':
                try:
                    user_input = user_input.strip()  # Vedrwijder spaties
                    print(f"User input for start date: '{user_input}'")  # Debugging statement
                    start_date = datetime.strptime(user_input, "%d/%m/%Y").date()

                    print(f"start date variable = '{start_date}':. User input: '{user_input}'")
                    
                    # Check if the start date is in the past
                    if start_date < datetime.now().date():
                        TelegramBot.send_message(chat_id, "De startdatum kan niet in het verleden liggen. Voer opnieuw een geldige startdatum in (DD/MM/YYYY).")
                    elif Vacation_handler.has_overlapping_vacation(state_data['user_id'], start_date, start_date):  # Check of startdatum overlapt
                        TelegramBot.send_message(chat_id, "De startdatum valt binnen een bestaande vakantie. Voer een andere startdatum in (DD/MM/YYYY).")
                    else:
                        # # Save the start date
                        state_data['start_date'] = start_date
                        state_data['step'] = 'end_date'  # Ga naar volgende stap
                        TelegramBot.send_message(chat_id, "Wat is de laatste datum van je vakantie tot en met? Voer de datum in DD/MM/YYYY.")
                except ValueError as e:
                    print(f"ValueError: {e}, User input: '{user_input}'")  # Debugging statement
                    TelegramBot.send_message(chat_id, "Ongeldige datum. Voer de datum in het formaat DD/MM/YYYY.")

            elif state_data['step'] == 'end_date':
                try:
                    end_date = datetime.strptime(user_input, "%d/%m/%Y").date()
                    start_date = state_data.get('start_date')

                    if not start_date:
                        TelegramBot.send_message(chat_id, "Er is geen geldige startdatum gevonden. Begin opnieuw met je vakantieaanvraag.")
                    elif end_date < start_date:
                        TelegramBot.send_message(chat_id, "De einddatum kan niet vóór de startdatum liggen. Voer een geldige einddatum in.")
                    elif Vacation_handler.has_overlapping_vacation(state_data['user_id'], start_date, end_date):  # Check if the end date overlaps
                        TelegramBot.send_message(chat_id, "De einddatum valt binnen een bestaande vakantie. Voer een andere einddatum in (DD/MM/YYYY).")
                    else:
                        state_data['end_date'] = end_date
                        state_data['step'] = 'confirmation'
                        TelegramBot.send_message(chat_id, f"Bevestig je vakantie van {start_date} tot {end_date}. Antwoord met 'ja' of 'nee'.")
                except ValueError:
                    TelegramBot.send_message(chat_id, "Ongeldige datum. Voer de datum in het formaat DD/MM/YYYY.")

            elif state_data['step'] == 'confirmation':
                if user_input == 'ja':
                    user_id = state_data['user_id']
                    start_date = state_data['start_date']
                    end_date = state_data['end_date']
                    Vacation_handler.save_vacation_request(user_id, start_date, end_date, "Vakantie")
                    TelegramBot.send_message(chat_id, "Je vakantieaanvraag is succesvol geregistreerd.")
                elif user_input == 'nee':
                    TelegramBot.send_message(chat_id, "Je vakantieaanvraag is geannuleerd.")
                else:
                    TelegramBot.send_message(chat_id, "Ongeldige invoer. Antwoord met 'ja' of 'nee'.")
                vacation_states.pop(chat_id, None)
            return "ok", 200

        # Get user by Telegram ID (returns both user_id and user_name)
        user = Database.get_user_by_telegram_id(chat_id)

        # Analyze the user's input for intent
        intent = IntentAnalyzer.analyze_intent(user_input)

        if intent == "greeting":
            TelegramBot.send_message(chat_id, "Hi, Hoe kan ik je vandaag helpen?")

        elif intent == "sick":
            if user:
                user_id, user_name = user  # Unpack the returned user tuple
                if SickReport_handler.has_already_reported_sick(user_id):
                    TelegramBot.send_message(chat_id, "Je hebt je vandaag al ziekgemeld.")
                else:
                    # Ask for confirmation
                    confirmation_states[chat_id] = user_id  # Store user_id and set confirmation state
                    TelegramBot.send_message(chat_id, f"Wil je je ziekmelden ({user_name})? Antwoord met 'ja' of 'nee'.")
            else:
                TelegramBot.send_message(chat_id, "Je bent niet geregistreerd. Neem contact op met de administratie.")

        
        elif intent == "vacation":
            if user:
                user_id, user_name = user
                vacation_states[chat_id] = {'user_id': user_id, 'step': 'start_date'}
                TelegramBot.send_message(chat_id, "Voer de datum van het begin van je vakantie in (DD/MM/YYYY).")
            else:
                TelegramBot.send_message(chat_id, "Je bent niet geregistreerd. Neem contact op met de administratie.")

        elif intent == "vacation_overview":
            if user:
                user_id, user_name = user
                overview_message = Vacation_handler.get_vacation_overview(user_id)
                print(overview_message)

                        
                TelegramBot.send_message(chat_id, overview_message)
            else:
                TelegramBot.send_message(chat_id, "Je bent niet geregistreerd. Neem contact op met de administratie.")
        else:
            TelegramBot.send_message(chat_id, "Het spijt me, ik begrijp het niet. Kun je het op een andere manier vragen?")
            
    return "ok", 200

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5000)
