from utils.utils import get_classification,return_class_number,get_class_dict




class OldBotStyleWrapper:
    def __init__(self,rasa_server_address,age_range) -> None:
        self.server_address = rasa_server_address
        self.age_range = age_range
    
    def predict(self,text):
        result= get_classification(transcript=text,server_address=self.server_address,
                                   age_range=self.age_range)
        class_number = return_class_number(result['final_intent'])
        return class_number,result['final_intent']
    
    def get_class_dict(self):
        return  get_class_dict()
    def get_class_number(self,text):
        return return_class_number(text)

if __name__ == '__main__':
    RASA_SERVER_ADDRESS = 'http://148.251.195.218:9097/model/parse'
    AGE_RANGE = (40,80)
    text = 'I am 45'
    old_bot_rasa = OldBotStyleWrapper(rasa_server_address=RASA_SERVER_ADDRESS,
                                      age_range=AGE_RANGE)
    ai_number = old_bot_rasa.predict('hello')
    print(ai_number)