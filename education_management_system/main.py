from fastapi import FastAPI

app = FastAPI(title='Education Management System')

@app.get('/test')
def for_test():
    return {'status': 'I am Live.'}