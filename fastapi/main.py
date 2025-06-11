from fastapi import FastAPI, UploadFile, File
import pandas as pd
import random
from transformers import pipeline
from PIL import Image
from io import BytesIO

app = FastAPI()

@app.get('/Perfil')
def perfil(name: str, age: int, country: str):
    """
    Endpoint to return personal data.
    """
    return {
        'Name': name,
        'Age': age,
        'Country': country
    }


@app.get('/DeathNumber')
def yourDeathAge(): 
    """
    Endpoint to calculate the age at which a person will die based on a random number.
    """
    random_number = random.randint(1, 100)
    death_age = 100 - random_number
    return f"you will die in {death_age} years."

@app.get('/Anagram')
def anagram(word: str):
    """
    Endpoint to return an anagram of the given word.
    """
    if len(word) < 2:
        return "Word must be at least 2 characters long."
    
    shuffled_word = ''.join(random.sample(word, len(word)))
    if word.lower() == 'tom marvelous riddle':
        shuffled_word = 'I am lord Voldemort'
    return f"An anagram of {word} is {shuffled_word}."

@app.get('/Analisis')
def sentiment_Classfier(query:str): 
    sentiment_analyzer = pipeline("sentiment-analysis", model="tabularisai/multilingual-sentiment-analysis")
    sentiment = sentiment_analyzer(query)
    
    ner_model = "mrm8488/bert-spanish-cased-finetuned-ner"
    recognizer = pipeline("ner", model=ner_model, tokenizer=ner_model, aggregation_strategy="simple")
    entities = recognizer(query)
    return {
        "sentiment": sentiment,
        "entities": entities
    }

@app.post('/ImageClassifier')
async def image_classifier(img: UploadFile = File(...)):
    """
    Endpoint to classify an image using a pre-trained model.
    """
    import traceback
    try:
        contents = await img.read()
        image = Image.open(BytesIO(contents)).convert("RGB")  # Asegura formato compatible

        classifier = pipeline("image-classification", model="google/vit-base-patch16-224")
        results = classifier(image)
        df_results = pd.DataFrame(results)
        results_dict = df_results.to_dict(orient='records')

        return results_dict
    except Exception as e:
        return {
            "error": str(e),
            "type": str(type(e)),
            "traceback": traceback.format_exc()
        }