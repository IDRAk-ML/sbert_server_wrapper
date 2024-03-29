from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from wrapper import OldBotStyleWrapper
from utils.utils import *
app = FastAPI()

# Example usage:
file_path = 'config.yml'  # Path to your YAML file
data = read_yaml_file(file_path)

class AI_VAR(BaseModel):
    text: str

old_bot_rasa = OldBotStyleWrapper(rasa_server_address=data['SERVER_ADDRESS'],
                                      age_range=data['AGE_RANGE'])

@app.post("/process-text/")
async def process_text(ai_str: AI_VAR):
    
    ai_number = old_bot_rasa.predict(ai_str.text)
    return {"ai_resp" : ai_number}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9096)
