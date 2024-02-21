from fastapi import FastAPI
from starlette.responses import FileResponse 

app = FastAPI()

@app.get('/')
def root():
    return FileResponse('static/index.html')

@app.get('/django')
def read_django():
    return FileResponse('static/django.html')

@app.get('/flask')
def read_flask():
    return FileResponse('static/flask.html')
