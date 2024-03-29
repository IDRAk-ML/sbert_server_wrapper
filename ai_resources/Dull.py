import pandas as pd
import nltk
import re

class Dull:
    def __init__(self,base_path='./',kw_pth='keywords.csv') -> None:
        # self.df = pd.read_csv(base_path+kw_pth)
        # self.df.columns = ['example','intent']
        # self.keywords = self.df.groupby('intent')['example'].apply(list).to_dict()
        pass
    
    def predict(self,text):
        # text = text.lower()
        # try:
        #     for keyword in self.keywords['scam']:
        #         if re.search(r'\b' + re.escape(keyword) + r'\b', text):
        #             return 'scam'
        # except:
        #     pass

        # for keyword in self.keywords['sorry_greeting']:
        #     if re.search(r'\b' + re.escape(keyword) + r'\b', text):
        #         return 'sorry_greeting'
            
        # for keyword in self.keywords['abusive']:
        #     if re.search(r'\b' + re.escape(keyword) + r'\b', text):
        #         return 'abusive'
        # # DNC
        # for keyword in self.keywords['DNC']:
        #     if re.search(r'\b' + re.escape(keyword) + r'\b', text):
        #         return 'DNC'

        # # calling_about   
        # for keyword in self.keywords['calling_about']:
        #     if re.search(r'\b' + re.escape(keyword) + r'\b', text):
        #         return 'calling_about'
            
        # for keyword in self.keywords['complain_calls']:
        #     if re.search(r'\b' + re.escape(keyword) + r'\b', text):
        #         return 'complain_calls'
            
        # for keyword in self.keywords['DNQ']:
        #     if re.search(r'\b' + re.escape(keyword) + r'\b', text):
        #         return 'DNQ'
        # # not_decision_maker
        # for keyword in self.keywords['not_decision_maker']:
        #     if re.search(r'\b' + re.escape(keyword) + r'\b', text):
        #         return 'not_decision_maker'

        # for keyword in self.keywords['Not_Interested']:
        #     if re.search(r'\b' + re.escape(keyword) + r'\b', text):
        #         return 'Not_Interested'

        # for keyword in self.keywords['BUSY']:
        #     if re.search(r'\b' + re.escape(keyword) + r'\b', text):
        #         return 'BUSY'
            
            
        # for keyword in self.keywords['say_again']:
        #     if re.search(r'\b' + re.escape(keyword) + r'\b', text):
        #         return 'say_again'
            
        # for keyword in self.keywords['transfer_request']:
        #     if re.search(r'\b' + re.escape(keyword) + r'\b', text):
        #         return 'transfer_request'
            
        # for keyword in self.keywords['decline']:
        #     if re.search(r'\b' + re.escape(keyword) + r'\b', text):
        #         return 'decline'

        # for keyword in self.keywords['answering_machine']:
        #     if re.search(r'\b' + re.escape(keyword) + r'\b', text):
        #         return 'answering_machine'
            
        # for keyword in self.keywords['already']:
        #     if re.search(r'\b' + re.escape(keyword) + r'\b', text):
        #         return 'already'
            
        # for keyword in self.keywords['affirmation']:
        #     if re.search(r'\b' + re.escape(keyword) + r'\b', text):
        #         return 'affirmation'
            
        # for keyword in self.keywords['interested']:
        #     if re.search(r'\b' + re.escape(keyword) + r'\b', text):
        #         return 'interested'
            
        # for keyword in self.keywords['who_are_you']:
        #     if re.search(r'\b' + re.escape(keyword) + r'\b', text):
        #         return 'who_are_you'
        
        # for keyword in self.keywords['who_are_you']:
        #     if re.search(r'\b' + re.escape(keyword) + r'\b', text):
        #         return 'who_are_you'
            
        # for keyword in self.keywords['GreetBack']:
        #     if re.search(r'\b' + re.escape(keyword) + r'\b', text):
        #         return 'GreetBack'
            
        # return None
        return None
    
if __name__ == "__main__":
    dull_ai = Dull(kw_pth='files/erc/keywords.csv')
    result = dull_ai.predict('This seems suspicious.')
    print(result)
