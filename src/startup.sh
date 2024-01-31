gunicorn -w 2 -k uvicorn.workers.UvicornWorker fast_api:app | streamlit run stream_lit.py
