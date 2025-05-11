from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

hotel_bot = ChatBot(
    'HotelBot',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. Could you please rephrase?',
            'maximum_similarity_threshold': 0.90
        }
    ]
)

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
    "air conditioning": "Yes, all rooms are equipped with air conditioning for your comfort.",
    "laundry service": "We offer laundry services, including same-day service for most items.",
    "luggage storage": "Yes, we provide luggage storage services if you need to store your belongings before or after check-in.",
    "pet policy": "Unfortunately, pets are not allowed in the hotel, except for service animals.",
    "family rooms": "Yes, we offer spacious family rooms for your convenience.",
    "accessibility": "Our hotel is wheelchair accessible, and we offer rooms designed to accommodate guests with disabilities.",
    "cancellation policy": "Our cancellation policy allows free cancellation up to 24 hours before check-in. After that, a cancellation fee may apply.",
    "room types": "We offer single rooms, double rooms, suites, and deluxe rooms, all designed for your comfort.",
    "reservations": "You can make a reservation online or by calling our front desk at any time.",
    "payment methods": "We accept major credit cards, debit cards, and cash payments for your convenience.",
    "early check-in": "Early check-in is subject to availability and may incur an additional charge.",
    "late check-out": "Late check-out is subject to availability and may incur an additional charge.",
    "non-smoking": "Our hotel is a non-smoking property. Designated smoking areas are available outside.",
    "gym": "Yes, our fitness center is available 24/7 for all guests.",
    "bar": "Yes, we have a bar that serves a wide range of alcoholic and non-alcoholic beverages.",
    "activities": "We offer various activities including guided tours, yoga sessions, and cooking classes.",
    "tour packages": "We offer various tour packages to explore the local attractions. Please ask at the front desk for more details.",
    "special offers": "We often have special offers and discounts. Please check our website or contact us for more information.",
    "meeting facilities": "We provide meeting and event facilities with all the necessary equipment. Please inquire about availability.",
    "business center": "We have a fully equipped business center with computers, printing, and fax services.",
    "wifi speed": "We provide high-speed Wi-Fi to ensure you stay connected during your stay.",
    "gift shop": "Yes, we have a gift shop offering a variety of souvenirs, snacks, and other items.",
    "wake-up call": "Yes, we can schedule a wake-up call for you at your preferred time.",
    "room cleaning": "Our housekeeping team provides daily cleaning services for all rooms.",
    "childcare": "We offer childcare services upon request. Please contact the front desk for more details.",
    "business hours": "Our front desk is open 24/7 for your convenience.",
    "airport shuttle": "Yes, we offer airport shuttle services for our guests. Please contact the front desk for scheduling.",
    "taxi service": "Taxi service is available on request. Please ask our staff to arrange a taxi for you.",
    "gym hours": "Our fitness center is open 24 hours for all guests.",
    "reception": "Our reception desk is available 24/7 to assist you with any requests.",
    "food options": "We offer a variety of food options, including breakfast, lunch, and dinner at our restaurant and through room service.",
    "event planning": "We offer event planning services to help you organize your meetings, weddings, or special events.",
    "valet service": "Yes, we offer valet service for parking your vehicle.",
    "hotel amenities": "Our hotel offers amenities such as free Wi-Fi, a swimming pool, a fitness center, a restaurant, and a spa.",
    "phone chargers": "We have phone chargers available at the front desk if you need one.",
    "complimentary breakfast": "Yes, we offer complimentary breakfast for all guests.",
    "airport": "We are located approximately 20 minutes from the nearest airport. Transportation options are available.",
    "city tours": "We offer guided city tours to explore local attractions. Please ask at the front desk for more information.",
    "booking confirmation": "You will receive a booking confirmation via email after making your reservation."
}

def get_response(user_input, last_response):
    user_input = user_input.lower()
    
    if "tell me more about it" in user_input and last_response:
        return f"You're asking about {last_response}. Here's more information: {keyword_responses.get(last_response, 'Sorry, no further details available.')}", last_response
    
    for keyword, response in keyword_responses.items():
        if keyword in user_input:
            return response, keyword
    
    return "Please contact our hotel or for more information, visit our website.", None

trainer = ListTrainer(hotel_bot)
trainer.train([
    "Hi",
    "Hello! Welcome to our hotel. How can I assist you today?",
])

def chat_with_hotel_bot():
    print("Welcome to HotelBot! How can I assist you today?")
    last_response = None
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("HotelBot: Thank you for using our service. Have a great day!")
                break
            response, last_response = get_response(user_input, last_response)
            print(f"HotelBot: {response}")
        except (KeyboardInterrupt, EOFError, SystemExit):
            break

if __name__ == "__main__":
    chat_with_hotel_bot()
