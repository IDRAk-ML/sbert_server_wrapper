#StateSpace Util functionsimport random
import requests
from ai_resources.KeywordChecker import KeywordModal
from ai_resources.SBertClassifier import SBertClassifier
from utils.enums import classes_dict
from word2number import w2n
keyword_model = KeywordModal()
sbert_classifier = SBertClassifier()
import yaml

def read_yaml_file(file_path):
    with open(file_path, 'r') as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as e:
            print("Error reading YAML:", e)

def parse_rasa_resp(text,rasa_server_url):
    # URL of your Rasa server API endpoint for message parsing
    # This URL might change depending on where your Rasa server is hosted
    # and how it's configured.
    url = rasa_server_url

    # Prepare the payload with the message text
    payload = {
        "text": text
    }

    # Make a POST request to the Rasa server
    response = requests.post(url, json=payload)
    result = {}
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        response_json = response.json()
        result['text'] = response_json.get('text','')
        # Extract the top predicted intent
        result['final_intent'] = response_json.get("intent", {}).get("name", "None")
        entities = response_json.get("entities", [])
        confidence = response_json.get("intent", {}).get("confidence", 0)
        if len(entities) > 0:
            result['entity_name'] = entities[0]['entity']
            result['entity'] = entities[0]['value']
        else:
            result['entity_name'] = 'None'
            result['entity'] = 'None'
        # print(f"Predicted Intent: {result}, Confidence: {confidence}")
        return result
    else:
        # print(f"Failed to classify intent. Status Code: {response.status_code}")
        result['text'] = ''
        result['final_intent'] = 'None'
        result['entity'] = ''


def get_classification(transcript,verbose=False,modules = {},server_address = '',
                       age_range=(40,80)):
    
    # ------------------- getting the entity from rasa -------------------------------
    result = parse_rasa_resp(transcript,rasa_server_url=server_address) #getting entity
    
    # -------------------- define the year, to get the age count ---------------------
    current_year = 2024
    age_count = 0
    age_mod_flag = False
    if result['entity'] != 'None' or result['entity'] != '':
            # --------------- if year of birth customer ---------------------------
            if result['entity_name'] == 'yob':
                try:
                    #-------------- for whisper ---------------
                    age_count = current_year - int(result['entity'])
                except:
                    #-------------- for kaldi style text entity -------------------
                    age_count = current_year - int(w2n.word_to_num(result['entity']))
                    
                age_mod_flag = True
            elif result['entity_name'] == 'age':
                try:
                    age_count = int(result['entity'])
                except:
                    age_count = int(w2n.word_to_num(result['entity']))
                age_mod_flag = True
            else:
                age_count = 0
    # ----------------- if age in age range return postive
    if (age_count >=age_range[0] and age_count<=age_range[1]) and (age_mod_flag):
        result['final_intent'] = 'affirmation'
    # ------------------ return negative
    elif (age_count < age_range[0] or  age_count>age_range[1]) and (age_mod_flag):
        result['final_intent'] = 'decline'
    # ------------------ if not age look for other classes -------------------
    if not age_mod_flag:
        # ------------- sbert inference --------------------
        sbert_prediction = sbert_classifier.predict(transcript)
        result['final_intent'] = sbert_prediction 
    return result 

def return_class_number(class_name):
    if not class_name:
        class_name = 'None'
    try:
        class_number = classes_dict[class_name]
    except:
        class_number = classes_dict['None']
    return class_number

