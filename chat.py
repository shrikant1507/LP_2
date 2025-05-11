from chatterbot import ChatBot
import tkinter as tk
from tkinter import scrolledtext

# Create the chatbot
hotel_bot = ChatBot(
    'HotelBot',
    logic_adapters=[{
        'import_path': 'chatterbot.logic.BestMatch',
        'default_response': 'Refer to our website for more details.',
        'maximum_similarity_threshold': 0.90
    }]
)

# Keyword-based manual responses
keyword_responses = {
    "check-in": "Check-in time is from 3:00 PM onwards. If you arrive earlier, we will do our best to accommodate you based on availability.",
    "check-out": "Check-out time is by 11:00 AM. Late check-out can be arranged upon request, subject to availability.",
    "swimming pool": "Yes, we have an outdoor swimming pool available for guests.",
    "fitness center": "Yes, we have a fully equipped fitness center that is open 24 hours for guests.",
    "restaurant": "Yes, our hotel has a multi-cuisine restaurant offering both local and international dishes.",
    "room service": "We offer 24/7 room service with a variety of food and beverage options.",
    "wi-fi": "Yes, we offer free Wi-Fi in all rooms and public areas.",
    "parking": "We offer free parking for guests during their stay.",
    "spa": "Yes, we have a luxurious spa offering a range of treatments to help you relax and rejuvenate.",
    "conference room": "We have a fully equipped conference room for meetings and events.",
    "gym": "Yes, our fitness center is available 24/7 for all guests.",
    "bar": "Yes, we have a bar that serves a wide range of alcoholic and non-alcoholic beverages.",
    "tour packages": "We offer various tour packages to explore the local attractions. Please ask at the front desk for more details.",
    "room cleaning": "Our housekeeping team provides daily cleaning services for all rooms.",
    "payment methods": "We accept major credit cards, debit cards, and cash payments for your convenience.",
    "wifi speed": "We provide high-speed Wi-Fi to ensure you stay connected during your stay.",
    "gift shop": "Yes, we have a gift shop offering a variety of souvenirs, snacks, and other items.",
    "address": "Our hotel is located at 123 Main Street, Cityville. You can find us easily on Google Maps.",
    "phone number": "You can reach us at +1-234-567-8900 for any inquiries or reservations.",
    "email": "You can email us at contact@sunsetgrandhotel.com for support, bookings, or general questions."
}

# Greetings
greetings = ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]
goodbyes = ["bye", "thank you", "goodbye", "thanks"]

# GUI setup
def send_message():
    user_input = user_entry.get().lower()
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + user_input + '\n')

    response = None

    # Check for goodbye phrases
    if any(goodbye in user_input for goodbye in goodbyes):
        response = "HotelBot: Thank you for using our service. Have a great day!"

    # Greet the user
    elif any(greet in user_input for greet in greetings):
        response = "Hello! How can I assist you today?"

    # Check for keyword responses
    else:
        for keyword in keyword_responses:
            if keyword in user_input:
                response = keyword_responses[keyword]
                break

        # If no keyword found, use chatbot
        if not response:
            bot_response = hotel_bot.get_response(user_input)
            # Check if the response is the default one
            if str(bot_response) == 'Refer to our website for more details.':
                response = "Refer to our website for more details."
            else:
                response = str(bot_response)

    chat_log.insert(tk.END, "Bot: " + response + '\n\n')
    chat_log.config(state=tk.DISABLED)
    user_entry.delete(0, tk.END)

# Main window
window = tk.Tk()
window.title("Sunset Grand Hotel - Chat Assistant")

chat_log = scrolledtext.ScrolledText(window, state=tk.DISABLED, width=70, height=20, wrap=tk.WORD, bg="#f0f0f0")
chat_log.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

user_entry = tk.Entry(window, width=60)
user_entry.grid(row=1, column=0, padx=10, pady=10)
user_entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(window, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

window.mainloop()
