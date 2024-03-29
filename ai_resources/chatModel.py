from ai_resources.KeywordChecker import KeywordModal

from nltk.chat.util import Chat
key_model = KeywordModal()
predicted_class = key_model.predict('I am homeless')
print(predicted_class)

