import fastapi

app = fastapi.FastAPI()

@app.get("/test")
def test() -> str:
    return "ok"