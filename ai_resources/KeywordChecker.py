from ai_resources.base_keywords import *
from ai_resources.one_word_keywords import double_metaphone_classes
from nltk.chat.util import Chat

class KeywordModal:
    def __init__(self,config={'is_fuzzy_match':False}) -> None:
        self.is_fuzzy_match = config.get('is_fuzzy_match',False)
        if self.is_fuzzy_match:
            from fuzzy import DMetaphone
            self.metaphone = DMetaphone()
        self.pairs = [
                # Decline Patterns
                [
                    r".*\b(no|not|never|refuse|reject|decline|negative|nope|incorrect|wrong|can't|cannot|don't|doesn't|never)\b.*",
                    ['decline']
                ],
                # Affirmation Patterns
                [
                    r".*\b(yes|yeah|yep|sure|correct|absolutely|agree|right|indeed|true|affirmative|of course|definitely|probably|maybe|just|jaw|hum)\b.*",
                    ['affirmation']
                ],
            ]
        self.ai_nltk_bot = Chat(self.pairs)
        self.all_keyword_classes = [
            (weather,'weather'),
            (language_barrier,'language_barrier'),
            (transfer_request,'transfer_request'), 
            (calling_about,'calling_about'),
            (answering_machine, "answering_machine"),
            (do_not_call_keywords, "DNC"),
            (say_again,'say_again'),
            (email, "can_you_email"),
            (who_keywords, "who_are_you"),
            (already_keywords, "already"),
            (dnq_keywords, "DNQ"),
            (greet_back,"GreetBack"),
            (sad_greeting_keywords, "sorry_greeting"),
            (busy_keywords, "BUSY"),
            (not_interested_keywords, "Not_Interested"),
            (bot_check_keywords, "are_you_bot"),
            (location_keywords, "where_are_you_calling_from"),
            (not_decision_maker,'not_decision_maker'),
            (greetings_keywords, "greetings"),
        ]
        

    def predict(self,input_string, keyword_classes=None):

        # print('------ Lets Simple thing going first ------'.center(50))
        if not keyword_classes:
            keyword_classes = self.all_keyword_classes
        # Initialize the metaphone object
        # Convert the input string to lower case for case insensitive matching
        input_string = input_string.lower()

        # if 'both' in input_string:
        #     return 'affirmation'
        flag = None
        # if 'no' in input_string:
        if 'no' in input_string.lower().split(" "):
             if any(keyword in input_string for keyword in affirm_keywords):
                 return 'affirmation'
        # print(input_string)
        # Check for exact matches first
        for keywords, class_name in self.all_keyword_classes:
            if any(keyword in input_string for keyword in keywords):
                return class_name
        predicted_class = self.ai_nltk_bot.respond(input_string)
        return predicted_class
        if self.is_fuzzy_match:
            return self.fuzzy_match(input_string,double_metaphone_classes = double_metaphone_classes)
        if flag == None:
            return None
    
    def fuzzy_match(self,input_string,double_metaphone_classes):
        input_words = input_string.split()
        input_metaphones = [self.metaphone(word) for word in input_words]
        linear_list = []
        for pair in input_metaphones:
            for item in pair:
                # Check if the item is not None
                if item is not None:
                    # Decode the byte string to a normal string and add to the linear list
                    linear_list.append(item.decode('utf-8'))
        linear_list = sorted(linear_list)
        # print(linear_list)
        for i in double_metaphone_classes:
            for keyword in double_metaphone_classes[i]:
                if len(keyword) > 1:
                    for value in linear_list:
                        score = fuzz.token_set_ratio(keyword,value)
                        # print(score)
                        if score >= 90:
                            return i
        return None

