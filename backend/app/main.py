from fastapi import FastAPI

app = FastAPI(title="SatQuery AI Backend Foundation")

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Backend service is running"}
