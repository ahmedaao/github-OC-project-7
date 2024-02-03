# Bad Buzz Detection

Creation of a prototype application capable of deducing the sentiment of a tweet using a Deep Learning model (DistilBERT).

 * * *

 ## Clone repo

 In your terminal, enter: 
    git clone git@github.com:ahmedaao/github-OC-project-7.git

 * * *

## Prerequisites

Go to the folder src/ and into a terminal, enter this command: 
    pip install -r requirements.txt

* * * 

## Run unit test with pytest

Go to the folder src, then enter into your terminal:
  pytest

 * * *
 
 ## Run fast_api.py as a standalone app

 Go to the sub-folder /github-OC-project-7/src/ then, into your local terminal : uvicorn fast_api:app --reload

 To access the Swagger UI enter http://127.0.0.1:8000/docs into your web browser

 * * *

 ## Run stream_lit.py as a frontal and fast_api.py in backend

Go to github-OC-project-7/src/ then enter : ./startup.sh
