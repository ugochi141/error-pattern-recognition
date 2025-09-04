from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="error-pattern-recognition")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"project": "error-pattern-recognition", "status": "operational"}

@app.get("/health")
def health():
    return {"status": "healthy"}
