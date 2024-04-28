# Tool Design to parse sbert response for Dr. Usama's bot
# set fit is added
## How to Use it
1. Please install requirementsz
2. python server.py to run server
3. python client.py for prediction
4. if you want to use some other age range just change AGE_RANGE limits

## Details of classes
classes_dict = {
    'affirmation' : 1, #positive
    'decline' : 2, #negative
    'weather':101,
    'language_barrier':9, #spanis
    'transfer_request':102,
    'calling_about': 103, #why
    'answering_machine': 3,
    'DNC' : 5,
    'say_again': 11,
    'can_you_email' : 105,
    'who_are_you' : 106, #who
    'already' : 107,
    'DNQ' : 108,
    'GreetBack' : 16,
    'sorry_greeting': 15,
    'BUSY': 4,
    'Not_Interested': 8,
    'are_you_bot': 14,
    'where_are_you_calling_from': 7,
    'not_decision_maker': 109,
    'greetings': 6,
    'scam':5, #return DNC
    'abusive': 5, #return DNC,
    'Afford': 12,
    'Insurance': 14,
    'rebuttal': 100,
    'None': 10,
}