from fastapi import FastAPI

app = FastAPI(title="Fast")

@app.get('/')
async def test():
    return {'title': "Test"}