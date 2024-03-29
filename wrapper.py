from utils.utils import get_classification,return_class_number

RASA_SERVER_ADDRESS = 'http://113.203.209.145:9097/model/parse'
AGE_RANGE = (40,80)
text = 'I am 45'


class OldBotStyleWrapper:
    def __init__(self,rasa_server_address,age_range) -> None:
        self.server_address = rasa_server_address
        self.age_range = age_range
    
    def predict(self,text):
        result= get_classification(transcript=text,server_address=self.server_address,
                                   age_range=self.age_range)
        class_number = return_class_number(result['final_intent'])
        return class_number


if __name__ == '__main__':
    old_bot_rasa = OldBotStyleWrapper(rasa_server_address=RASA_SERVER_ADDRESS,
                                      age_range=AGE_RANGE)
    ai_number = old_bot_rasa.predict('hello')
    print(ai_number)