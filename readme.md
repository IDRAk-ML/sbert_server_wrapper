# Tool Design to parse sbert response for Dr. Usama's bot
# set fit is added
## How to Use it
1. Please install requirementsz
2. python server.py to run server
3. python client.py for prediction
4. if you want to use some other age range just change AGE_RANGE limits

## Details of classes
classes_dict = {
    'affirmation' : 1, # positive 
    'decline' : 2, # negative
    'weather':101, # weather queries
    'language_barrier':9,
    'transfer_request':102, #ask to transfer me to superviouser
    'calling_about': 103, # asking about reson
    'answering_machine': 3,
    'DNC' : 5, #
    'say_again': 11, #user ask to repeat
    'can_you_email' : 105, 
    'who_are_you' : 106,
    'already' : 107,
    'DNQ' : 108,
    'GreetBack' : 16,
    'sorry_greeting': 15,
    'BUSY': 4, #
    'Not_Interested': 8,
    'are_you_bot': 14,
    'where_are_you_calling_from': 7, #location
    'not_decision_maker': 109,
    'greetings': 6,
    'scam':5, #return DNC
    'abusive': 5, #return DNC,
    'Afford': 12,
    'Insurance': 14,
    'rebuttal': 100,
    'None': 10,
    'complain_calls':5, # return DNC; customer complaining about calls,
    'hold_a_sec':4, # like busy
    'interested':1, #some sort of affirm
    'other':10,
    'transfer_request': 111,
    'where_get_number':112, #asking where did you get his info
}
