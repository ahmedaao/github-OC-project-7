# Import python packages
from fastapi.testclient import TestClient
from fast_api import app


client = TestClient(app)


def test_index():
    """ Test function index """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Tweets Sentiment Analysis ML API"}


def test_predict_tweet_sentiment_negative():
    """ Test negative text """
    response = client.post("/predict", json={"text": "It was a bad day"})
    assert response.status_code == 200
    assert response.json() == "negative"


def test_predict_tweet_sentiment_positive():
    """ Test positive text """
    response = client.post("/predict", json={"text": "It was a good day"})
    assert response.status_code == 200
    assert response.json() == "positive"
