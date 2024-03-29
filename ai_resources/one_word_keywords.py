answering_machine_keywords = ["message", "beep", "voicemail", "unavailable", "leave", "record","tone"]

do_not_call_keywords = ["remove", "unsubscribe", "stop", "off","list","cease","fuck", "calls",'shit','sex',
                        'dirty','fucker','fucking','bullshit','suck','ass','bitch',
                        'shut','asshole','dumbass','kill','piss','dickweed','cunt',
                        'bastard', 'damn','bollocks','bugger','cocknose','bloody','rubbish',
                        'shag','jizzcock','cum','cock','penis','buster','bastard','mad','fuck',"dick"]

who_keywords = ["who", "name", "identity", "caller", "who","name","person"]

bot_check_keywords = ["bot", "real", "human", "robot", "automated"]

already_keywords = ["already", "using", "subscribed", "member","having","existing","previosuly"]

dnq_keywords = ["qualify", "ineligible", "applicable", "can't use","unqualify"]

sad_greeting_keywords = ["sick", "unwell", "sad", "bad", "tough","ill","fever","hospital"]

busy_keywords = ["busy", "later", "meeting", "occupied", "engaged","sleeping","busy", "later", "meeting", "occupied", "engaged"]

not_interested_keywords = ["uninterested", "interest", "nope", "decline","refuse"]

decline_keywords = ["no", "refuse", "reject", "decline", "negative","nah"]

affirm_keywords = ["yes", "sure", "okay", "definitely", "agree","yeah","yup"]

greetings_keywords = ["hello", "hi", "morning", "evening", "greetings","good", "fine", "well", "thanks", "okay","how"]

location_keywords = ["location", "where", "address", "office", "headquarters","city","country","pakistani","indian"]


# Your lists of keywords, each list representing a class
keywords_dict = {
    "answering_machine": answering_machine_keywords,
    "DNC": do_not_call_keywords,
    "who_are_you": who_keywords,
    "are_you_bot": bot_check_keywords,
    "already": already_keywords,
    "DNQ": dnq_keywords,
    "sorry_greeting": sad_greeting_keywords,
    "BUSY": busy_keywords,
    "Not_Interested": not_interested_keywords,
    "decline": decline_keywords,
    "affirmation": affirm_keywords,
    "greetings": greetings_keywords,
    "where_are_you_calling_from": location_keywords
    #language_barrier
    #GreetBack
}

# A dictionary to hold the classes and their keywords' Double Metaphone codes
double_metaphone_classes = {}

try:
    import fuzzy

    # Using Double Metaphone
    doublemetaphone = fuzzy.DMetaphone()

    # Iterate over each class and its keywords
    for class_name, keywords in keywords_dict.items():
        # Store the Double Metaphone values for each keyword in the class
        temp = [doublemetaphone(keyword) for keyword in keywords]
        linear_list = []
        for pair in temp:
            for item in pair:
                # Check if the item is not None
                if item is not None:
                    # Decode the byte string to a normal string and add to the linear list
                    linear_list.append(item.decode('utf-8'))
        double_metaphone_classes[class_name] = sorted(linear_list)
except Exception as e:
    print(f'Error in fuzz {e}')

# print(double_metaphone_classes)