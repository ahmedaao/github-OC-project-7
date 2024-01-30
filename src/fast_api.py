from pydantic import BaseModel
import tensorflow as tf
import uvicorn
from fastapi import FastAPI

# from pydantic import BaseModel
from transformers import AutoTokenizer
from transformers import (
    TFAutoModelForSequenceClassification,
    AutoModelForSequenceClassification,
)


class User_input(BaseModel):
    """User input data validation"""

    text: str


# Define the app
app = FastAPI(title="MyApp", description="Bad Buzz Detection")

# Load distilbert model
NUM_CLASSES = 2
CHECKPOINT = "distilbert-base-uncased-finetuned-sst-2-english"
distil_bert_tokenizer = AutoTokenizer.from_pretrained(CHECKPOINT)
distil_bert_model = TFAutoModelForSequenceClassification.from_pretrained(
    CHECKPOINT, num_labels=NUM_CLASSES
)


@app.get("/")
def index():
    """Generic message"""
    return {"message": "Tweets Sentiment Analysis ML API"}


@app.post("/predict")
def predict_tweet_sentiment(input: User_input):
    """Predict sentiment for a tweet"""
    # Tokenize the input text
    input_ids = distil_bert_tokenizer.encode(input.text, return_tensors="tf")
    # Make a prediction
    predictions = distil_bert_model(input_ids)[0]
    # Get the predicted class
    predicted_class = tf.argmax(predictions, axis=1).numpy()[0]
    # Map predicted class to sentiment
    prediction = "negative" if predicted_class == 0 else "positive"

    return prediction


if __name__ == "__main__":
    uvicorn.run("fast_api:app", host="0.0.0.0", port=8000)
