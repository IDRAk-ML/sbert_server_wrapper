from setfit import SetFitModel
class SBertClassifier:
    def __init__(self,model_path='m-aliabbas1/medicare_idrak') -> None:
        self.model = SetFitModel.from_pretrained(model_path)
        self.classes_dict = {
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
    def label_to_num(self,class_name):
        return str(self.classes_dict.get(class_name,'None'))
    
    
    def predict(self,text='',return_enum=False):
        result = self.infer(text=text)
        if return_enum:
            result = self.label_to_num(class_name=result)
        return result

    def infer(self,text):
        try:
            y_hat = self.model([str(text)])
            return str(y_hat[0])
        except:
            return 'None'
        
if __name__ == '__main__':
    model = SBertClassifier()
    print(model.predict('Hello World!',return_enum=True))