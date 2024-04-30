from setfit import SetFitModel
class SBertClassifier:
    def __init__(self,model_path='m-aliabbas1/medicare_idrak') -> None:
        self.model = SetFitModel.from_pretrained(model_path)
        
    def label_to_num(self,class_name):
        return str(self.classes_dict.get(class_name,'None'))
    
    def get_labels(self):
        return self.model.labels
    
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